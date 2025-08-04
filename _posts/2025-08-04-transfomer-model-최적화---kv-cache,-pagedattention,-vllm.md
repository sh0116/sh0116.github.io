---
title: "Transfomer model 최적화 - KV Cache, PagedAttention, vLLM"
date: 2025-08-04 06:05:00 +0900
categories: [기술소개]
tags: [Transfomer, LLM, AI]
description: Transfomer model 기술 소개
toc: true
comments: true
---

# Transfomer model 최적화 - KV Cache, PagedAttention, vLLM

Transfomer 모델을 최적화하기 위한 방식 KV Cache와 해당 방법의 단점을 보완한 Paged KV Cache방식 그리고 실제 응용 사례인 vLLM을 소개하는 페이지이다. 

## KV Cache

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/d2dedcd2-1e43-4280-baf2-bb42f853c099/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SOQPRTED%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T072220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJIMEYCIQDF0gxhlo23Y9LGVPkwrkI3ZUn1Lw7d3X4PufiAK0Z7XQIhAMtjkUtr464pq%2F2QQUr8TxI0LVl0NdJONtIjULibvQwWKv8DCEAQABoMNjM3NDIzMTgzODA1IgzH6KBco3yvv970hMAq3AOo%2B3lOfU%2FewsivOyHG1j50YGwe60WTkMXsvNQCIJwSS4NHkFqX%2F2RwrUR5mEUNs6%2BHe6L7MUA0ykVJAgPjp2cOAr5uJVxnnCy4Uyq1UKYfYGa7jp2TK8qbsh939A%2BjSeHuI1MaqpEDiN4jO4X2gd3z%2FiJ9n9SRYStz3Yocrzh8spOpE4EanTTsgjMVkwXTknZKsddbfGSnv8tFBLW7%2F0LhSAv08b%2Fzl8IP22LfO25jjal5qoAVBflg83VkS%2BVi94WLu7uY2bTQA22xSKCkAn%2Fhpwkvi2c%2BILVjUwjccoZRZQZpsJsOBB0Z8zOXmqvCMsDJyiyI11%2BgavMe4J1qh7lNHyL6AQIEOLw9oUKT3aelz2uKRhx7kk5caP5fXwTeojDSuJnJo5LfP3YomKKtl30dYYXCQsuIdv8n2gRfkcYEVc9ILDHflME0UCIDjXBv%2F%2Bbc8FixQCLq8yv1qRf4A5z6M5tCeQLQt5qaUoyw7iYBXoxgAdxOQuy3YQ9itV74SKX32MV%2FMIoYttddnXFMm4gAwlD5MBhEoJYT1oJGQdh0exoxYXrY2OSNaMlKvRjG%2BwuesAD0Hy6TfOebxxy5pl%2FxIIcBUXep5D%2F%2FmbYbZCkSLQiEvypZPL%2FVAslnPTDFt8HEBjqkARZYW8dUDgutlmSCkgZZs3oWJ7JWM5iyobaP8BT74Bxc8CAqr8%2BcJyvpQYOr8y%2Bi251E6bH3cG1AQUtwC9GNwQSiOZ1EVukZUC2v86%2BpcCZSvn6GzPzTx9AbmG4lq4%2BbZuUPzFjDM9fEnMiNpsmzkzcQvNQCVjA2fpTShDH9pLKlGbZS%2FTVrM76c0RdaiVM7hX4AsgNGyqyogUBFa2iRDtd5gNLL&X-Amz-Signature=6cbcd60fe0bf1685f8b99d5f4116b0bebe1afe890afa892e4582cb81d865c1ba&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

트랜스포머 모델의 Attention 매커니즘을 짧게 소개하자면 Scaled Dot-Product Attention 연산을 여러 겹 올린 Multi-Head Attention 이 기본적이다.

이 모델 구조에서 Scaled Dot-Product Attention 연산을 반복적으로 수행하게 되는데 이 과정에서 중복된 연산이 많이 일어난다. 

Decoder에서 토큰을 생성하면서 Scaled Dot-Product Attention을 반복적으로 수행하는 과정 속에서 이전 토큰들의 계산을 중복적으로 계산을 하는데 이 과정을 Cache를 통해서 일정량의 저장비용을 통해 연산비용을 줄이는 기술이 KV Cache이다!

(KV Cahce인 이유는Key와 Value 영역의 정보를 Cache하기 때문에)

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/75f005c6-c2f9-45e8-ad7a-efb9ebedb50e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SOQPRTED%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T072220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJIMEYCIQDF0gxhlo23Y9LGVPkwrkI3ZUn1Lw7d3X4PufiAK0Z7XQIhAMtjkUtr464pq%2F2QQUr8TxI0LVl0NdJONtIjULibvQwWKv8DCEAQABoMNjM3NDIzMTgzODA1IgzH6KBco3yvv970hMAq3AOo%2B3lOfU%2FewsivOyHG1j50YGwe60WTkMXsvNQCIJwSS4NHkFqX%2F2RwrUR5mEUNs6%2BHe6L7MUA0ykVJAgPjp2cOAr5uJVxnnCy4Uyq1UKYfYGa7jp2TK8qbsh939A%2BjSeHuI1MaqpEDiN4jO4X2gd3z%2FiJ9n9SRYStz3Yocrzh8spOpE4EanTTsgjMVkwXTknZKsddbfGSnv8tFBLW7%2F0LhSAv08b%2Fzl8IP22LfO25jjal5qoAVBflg83VkS%2BVi94WLu7uY2bTQA22xSKCkAn%2Fhpwkvi2c%2BILVjUwjccoZRZQZpsJsOBB0Z8zOXmqvCMsDJyiyI11%2BgavMe4J1qh7lNHyL6AQIEOLw9oUKT3aelz2uKRhx7kk5caP5fXwTeojDSuJnJo5LfP3YomKKtl30dYYXCQsuIdv8n2gRfkcYEVc9ILDHflME0UCIDjXBv%2F%2Bbc8FixQCLq8yv1qRf4A5z6M5tCeQLQt5qaUoyw7iYBXoxgAdxOQuy3YQ9itV74SKX32MV%2FMIoYttddnXFMm4gAwlD5MBhEoJYT1oJGQdh0exoxYXrY2OSNaMlKvRjG%2BwuesAD0Hy6TfOebxxy5pl%2FxIIcBUXep5D%2F%2FmbYbZCkSLQiEvypZPL%2FVAslnPTDFt8HEBjqkARZYW8dUDgutlmSCkgZZs3oWJ7JWM5iyobaP8BT74Bxc8CAqr8%2BcJyvpQYOr8y%2Bi251E6bH3cG1AQUtwC9GNwQSiOZ1EVukZUC2v86%2BpcCZSvn6GzPzTx9AbmG4lq4%2BbZuUPzFjDM9fEnMiNpsmzkzcQvNQCVjA2fpTShDH9pLKlGbZS%2FTVrM76c0RdaiVM7hX4AsgNGyqyogUBFa2iRDtd5gNLL&X-Amz-Signature=8eb00698f23013638851d0ccdf643b47bcdb991bc650004c6b5ae671f6d7abee&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

결국 백터의 내적 계산을 반복적으로 수행하는 것 이기 때문에

K^t에서 Token1,2,3을 기억하고 있다면 Token 4의 Attention을 구할 때 굳이 1,2,3을 다시 계산할 필요가 없다. 

### KV 캐싱 문제점

### 참조


