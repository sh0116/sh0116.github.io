---
title: "**Transformer 모델 - Self-Attention**"
date: 2025-08-04 06:06:00 +0900
categories: [기술소개]
tags: [Transfomer, AI, LLM]
description: Self-Attention 개념
toc: true
comments: true
---

## 개요

2017년 NIPS에서 'Attention Is All You Need’ 라는 논문으로 Transformer 모델이 나왔다.

병렬 처리가 안되던 RNN의 한계를 극복한 알고리즘으로 자연어처리에서 좋은 결과를 보여줬다.

## 내용

### ASIS

17년도에 나온 Attentions Is All You Need 논문에서는 Attention만으로 구현된 모델을 소개한다. RNN 기법을 사용하지 않고 인코더, 디코더 구조로만 설계하고 번역 성능에서 RNN보다 뛰어난 성과를 냈습니다.

기존의 seq2seq 모델도 인코더와 디코더는 있었습니다.

입력  seq 를 하나의 백터로 압축하고 디코더는 이 백터를 기반으로 출력 seq 를 만들었습니다. 

이 과정에서 입력 seq의 정보가 손실되는 점이 문제였습니다.

RNN 구조를 사용하면 먼 단어일 수록 흐려진다는 단점들이 있었습니다. 

또한 병렬 처리가 안된다..

RNN모델은 이전Tn-1에 결과값을 현재Tn 연산에 사용하는 점 때문이다. 

따라서 n의 차이가 크면 흐려지고, 이전 결과값을 재귀적으로 받기 때문에 병렬 연산이 불가능하다.

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/1e7f5e6f-9228-4d68-9d1d-6554327138c3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T7GLF2GF%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T063223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJGMEQCIBd14y3%2BVI8DaoabMTUu7AYKc002jEBk76%2F%2FemibFcCQAiBGzXZFlBo5P7k8PQWO8xBFGzoCmP05ktRxmj1hQ0uLfCr%2FAwg%2FEAAaDDYzNzQyMzE4MzgwNSIMRCTm6ei7mM8OQWHOKtwDPrgH6m8phDCEnIdneJFsAO926juGOkz4wdT%2BELO3z91rN7hfiZr%2Bscufu9DGMCEcYaLj4bSWKKvk3nQ5evQsSBL6vhnpDn56%2FjrJbg9jCVX4dTNB%2FRlBAzu05Z9RCrh%2FjpcPkewZIO1zr8O1FLBVNvTqa8Xr3aY5d2Vc1DYiNqFFRvNkuluHgB%2B6%2BipLphdcgVf8kS%2FjiljcjssiWqZSvoyUohMmjNwHCoMJ8qXvtlt%2FMgUjt8sJCe%2FOsTPjk428xrVPo0vhD4G40xjw12%2Fq7YzJzPQbyiFUg7ISS4PRB3fJFZtNlu97nLjmTWYsoUWqlvTk5MCvIpq7nl2dc1XzOn4ZGZA2o%2BZO8uwyWKb4KsfhcIaJOOrOkxry%2BbLb%2Bg7LU4i3IojGbsaJjY2wpQHj0hh8Td3Z8mJb24rTL4oTLI5w5zdX%2FAaC72CxsDLlR4GyVJsUnmV%2BZpQ%2BMSFIg6NUGnKctWMCLQzxHeNT2DTpoek%2FKexEsCbQL6bSDYOqTF3YC1Btd7aXBflEI9UD%2BBEeteRSF81A0ewqhy8pgMwJJ6YmKKRmzMHuRCnoKxOP0ubqlkRjZ8Ih2pOztsZ8yb4g23VIFqaHkt1rWYsAs4z2sL9J6AfAjrfg1Wg3YY8wuY3BxAY6pgHxR87wJiFjW3XLpdGx20srG%2FRPQ70T3irEEOzUuWbS%2B0hX3DMFDqq9dSeCwblyysQfkjQyY%2FZS2l05GGlDtQaVdT5gmD2ylWwYDUJL%2BmJ%2Bm8xDM%2FQtkQpXps0q0%2BuGZBE%2FqklWovglrDmNxY3TQmfPxZK99SlnUMUd4pKYIu1e8M1LjC4X4DqhJdXM5jKwxIvCBUdWenR7ng5QUSJ%2FdIUHHmjR4%2Bz8&X-Amz-Signature=d2bf28716ea9954e951c44a699d8de242694019e1536b9b59d8c6f713c02200c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### TOBE

이런 구조를 바꾼게 바로 2017년 NIPS에서 'Attention Is All You Need’ 라는 논문이다. 

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/6e9cd139-802d-46d7-a36a-93043fd1cafc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T7GLF2GF%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T063223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJGMEQCIBd14y3%2BVI8DaoabMTUu7AYKc002jEBk76%2F%2FemibFcCQAiBGzXZFlBo5P7k8PQWO8xBFGzoCmP05ktRxmj1hQ0uLfCr%2FAwg%2FEAAaDDYzNzQyMzE4MzgwNSIMRCTm6ei7mM8OQWHOKtwDPrgH6m8phDCEnIdneJFsAO926juGOkz4wdT%2BELO3z91rN7hfiZr%2Bscufu9DGMCEcYaLj4bSWKKvk3nQ5evQsSBL6vhnpDn56%2FjrJbg9jCVX4dTNB%2FRlBAzu05Z9RCrh%2FjpcPkewZIO1zr8O1FLBVNvTqa8Xr3aY5d2Vc1DYiNqFFRvNkuluHgB%2B6%2BipLphdcgVf8kS%2FjiljcjssiWqZSvoyUohMmjNwHCoMJ8qXvtlt%2FMgUjt8sJCe%2FOsTPjk428xrVPo0vhD4G40xjw12%2Fq7YzJzPQbyiFUg7ISS4PRB3fJFZtNlu97nLjmTWYsoUWqlvTk5MCvIpq7nl2dc1XzOn4ZGZA2o%2BZO8uwyWKb4KsfhcIaJOOrOkxry%2BbLb%2Bg7LU4i3IojGbsaJjY2wpQHj0hh8Td3Z8mJb24rTL4oTLI5w5zdX%2FAaC72CxsDLlR4GyVJsUnmV%2BZpQ%2BMSFIg6NUGnKctWMCLQzxHeNT2DTpoek%2FKexEsCbQL6bSDYOqTF3YC1Btd7aXBflEI9UD%2BBEeteRSF81A0ewqhy8pgMwJJ6YmKKRmzMHuRCnoKxOP0ubqlkRjZ8Ih2pOztsZ8yb4g23VIFqaHkt1rWYsAs4z2sL9J6AfAjrfg1Wg3YY8wuY3BxAY6pgHxR87wJiFjW3XLpdGx20srG%2FRPQ70T3irEEOzUuWbS%2B0hX3DMFDqq9dSeCwblyysQfkjQyY%2FZS2l05GGlDtQaVdT5gmD2ylWwYDUJL%2BmJ%2Bm8xDM%2FQtkQpXps0q0%2BuGZBE%2FqklWovglrDmNxY3TQmfPxZK99SlnUMUd4pKYIu1e8M1LjC4X4DqhJdXM5jKwxIvCBUdWenR7ng5QUSJ%2FdIUHHmjR4%2Bz8&X-Amz-Signature=dd435b964a25be5b4ec352359234929c08317c4dc3ab8107acec3e94cd81f5f0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 참조

https://namu.wiki/w/트랜스포머(인공신경망)

https://chonchony.tistory.com/entry/순환신경망-RNN의-문제점-기울기-소실-기울기-폭주-Gradient-Vanishing-Exploding

https://calmmimiforest.tistory.com/110


