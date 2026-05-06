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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/d2dedcd2-1e43-4280-baf2-bb42f853c099/Untitled.png)

트랜스포머 모델의 Attention 매커니즘을 짧게 소개하자면 Scaled Dot-Product Attention 연산을 여러 겹 올린 Multi-Head Attention 이 기본적이다.

이 모델 구조에서 Scaled Dot-Product Attention 연산을 반복적으로 수행하게 되는데 이 과정에서 중복된 연산이 많이 일어난다. 

Decoder에서 토큰을 생성하면서 Scaled Dot-Product Attention을 반복적으로 수행하는 과정 속에서 이전 토큰들의 계산을 중복적으로 계산을 하는데 이 과정을 Cache를 통해서 일정량의 저장비용을 통해 연산비용을 줄이는 기술이 KV Cache이다!

(KV Cahce인 이유는Key와 Value 영역의 정보를 Cache하기 때문에)

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/75f005c6-c2f9-45e8-ad7a-efb9ebedb50e/Untitled.png)

결국 백터의 내적 계산을 반복적으로 수행하는 것 이기 때문에

K^t에서 Token1,2,3을 기억하고 있다면 Token 4의 Attention을 구할 때 굳이 1,2,3을 다시 계산할 필요가 없다. 

### KV 캐싱 문제점

### 참조


