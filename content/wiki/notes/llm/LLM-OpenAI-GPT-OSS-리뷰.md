---
source: knowledge-base
origin: notion
title: "[LLM] OpenAI GPT-OSS 리뷰"
area: "LLM"
tags: ["area/llm", "model/gpt", "model/gpt-oss", "vendor/openai"]
created: "2025-08-06T01:28:00.000Z"
last_edited: "2025-08-06T02:06:00.000Z"
status: published
public: true
notion_id: "247172a5-56d6-8058-9632-d83f4a7ffe57"
notion_url: "https://www.notion.so/LLM-OpenAI-GPT-OSS-247172a556d680589632d83f4a7ffe57"
type: note
updated: 2026-07-07
---

# [LLM] OpenAI GPT-OSS 리뷰

## 요약

OpenAI GPT-OSS 리뷰

LLM 기술 흐름과 구현 포인트를 비교하기 위한 기술 노트입니다.

## 핵심 포인트

- OpenAI GPT-OSS 리뷰
- 🔍 개요
- ⚙️ 주요 특징
- ⚖️ 성능 및 비교
- 🛡️ 안전성 및 평가

## 지식 그래프

- [[wiki/mocs/Knowledge Base|Knowledge Base]]
- [[wiki/mocs/LLM|LLM]]

## 정리 내용

#### 🔍 개요
- gpt‑oss는 OpenAI가 2025년 8월 5일에 발표한 첫 번째 오픈‑웨이트 언어모델 시리즈로, GPT‑2 이후 약 6년 만의 ‘공개 가중치’ 모델 출시입니다 [cdn.openai.com+8cookbook.openai.com+8GitHub+8](https://cookbook.openai.com/articles/gpt-oss/run-locally-ollama?utm_source=chatgpt.com)[OpenAI+15The Verge+15GitHub+15](https://www.theverge.com/openai/718785/openai-gpt-oss-open-model-release?utm_source=chatgpt.com).
- 두 가지 버전으로 제공되며:
  - gpt-oss‑120b (120B 파라미터): 고성능·추론 중심 모델, 단일 GPU에서도 실행 가능 [cookbook.openai.com+15WIRED+15Reuters+15](https://www.wired.com/story/openai-just-released-its-first-open-weight-models-since-gpt-2?utm_source=chatgpt.com).
  - gpt-oss‑20b (20B 파라미터): 일반 하드웨어(16GB RAM)에서도 실행 가능하도록 설계 [Financial Times+15WIRED+15위키백과+15](https://www.wired.com/story/openai-just-released-its-first-open-weight-models-since-gpt-2?utm_source=chatgpt.com).
#### ⚙️ 주요 특징
- Apache 2.0 라이선스 기반으로 제공되어, 상업적 사용 및 재배포가 가능 [WIRED](https://www.wired.com/story/openai-just-released-its-first-open-weight-models-since-gpt-2?utm_source=chatgpt.com).
- 오픈 웨이트(open‑weight) 모델: 학습된 파라미터는 공개되지만, 학습 데이터셋이나 학습 코드 자체는 공개되지 않음 [cdn.openai.com+7Reuters+7Simon Willison’s Weblog+7](https://www.reuters.com/business/media-telecom/openai-releases-open-weight-reasoning-models-optimized-running-laptops-2025-08-05/?utm_source=chatgpt.com).
- 체인‑오브‑생각(chain‑of‑thought) 추론 방식 지원: 복잡한 문제를 단계적으로 해결하며, 내부 사고 흐름을 드러냄 [WIRED](https://www.wired.com/story/openai-just-released-its-first-open-weight-models-since-gpt-2?utm_source=chatgpt.com)[OpenAI](https://openai.com/index/introducing-gpt-oss/?utm_source=chatgpt.com).
- 코드 작성, 수학 논증, 헬스케어 질문, 에이전트 운영 등 고도 추론 작업에 강점 [Reuters](https://www.reuters.com/business/media-telecom/openai-releases-open-weight-reasoning-models-optimized-running-laptops-2025-08-05/?utm_source=chatgpt.com)[WIRED](https://www.wired.com/story/openai-just-released-its-first-open-weight-models-since-gpt-2?utm_source=chatgpt.com).
#### ⚖️ 성능 및 비교
- gpt‑oss‑120b는 OpenAI의 o4‑mini 모델과 유사하거나 일부 벤치마크에서 더 나은 성능을 보여줌 [The Verge+15OpenAI+15Simon Willison’s Weblog+15](https://openai.com/index/introducing-gpt-oss/?utm_source=chatgpt.com).
- gpt‑oss‑20b는 o3‑mini 수준의 성능과 비슷하며, 일반적인 데스크탑 수준 하드웨어에서 실행 가능 [Omni Ekonomi+15WIRED+15Reuters+15](https://www.wired.com/story/openai-just-released-its-first-open-weight-models-since-gpt-2?utm_source=chatgpt.com).
- 전체적으로, GPT‑OSS는 Meta의 Llama 4나 중국 DeepSeek R1 등 오픈‑웨이트 모델들과 경쟁할 만한 수준으로 평가받고 있음 [Business Insider+6Financial Times+6Reuters+6](https://www.ft.com/content/4f7734a9-9f47-4f23-98f8-3083cd572663?utm_source=chatgpt.com).
- 지원 플랫폼 및 설치 방법
  - NVIDIA Blackwell(B200), Hopper(H100/H200) 계열 GPU뿐 아니라 AMD MI300x/MI355x에서도 gpt-oss를 돌릴 수 있게 되었습니다.
  - 빠른 시작을 위해 Docker 이미지(vllm/vllm-openai:gptoss)를 바로 띄우거나, Python 패키지(버전 0.10.1+gptoss)를 pip로 설치하는 법을 안내합니다.
- gpt-oss 모델 구조: MXFP4 MoE
  - gpt-oss는 “Mixture of Experts”(MoE) 방식으로, 20B 모델은 32개의 전문가(experts), 120B 모델은 128개의 전문가로 구성됩니다.
  - 각 토큰은 4개의 전문가로 라우팅되며(전문가 간 공유 없음), MoE 파트 전체에 대해서만 4비트 그룹화-양자화(MXFP4)를 적용해 모델 크기를 대폭 줄였습니다.
    - 20B 모델: 14 GB → 단일 GPU에서도 로딩 가능
    - 120B 모델: 63 GB
  - MXFP4는 32개 값마다 pow-of-two 스케일링을 추가하고, 메모리상에 두 개의 4비트 값을 8비트로 패킹했다가 연산 시 언팩하여 쓰는 형식입니다.
- 하드웨어별 최적화된 GPU 커널
  - Blackwell (B200): NVIDIA의 FlashInfer MoE 커널이 Blackwell MXFP4 텐서 코어를 직접 활용
  - Hopper (H100/H200): OpenAI Triton 팀의 matmul_ogs 커널로, 스위즐링 최적화와 자동 휴리스틱 지원
- 효율적 어텐션 디자인
  - GQA(Generalized Query Attention) 구조: 쿼리 헤드 64, KV 헤드 8
  - 레이어별로 전체(full) 어텐션과 슬라이딩 윈도우(window size=128) 어텐션을 1:1 비율로 섞어 사용
  - 표준(128) 대비 절반 크기(64)의 헤드 차원을 쓰고, 각 쿼리 헤드에 학습된 “attention sink” 벡터를 추가
  - 이 모든을 위해 FlashInfer·FlashAttention 3·Triton 기반의 특수 GPU 커널을 통합
- 하이브리드 KV 캐시 관리자
  - 전체 어텐션·슬라이딩 윈도우 어텐션이 섞여 있어도 캐시 공간을 동적으로 공유·재분배하여 메모리 단편화를 0으로 줄입니다.
- 내장된 툴 지원 (Agent Loop & Tool Server)
  - 웹 브라우징, Python 코드 인터프리터 같은 도구 호출을 모델이 스스로 결정하고 수행
  - vLLM은 OpenAI Responses API와 gpt-oss 툴킷을 연동해, 모델의 툴 콜을 파싱→실제 호출→결과 재전달 루프를 구현
  - 또는 MCP(Multi-Context Protocol) 호환 외부 툴 서버를 연동해 모듈형으로 운영할 수도 있습니다.
#### 🛡️ 안전성 및 평가
- 내부적으로 악의적 사용 시나리오를 모방한 모델을 제작하고 테스트했으며, 피해 가능성이 “높은 수준(capability)”에 이르지 않았다고 밝힘 [OpenAI](https://openai.com/open-models/?utm_source=chatgpt.com)[WIRED](https://www.wired.com/story/openai-just-released-its-first-open-weight-models-since-gpt-2?utm_source=chatgpt.com)[Reuters](https://www.reuters.com/business/media-telecom/openai-releases-open-weight-reasoning-models-optimized-running-laptops-2025-08-05/?utm_source=chatgpt.com).
- 독립 안전 감사 기관들에 의해 외부 리뷰를 받은 후 출시되었으며, OpenAI는 이 출시를 가장 엄격하게 테스트된 모델이라고 설명 [Financial Times](https://www.ft.com/content/4f7734a9-9f47-4f23-98f8-3083cd572663?utm_source=chatgpt.com)[WIRED](https://www.wired.com/story/openai-just-released-its-first-open-weight-models-since-gpt-2?utm_source=chatgpt.com)[The Verge](https://www.theverge.com/openai/718785/openai-gpt-oss-open-model-release?utm_source=chatgpt.com).
#### 🚀 활용 방법
- 모델은 Hugging Face, AWS Bedrock, Azure, Databricks, Ollama 등 다양한 플랫폼에서 무료로 다운로드 및 실행 가능 [WIRED](https://www.wired.com/story/openai-just-released-its-first-open-weight-models-since-gpt-2?utm_source=chatgpt.com)[Reuters](https://www.reuters.com/business/media-telecom/openai-releases-open-weight-reasoning-models-optimized-running-laptops-2025-08-05/?utm_source=chatgpt.com)[cookbook.openai.com](https://cookbook.openai.com/articles/gpt-oss/run-locally-ollama?utm_source=chatgpt.com)[Hugging Face](https://huggingface.co/blog/welcome-openai-gpt-oss?utm_source=chatgpt.com).
- Ollama를 통해 로컬 머신에서 손쉽게 gpt‑oss‑20b 또는 120b 모델을 실행하고 챗 인터페이스 또는 API 형식으로 활용 가능 [Business Insider+3cookbook.openai.com+3OpenAI Community+3](https://cookbook.openai.com/articles/gpt-oss/run-locally-ollama?utm_source=chatgpt.com).
- AWS Bedrock 및 SageMaker JumpStart에 통합되어, 클라우드 기반 애플리케이션 개발에 바로 사용 가능하며 높은 가격 효율성도 제공 [The Times of India](https://timesofindia.indiatimes.com/technology/tech-news/amazon-announces-first-ever-availability-of-openai-models-for-its-cloud-customers-company-says-the-addition-of-/articleshow/123125170.cms?utm_source=chatgpt.com).
#### 📌 요약 정리
| 항목 | gpt‑oss‑120b | gpt‑oss‑20b |
| --- | --- | --- |
| 파라미터 수 | 120B | 20B |
| 성능 비교 | o4‑mini 수준 또는 그 이상 | o3‑mini 수준 |
| 하드웨어 요구치 | 단일 GPU (80GB VRAM 등) | 일반 데스크탑 수준 (≥16GB RAM) |
| 라이선스 | Apache 2.0 | Apache 2.0 |
| 주 활용 분야 | 고성능 추론, 에이전트 운영 | 경량, 로컬 실행, 실험적 사용 |
#### ✨ 의미와 영향
- OpenAI의 전략 변화: 기존에는 주로 폐쇄형 모델 중심이었지만, GPT‑OSS는 다시 ‘개방성(openness)’을 향한 전략 전환을 의미합니다 [WIRED+7Business Insider+7Simon Willison’s Weblog+7](https://www.businessinsider.com/openai-gpt-oss-open-weight-llm-ai-model-2025-8?utm_source=chatgpt.com)[GitHub+6WIRED+6The Verge+6](https://www.wired.com/story/openai-just-released-its-first-open-weight-models-since-gpt-2?utm_source=chatgpt.com).
- 글로벌 오픈‑웨이트 경쟁 강화: 중국의 DeepSeek R1, Meta의 Llama 4 등에 대응하며, 미국 주도의 오픈 AI 스택을 강조하는 방향으로 진화 [The Verge+5Financial Times+5Reuters+5](https://www.ft.com/content/4f7734a9-9f47-4f23-98f8-3083cd572663?utm_source=chatgpt.com).
- 개발자·스타트업·연구자에 기회 확대: 상용 또는 커스터마이징 가능한 강력한 모델이 무료로 제공됨으로써 혁신의 기반이 강화됨을 의미합니다.

## 출처

- 원문: https://www.notion.so/LLM-OpenAI-GPT-OSS-247172a556d680589632d83f4a7ffe57
- Vault path: wiki/notes/llm/LLM-OpenAI-GPT-OSS-리뷰.md
