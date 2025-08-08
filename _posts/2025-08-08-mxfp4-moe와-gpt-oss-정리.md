---
title: "MXFP4 MoE와 GPT-OSS 정리"
date: 2025-08-08 05:23:00 +0900
categories: [기술소개]
tags: [LLM, vLLM, GPT-OSS, GPT, OPENAI]
description: MXFP4 MoE 기술 소개
toc: true
comments: true
---

## MXFP4 MoE와 GPT-OSS 정리

- **GPT-OSS**: 오픈 가중치(Open-Weight)로 공개된 **120B / 20B** 텍스트 LLM.
- **MXFP4 MoE**: MoE 구조의 **전문가(Expert) 선형 가중치**를 **Microscaling FP4(4비트 부동소수 + 블록 스케일)**로 저장·서빙하는 방식.
- **효과**: 가중치 메모리·대역폭이 크게 줄어 **120B가 H100 80GB 1장**, **20B가 16GB급**에서도 동작 가능한 수준으로 설계됨(보고 수치 기준).
- **한계**: 텍스트 전용(멀티모달 X), 최신 사실은 RAG/브라우징 결합 필요, 4bit 경로는 런타임/커널 지원이 관건.
## 왜 MXFP4 MoE가 중요할까?

- **MoE의 장점**: 토큰별로 소수 전문가만 활성화(Top-k) → “활성 파라미터”가 적어 추론 비용↓.
- **MXFP4의 장점**: 전문가 가중치를 **4bit FP**로 저장하되, **작은 블록마다 스케일**을 공유(미분포 보정) → 4bit의 손실을 완화하며 **메모리·대역폭**을 추가로 절약.
결과적으로 **“MoE(활성 파라미터 절약)” + “MXFP4(비트폭 축소)”**의 조합으로 **대형 모델의 단일 GPU 탑재**가 현실화됩니다.

## GPT-OSS 한눈에 보기

- **모델 크기**: 120B / 20B (MoE)
- **형식**: 텍스트 전용(대화/툴 사용 전제 가능)
- **컨텍스트 창**: 최대 대형(예: 131K 등 보고치)
- **가중치 저장**: MoE 선형층은 **MXFP4**, 그 외 텐서는 고정소수/부동소수(예: BF16 등) 혼용
- **실사용 감**(보고치 기준):
> ⚠️ 수치(컨텍스트 창, 체크포인트 크기 등)는 릴리스 노트/모델 카드에서 꼭 다시 확인하세요.

## MXFP4 vs. “일반” 양자화/포맷 이해하기

### MXFP4는 **숫자 형식**, GGUF는 **파일 포맷**

- **MXFP4**: 4bit 부동소수(E2M1 등) + **블록 스케일**을 별도 저장 → 런타임 커널이 FP4+스케일을 직접 처리.
- **GGUF**: llama.cpp 생태계의 **가중치 컨테이너 포맷**(Q4_K_M, Q8_0 등 다양한 스킴을 담을 수 있음).
### MXFP4 MoE가 다른 정밀도 대비 어떤가?

| 항목 | MXFP4 MoE | INT4(전면) | INT8/FP8 | BF16 |
| --- | --- | --- | --- | --- |
| 가중치 비트폭(대표) | ~4bit(블록 스케일) | 4bit | 8bit | 16bit |
| 정확도 보전 | **블록 스케일로 보정** | 과제별 편차 | 중간 | 높음 |
| 메모리/대역폭 | **매우 낮음** | 매우 낮음 | 낮음 | 높음 |
| 요구 툴체인 | 전용 커널/디코딩 | 비교적 광범위 | 광범위 | 광범위 |

> 포인트: MXFP4는 “그냥 4bit”가 아니라 부동소수 4bit + 마이크로스케일이라 품질 저하를 줄이도록 설계되어 있습니다.

## “H100 80GB 1장에 120B가 들어간다”는 말의 의미

- **핵심 조건**: **전문가 가중치가 MXFP4**로 저장, 비활성 전문가 대부분은 메모리·대역폭 부하가 낮음.
- **일반 정밀도라면?**
즉, **MXFP4 MoE 설계**가 아니면 **120B를 80GB 1장**에 올리기 어렵습니다(샤딩/오프로딩 필요).

## VRAM 추산 가이드: *가중치 + KV 캐시 + 오버헤드*

> 아래 계산은 “모델 카드에 보고된 예시 하이퍼파라미터”를 가정한 개략 추정입니다. 엔진(vLLM/TensorRT-LLM), 활성 전문가 수, 로스케일, 런타임 오버헤드에 따라 달라질 수 있어요.

### 1) 가중치(Weights)

- **120B (MXFP4 MoE)**: ~**60.8 GiB** (보고값)
- **20B (MXFP4 MoE)**: ~**12.8 GiB** (보고값)
### 2) KV 캐시(토큰 수에 비례)

일반화 식(배치 1 기준):

```scss
KV_bytes_per_token ≈ 2 × L × (KV_heads × head_dim) × bytes_per_element
```

- `L`: 레이어 수
- `KV_heads × head_dim`: KV 총 차원
- `bytes_per_element`: FP16=2, FP8=1 등
> 예시(보고 하이퍼파라미터 가정: L=36, KV_heads=8, head_dim=64)

문맥 길이별(배치 1):

| 컨텍스트 | FP16 KV | FP8 KV |
| --- | --- | --- |
| 8K | ~0.56 GB | ~0.28 GB |
| 32K | ~2.25 GB | ~1.13 GB |
| 131K | ~9.0 GB | ~4.5 GB |

### 3) 대략 합계(120B, 배치 1)

- **MXFP4 가중치(≈65.3 GB, GiB→GB 환산 포함)** + **KV(FP16, 8K ≈0.56 GB)** + **엔진 오버헤드(수 GB)**
- **최대 창(131K) + FP16 KV**를 써도 **70GB대 중후반**에서 운영 가능(배치↑/동시성↑ 시 KV가 급증하므로 주의).
> 팁: vLLM의 --kv-cache-dtype(예: fp8)과 --gpu-memory-utilization로 KV·오버헤드를 조율하세요.

## 실전: 배포/서빙 팁

> 실제 명령은 체크포인트 경로/모델 ID에 맞게 바꿔 쓰세요.

### vLLM 예시

```bash
vllm serve /path/to/gpt-oss-120b \
  --dtype auto \
  --tensor-parallel-size 1 \
  --max-model-len 131072 \
  --kv-cache-dtype fp8 \
  --gpu-memory-utilization 0.92
```

### Transformers (Python) 예시

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_id = "/path/to/gpt-oss-120b"   # 또는 20b
tok = AutoTokenizer.from_pretrained(model_id, use_fast=True)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16,      # 비-MX 텐서는 BF16 등
    device_map="auto"                # 단일 GPU면 "cuda:0"
)

prompt = "Explain MXFP4 MoE in simple terms."
out = model.generate(**tok(prompt, return_tensors="pt").to(model.device),
                     max_new_tokens=256)
print(tok.decode(out[0], skip_special_tokens=True))

```

### 체크리스트

## 장점과 단점 요약

**장점**

- **메모리/대역폭 절감**으로 대형 모델의 **단일 GPU 탑재** 실현
- **MoE + 4bit 부동소수** 조합으로 **성능-비용 스윗스팟** 달성
- **툴/함수 호출** 등 에이전트형 워크로드에 적합(구현 가이드 다수)
**단점/주의**

- **전용 커널/런타임 의존**(환경 호환성 점검 필수)
- **텍스트 전용**, 최신 사실성은 **RAG/브라우징** 결합 권장
- **오픈 가중치**이지만, FOSS 의미의 “완전 오픈소스”와는 구분(정책/라이선스 확인)
## MXFP4 MoE vs. 비-MXFP4(일반) VRAM 필요량 요약

| 모델/정밀도 | 가중치 메모리(120B 가정) | 80GB 1장 탑재 | 비고 |
| --- | --- | --- | --- |
| **MXFP4 MoE** | ~60.8 GiB(보고) | **가능** | KV·오버헤드 포함 시 70GB 내외 |
| INT4(전면) | ~58.4 GB(이론) | 가능성 | 커널/품질 차이, 동일 개념 아님 |
| FP8/INT8(전면) | ~116.8 GB | **불가** | 2장 이상 또는 오프로딩 필요 |
| BF16(전면) | ~233.7 GB | **불가** | 대규모 샤딩 필요 |

> 표는 가중치만 기준. 실제 서비스는 KV 캐시 + 엔진 오버헤드를 합산해야 합니다.

## FAQ

**Q. MXFP4는 GGUF 같은 건가요?**

A. 목적(메모리 절약)은 비슷하지만 **다른 층위**입니다. **MXFP4=숫자 형식**, **GGUF=파일 포맷(컨테이너)**.

**Q. 왜 MoE에만 MXFP4를 쓰나요?**

A. 파라미터 대부분이 전문가 가중치에 몰려 있고, 토큰당 활성 전문가 수가 적어 **효율 효과**가 극대화되기 때문입니다.

**Q. MXFP4가 성능을 많이 깎지 않나요?**

A. 일반 FP4보다 **블록 스케일링(마이크로스케일)**로 손실을 보정하도록 설계되어 품질 저하를 줄입니다. 다만 태스크/튜닝에 따라 차이가 날 수 있어 **벤치마크 검증**이 필요합니다.

## 마무리

**MXFP4 MoE**는 “모델 구조(MoE)”와 “가중치 표현(MXFP4)”을 결합해 대형 모델을 **현실적인 리소스**로 운영하게 만든 접근입니다. **GPT-OSS(120B/20B)**는 그 성과를 보여주는 대표 예로, **온프렘/단일 GPU** 시나리오까지 커버 가능한 게 큰 장점이죠.

게시 전에 다음만 체크해 주세요:

1. 사용하려는 **체크포인트의 실제 크기/요구사항**,
1. **KV 캐시**(컨텍스트·배치)에 따른 총 VRAM,
1. **런타임 커널/드라이버** 호환성.

