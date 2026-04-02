---
title: "Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters 논문 리뷰"
date: 2025-08-04 06:05:00 +0900
categories: [논문리뷰]
tags: [LLM, AI]
description: Test-Time Compute 소개
toc: true
comments: true
---

# Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters 

## 개요

**Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters (Arxiv, 2023/2024)**

기본적으로 LLM 모델의 성능을 높이기 위해서 파라미터 수를 계속해서 확대하고 있었다, 최근에는 추론 시점(Test-time) 시점에 발생하는 계산량을 늘려 성능을 개선하는 연구가 활발하게 시도되고 있다. 

**추론 시점의 연산량**

- 단순히 LLM에게 많은 양의 데이터를 많은 양의 파라미터를 넣는 것이 아니라 여러번 생각하고 깊게 생각하는 방법에 대해 연구가 되고 있는 것이다.
- 반복 수정, 다중 샘플링, 트리 검색 등
**난이도 별 접근법**

- 사람의 문제 풀이 과정을 보면 쉬운 답은 빠르게 답을 내고, 어려운 문제는 합리적인 추론을 위해 다양한 방식을 적용해본다.
- 이와 유사하게 LLM에게도 문제를 난이도에 따라 추론 전략을 다르게 갖고 가면 어떨까라는 논의 주제가 나온다. 
### Test-Time Compute 기법

- **Proposer(생성) + Verifier(검증) 구조**
- **Output-Level 추가 연산(Refinement, Searching 등)**
## 난이도에 따른 최적 접근 전략

### 3.1 쉬운 문제 vs. 어려운 문제

1. **쉬운 문제**
1. **어려운 문제**
### 3.2 Adaptive “Compute-Optimal” 전략

- 최종적으로, **문제의 난이도를 추정**한 뒤, 난이도 레벨에 따라 다른 추론 전략(Refinement vs. Best-of-N vs. Tree Search 등)을 사용하면, 주어진 **테스트 타임 연산 자원(추론 예산)**을 가장 효율적으로 쓸 수 있다는 결론을 제시한다.
- 실제 시스템 구현 관점에서, “현재 주어진 문제(프롬프트)가 쉽거나 어려움을 어떻게 판단할 것인가?”가 추가 과제로 남는다.
## 테스트 설계 및 결과 요약

### #1 난이도 분류

- <u>**난이도 정의**</u><u>: LLM이 2048회 샘플링할 때 pass@1(한 번에 정답 맞추는 비율)을 측정, 이를 5개 구간(quantile)으로 나누어 쉽고 어려운 문제를 분류.</u>
- 이 방식으로 분류한 난이도(“model-specific difficulty bins”)가, 기존에 인간이 수동 라벨링한 난이도보다도 **추론 성능 예측**에 더 잘 맞았다고 보고함.
### #2 Verifier / Reward Model

- 논문에서는 **PRM(Process-based Reward Model)**을 사용해, “풀이 과정” 단위로 정답 여부를 판별하는 모델을 제안/활용한다.
- PRM은 각 단계(step)의 정확도를 점수화하고, 이를 바탕으로 탐색(search) 알고리즘(beam-search, lookahead-search, 등)에 결합하거나 Best-of-N 선택 기준으로 쓴다.
- PRM 훈련 시: GPT-4 등으로 생성한 데이터나 Monte Carlo rollouts를 통해 얻은 중간 스텝별 correctness를 라벨로 활용.
### #3 Iterative Refinement 모델 (Revision Model)

- 단순히 LLM에게 “이 답안을 스스로 수정하라”는 프롬프트만 주어서는 큰 성능 향상이 어려운 경우가 많았다(“LLM cannot self-correct reasoning yet”).
- 이에, 논문에서는 **Revision Model**을 별도 파인튜닝:
- 이렇게 학습한 모델은 추론 시에도 **이전 답변을 문맥으로 받고, 새롭게 수정된 답변을 생성**할 수 있어 효과적인 iterative refinement가 가능했다.
### #4 실험 결과 (정성적 결론)

1. **쉬운 문제**
1. **어려운 문제**
1. **난이도에 따라 적응적으로 전략을 선택하면 가장 성능이 높음**
## 연구 의의 및 한계

### 의의

1. **Test-Time Compute  효과 증명**
1. **난이도에 따른 맞춤 접근**
1. **Revision Model의 효과**
### 한계 및 향후 과제

1. **난이도 추정 자체의 비용**
1. **Verifiers / RMs의 OOD 일반화**
1. **추론 비용 vs. 실제 서비스 적용**
## 결론

- **핵심 결론**:

