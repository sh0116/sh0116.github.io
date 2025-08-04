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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/1e7f5e6f-9228-4d68-9d1d-6554327138c3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662YFUAVXN%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T071355Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJIMEYCIQDHcE0cUuOsME7Z9pSFJl692TRUUokoBThlYzqUjoAAJAIhALigsnR0D8cR5GhkspAzzkI8HEmYbRPuq%2BSSPS33%2FSTmKv8DCEAQABoMNjM3NDIzMTgzODA1IgwRKULD4KxbaIy6H3Uq3ANYrMNy7tk0eAbER%2FR%2FXd64W%2ByAuvkZgx3LIJKbPqXPW%2B2Srg%2FiNgOBGcqHOivjNr7Zulo3X0Qfy1mNu7qYyxuhvi8Fa%2FZor3hOzuHKnv0eYQzw5UW%2B9MNXXPNbCO88zlP4Ovg94bZ%2BNVoKjAED3R70QOLbyb%2BHrX6etvQXexMobMrcm%2BjdvkUk9q5pGhrJ%2FDGaD5g9YOQH2J2NWYBkyJ9Y6mvd72xZ%2ByvXgJaANeDcOLTQ9RoYVNmGjOhkvkMF8QcWhg3NCgySB9d80Ikt2t2Tap6Wgon83X3x%2BZDJhIFPDFwSGcEEPpY90wbl4czeCDomsadyVeV3eIDWDDi3lsZnUXX%2FHDUSxDZjk5%2BXIV00zG1Est3gCqCC8GfU%2FEdfvX1xiMBsXvs3AtQfHit%2FhDv%2FOz9z8MAs1UklBMOMwxNpFyVxWgZdzU12OgVvSznIFlRPLyP9E5s8i7Caa5GNf6%2FXuRULJznW5rdwIwJfOzWyURm9jbUM6BnVFFaYblLMA0QLst34xfPCX%2FBYrW9%2FpiZV8uGK1FtNoBcE2i9%2FgcLKCuL78QJbmQt5uwvAV06o0xIzYGJY8D0S1urFvrAF2xN21FtDJwI2xMlauioOtMKY%2FLz5Ka8n%2F256q5zq9zCjt8HEBjqkAZDMxIWMYtYa%2FRf1Uv%2FWr0%2BbIhYqTrEB1ErC0vCVj3zqDopNoHew1zImscnF40iUjdnupaAMHsk8DjU4WA8MuHZ6APEAuvK6yWnE45jDvL7PbuWdJ66gPKOdkRTw5%2FaE4Xh1GqF0LMTFwvr0N6VYCsPFEJoITUgi2oZWOvkOh1wyS%2BWFZ0k7kvCxfSq2kOSn2bpHzuz2MBA%2F4DKdYpOiQKqPr3q%2F&X-Amz-Signature=262695c5f032847e12893b2775cfdcced93bbc95bd9bd5e1d8b6f8f03fb1b70a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### TOBE

이런 구조를 바꾼게 바로 2017년 NIPS에서 'Attention Is All You Need’ 라는 논문이다. 

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/6e9cd139-802d-46d7-a36a-93043fd1cafc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662YFUAVXN%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T071355Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJIMEYCIQDHcE0cUuOsME7Z9pSFJl692TRUUokoBThlYzqUjoAAJAIhALigsnR0D8cR5GhkspAzzkI8HEmYbRPuq%2BSSPS33%2FSTmKv8DCEAQABoMNjM3NDIzMTgzODA1IgwRKULD4KxbaIy6H3Uq3ANYrMNy7tk0eAbER%2FR%2FXd64W%2ByAuvkZgx3LIJKbPqXPW%2B2Srg%2FiNgOBGcqHOivjNr7Zulo3X0Qfy1mNu7qYyxuhvi8Fa%2FZor3hOzuHKnv0eYQzw5UW%2B9MNXXPNbCO88zlP4Ovg94bZ%2BNVoKjAED3R70QOLbyb%2BHrX6etvQXexMobMrcm%2BjdvkUk9q5pGhrJ%2FDGaD5g9YOQH2J2NWYBkyJ9Y6mvd72xZ%2ByvXgJaANeDcOLTQ9RoYVNmGjOhkvkMF8QcWhg3NCgySB9d80Ikt2t2Tap6Wgon83X3x%2BZDJhIFPDFwSGcEEPpY90wbl4czeCDomsadyVeV3eIDWDDi3lsZnUXX%2FHDUSxDZjk5%2BXIV00zG1Est3gCqCC8GfU%2FEdfvX1xiMBsXvs3AtQfHit%2FhDv%2FOz9z8MAs1UklBMOMwxNpFyVxWgZdzU12OgVvSznIFlRPLyP9E5s8i7Caa5GNf6%2FXuRULJznW5rdwIwJfOzWyURm9jbUM6BnVFFaYblLMA0QLst34xfPCX%2FBYrW9%2FpiZV8uGK1FtNoBcE2i9%2FgcLKCuL78QJbmQt5uwvAV06o0xIzYGJY8D0S1urFvrAF2xN21FtDJwI2xMlauioOtMKY%2FLz5Ka8n%2F256q5zq9zCjt8HEBjqkAZDMxIWMYtYa%2FRf1Uv%2FWr0%2BbIhYqTrEB1ErC0vCVj3zqDopNoHew1zImscnF40iUjdnupaAMHsk8DjU4WA8MuHZ6APEAuvK6yWnE45jDvL7PbuWdJ66gPKOdkRTw5%2FaE4Xh1GqF0LMTFwvr0N6VYCsPFEJoITUgi2oZWOvkOh1wyS%2BWFZ0k7kvCxfSq2kOSn2bpHzuz2MBA%2F4DKdYpOiQKqPr3q%2F&X-Amz-Signature=f3c8cfe8aeb249ffdc0712fe3be28260490465625d2e2eb35ad688afee753a00&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 참조

https://namu.wiki/w/트랜스포머(인공신경망)

https://chonchony.tistory.com/entry/순환신경망-RNN의-문제점-기울기-소실-기울기-폭주-Gradient-Vanishing-Exploding

https://calmmimiforest.tistory.com/110


