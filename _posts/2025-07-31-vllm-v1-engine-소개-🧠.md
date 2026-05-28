---
title: "vLLM v1 Engine 소개 🧠"
date: 2025-07-31 06:20:00 +0900
categories: [vLLM]
tags: [vLLM]
description: vLLM 아키텍처 설명
toc: true
comments: true
---

## vLLM v1 Engine 소개 🧠

### ❓ v1 Engine이란?

- **vLLM v1 engine**은 기존 v0 엔진을 대체하는 새로운 핵심 아키텍처로, 스케줄러, KV 캐시 매니저, 워커, 샘플러, API 서버 등이 모두 재설계된 구조입니다. 기존의 코드 복잡성을 줄이고 유지보수성을 높인 모듈형 설계가 특징입니다 
- v1은 CPU 오버헤드를 극소화하고, 디코드와 프리필(prefill)을 단일 스케줄러 안에서 효율적으로 처리하여 전체적인 처리 속도와 안정성을 향상시켰습니다 
## ⚖️ v0 vs v1 비교

| 항목 | v0 Engine | v1 Engine (현재 권장) |
| --- | --- | --- |
| **아키텍처** | 복잡한 개별 구성 요소 | 통합된 단일 스케줄러 및 모듈형 구조 docs.vllm.aivLLM Blog |
| **성능** | 안정적이나 스케일에 따라 CPU 오버헤드 발현 | **최대 1.7배 높은 처리량**, 고 QPS 환경에서 일관된 낮은 레이턴시 vLLM BlogRed Hat DeveloperRed Hat Developer |
| **프리필 방식** | 입력 전처리 이후 디코딩 | **chunked-prefill**으로 입력과 디코딩 동시 처리 가능 → TTFT 감소 kaitchup.substack.comrocm.blogs.amd.com |
| **Prefix Caching** | 제한적 사용 | VLM 포함 prefix-caching이 기본 활성화 및 최적화 vLLM Blogrocm.blogs.amd.com |
| **지원 모델** | 폭넓은 모델 지원 | **Decoder-only**, MoE, 일부 VLM 지원. 아직 embedding, encoder-decoder 및 Mamba 계열은 제한적 지원 vLLM Blogdocs.vllm.ai |
| **지원 기능** | LoRA, speculative decoding, structured output 등 범위 넓음 | 일부 기능은 아직 부족 (pipeline parallelism, best_of, structured decoding 등 deprecated) docs.vllm.aidocs.vllm.ai |
| **하드웨어 호환성** | 다양한 GPU 및 TPU 지원 | 현재는 **Ampere 이상 NVIDIA GPU만 공식 지원** (TPU, AMD 등은 WIP) docs.vllm.airocm.blogs.amd.com |

## 🚀 왜 v1을 만들었나?

### 1. 코드 복잡성 해결 및 확장성 확보

v0 엔진이 성장하면서 다양한 기능이 독립적으로 추가되어 시스템 복잡성이 높아졌고, 유지보수 및 신규 기능 추가가 어려워졌습니다. v1은 이를 단순화하고 구조화된 설계를 통해 개발 생산성을 높였습니다 docs.vllm.aiGitHub.

### 2. 성능 최적화

- CPU 오버헤드를 줄이고, **chunked-prefill**과 **FlashAttention 3**를 활용해 높은 QPS 환경에서도 **1.7배 빠른 처리량**을 유지하도록 설계되었습니다 
- 특히 VLM(vision-language) 작업에서 **prefix caching**, 멀티모달 스케줄링 등이 최적화되어 성능 향상이 더욱 두드러집니다 
### 3. 새로운 기능의 기반

단일 스케줄러 기반 설계, 일관적 로직 흐름, 캐시 아키텍처 개편 등을 통해 향후 speculative decoding, 구조화 출력, 로지츠 프로세서 등 신규 기능 도입에 유리한 구조를 마련했습니다 

## ✅ 사용 방법 요약

1. `vLLM_USE_V1=1` 환경변수 설정
1. `VLLM_WORKER_MULTIPROC_METHOD=spawn` 등 multiprocessing 방식 설정
1. Python API 또는 `vllm serve <모델명>` 실행 시 자동으로 v1 엔진 활성화 (v0 로 백워드 호환 유지 가능) 
## ⚠️ 현재 제약 및 향후 계획

- **현재 제한된 지원**: encoder-decoder 모델, embedding 모델, 일부 Mamba 계열 미지원
- **기능 격차**: best_of, structured decoding, pipeline parallelism, 일부 로라 및 speculative decoding 기능은 여전히 v0에 비해 제한적입니다 (현재 진행 중) 
- **향후 개선 방향**: FP8 KV 캐시, LoRA 최적화, embedding 및 encoder-decoder 모델 지원 확대, VLM 및 TPU/AMD와의 호환성 확장 
## 📚 참고 링크

- vLLM 블로그: **“vLLM V1: A Major Upgrade to vLLM’s Core Architecture”** vllm-ascend.readthedocs.io+14vLLM Blog+14docs.vllm.ai+14
- 공식 문서: **v1 User Guide**, Deprecated/Feature 비교, 모델 지원 현황 Red Hat Developer+2docs.vllm.ai+2docs.vllm.ai+2
- 성능 벤치마크: **v0.8.1 비교 결과** 및 **v1 기반 서버 성능 분석** Red Hat DeveloperRed Hat Developer

