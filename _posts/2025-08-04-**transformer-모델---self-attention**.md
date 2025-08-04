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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/1e7f5e6f-9228-4d68-9d1d-6554327138c3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666PTTXKXP%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T072123Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIFGDJrDwqO%2Bf9QzhwI29QPFdV5DPoCsO9JYrL%2B8ggo0kAiEA5bnMSA5qCbls3cTfQR%2F5gWh9aOiWpGk%2FsknbV1h38ywq%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDINlG7cBdao9fP%2FvIircA5rgvMZkNH4V1xd%2B70XTPnpIn3K%2BwSyVrOIsg%2BfsrY%2FhlQEhTNq23DUuK%2Bxp39MQQMmeuKANkcRa4Q4CMlhGg8c4iaKkvOVt%2FYI6h7zCxYwjzeZYiFlnXCD4LjAPFRaAwBf%2F59%2F6I2o%2FvholHtMWQ2WYvrmNR9GCfir7WY%2FaXNIUiMK0WcV91oFhamY4UnPAr62NRoL4sLA%2BA46u9Hv0Uw5XIe%2BoWlC6DXZKyb8KV937iYjvQKpWO4qPsqFP%2FGzqh%2FuILiBTJ2qKIrUejt3U9byuGVm8EsaXIGH%2FOUOPXlVmQX1e0kQUsWmcehxM6KQSdOa0EpNyfh52NXu5rsTzZhRJuYUsZmy134seY8Saq0u9vgLoFaR6JGVkS0KRUBesw0ZOy3Ha2ii8jWHRekyUQPXAqTCdHBPDJgxi4KxGMcOC2qydwNUkoKvP9wwVdu9QiqGaK0p%2F91Lvzc6GjimfwBOhe4yuG4YxlPYqE%2BPP%2F1U%2BUhyTx%2F%2F%2FIpjEZXS1fKQrMJ3oRXLJEw3cY%2FPsn8EvCRk0HdKEvnEDDen70XAfib%2FXbGxEmpfuZL4FyigN2Z6xFp%2F5q%2F5pX%2FvxEgIEtEZFqMdfJPwaojq8Gnn7bpf9BMkTfxM%2Fr024ClsLdUQfMIG4wcQGOqUBGLIJu43Fj2rsVQbjquxdCe9LqeBFS9%2FWw7aNTdIzY2vZxw%2Fih%2FrwGNTs3ezExGUhzj4IkiIIqqMF8mE5%2FyOH9M3Mts0jftwGumjC205s0Pz%2BcvpMXCYHQZdO6J12TsUquv3%2BcbP8dJScMNLUiMYtch1DaCTB%2FXPUfghIY6jaClaLwGe0bICS%2Fq9zemSKP4fwqXXcRMD63Wlif5TiohINNGlZNUAj&X-Amz-Signature=c8feeb0bebea0bd326bdc443d23b2d8a7ffb9715cb1fb7ae0b5b63d2c502b376&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### TOBE

이런 구조를 바꾼게 바로 2017년 NIPS에서 'Attention Is All You Need’ 라는 논문이다. 

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/6e9cd139-802d-46d7-a36a-93043fd1cafc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666PTTXKXP%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T072123Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIFGDJrDwqO%2Bf9QzhwI29QPFdV5DPoCsO9JYrL%2B8ggo0kAiEA5bnMSA5qCbls3cTfQR%2F5gWh9aOiWpGk%2FsknbV1h38ywq%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDINlG7cBdao9fP%2FvIircA5rgvMZkNH4V1xd%2B70XTPnpIn3K%2BwSyVrOIsg%2BfsrY%2FhlQEhTNq23DUuK%2Bxp39MQQMmeuKANkcRa4Q4CMlhGg8c4iaKkvOVt%2FYI6h7zCxYwjzeZYiFlnXCD4LjAPFRaAwBf%2F59%2F6I2o%2FvholHtMWQ2WYvrmNR9GCfir7WY%2FaXNIUiMK0WcV91oFhamY4UnPAr62NRoL4sLA%2BA46u9Hv0Uw5XIe%2BoWlC6DXZKyb8KV937iYjvQKpWO4qPsqFP%2FGzqh%2FuILiBTJ2qKIrUejt3U9byuGVm8EsaXIGH%2FOUOPXlVmQX1e0kQUsWmcehxM6KQSdOa0EpNyfh52NXu5rsTzZhRJuYUsZmy134seY8Saq0u9vgLoFaR6JGVkS0KRUBesw0ZOy3Ha2ii8jWHRekyUQPXAqTCdHBPDJgxi4KxGMcOC2qydwNUkoKvP9wwVdu9QiqGaK0p%2F91Lvzc6GjimfwBOhe4yuG4YxlPYqE%2BPP%2F1U%2BUhyTx%2F%2F%2FIpjEZXS1fKQrMJ3oRXLJEw3cY%2FPsn8EvCRk0HdKEvnEDDen70XAfib%2FXbGxEmpfuZL4FyigN2Z6xFp%2F5q%2F5pX%2FvxEgIEtEZFqMdfJPwaojq8Gnn7bpf9BMkTfxM%2Fr024ClsLdUQfMIG4wcQGOqUBGLIJu43Fj2rsVQbjquxdCe9LqeBFS9%2FWw7aNTdIzY2vZxw%2Fih%2FrwGNTs3ezExGUhzj4IkiIIqqMF8mE5%2FyOH9M3Mts0jftwGumjC205s0Pz%2BcvpMXCYHQZdO6J12TsUquv3%2BcbP8dJScMNLUiMYtch1DaCTB%2FXPUfghIY6jaClaLwGe0bICS%2Fq9zemSKP4fwqXXcRMD63Wlif5TiohINNGlZNUAj&X-Amz-Signature=4e7b6c52572c0a990637deef73bb5fdc49dcf8a6c36baa7ae648f4a26ad9857c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 참조

https://namu.wiki/w/트랜스포머(인공신경망)

https://chonchony.tistory.com/entry/순환신경망-RNN의-문제점-기울기-소실-기울기-폭주-Gradient-Vanishing-Exploding

https://calmmimiforest.tistory.com/110


