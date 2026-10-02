---
source: knowledge-base
origin: notion
title: "How to Safeguard AI Agents for Customer Service with NVIDIA NeMo Guardrails - 소개 "
area: "아키텍처와 기술 소개"
tags: ["area/architecture", "area/llm", "vendor/nvidia"]
created: "2025-08-04T06:05:00.000Z"
last_edited: "2025-08-04T06:28:00.000Z"
status: published
public: true
notion_id: "245172a5-56d6-8004-83b9-c5299cecd414"
notion_url: "https://www.notion.so/How-to-Safeguard-AI-Agents-for-Customer-Service-with-NVIDIA-NeMo-Guardrails-245172a556d6800483b9c5299cecd414"
type: note
updated: 2026-07-07
---

# How to Safeguard AI Agents for Customer Service with NVIDIA NeMo Guardrails - 소개 

## 요약

NVIDIA NeMo Guardrails 소개

LLM 기술 흐름과 구현 포인트를 비교하기 위한 기술 노트입니다.

## 핵심 포인트

- NVIDIA NeMo Guardrails 소개
- #1 NeMo Guardrails란
- #2 NeMo Guardrails 기능 및 특징
- #3 NeMo Guardrails 예시
- #4 결론

## 지식 그래프

- [[wiki/mocs/Knowledge Base|Knowledge Base]]
- [[wiki/mocs/아키텍처와-기술-소개|아키텍처와 기술 소개]]

## 정리 내용

## #1 NeMo Guardrails란
- NVIDIA에서 개발한 오픈 소스 LIB로, LLM 기반 Application 에 안전 장치(가드레일)을 설치하여 모델에서 예상하지 못한 대답이나 민감정보를 노출하지 않도록 제어하는 기술임
  - 컨텐츠 및 맥락 제한 : AI가 부적절하거나 회사 정책에 어긋나는 발언을 하지 않도록 제어한다. 
  - 브랜드 정체성과 일관성 : 기업의 브랜드 가치나 톤에 맞는 일관적인 답변을 한다.
  - 발언 제어 : 개인정보, 저작권, 윤리, 규제에 맞는 않는 발언을 방지한다.
## #2 NeMo Guardrails 기능 및 특징
- 룰(규칙) 기반 프레임워크
  - NeMo Guardrails는 룰(규칙) 정의와 템플릿 기반의 설정을 통해서 LLM의 응답을 제어한다.
    - Ex : 사용자가 신용카드 번호를 질문하면, 그 정보를 노출하지 않고 ‘보안 절차상 해당 정보를 공유할 수 없다’ 라고 답변하는 식으로 룰을 정할 수 있다. 
- 대화 흐름 관리
  - 요청이 허용된 범위 인지, 다른 문맥으로 바뀌어야 하는지 파악해 대화(채팅) 을 이끌어간다.
  - 필요 시 특정 절차로 자동 전환하는 로직을 포함할 수 있다. (ex : 상담사 연결)
- 세분화된 컨텐츠 필터링 
  - 폭력, 차별, 음란 관련 콘텐츠 및 내부적으로 정한 부적절한 표현까지 필터링이 가능하다.
  - 금칙어 필터링이 아닌 문맥적 판단을 통해 응답을 수정한다.
- 개인정보 보호와 보안
  - 사용자나 기업에 민감한 정보를 모델이 학습 데이터로 활용하거나 외부에 유출하지 않도록 특별 관리가 가능
- 멀티 모달 확장 
  - 음성(콜센터), 텍스트입력(챗봇, 이메일, SNS) 등 다양한 입력에 대해 대응할 수 있다.
## #3 NeMo Guardrails 예시
![[_attachments/notion/How-to-Safeguard-AI-Agents-for-Customer-Service-with-NVIDIA-NeMo-Guardrails---소개/245172a556d6815f8fe4eda0157e0773.png]]
[NVIDIA Tech Blog](https://developer.nvidia.com/blog/how-to-safeguard-ai-agents-for-customer-service-with-nvidia-nemo-guardrails/?ncid=em-anno-992783&nvweb_e=RxdFu0-dUQxfxKZiwOIPm2US1XFESXCNkvQxVrppAtu3eU9W_ynGFRWI3DLCnxfVFhQ2u1nGF3P_2LjrG9McUQ&mkt_tok=MTU2LU9GTi03NDIAAAGYDtEl_8qTmVUYtgaCwaGLQ5KXC3j4dj6z8KOChtsSuTRmZHeW1dXqos3qNSefU_XvCQJBvBf_qf4A-XvoB1XlRx-G9iuSgNWOc5VvXku4nxMW0ZqD), figure 1
![[_attachments/notion/How-to-Safeguard-AI-Agents-for-Customer-Service-with-NVIDIA-NeMo-Guardrails---소개/245172a556d68111a86cce2f40dc0889.png]]
- ContentSafety NIM : 부적절한 언어 탐지
  -  욕설, 폭언, 혐오 표현 등을 차단
- TopicControl NIM : 주제에 맞는 질문 제한
  - 주제 일탈 상황 감지 및 제어
- RAG Enforcement : 검색 범위 한정
  - RAG 검색을 통해 검증된 답변만 활용
- JailbreakDetect NIM : LLM Jailbreak 탐지
  - 악의적인 LLM Response에 대한 우회 시도 탐지
- PII Detection : 데이터 보호
  - 민감 정보가 노출되지 않도록 보호
## #4 결론
- NVIDIA NeMo Guardrails와 NIM 마이크로서비스의 역할
  - NeMo Guardrails(오케스트레이션 플랫폼)과 NIM(NeMo Inference Model) 마이크로서비스를 결합하면, 고객과의 AI 대화에서 안전성, 적절성, 정확성을 모두 강화할 수 있다.
- 안전·보안 모델 3종
  - Llama 3.1 NemoGuard 8B ContentSafety: 유해·부적절한 언어를 걸러내고 전반적인 콘텐츠 중재 기능을 수행한다.
  - Llama 3.1 NemoGuard 8B TopicControl: 대화를 미리 정해진 주제 범위 안에서 유지하도록 관리해, 맥락 이탈을 방지한다.
  - NemoGuard JailbreakDetect: 악의적 우회(Jailbreak) 시도를 탐지·방어해, 모델이 윤리·규제 기준을 벗어나지 않도록 보장한다.
- 적용 효과
  - 신속하면서도 맥락적으로 정확한 응답을 제공하는 동시에, 고객 신뢰와 브랜드 무결성을 지킬 수 있다.
  - 콘텐츠 안전성, 주제 일치, 악용 방지 등 주요 이슈를 포괄적으로 다루어, 디지털 고객 서비스 분야에서 안전하고 효과적인 AI 에이전트를 구현한다.

## 출처

- 원문: https://www.notion.so/How-to-Safeguard-AI-Agents-for-Customer-Service-with-NVIDIA-NeMo-Guardrails-245172a556d6800483b9c5299cecd414
- Vault path: wiki/notes/architecture/How-to-Safeguard-AI-Agents-for-Customer-Service-with-NVIDIA-NeMo-Guardrails---소개.md
