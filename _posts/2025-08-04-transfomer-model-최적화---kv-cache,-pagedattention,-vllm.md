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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/d2dedcd2-1e43-4280-baf2-bb42f853c099/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663JUYHGT6%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T071444Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIQDxKNy%2BSRMmRgXZh7K7y2erNE76a6ia9JHsr%2FKSYdp8NAIgJCgH93VSfTSjLIkDK5ESJiO%2FaVIVrpRHme8y3P4O2xcq%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDGVPKd1dfOIYee2u5SrcA%2BIgKLiyVvpj2yPj3T%2BWMrkQAR7sGjAuVwEBnOGaTGq0Yn2Vdjy0D%2FRXXzxMEbB%2F4HRe%2FNdgJ03%2FHmlnIzmAIiE%2FYPCokz9pRLnLh%2BATN95KfASfVs6B5PT%2Fw9FsI4395M9mUaVZYiIIKcmynWlWzpOB49lJl7GG5bEibW2jeAjwTJrdTe6dQHG5aBICY2Fv5vv7NzchpUqRAzYJ176C8BCug1byHO6zUNIVpnYctN3b1R8G%2FZtQ5dutCBU0fE%2BeRnvq7iTvpwBNofB0luYHJdKGtvM%2BchWT%2BZymk9cH%2B0WGcBDbOxTB6rkw4SY4RTUX%2BTDTltxXboTzwnghoRabSQQLNsgFO89qSRH%2FqGsKJ263qZtBIXATRjeZ169dS8iAL0XYwoPiM5tmzsaeX4yPHpXbjIcWZXn3iubvVP8GhkT18hF7pLHKiORhw5rnOubbRMKius9uEBeGGsVbLjJifJvTEDtu6ms4GgT1584TU%2B92sT%2FEAOgLr%2FuOUOxCdFj2kfTlywEW1VR568B1NN3MjAnH6vw2kRAOmdUaLtzmh6Ei7fPIO1urDkFLJC8USB2Nmd8edH1IJNBAslyqXn%2F%2FmA9ehT9O0XpRzww6P6ERF7PybyZJ%2FnHmsPecbri8MOO3wcQGOqUB72ofX0XGN1GZEW%2FqmJ0qidkRRxhLwrDSwKqnUVbQ0lUt1Y1SiY25r1NFUeoMD3R1cdJK8EQb85yRNN2J3v0WmZdaIv%2Frq74hZwX4S5FEW0uf0wGdBxlr56rYLpGeTcXowBRUDcXqJodlqI0%2FkBQGA9TBrfyPdN6Kj20%2Fkxf2o7G8fowsfZ5upp8lc6cEUHh6ehfN8m0Qdmeh%2FJnKLjEsssbC3eGe&X-Amz-Signature=5b0bb6749bf18c1cf729ad43c7cac31bf809e1a89787916a1264b5ad28ca5c87&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

트랜스포머 모델의 Attention 매커니즘을 짧게 소개하자면 Scaled Dot-Product Attention 연산을 여러 겹 올린 Multi-Head Attention 이 기본적이다.

이 모델 구조에서 Scaled Dot-Product Attention 연산을 반복적으로 수행하게 되는데 이 과정에서 중복된 연산이 많이 일어난다. 

Decoder에서 토큰을 생성하면서 Scaled Dot-Product Attention을 반복적으로 수행하는 과정 속에서 이전 토큰들의 계산을 중복적으로 계산을 하는데 이 과정을 Cache를 통해서 일정량의 저장비용을 통해 연산비용을 줄이는 기술이 KV Cache이다!

(KV Cahce인 이유는Key와 Value 영역의 정보를 Cache하기 때문에)

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/75f005c6-c2f9-45e8-ad7a-efb9ebedb50e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663JUYHGT6%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T071444Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIQDxKNy%2BSRMmRgXZh7K7y2erNE76a6ia9JHsr%2FKSYdp8NAIgJCgH93VSfTSjLIkDK5ESJiO%2FaVIVrpRHme8y3P4O2xcq%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDGVPKd1dfOIYee2u5SrcA%2BIgKLiyVvpj2yPj3T%2BWMrkQAR7sGjAuVwEBnOGaTGq0Yn2Vdjy0D%2FRXXzxMEbB%2F4HRe%2FNdgJ03%2FHmlnIzmAIiE%2FYPCokz9pRLnLh%2BATN95KfASfVs6B5PT%2Fw9FsI4395M9mUaVZYiIIKcmynWlWzpOB49lJl7GG5bEibW2jeAjwTJrdTe6dQHG5aBICY2Fv5vv7NzchpUqRAzYJ176C8BCug1byHO6zUNIVpnYctN3b1R8G%2FZtQ5dutCBU0fE%2BeRnvq7iTvpwBNofB0luYHJdKGtvM%2BchWT%2BZymk9cH%2B0WGcBDbOxTB6rkw4SY4RTUX%2BTDTltxXboTzwnghoRabSQQLNsgFO89qSRH%2FqGsKJ263qZtBIXATRjeZ169dS8iAL0XYwoPiM5tmzsaeX4yPHpXbjIcWZXn3iubvVP8GhkT18hF7pLHKiORhw5rnOubbRMKius9uEBeGGsVbLjJifJvTEDtu6ms4GgT1584TU%2B92sT%2FEAOgLr%2FuOUOxCdFj2kfTlywEW1VR568B1NN3MjAnH6vw2kRAOmdUaLtzmh6Ei7fPIO1urDkFLJC8USB2Nmd8edH1IJNBAslyqXn%2F%2FmA9ehT9O0XpRzww6P6ERF7PybyZJ%2FnHmsPecbri8MOO3wcQGOqUB72ofX0XGN1GZEW%2FqmJ0qidkRRxhLwrDSwKqnUVbQ0lUt1Y1SiY25r1NFUeoMD3R1cdJK8EQb85yRNN2J3v0WmZdaIv%2Frq74hZwX4S5FEW0uf0wGdBxlr56rYLpGeTcXowBRUDcXqJodlqI0%2FkBQGA9TBrfyPdN6Kj20%2Fkxf2o7G8fowsfZ5upp8lc6cEUHh6ehfN8m0Qdmeh%2FJnKLjEsssbC3eGe&X-Amz-Signature=804c2ae615bc47cedac740ba347bca73ab2c2d533617e927304a362b380d9169&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

결국 백터의 내적 계산을 반복적으로 수행하는 것 이기 때문에

K^t에서 Token1,2,3을 기억하고 있다면 Token 4의 Attention을 구할 때 굳이 1,2,3을 다시 계산할 필요가 없다. 

### KV 캐싱 문제점

### 참조


