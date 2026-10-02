---
source: knowledge-base
origin: notion
title: "Transfomer model 최적화 - KV Cache, PagedAttention, vLLM "
area: "아키텍처와 기술 소개"
tags: ["area/architecture", "area/llm", "concept/ai", "concept/transformer"]
created: "2025-08-04T06:05:00.000Z"
last_edited: "2025-08-04T06:31:00.000Z"
status: published
public: true
notion_id: "245172a5-56d6-80a6-a551-ee4438accbfe"
notion_url: "https://www.notion.so/Transfomer-model-KV-Cache-PagedAttention-vLLM-245172a556d680a6a551ee4438accbfe"
type: note
updated: 2026-07-07
---

# Transfomer model 최적화 - KV Cache, PagedAttention, vLLM 

## 요약

Transfomer model 기술 소개

LLM 기술 흐름과 구현 포인트를 비교하기 위한 기술 노트입니다.

## 핵심 포인트

- Transfomer model 기술 소개
- Transfomer model 최적화 - KV Cache, PagedAttention, vLLM
- KV Cache
- KV 캐싱 문제점
- 참조

## 지식 그래프

- [[wiki/mocs/Knowledge Base|Knowledge Base]]
- [[wiki/mocs/아키텍처와-기술-소개|아키텍처와 기술 소개]]

## 정리 내용

## Transfomer model 최적화 - KV Cache, PagedAttention, vLLM
Transfomer 모델을 최적화하기 위한 방식 KV Cache와 해당 방법의 단점을 보완한 Paged KV Cache방식 그리고 실제 응용 사례인 vLLM을 소개하는 페이지이다. 
### KV Cache
![[_attachments/notion/Transfomer-model-최적화---KV-Cache,-PagedAttention,-vLLM/245172a556d68144bcd6f0515b53ae43.png]]
트랜스포머 모델의 Attention 매커니즘을 짧게 소개하자면 Scaled Dot-Product Attention 연산을 여러 겹 올린 Multi-Head Attention 이 기본적이다.
이 모델 구조에서 Scaled Dot-Product Attention 연산을 반복적으로 수행하게 되는데 이 과정에서 중복된 연산이 많이 일어난다. 
Decoder에서 토큰을 생성하면서 Scaled Dot-Product Attention을 반복적으로 수행하는 과정 속에서 이전 토큰들의 계산을 중복적으로 계산을 하는데 이 과정을 Cache를 통해서 일정량의 저장비용을 통해 연산비용을 줄이는 기술이 KV Cache이다!
(KV Cahce인 이유는Key와 Value 영역의 정보를 Cache하기 때문에)
![[_attachments/notion/Transfomer-model-최적화---KV-Cache,-PagedAttention,-vLLM/245172a556d6819a9873f81162a76b1e.png]]
결국 백터의 내적 계산을 반복적으로 수행하는 것 이기 때문에
K^t에서 Token1,2,3을 기억하고 있다면 Token 4의 Attention을 구할 때 굳이 1,2,3을 다시 계산할 필요가 없다. 
#### KV 캐싱 문제점
KV 캐싱은 메모리 활용에 문제점이 있다. 
어탠션 매커니즘에서 output 토큰의 크기와 KV 캐싱의 내용이 각기 다를기 때문에 각각 메모리할당이 필요하다. 
메모리를 제대로 처리하지 못하면 단편화가 심하거나 낭비가 되는 부분이 많아 배치 크기가 제한된다.
vLLM(Paged Attention)이전의 KV캐싱은 연속적인 메모리 공간에 캐시들을 저장했다. 
KV캐시는 동적으로 커졌다가, 작아졌다가 하기 때문에 항상 미리 최대 길이의 메모리를 할당해놔야 했다. 
1. 내부 단편화(Internal Fragmentation) - 필요한 양 보다 더 큰 메모리 할당
1. 외부 단편화(External Fragmentation) - 메모링 할당/해제 작업 시 작은 메모리 공간들이 생기고 총 사용 가능한 메모리는 많지만, 실제 사용 가능한 메모리는 없는 현상이 생김 ( 작은 메모리들이라 연속된 할당이 불가능 )
1. 메모리 공유 불가능, ( 병렬 샘플링, Beam Search같은 병렬 디코딩 방식을 사용하는데, 연속된 공간에서 KV 캐시들이 할당되어 공유가 불가능합니다.) 

![[_attachments/notion/Transfomer-model-최적화---KV-Cache,-PagedAttention,-vLLM/245172a556d6818daed1e8adb163e05b.png]]
#### 참조

## 출처

- 원문: https://www.notion.so/Transfomer-model-KV-Cache-PagedAttention-vLLM-245172a556d680a6a551ee4438accbfe
- Vault path: wiki/notes/architecture/Transfomer-model-최적화---KV-Cache,-PagedAttention,-vLLM.md
