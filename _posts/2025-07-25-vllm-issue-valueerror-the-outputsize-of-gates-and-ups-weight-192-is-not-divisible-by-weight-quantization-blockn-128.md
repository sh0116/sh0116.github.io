---
title: "[vLLM Issue]: ValueError: The output_size of gate's and up's weight = 192 is not divisible by weight quantization block_n = 128"
date: 2025-07-25 08:00:00 +0900
categories: [Trouble Shooting]
tags: [LLM, vLLM, Issue]
description: vLLM Issue 및 해결방법
toc: true
comments: true
redirect_from:
  - /posts/[vllm-issue]:-valueerror:-the-output_size-of-gate's-and-up's-weight-=-192-is-not-divisible-by-weight-quantization-block_n-=-128/
---

### 🧩 무엇이 잘못됐는가?

에러 메시지: 

```text
ValueError: The output_size of gate's and up's weight = 192 is not divisible by weight quantization block_n = 128
```

이 뜻은 “gate”와 “up” 레이어의 가중치 크기(`output_size`가 192)가 **quant block 크기(128)**로 나누어떨어지지 않기 때문에 vLLM이 이를 할당할 수 없다는 것입니다.

vLLM의 FP8 block quant 모델은 아래 조건을 요구합니다 (소스 코드 기준):

- gate/up 레이어 `intermediate_size_per_partition % block_n == 0`여야 한다 arXiv+7vLLM+7qwen.readthedocs.io+7qwen.readthedocs.io+4GitHub+4知乎+4qwen.readthedocs.io.
즉, gate/up weight 차원이 block_n의 배수여야만 정상 동작할 수 있습니다.

### 🎯 언제 발생하나?

이 에러는 보통 **Qwen3‑FP8** 같은 모델들을 **FP8+block‑wise quantization** 옵션으로 실행할 때, 특히 **tensor parallel(tensor‑parallel‑size)** 또는 **expert parallel** 구성에 따라 weight가 여러 partition로 나뉘면서 발생할 수 있습니다.

이때 각 partition의 gate/up weight 크기가 block_n (예: 128)로 나누어떨어지지 않으면 위와 같은 에러가 발생합니다 GitHub+5GitHub+5qwen.readthedocs.io+5.

### ✅ 해결 방법은?

**Qwen 공식 가이드**에서는 아래 두 가지 방안을 권장합니다 :

1. **Tensor‑parallel 수 줄이기**
1. 또는 **Expert‑parallel 모드 활성화**
이렇게 하면 partition된 weight의 크기가 block_n(128)의 배수가 되거나, block‑quant 로직이 중심 되지 않도록 변경되어 에러를 피할 수 있습니다.

### 📌 요약

- **원인**: FP8 block quant에서 gate/up 레이어 weight 크기(192)가 quant block 크기(128)로 나눠지지 않음 → 오류 발생
- **해결법**:

