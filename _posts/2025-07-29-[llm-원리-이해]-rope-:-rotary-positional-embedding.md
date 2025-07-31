---
title: "[LLM 원리 이해] RoPE : Rotary Positional Embedding"
date: 2025-07-29 05:48:00 +0900
categories: [LLM]
tags: [Llama, LLM]
description: "🍟"
toc: true
comments: true
---

# 🧠 RoPE (Rotary Positional Encoding)란?

Transformer는 순서를 고려하지 않는 Attention 구조이기 때문에, **토큰의 위치 정보**를 표현하기 위해 positional embedding이 필수입니다.

RoPE는 이러한 위치 정보를 **회전(rotation)**이라는 방식으로 삽입하여, 자연스럽게 **상대적 위치 정보**까지 함께 반영하는 기술입니다

## 1. 기존 Absolute Positional Embedding의 한계

### 📍 1) 고정된 최대 시퀀스 길이

- **Learned embedding** 방식은 사전 정의된 최대 길이 내에서만 동작합니다. 이를 넘으면 확장할 수 없습니다.
- **Sinusoidal embedding**도 학습되지 않은 길이에는 일반화가 제한적입니다.
### 📍 2) 상대적 위치 정보를 잘 반영하지 못함

- 서로 멀리 떨어진 두 위치(예: 2와 500)는 벡터 간 유사성이 전혀 반영되지 않으므로, **상대적 의미**를 추정하기 어렵습니다.
### 📍 3) 일반화와 extrapolation 한계

- 새로운 문장을 길게 연결하거나 테스트 시퀀스가 학습 시퀀스보다 길 경우, embedding이 제대로 작동하지 않아 **퍼플렉시티가 급등**하기도 합니다. 
## 2. RoPE의 핵심 아이디어 및 메커니즘

RoPE는 쿼리(Q)와 키(K)의 임베딩에 **회전 행렬(rotation matrix)** 을 적용해서 순서 정보를 포함시킵니다:

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/5e2fe1e1-9eb2-43b5-9a93-4be21c14ddcc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664EH2H6PC%2F20250731%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250731T034805Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCSVlKoWEUPu%2B8kNI8GbdDJlVOlmYeC05wjlsooF5JGLgIhAM7PP%2BQy2KUjWBtVa8uZTEy%2FTNMZ8ZhUuo6%2BQW4J9Dx1KogECM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy1AnC1RYAYAME3kb4q3AN3lfmrWSE%2Fal7QG4i0Cx8bU3OsM%2BtOh7BNlfx5tJB6M32j%2FbTLjnwo5ifmuhGKE0d0%2Biv1wb9bYvgUPXY7vu0r%2BTgxMf3ykz7DFLE%2FeZ3Bszi%2BInpZ8aKsIt61xG%2B9C7qiBGeUaafO9NNgC8TVRBCIp1jSeYnLcPBRBcJzzGbG8b6NISf7MC05VTa%2BUVLPq0nNXXwhfeRUo0NOKfSLmmE2AYk34XHJ7nvEZX5VQb5XomV8Myl%2Fyi9Hs8kr7ClQyn1KXzj1GSsOG%2BdLmrKAlhOBaiNWffV0Xj2pQdmXU2hPRQZ9jcmzd3NVmd%2BF1fht8h3V63IjZK5sBmMUWnJbnzHMY2vp5TGRPc%2FmHGBY3X7Y0HyruslB10miO%2BiFI4U8nKcWrQfLg16em%2FYYqI3TeeU1aqFJa4z2XK8ne9SQSZ9gSLYRXjpr23g1sh0%2BT2%2Fdr28Zox3uPK7dz09DBRWtT2MGnqvKOlg3pXF91gaqjfYWGSVnwdkue8qu6HdofazX2C1%2BUf86MSRHk3ihNTCFi97BA%2BJDQZPe5u1uXRZxDSgfGkLGewl1EYeaE8YBnU9S8N6TwQChJaE6bmuGuPSF3WG7dcdkSzryho4lkhi58SrOvXYBD2HsWd76B8L5zjCty6vEBjqkASbEemiMjyqMHlTMaTyFaKX5ddJS3BXELKkSwJIJcjiaHr93%2BcAfMkTOqc84s%2F66EtJVous9dd8bS6bu3n6x2bgcj7Cgymo0yzkT%2BPQrcgbH4hEDeokbKes2UOfGEJrpZkwXeQATUeWf%2B0yy5EaQTW9TzN7eh%2BNMisVc4ha8CJghVH4%2FcWt9xwRnQWtvOrGo7Bm51f25eNMjhMRQMIiTcfXuhTwU&X-Amz-Signature=eb2144afde6f0f10b682e6d3e0629a5335ebab3afb6d2da3691390af7159c8c1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

RoPE는 백터의 회전을 통해 위치를 표현합니다, 백터의 회전은 복소수( Complex Number) 를 먼저 이해 해야하는데요.

복소수를 A+Bi 형태로 표현하여 2차원 평면에 복소평면을 그리면 위 그림과 같습니다.

실수축과 허수축으로 구성되어있는 형식입니다.

여기서 Euler 공식을 통해 회전시킬 수 있습니다.

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/b351347d-7727-489a-ae89-52f7948111de/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664EH2H6PC%2F20250731%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250731T034805Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCSVlKoWEUPu%2B8kNI8GbdDJlVOlmYeC05wjlsooF5JGLgIhAM7PP%2BQy2KUjWBtVa8uZTEy%2FTNMZ8ZhUuo6%2BQW4J9Dx1KogECM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy1AnC1RYAYAME3kb4q3AN3lfmrWSE%2Fal7QG4i0Cx8bU3OsM%2BtOh7BNlfx5tJB6M32j%2FbTLjnwo5ifmuhGKE0d0%2Biv1wb9bYvgUPXY7vu0r%2BTgxMf3ykz7DFLE%2FeZ3Bszi%2BInpZ8aKsIt61xG%2B9C7qiBGeUaafO9NNgC8TVRBCIp1jSeYnLcPBRBcJzzGbG8b6NISf7MC05VTa%2BUVLPq0nNXXwhfeRUo0NOKfSLmmE2AYk34XHJ7nvEZX5VQb5XomV8Myl%2Fyi9Hs8kr7ClQyn1KXzj1GSsOG%2BdLmrKAlhOBaiNWffV0Xj2pQdmXU2hPRQZ9jcmzd3NVmd%2BF1fht8h3V63IjZK5sBmMUWnJbnzHMY2vp5TGRPc%2FmHGBY3X7Y0HyruslB10miO%2BiFI4U8nKcWrQfLg16em%2FYYqI3TeeU1aqFJa4z2XK8ne9SQSZ9gSLYRXjpr23g1sh0%2BT2%2Fdr28Zox3uPK7dz09DBRWtT2MGnqvKOlg3pXF91gaqjfYWGSVnwdkue8qu6HdofazX2C1%2BUf86MSRHk3ihNTCFi97BA%2BJDQZPe5u1uXRZxDSgfGkLGewl1EYeaE8YBnU9S8N6TwQChJaE6bmuGuPSF3WG7dcdkSzryho4lkhi58SrOvXYBD2HsWd76B8L5zjCty6vEBjqkASbEemiMjyqMHlTMaTyFaKX5ddJS3BXELKkSwJIJcjiaHr93%2BcAfMkTOqc84s%2F66EtJVous9dd8bS6bu3n6x2bgcj7Cgymo0yzkT%2BPQrcgbH4hEDeokbKes2UOfGEJrpZkwXeQATUeWf%2B0yy5EaQTW9TzN7eh%2BNMisVc4ha8CJghVH4%2FcWt9xwRnQWtvOrGo7Bm51f25eNMjhMRQMIiTcfXuhTwU&X-Amz-Signature=730c5c0666689210c902a79390881c343fa9e1a2aa259d24a163809c2bc142c5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

복소수에 eⁱᶿ를 곱하면 각도 θ만큼 회전을 한다는 공식입니다.

예를 들어 A+Bi라는 벡터를 eⁱᶿ로 곱하면, 벡터의 크기는 유지하고 각도만 θ만큼 회전하여 새로운 벡터를 얻을 수 있다는 것 입니다.

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/beb7173f-68a2-43d0-bd38-5fbaca0c978a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664EH2H6PC%2F20250731%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250731T034805Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCSVlKoWEUPu%2B8kNI8GbdDJlVOlmYeC05wjlsooF5JGLgIhAM7PP%2BQy2KUjWBtVa8uZTEy%2FTNMZ8ZhUuo6%2BQW4J9Dx1KogECM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy1AnC1RYAYAME3kb4q3AN3lfmrWSE%2Fal7QG4i0Cx8bU3OsM%2BtOh7BNlfx5tJB6M32j%2FbTLjnwo5ifmuhGKE0d0%2Biv1wb9bYvgUPXY7vu0r%2BTgxMf3ykz7DFLE%2FeZ3Bszi%2BInpZ8aKsIt61xG%2B9C7qiBGeUaafO9NNgC8TVRBCIp1jSeYnLcPBRBcJzzGbG8b6NISf7MC05VTa%2BUVLPq0nNXXwhfeRUo0NOKfSLmmE2AYk34XHJ7nvEZX5VQb5XomV8Myl%2Fyi9Hs8kr7ClQyn1KXzj1GSsOG%2BdLmrKAlhOBaiNWffV0Xj2pQdmXU2hPRQZ9jcmzd3NVmd%2BF1fht8h3V63IjZK5sBmMUWnJbnzHMY2vp5TGRPc%2FmHGBY3X7Y0HyruslB10miO%2BiFI4U8nKcWrQfLg16em%2FYYqI3TeeU1aqFJa4z2XK8ne9SQSZ9gSLYRXjpr23g1sh0%2BT2%2Fdr28Zox3uPK7dz09DBRWtT2MGnqvKOlg3pXF91gaqjfYWGSVnwdkue8qu6HdofazX2C1%2BUf86MSRHk3ihNTCFi97BA%2BJDQZPe5u1uXRZxDSgfGkLGewl1EYeaE8YBnU9S8N6TwQChJaE6bmuGuPSF3WG7dcdkSzryho4lkhi58SrOvXYBD2HsWd76B8L5zjCty6vEBjqkASbEemiMjyqMHlTMaTyFaKX5ddJS3BXELKkSwJIJcjiaHr93%2BcAfMkTOqc84s%2F66EtJVous9dd8bS6bu3n6x2bgcj7Cgymo0yzkT%2BPQrcgbH4hEDeokbKes2UOfGEJrpZkwXeQATUeWf%2B0yy5EaQTW9TzN7eh%2BNMisVc4ha8CJghVH4%2FcWt9xwRnQWtvOrGo7Bm51f25eNMjhMRQMIiTcfXuhTwU&X-Amz-Signature=a16bd9078f7f427f9113ae38b0a74a745cd5d0dacf25e06ed72bcf2e6add5ebd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 3. RoPE의 주요 장점

### ✅ 1) **길이 확장성 (Context Extrapolation)**

학습 시보다 긴 시퀀스에도 embedding 벡터 재생성이 가능하여, **문맥 길이 초과 문제를 회피**할 수 있습니다 

### ✅ 2) **상대적 위치 표현**

회전을 통해 dot product가 **상대 거리 정보만 반영**되므로, 토큰 간의 상대적 관계를 자연스럽게 반영합니다 

### ✅ 3) **Linear attention과도 호환 가능**

RoPE는 기존 relative embedding보다 구현이 단순하고, **linear self-attention 구조에도 결합할 수 있다는 이점**이 있습니다 

### ✅ 4) **자연어 모델과 언어 장비에 강건한 사용성**

예를 들어, 최신 LLM에서 RoPE는 **Gemma 7B, LLaMA 3 등에서 활용되며**, 토큰 간 의미 관계를 효과적으로 반영하는 것으로 알려져 있습니다 

### ✅ 5) **의미와 위치 정보를 함께 담는 효율성**

기존 Transfomer의 방식은 SelfAttention과정에서 Pt(포지션 임베딩)을 적용하는 방식입니다.

RoPE의 아이디어는 임베딩은 그대로 두고, Query(Q) / Key(K) 계산 과정에서 Rotation Matrix를 반영하자는 아이디어 입니다.

같은 단어가 여러번 등장해도 상대적인 위치를 잘 반영하여 의미를 파악할 수 있는 장점이 있습니다.

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/ec91cb0a-d924-4728-a8c8-be0ed6b8ea49/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664EH2H6PC%2F20250731%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250731T034805Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCSVlKoWEUPu%2B8kNI8GbdDJlVOlmYeC05wjlsooF5JGLgIhAM7PP%2BQy2KUjWBtVa8uZTEy%2FTNMZ8ZhUuo6%2BQW4J9Dx1KogECM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy1AnC1RYAYAME3kb4q3AN3lfmrWSE%2Fal7QG4i0Cx8bU3OsM%2BtOh7BNlfx5tJB6M32j%2FbTLjnwo5ifmuhGKE0d0%2Biv1wb9bYvgUPXY7vu0r%2BTgxMf3ykz7DFLE%2FeZ3Bszi%2BInpZ8aKsIt61xG%2B9C7qiBGeUaafO9NNgC8TVRBCIp1jSeYnLcPBRBcJzzGbG8b6NISf7MC05VTa%2BUVLPq0nNXXwhfeRUo0NOKfSLmmE2AYk34XHJ7nvEZX5VQb5XomV8Myl%2Fyi9Hs8kr7ClQyn1KXzj1GSsOG%2BdLmrKAlhOBaiNWffV0Xj2pQdmXU2hPRQZ9jcmzd3NVmd%2BF1fht8h3V63IjZK5sBmMUWnJbnzHMY2vp5TGRPc%2FmHGBY3X7Y0HyruslB10miO%2BiFI4U8nKcWrQfLg16em%2FYYqI3TeeU1aqFJa4z2XK8ne9SQSZ9gSLYRXjpr23g1sh0%2BT2%2Fdr28Zox3uPK7dz09DBRWtT2MGnqvKOlg3pXF91gaqjfYWGSVnwdkue8qu6HdofazX2C1%2BUf86MSRHk3ihNTCFi97BA%2BJDQZPe5u1uXRZxDSgfGkLGewl1EYeaE8YBnU9S8N6TwQChJaE6bmuGuPSF3WG7dcdkSzryho4lkhi58SrOvXYBD2HsWd76B8L5zjCty6vEBjqkASbEemiMjyqMHlTMaTyFaKX5ddJS3BXELKkSwJIJcjiaHr93%2BcAfMkTOqc84s%2F66EtJVous9dd8bS6bu3n6x2bgcj7Cgymo0yzkT%2BPQrcgbH4hEDeokbKes2UOfGEJrpZkwXeQATUeWf%2B0yy5EaQTW9TzN7eh%2BNMisVc4ha8CJghVH4%2FcWt9xwRnQWtvOrGo7Bm51f25eNMjhMRQMIiTcfXuhTwU&X-Amz-Signature=e4ef01ed274dfdae5aecf16fc1f41fac2ba97362a04bbea24b249851b1690717&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

예를 들어 “애플 애플 애플 애플” 이라는 문장이 있을 때

기존 Transfomer 모델의 경우 Q/K 값이 같습니다, 상대 위치 정보를 파악할 수 없지만

RoPE 방식을 쓴다면 각 토큰의 위치별로 Rotation 값이 다르기 때문에 상대적인 각도(위치)가 반영됩니다.

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/862fb2ea-37e8-45c0-b8ce-bbb78d63f0c3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664EH2H6PC%2F20250731%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250731T034805Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCSVlKoWEUPu%2B8kNI8GbdDJlVOlmYeC05wjlsooF5JGLgIhAM7PP%2BQy2KUjWBtVa8uZTEy%2FTNMZ8ZhUuo6%2BQW4J9Dx1KogECM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy1AnC1RYAYAME3kb4q3AN3lfmrWSE%2Fal7QG4i0Cx8bU3OsM%2BtOh7BNlfx5tJB6M32j%2FbTLjnwo5ifmuhGKE0d0%2Biv1wb9bYvgUPXY7vu0r%2BTgxMf3ykz7DFLE%2FeZ3Bszi%2BInpZ8aKsIt61xG%2B9C7qiBGeUaafO9NNgC8TVRBCIp1jSeYnLcPBRBcJzzGbG8b6NISf7MC05VTa%2BUVLPq0nNXXwhfeRUo0NOKfSLmmE2AYk34XHJ7nvEZX5VQb5XomV8Myl%2Fyi9Hs8kr7ClQyn1KXzj1GSsOG%2BdLmrKAlhOBaiNWffV0Xj2pQdmXU2hPRQZ9jcmzd3NVmd%2BF1fht8h3V63IjZK5sBmMUWnJbnzHMY2vp5TGRPc%2FmHGBY3X7Y0HyruslB10miO%2BiFI4U8nKcWrQfLg16em%2FYYqI3TeeU1aqFJa4z2XK8ne9SQSZ9gSLYRXjpr23g1sh0%2BT2%2Fdr28Zox3uPK7dz09DBRWtT2MGnqvKOlg3pXF91gaqjfYWGSVnwdkue8qu6HdofazX2C1%2BUf86MSRHk3ihNTCFi97BA%2BJDQZPe5u1uXRZxDSgfGkLGewl1EYeaE8YBnU9S8N6TwQChJaE6bmuGuPSF3WG7dcdkSzryho4lkhi58SrOvXYBD2HsWd76B8L5zjCty6vEBjqkASbEemiMjyqMHlTMaTyFaKX5ddJS3BXELKkSwJIJcjiaHr93%2BcAfMkTOqc84s%2F66EtJVous9dd8bS6bu3n6x2bgcj7Cgymo0yzkT%2BPQrcgbH4hEDeokbKes2UOfGEJrpZkwXeQATUeWf%2B0yy5EaQTW9TzN7eh%2BNMisVc4ha8CJghVH4%2FcWt9xwRnQWtvOrGo7Bm51f25eNMjhMRQMIiTcfXuhTwU&X-Amz-Signature=d7de68e2d618be9bc53ed55a0add561193c31fbd42de39c731bf48c1f75135ed&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 참고

- https://medium.com/@hugmanskj/mastering-llama-rotary-positional-embedding-rope-이해하기-9b1963a22852
- https://en.wikipedia.org/wiki/Transformer_(deep_learning_architecture)?utm_source=chatgpt.com
- https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/01584.pdf?utm_source=chatgpt.com
- https://medium.com/ai-insights-cobet/rotary-positional-embeddings-a-detailed-look-and-comprehensive-understanding-4ff66a874d83
- https://karthick.ai/blog/2024/Rotatory-Position-Embedding-(RoPE)/?utm_source=chatgpt.com
- https://newsletter.theaiedge.io/p/all-about-the-modern-positional-encodings?utm_source=chatgpt.com

