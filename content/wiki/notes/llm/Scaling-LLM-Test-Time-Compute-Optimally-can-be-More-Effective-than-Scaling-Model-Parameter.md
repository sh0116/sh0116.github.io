---
source: knowledge-base
origin: notion
title: "Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters 논문 리뷰"
area: "LLM"
tags: ["area/llm", "concept/ai"]
created: "2025-08-04T06:05:00.000Z"
last_edited: "2025-08-04T06:29:00.000Z"
status: published
public: true
notion_id: "245172a5-56d6-80eb-a43a-ea87e3e13745"
notion_url: "https://www.notion.so/Scaling-LLM-Test-Time-Compute-Optimally-can-be-More-Effective-than-Scaling-Model-Parameters-245172a556d680eba43aea87e3e13745"
type: note
updated: 2026-07-07
---

# Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters 논문 리뷰

## 요약

Test-Time Compute 소개

LLM 기술 흐름과 구현 포인트를 비교하기 위한 기술 노트입니다.

## 핵심 포인트

- Test-Time Compute 소개
- Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters
- 개요
- Test-Time Compute 기법
- 난이도에 따른 최적 접근 전략

## 지식 그래프

- [[wiki/mocs/Knowledge Base|Knowledge Base]]
- [[wiki/mocs/LLM|LLM]]

## 정리 내용

## Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters 
> [!note] 테스트 타임에서의 계산량 증대가 때로는 모델 파라미터 스케일업보다 더 큰 가성비(성능 향상)를 제공할 수 있음을 잘 보여주는 연구 사례이며, 
  이를 구현할 때는 문제 난이도에 따른 ‘적응적 전략(adaptive strategy)’이 핵심이라는 점이 주된 메시지다.
### 개요
[Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters (Arxiv, 2023/2024)](https://arxiv.org/abs/2408.03314)
기본적으로 LLM 모델의 성능을 높이기 위해서 파라미터 수를 계속해서 확대하고 있었다, 최근에는 추론 시점(Test-time) 시점에 발생하는 계산량을 늘려 성능을 개선하는 연구가 활발하게 시도되고 있다. 
추론 시점의 연산량
- 단순히 LLM에게 많은 양의 데이터를 많은 양의 파라미터를 넣는 것이 아니라 여러번 생각하고 깊게 생각하는 방법에 대해 연구가 되고 있는 것이다.
- 반복 수정, 다중 샘플링, 트리 검색 등
난이도 별 접근법
- 사람의 문제 풀이 과정을 보면 쉬운 답은 빠르게 답을 내고, 어려운 문제는 합리적인 추론을 위해 다양한 방식을 적용해본다.
- 이와 유사하게 LLM에게도 문제를 난이도에 따라 추론 전략을 다르게 갖고 가면 어떨까라는 논의 주제가 나온다. 
#### Test-Time Compute 기법
- Proposer(생성) + Verifier(검증) 구조
  - Proposer: 답변을 생성하는 역할(기존 LLM)
  - Verifier(Reward Model·RM 등): 생성된 답변이 얼마나 올바른지, 유용한지 점수를 매기는 모델
  - 이때 Verifier를 활용해 잘못된 답변을 걸러내거나, 올바른 답변 쪽으로 탐색을 좁혀나가는 식으로 추가 계산을 수행할 수 있다.
- Output-Level 추가 연산(Refinement, Searching 등)
  - Best-of-N: 한 번에 병렬로 N개의 답변을 생성 후, 그중 최고 점수를 가진(혹은 가장 적합한) 답을 고르기
  - Iterative Refinement(수정): 답변을 한 번 생성한 후, 필요한 경우 모델이 스스로 수정 과정을 여러 번 거치도록 함
  - Tree Search: Verifier(혹은 RM)를 결합하여, 단계별로 분기 탐색하면서 최적 해법을 찾는 방식
### 난이도에 따른 최적 접근 전략
#### 3.1 쉬운 문제 vs. 어려운 문제
1. 쉬운 문제
  - 이미 한두 번의 시도만으로도 비교적 괜찮은 답변이 나오므로, iterative refinement(수정)가 더 효율적일 수 있음.
  - 즉, N번 병렬 샘플링(Best-of-N)보다도 “하나의 샘플(초안)을 만들고 → 모델이 자체적으로 수정”을 여러 번 수행하는 편이 계산 비용 대비 성능 개선에 유리.
  - 예: 수학 문제에서 모델이 대체로 맞으나 소소한 오류가 있을 때, 해당 오류를 점진적으로 제거하는 식.
1. 어려운 문제
  - 다양한 “고차원적 아이디어(풀이 접근법)”가 필요할 수 있으므로, 독립적으로 여러 답안을 생성하거나 Tree Search처럼 대폭적인 탐색을 하는 편이 효과적.
  - 즉, 한 가지 답안을 붙잡고 계속 수정하는 것만으로는 국소적인 해법(로컬 옵티마)에 빠질 위험이 있으며, 병렬로 다른 경로를 시도하거나, 트리 형태로 다양한 부분 풀이를 동시에 살펴보는 것이 중요.
#### 3.2 Adaptive “Compute-Optimal” 전략
- 최종적으로, 문제의 난이도를 추정한 뒤, 난이도 레벨에 따라 다른 추론 전략(Refinement vs. Best-of-N vs. Tree Search 등)을 사용하면, 주어진 **테스트 타임 연산 자원(추론 예산)**을 가장 효율적으로 쓸 수 있다는 결론을 제시한다.
- 실제 시스템 구현 관점에서, “현재 주어진 문제(프롬프트)가 쉽거나 어려움을 어떻게 판단할 것인가?”가 추가 과제로 남는다.
  - 논문에서는 오라클 접근(정답 여부가 아는 상황)과 모델 기반 접근(Verifier 점수로 추정) 모두를 실험하여 비교했다.
### 테스트 설계 및 결과 요약
#### #1 난이도 분류
- 난이도 정의: LLM이 2048회 샘플링할 때 pass@1(한 번에 정답 맞추는 비율)을 측정, 이를 5개 구간(quantile)으로 나누어 쉽고 어려운 문제를 분류.
- 이 방식으로 분류한 난이도(“model-specific difficulty bins”)가, 기존에 인간이 수동 라벨링한 난이도보다도 추론 성능 예측에 더 잘 맞았다고 보고함.
#### #2 Verifier / Reward Model
- 논문에서는 PRM(Process-based Reward Model)을 사용해, “풀이 과정” 단위로 정답 여부를 판별하는 모델을 제안/활용한다.
- PRM은 각 단계(step)의 정확도를 점수화하고, 이를 바탕으로 탐색(search) 알고리즘(beam-search, lookahead-search, 등)에 결합하거나 Best-of-N 선택 기준으로 쓴다.
- PRM 훈련 시: GPT-4 등으로 생성한 데이터나 Monte Carlo rollouts를 통해 얻은 중간 스텝별 correctness를 라벨로 활용.
#### #3 Iterative Refinement 모델 (Revision Model)
- 단순히 LLM에게 “이 답안을 스스로 수정하라”는 프롬프트만 주어서는 큰 성능 향상이 어려운 경우가 많았다(“LLM cannot self-correct reasoning yet”).
- 이에, 논문에서는 Revision Model을 별도 파인튜닝:
  1. 높은 온도에서 여러 개의 독립 샘플을 생성
  1. 이 중 정답/오답을 묶어서 “multi-turn 롤아웃” 데이터를 만든 후
  1. “이전 오답을 바탕으로 최종 정답을 만들어보라” 식의 학습을 진행
- 이렇게 학습한 모델은 추론 시에도 이전 답변을 문맥으로 받고, 새롭게 수정된 답변을 생성할 수 있어 효과적인 iterative refinement가 가능했다.
#### #4 실험 결과 (정성적 결론)
1. 쉬운 문제
  - Revision(Iterative Refine) 모델을 몇 번 반복 시도하는 방식이, 병렬 Best-of-N보다 효율이 높았다.
1. 어려운 문제
  - 병렬 Re-Sampling 혹은 Tree Search를 활용하는 것이 더 나은 성능 개선을 보였다.
1. 난이도에 따라 적응적으로 전략을 선택하면 가장 성능이 높음
  - “적응적(adaptive) 전략”은 난이도를 판별하고, 그에 맞춰 (Refinement vs. Searching vs. 단순 Best-of-N)을 할당.
### 연구 의의 및 한계
#### 의의
1. Test-Time Compute  효과 증명
  - 모델 파라미터를 키우지 않고도, 추론 과정에서 필요한 계산을 늘리는 것만으로 상당한 성능 향상이 가능함을 실험적으로 제시했다.
1. 난이도에 따른 맞춤 접근
  - 모든 문제에 똑같이 Best-of-N 혹은 똑같이 Iterative Refine만 쓰는 것은 최적이 아님을 보여준다.
  - 실제 시스템에서는 문제 특성(난이도)에 따라 다른 방식을 동적으로 적용함으로써, 추론 비용 vs. 성능의 밸런스를 극대화할 수 있다는 점이 핵심.
1. Revision Model의 효과
  - 단순 self-correct 프롬프트보다도, 별도로 파인튜닝된 모델(iterative refinement)과 Verifier를 사용했을 때 실제로 의미 있는 성능 향상을 달성.
  - 이는 “LLM이 자기 실수를 완벽히 인지·수정할 수 없는 한계”를 대안적으로 해결하려면, 충분한 학습 데이터와 추가 모델 구조가 필요함을 시사한다.
#### 한계 및 향후 과제
1. 난이도 추정 자체의 비용
  - 난이도를 추정하기 위해서는 어느 정도 샘플링과 Verifier 계산을 해야 하므로, 추가 비용이 발생한다.
  - “탐색(exploration) vs. 활용(exploitation)”의 관점에서, 실제 시스템은 난이도를 얼마나 정교하게 측정할지와 바로 풀이에 들어갈지 사이의 트레이드오프를 고려해야 한다.
1. Verifiers / RMs의 OOD 일반화
  - PRM 등의 Verifier가 훈련되지 않은(Out-of-distribution) 문제 유형에서 얼마나 일관된 성능을 낼지는 여전히 불확실.
  - 특히 복잡하고 창의적인 추론이 필요한 문제들에서 얼마나 Robust한지도 추가 연구 필요.
1. 추론 비용 vs. 실제 서비스 적용
  - 연구에서는 “추론 시점에서의 계산량”이 사실상 무한히 가능하다고 가정할 수 있지만, 실제 서비스 환경에서는 토큰 비용, 지연시간(latency) 등이 중요.
  - 이를 최적화하려면 “적응적 전략을 설계하되, 제한된 시간/비용 안에서의 효율성”을 더 면밀히 연구해야 한다.
### 결론
- 핵심 결론:
  - 모델 크기를 단순히 늘리기만 하는 것보다, 문제 난이도별로 다른 기법(iterative refinement, parallel sampling, tree search, verifier 활용 등)을 테스트 타임에 적용하는 편이 계산 대비 성능 향상 폭이 더 클 수 있다.
  - 특히 쉬운 문제와 어려운 문제를 구분해, 쉬운 문제에는 iterative refinement, 어려운 문제에는 tree search(혹은 병렬 샘플링) 등의 전략을 쓰는 “Adaptive Compute-Optimal” 방식이 최적임을 다수 실험을 통해 보여주었다.
> [!note] 테스트 타임에서의 계산량 증대가 때로는 모델 파라미터 스케일업보다 더 큰 가성비(성능 향상)를 제공할 수 있음을 잘 보여주는 연구 사례이며, 
  이를 구현할 때는 문제 난이도에 따른 ‘적응적 전략(adaptive strategy)’이 핵심이라는 점이 주된 메시지다.

## 출처

- 원문: https://www.notion.so/Scaling-LLM-Test-Time-Compute-Optimally-can-be-More-Effective-than-Scaling-Model-Parameters-245172a556d680eba43aea87e3e13745
- Vault path: wiki/notes/llm/Scaling-LLM-Test-Time-Compute-Optimally-can-be-More-Effective-than-Scaling-Model-Parameter.md
