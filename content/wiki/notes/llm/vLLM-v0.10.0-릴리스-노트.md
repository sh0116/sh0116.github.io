---
source: knowledge-base
origin: notion
title: "vLLM v0.10.0 릴리스 노트 ✨"
area: "LLM"
tags: ["area/llm", "tech/vllm"]
created: "2025-07-31T06:18:00.000Z"
last_edited: "2025-07-31T07:17:00.000Z"
status: published
public: true
notion_id: "241172a5-56d6-8022-8043-fa7940db1771"
notion_url: "https://www.notion.so/vLLM-v0-10-0-241172a556d680228043fa7940db1771"
type: note
updated: 2026-07-07
---

# vLLM v0.10.0 릴리스 노트 ✨

## 요약

vLLM 릴리즈 리뷰

LLM 기술 흐름과 구현 포인트를 비교하기 위한 기술 노트입니다.

## 핵심 포인트

- vLLM 릴리즈 리뷰
- vLLM v0.10.0 릴리스 노트 ✨
- 🚀 Highlights
- 🧠 지원 모델 및 호환성 강화
- 🔧 OpenAI /responses API 초기 지원

## 지식 그래프

- [[wiki/mocs/Knowledge Base|Knowledge Base]]
- [[wiki/mocs/LLM|LLM]]

## 정리 내용

### vLLM v0.10.0 릴리스 노트 ✨
릴리즈 날짜: 2025‑07‑24 / 25 (GitHub, PyPI 기준) 
#### 🚀 Highlights
- 308 커밋, 168명의 기여자 (그중 62명은 신규 기여자 포함) 
- V0 엔진 코드베이스 정리 시작:
  - V0 CPU/XPU/TPU/HPU 백엔드 완전 제거 (#20412)
  - 롱 컨텍스트 LoRA (#21169), Prompt Adapters (#20588), Phi3‑Small 및 BlockSparse Attention (#21217), Spec Decode workers (#21152) 삭제 시작 
#### 🧠 지원 모델 및 호환성 강화
- 신규 모델군 추가:
  - Llama 4 + EAGLE 지원, EXAONE 4.0, Microsoft Phi‑4‑mini‑flash‑reasoning
  - Hunyuan V1 Dense + A13B (reasoning/tool parsing), Ling MoE, JinaVL Reranker, Nemotron‑Nano‑VL‑8B‑V1, Arcee, Voxtral 등 
- 호환성 향상:
  - BERT/RoBERTa AutoWeightsLoader 적용, MiniMax HF 형식 지원, Gemini 설정 구성 적용, GLM‑4 업데이트 [GitHub](https://github.com/vllm-project/vllm/releases?utm_source=chatgpt.com)
- 구조 확장 기능:
  - Attention‑free 모델, V1 엔진에서 Hybrid SSM/Attention 모델, LlamaForSequenceClassification, Mamba2 레이어 확장 지원 
#### 🔧 OpenAI /responses API 초기 지원
- OpenAI Responses API에 대한 초기 지원이 이 릴리즈의 숨은 핵심 기능입니다 
  - 단일 응답 내에 "think → tool call → reason → next tool call"을 체인 형식으로 수행할 수 있는 구조로, 차세대 에이전트 개발 패러다임으로 기대됨
  - 추후 모델별 tool-calling 통합 기능도 함께 발전 예정
#### 🧹 V0 엔진 정리 및 코드 청소 (계속 예정)
- V0 CPU/XPU/TPU/HPU 백엔드를 제거하는 등, 더 이상 사용되지 않는 코드 정리에 본격 착수 
#### 📌 정리 요약 (Markdown 표)
| 항목 | 주요 변경 내용 |
| --- | --- |
| 릴리스 통계 | 308 커밋, 168 기여자, 62 신규 기여자 |
| V0 코드 정리 | 오래된 백엔드 및 기능 제거 시작 |
| 모델 지원 확대 | 다양한 신규 모델 및 구조 통합 |
| 호환성 강화 | HuggingFace 포맷, GLM‑4 등 서비스 지원 |
| 구조 확장 | Attention‑free, Hybrid SSM/Attention, Mamba2 등 |
| OpenAI /responses API | Thinking → Tool‑call 패턴 초기 도입 |

## 출처

- 원문: https://www.notion.so/vLLM-v0-10-0-241172a556d680228043fa7940db1771
- Vault path: wiki/notes/llm/vLLM-v0.10.0-릴리스-노트.md
