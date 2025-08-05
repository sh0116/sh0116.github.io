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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/d2dedcd2-1e43-4280-baf2-bb42f853c099/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UU5NVNA5%2F20250805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250805T002747Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJGMEQCIFFlPnhmphoIBqa%2BQDPJAcQvmeycmE8Qcb4o2csiscEmAiBao215%2Bc%2BCr2UyG4GUV6ywZhORmLAPZlBoBeUH9ss62ir%2FAwhQEAAaDDYzNzQyMzE4MzgwNSIMOG4zKVSfyhZuQ4CYKtwDdO7pOUL6bi1x8l8YLcNwapc2rgndPEaLcrrvCir2hqJYnMXKFzVD3mTh6UOxM1mGowc7effmUfZ8gXo21dM0ewz%2Fuuo19vuSHVeE73yWQuTbGWzizXyqGS54o4jMw4AR4zI1b4k99UeBNjCSt4WuEYRkzmNGDOuxHAgpBTFEOgynFL4ciMNn7ZJXadeae4pAo3H4Sk86VCgCRMjuU3MJDiHisQuN%2Bin%2BDm0PScgiJqx2j60bnREq3hAl4sEo9v2JaW5bYUe9GxdCsoMc4UZy%2FrVOAOFQc9G9MNBib4%2B4b1gYjLjEHFjN8zmVkt4WduqEFy4c72FBzvIN5BUcaL%2BTnsM4aHjHE05IxuoCDXit98QasWrDjkAZs667vO6oi52QsJMm9wjVlOZQNaxPd2W8D2legj0sgrhtwHwHg48OutGhC8wU8k43c%2BcaAlCIaKI31YZTMSMghwXgIgR7e6mxGYNoweZ6v9SZcQr2%2FWC3EBJBFfF2AJ7vdxrMnRm4DEgKGZGuE65E7ll3X5F53ZjYB3fpO7Wz0JJ3usZkxSv9ebbx%2Fojx7Lh4pu1yzjGDbWJmyHTEY%2FSndgfIWe3SclKPmTbXaKRT0x%2FSQ3yBp31gRfky1gmWGXDFtUaCfcgwwfTExAY6pgEnixYcG53MHz5l15s9dP%2F9yxXvbard3KzzYsxw1H7ipx6sTEcJk1WHrHYNhYbqYDplLOU7uIeXjaSfz3w3b7vR%2FqPjBCJOP8%2F8%2B%2F2mFdZyvdvkBS4UuqtYZuiixCMr%2Bm99MZjX3Ml5lTE0HpqCaJGJwTB7Nf2KxUnBUO9%2FhWMkeJGKpRbSg9tCtQCOhDFT5zYRH44l%2BW12cIcUaVhOPb15YyGC1tdF&X-Amz-Signature=9251920682368cd436451bbd9ab42f05b5e8c5450eecf5db5c6a774ae5449241&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

트랜스포머 모델의 Attention 매커니즘을 짧게 소개하자면 Scaled Dot-Product Attention 연산을 여러 겹 올린 Multi-Head Attention 이 기본적이다.

이 모델 구조에서 Scaled Dot-Product Attention 연산을 반복적으로 수행하게 되는데 이 과정에서 중복된 연산이 많이 일어난다. 

Decoder에서 토큰을 생성하면서 Scaled Dot-Product Attention을 반복적으로 수행하는 과정 속에서 이전 토큰들의 계산을 중복적으로 계산을 하는데 이 과정을 Cache를 통해서 일정량의 저장비용을 통해 연산비용을 줄이는 기술이 KV Cache이다!

(KV Cahce인 이유는Key와 Value 영역의 정보를 Cache하기 때문에)

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/75f005c6-c2f9-45e8-ad7a-efb9ebedb50e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UU5NVNA5%2F20250805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250805T002747Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJGMEQCIFFlPnhmphoIBqa%2BQDPJAcQvmeycmE8Qcb4o2csiscEmAiBao215%2Bc%2BCr2UyG4GUV6ywZhORmLAPZlBoBeUH9ss62ir%2FAwhQEAAaDDYzNzQyMzE4MzgwNSIMOG4zKVSfyhZuQ4CYKtwDdO7pOUL6bi1x8l8YLcNwapc2rgndPEaLcrrvCir2hqJYnMXKFzVD3mTh6UOxM1mGowc7effmUfZ8gXo21dM0ewz%2Fuuo19vuSHVeE73yWQuTbGWzizXyqGS54o4jMw4AR4zI1b4k99UeBNjCSt4WuEYRkzmNGDOuxHAgpBTFEOgynFL4ciMNn7ZJXadeae4pAo3H4Sk86VCgCRMjuU3MJDiHisQuN%2Bin%2BDm0PScgiJqx2j60bnREq3hAl4sEo9v2JaW5bYUe9GxdCsoMc4UZy%2FrVOAOFQc9G9MNBib4%2B4b1gYjLjEHFjN8zmVkt4WduqEFy4c72FBzvIN5BUcaL%2BTnsM4aHjHE05IxuoCDXit98QasWrDjkAZs667vO6oi52QsJMm9wjVlOZQNaxPd2W8D2legj0sgrhtwHwHg48OutGhC8wU8k43c%2BcaAlCIaKI31YZTMSMghwXgIgR7e6mxGYNoweZ6v9SZcQr2%2FWC3EBJBFfF2AJ7vdxrMnRm4DEgKGZGuE65E7ll3X5F53ZjYB3fpO7Wz0JJ3usZkxSv9ebbx%2Fojx7Lh4pu1yzjGDbWJmyHTEY%2FSndgfIWe3SclKPmTbXaKRT0x%2FSQ3yBp31gRfky1gmWGXDFtUaCfcgwwfTExAY6pgEnixYcG53MHz5l15s9dP%2F9yxXvbard3KzzYsxw1H7ipx6sTEcJk1WHrHYNhYbqYDplLOU7uIeXjaSfz3w3b7vR%2FqPjBCJOP8%2F8%2B%2F2mFdZyvdvkBS4UuqtYZuiixCMr%2Bm99MZjX3Ml5lTE0HpqCaJGJwTB7Nf2KxUnBUO9%2FhWMkeJGKpRbSg9tCtQCOhDFT5zYRH44l%2BW12cIcUaVhOPb15YyGC1tdF&X-Amz-Signature=8a1ececa7fd9637324f7459fa7111b9ed84eb32ab0e1169ca31de07997b43f7b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

결국 백터의 내적 계산을 반복적으로 수행하는 것 이기 때문에

K^t에서 Token1,2,3을 기억하고 있다면 Token 4의 Attention을 구할 때 굳이 1,2,3을 다시 계산할 필요가 없다. 

### KV 캐싱 문제점

### 참조


