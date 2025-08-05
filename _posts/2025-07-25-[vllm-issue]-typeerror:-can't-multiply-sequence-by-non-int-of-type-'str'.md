---
title: "[vLLM Issue] TypeError: can't multiply sequence by non-int of type 'str'"
date: 2025-07-25 07:57:00 +0900
categories: [Trouble Shooting]
tags: [vLLM, LLM, Issue]
description: vLLM Issue 및 해결방법
toc: true
comments: true
---

## 💥 vLLM 0.9.1에서 `rope_scaling.factor` 관련 TypeError 문제 해결기

### 🧩 문제 상황

vLLM 0.9.1에서 다음과 같은 커맨드로 모델을 띄우는 도중, 서버가 시작되지 않고 `TypeError`가 발생했습니다:

```shell
python3 -m vllm.entrypoints.openai.api_server \
  --model /datasets/DTS2025000100/data \
  --host 0.0.0.0 --port 8001 \
  --served-model-name /datasets/DTS2025000100/data \
  --tokenizer-mode auto --gpu-memory-utilization 0.95 \
  --tensor-parallel-size 8 --max-model-len 131072 \
  --max-num-batched-tokens 131072 --block-size 16 \
  --swap-space 0 --max-num-seqs 256 \
  --max-seq-len-to-capture 131072 --kv-cache-dtype auto \
  --disable-log-requests --trust-remote-code --dtype auto \
  --hf-overrides.rope_scaling.rope_type yarn \
  --hf-overrides.rope_scaling.factor 4.0 \
  --hf-overrides.rope_scaling.original_max_position_embeddings 32768
```

### 🛑 에러 메시지 요약

```plain text
TypeError: can't multiply sequence by non-int of type 'str'
```

에러의 원인은 `rope_scaling.factor`가 문자열로 인식되어 `float` 연산이 불가능했던 점입니다. 내부적으로는 아래 코드에서 문제가 발생합니다:

```python
derived_max_model_len *= scaling_factor 
```

즉, `--hf-overrides.rope_scaling.factor 4.0` 이 CLI에서 문자열 `"4.0"`으로 들어가서 파싱 시 타입 캐스팅이 되지 않았고, 이로 인해 `TypeError`가 발생한 것입니다.

### ✅ 해결 방법

이 문제는 **vLLM 0.9.2**에서 **`rope_scaling.factor`**** 타입 캐스팅 처리**를 추가함으로써 해결되었습니다.

### 관련 PR (예상 코드 변경):

vLLM 내부에서 `hf_overrides` 처리 시, `"factor"` 값을 명시적으로 `float()` 처리하도록 변경되었습니다. 예시 코드:

```python
"rope_scaling": {
    "rope_type": "dynamic",
    "factor": float(config.rotary_scaling_factor)  # 타입 캐스팅 명확히 수행
}
```

이로 인해 CLI 인자에서 `"4.0"`과 같은 문자열로 입력해도 내부에서는 `float`로 올바르게 처리되어 에러 없이 실행됩니다.

### ✍️ 마무리

vLLM 0.9.1에서는 `--hf-overrides`로 `rope_scaling.factor`를 입력할 때 **타입 오류로 인한 서버 실행 실패** 문제가 있었고, 0.9.2에서는 이를 **명시적 타입 변환 처리로 안정적으로 해결**하였습니다.

> 교훈: CLI를 통해 JSON-like 구조체를 넘길 때는 내부 파싱 로직에서 타입 검증이 중요하다!


