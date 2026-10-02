---
source: knowledge-base
origin: notion
title: "[LLM 원리 이해] RoPE : Rotary Positional Embedding"
area: "LLM"
tags: ["area/llm", "model/llama"]
created: "2025-07-29T05:48:00.000Z"
last_edited: "2025-07-31T07:17:00.000Z"
status: published
public: true
notion_id: "23f172a5-56d6-80ab-997f-f1d09faa757b"
notion_url: "https://www.notion.so/LLM-RoPE-Rotary-Positional-Embedding-23f172a556d680ab997ff1d09faa757b"
type: note
updated: 2026-07-07
---

# [LLM 원리 이해] RoPE : Rotary Positional Embedding

## 요약

LLM 아키텍처 설명

LLM 기술 흐름과 구현 포인트를 비교하기 위한 기술 노트입니다.

## 핵심 포인트

- LLM 아키텍처 설명
- 🧠 RoPE (Rotary Positional Encoding)란?
- 1. 기존 Absolute Positional Embedding의 한계
- 📍 1) 고정된 최대 시퀀스 길이
- 📍 2) 상대적 위치 정보를 잘 반영하지 못함

## 지식 그래프

- [[wiki/mocs/Knowledge Base|Knowledge Base]]
- [[wiki/mocs/LLM|LLM]]

## 정리 내용

## 🧠 RoPE (Rotary Positional Encoding)란?
Transformer는 순서를 고려하지 않는 Attention 구조이기 때문에, 토큰의 위치 정보를 표현하기 위해 positional embedding이 필수입니다.
RoPE는 이러한 위치 정보를 회전(rotation)이라는 방식으로 삽입하여, 자연스럽게 상대적 위치 정보까지 함께 반영하는 기술입니다
### 1. 기존 Absolute Positional Embedding의 한계
#### 📍 1) 고정된 최대 시퀀스 길이
- Learned embedding 방식은 사전 정의된 최대 길이 내에서만 동작합니다. 이를 넘으면 확장할 수 없습니다.
- Sinusoidal embedding도 학습되지 않은 길이에는 일반화가 제한적입니다.
#### 📍 2) 상대적 위치 정보를 잘 반영하지 못함
- 서로 멀리 떨어진 두 위치(예: 2와 500)는 벡터 간 유사성이 전혀 반영되지 않으므로, 상대적 의미를 추정하기 어렵습니다.
#### 📍 3) 일반화와 extrapolation 한계
- 새로운 문장을 길게 연결하거나 테스트 시퀀스가 학습 시퀀스보다 길 경우, embedding이 제대로 작동하지 않아 퍼플렉시티가 급등하기도 합니다. 
### 2. RoPE의 핵심 아이디어 및 메커니즘
RoPE는 쿼리(Q)와 키(K)의 임베딩에 회전 행렬(rotation matrix) 을 적용해서 순서 정보를 포함시킵니다:
![[_attachments/notion/LLM-원리-이해-RoPE-Rotary-Positional-Embedding/23f172a556d6807695a3eb4ec912105a.png]]
RoPE는 백터의 회전을 통해 위치를 표현합니다, 백터의 회전은 복소수( Complex Number) 를 먼저 이해 해야하는데요.
복소수를 A+Bi 형태로 표현하여 2차원 평면에 복소평면을 그리면 위 그림과 같습니다.
실수축과 허수축으로 구성되어있는 형식입니다.
여기서 Euler 공식을 통해 회전시킬 수 있습니다.
![[_attachments/notion/LLM-원리-이해-RoPE-Rotary-Positional-Embedding/23f172a556d680baad27d59d264fce22.png]]
복소수에 eⁱᶿ를 곱하면 각도 θ만큼 회전을 한다는 공식입니다.
예를 들어 A+Bi라는 벡터를 eⁱᶿ로 곱하면, 벡터의 크기는 유지하고 각도만 θ만큼 회전하여 새로운 벡터를 얻을 수 있다는 것 입니다.
![[_attachments/notion/LLM-원리-이해-RoPE-Rotary-Positional-Embedding/23f172a556d680fd8aa5c93f5bb824c5.png]]
### 3. RoPE의 주요 장점
#### ✅ 1) 길이 확장성 (Context Extrapolation)
학습 시보다 긴 시퀀스에도 embedding 벡터 재생성이 가능하여, 문맥 길이 초과 문제를 회피할 수 있습니다 
#### ✅ 2) 상대적 위치 표현
회전을 통해 dot product가 상대 거리 정보만 반영되므로, 토큰 간의 상대적 관계를 자연스럽게 반영합니다 
#### ✅ 3) Linear attention과도 호환 가능
RoPE는 기존 relative embedding보다 구현이 단순하고, linear self-attention 구조에도 결합할 수 있다는 이점이 있습니다 
#### ✅ 4) 자연어 모델과 언어 장비에 강건한 사용성
예를 들어, 최신 LLM에서 RoPE는 Gemma 7B, LLaMA 3 등에서 활용되며, 토큰 간 의미 관계를 효과적으로 반영하는 것으로 알려져 있습니다 
#### ✅ 5) 의미와 위치 정보를 함께 담는 효율성
기존 Transfomer의 방식은 SelfAttention과정에서 Pt(포지션 임베딩)을 적용하는 방식입니다.
RoPE의 아이디어는 임베딩은 그대로 두고, Query(Q) / Key(K) 계산 과정에서 Rotation Matrix를 반영하자는 아이디어 입니다.
같은 단어가 여러번 등장해도 상대적인 위치를 잘 반영하여 의미를 파악할 수 있는 장점이 있습니다.
![[_attachments/notion/LLM-원리-이해-RoPE-Rotary-Positional-Embedding/23f172a556d6808f93bce67d5566b4b6.png]]
예를 들어 “애플 애플 애플 애플” 이라는 문장이 있을 때
기존 Transfomer 모델의 경우 Q/K 값이 같습니다, 상대 위치 정보를 파악할 수 없지만
RoPE 방식을 쓴다면 각 토큰의 위치별로 Rotation 값이 다르기 때문에 상대적인 각도(위치)가 반영됩니다.
![[_attachments/notion/LLM-원리-이해-RoPE-Rotary-Positional-Embedding/23f172a556d6800db569fcce20f76b00.png]]
### 참고
- [https://medium.com/@hugmanskj/mastering-llama-rotary-positional-embedding-rope-이해하기-9b1963a22852](https://medium.com/@hugmanskj/mastering-llama-rotary-positional-embedding-rope-%EC%9D%B4%ED%95%B4%ED%95%98%EA%B8%B0-9b1963a22852)
- [https://en.wikipedia.org/wiki/Transformer_(deep_learning_architecture)?utm_source=chatgpt.com](https://en.wikipedia.org/wiki/Transformer_%28deep_learning_architecture%29?utm_source=chatgpt.com)
- [https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/01584.pdf?utm_source=chatgpt.com](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/01584.pdf?utm_source=chatgpt.com)
- [https://medium.com/ai-insights-cobet/rotary-positional-embeddings-a-detailed-look-and-comprehensive-understanding-4ff66a874d83](https://medium.com/ai-insights-cobet/rotary-positional-embeddings-a-detailed-look-and-comprehensive-understanding-4ff66a874d83)
- [https://karthick.ai/blog/2024/Rotatory-Position-Embedding-(RoPE)/?utm_source=chatgpt.com](https://karthick.ai/blog/2024/Rotatory-Position-Embedding-%28RoPE%29/?utm_source=chatgpt.com)
- [https://newsletter.theaiedge.io/p/all-about-the-modern-positional-encodings?utm_source=chatgpt.com](https://newsletter.theaiedge.io/p/all-about-the-modern-positional-encodings?utm_source=chatgpt.com)

## 출처

- 원문: https://www.notion.so/LLM-RoPE-Rotary-Positional-Embedding-23f172a556d680ab997ff1d09faa757b
- Vault path: wiki/notes/llm/LLM-원리-이해-RoPE-Rotary-Positional-Embedding.md
