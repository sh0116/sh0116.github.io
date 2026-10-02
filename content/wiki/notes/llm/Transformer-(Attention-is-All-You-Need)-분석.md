---
source: knowledge-base
origin: notion
title: "Transformer (Attention is All You Need) 분석 "
area: "LLM"
tags: ["area/llm", "concept/ai", "concept/transformer"]
created: "2025-08-04T06:05:00.000Z"
last_edited: "2025-08-04T06:29:00.000Z"
status: published
public: true
notion_id: "245172a5-56d6-80ab-84a0-ea2242c3b1ab"
notion_url: "https://www.notion.so/Transformer-Attention-is-All-You-Need-245172a556d680ab84a0ea2242c3b1ab"
type: note
updated: 2026-07-07
---

# Transformer (Attention is All You Need) 분석 

## 요약

Attention is All You Need 리뷰

LLM 기술 흐름과 구현 포인트를 비교하기 위한 기술 노트입니다.

## 핵심 포인트

- Attention is All You Need 리뷰
- Transformer (Attention is All You Need)
- Transformer Encoder / Decoder
- Encoder 방식
- Encoder Block

## 지식 그래프

- [[wiki/mocs/Knowledge Base|Knowledge Base]]
- [[wiki/mocs/LLM|LLM]]

## 정리 내용

## Transformer (Attention is All You Need)
### Transformer Encoder / Decoder
트랜스포머는 크게 Encoder / Decoder로 나뉜다. 
Encoder 는 문장(Sentence)을 받아 Vector(Context)로 반환하고
Decoder는 Vector(Context)를 받아 문장(Senetence)로 반환한다.

![[_attachments/notion/Transformer-(Attention-is-All-You-Need)-분석/245172a556d681199201d510923e675d.png]]
#### Encoder 방식
![[_attachments/notion/Transformer-(Attention-is-All-You-Need)-분석/245172a556d6814b92a1cb956cb8c669.png]]
Encoder 는 N개의 Encoder Block 으로 구성되어 있다.  (논문에서는 N = 6으로 사용했다. )
Encoder Block의 Input/output 형태는 동일하다. 어떤 Matrix 를 Input으로 받는다고 했을 때, output 역시 해당 Matrix와 같은 형태(Shape)를 갖고있다. → Shape이 바뀌지 않는다 (멱등하다.)
각 Encoder 모델은 연결되어 있다. N-1 EB 와 N EB가 연결되어 있다. 각 Input / Output Matrix Shape도 같기 때문에 전체 Encoder의 Shape은 항상 일정하다 (멱등하다.)
Encoder Block을 여러 겹으로 쌓는 것인가? 
Encoder Block은 Input으로 들어오는 문장을 Vector화 하여 Context로 만든다, Context로 만들어진 문장은 추상화되어 더 넓은 관점으로 높은 차원에서 고려될 수 있는 정보로 바뀌고 이 과정을 반복하면 매우 높은 차원의(추상화된 정보) Context가 생성되고 더 많은 관점에서 피처들을 뽑아낼 수 있다.

문장 → 높은 차원의 Context → 보다 더 높은 차원의 Context → …. → Output

일단 이 정도로만 하고 넘어가면 될 것 같다. 
### Encoder Block
![[_attachments/notion/Transformer-(Attention-is-All-You-Need)-분석/245172a556d681a09f14e22739ee84bc.png]]
Encoder Block은 크게 Multi-Head Attention Layer, Position-wise Feed-Forward Layer로 구성된다.
![[_attachments/notion/Transformer-(Attention-is-All-You-Need)-분석/245172a556d681a89c68ef0fb74bb57f.png]]
Multi-Head Attention은 Attention을 여러 개 수행하는 layer이다. 
Multi-Head Attention을 이해하기 위해서는 Scaled Dot-Product Attention에 대해 먼저 알아야만 한다. Attention이라는 것은 넓은 범위의 전체 data에서 특정한 부분에 집중한다는 의미이다. 
Scaled Dot-Product Attention 자체를 줄여서 Attention 이라고 한다.
> The animal didn’t cross the street, because it was too tired.
위 문장에서 ‘it’은 무엇을 지칭하는 것일까? 
사람이라면 직관적으로 ‘animal’과 연결지을 수 있지만, 컴퓨터는 ‘it’이 ‘animal’을 가리키는지, ‘street’를 가리키는지 알지 못한다.
Attention은 이러한 문제를 해결하기 위해 두 token 사이의 연관 정도를 계산해내는 방법론이다. 
위의 경우에는 같은 문장 내의 두 token 사이의 Attention을 계산하는 것이므로, Self-Attention이라고 부른다. 반면, 
서로 다른 두 문장에 각각 존재하는 두 token 사이의 Attention을 계산하는 것을 Cross-Attention이라고 부른다.

#### Attention 모델의 기본 구조
Q, K, V
Attention 계산에는 Query, Key, Value라는 3가지 vector가 사용된다. 각 vector의 역할을 정리하면 다음과 같다.
1. Query: 입력 시퀸스에서 관련 부분을 찾으려고하는 현재의 상태 벡터 (소스)
1. Key: 관계의 연관도를 찾기 위해 Query와 비교하는데 사용되는 벡터 (타겟)
1. Value: 특정 Key에 해당하는 입력 시퀸스의 가중치를 구하는데 사용되는 벡터 (벨류)
#### Scaled Dot-Product Attention 상세
![[_attachments/notion/Transformer-(Attention-is-All-You-Need)-분석/245172a556d681b5ab1cf1788b329dfc.png]]
1. Input에는 Position Encoding + Embeding된 데이터가 들어온다.
1. Linear에서는 1번 Input Matrix에 대해 차원 축소와 출력 Matrix의 모양과 맞춰주는 역할을 한다. 
1. MatMUL에서는 Query와 Key 행렬의 내적을 통해 Attention Score Matrix 를 만든다. 
  1. Attention Score Matrix 의 의미는 Key와 Query간의 유사도를 행렬로 나타내는 것이다.
1. 이후에 Scale과 SoftMax를 통해서 각 유사도의 값의 합(항목별)이 1이 되도록 SoftMax해준다.
![[_attachments/notion/Transformer-(Attention-is-All-You-Need)-분석/245172a556d681bd8c44cfa2f0176215.png]]
![[_attachments/notion/Transformer-(Attention-is-All-You-Need)-분석/245172a556d6819cae03d8c348f15841.png]]
마지막에 Value Matrix와 내적한다. 
조금 주요 부분을 리즈너블하게 설명을 하자면
![[_attachments/notion/Transformer-(Attention-is-All-You-Need)-분석/245172a556d681c88c80f0db574e4455.png]]
1. Matmul에서 Query와 Key 간의 유사도를 계산한다, 각 단어(토큰) 간의 유사도를 계산해서 관련 있는 부분은 더 많은 정보를, 유사도가 적은 단어(토큰)은 적은 정보를 가져간다. 
  1. 각 토큰이 전체 토큰에서 어떤 역할을 하고 어떤 토큰과 연관이 강한지 표현
1. 마지막에 Value를 내적하여 Attention Score Matrix를 적용한다.
  1. 각 Token에 해당 Token의 전체 Token의 유사도 값을 담는다. 
  1. N번째 토큰의 경우, N번째 토큰이 전체 토큰에서 각각 어떤 중요도(Attention) 를 갖는지 나타낸다. 
  1. 1번 Matrix 현재 토큰이 전체 토큰에서 어떤 역할을 하는지에 대한 데이터를 Matrix로써, 중요한 데이터를 많이 남기고 중요하지 않은 데이터를 적게 남게한다. 
  1. 해당 토큰에 연관된(중요한) 토큰을 집중하게 한다.
1. 이걸 Multi Head 방식으로 여러 겹 쌓는 이유는 위 그림처럼 다양한 관점에서 더 복잡한 관계성을 파악할 수 있는 장점이 있기 때문이다. 
참조
[https://www.blossominkyung.com/deeplearning/transformer-mha](https://www.blossominkyung.com/deeplearning/transformer-mha)
[https://tech.scatterlab.co.kr/vllm-implementation-details/](https://tech.scatterlab.co.kr/vllm-implementation-details/)
[https://cpm0722.github.io/pytorch-implementation/transformer](https://cpm0722.github.io/pytorch-implementation/transformer)

## 출처

- 원문: https://www.notion.so/Transformer-Attention-is-All-You-Need-245172a556d680ab84a0ea2242c3b1ab
- Vault path: wiki/notes/llm/Transformer-(Attention-is-All-You-Need)-분석.md
