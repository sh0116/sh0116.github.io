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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/5e2fe1e1-9eb2-43b5-9a93-4be21c14ddcc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RNNGALM6%2F20250729%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250729T073215Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIQDNsYuOeKvRPkLmAUZKE%2FlUQh1pV9CFbbrf11CSqUj16QIgMW79d8ZQ8s9IvS84C3zXjjuJfNX6ah0uMqmjCQ4ppBUqiAQInv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKszbMSK3VWFtr3n%2BCrcA%2BPX46GAkLSnL%2BSZ44PVQ%2BMHZGKqySaVIBEhLsgB4xEbxooubjAlLFVnItU3Cv9brbIBirQ1MxD9GWMTCjKsBrJ0MkTBuDjru8i89CEUIIeJr0CT1AQtpTe5TEEwnB5F0BzTho8lPkuYYWNCyxt5mjHBtHJhsUoKVWqESLI5oDC1Rs4fPpJZ6GPJGObF9Nk%2FCwMb4mAIl6qRkMrdTnShm7hXrZKDdgiZW6ZmiY6QSZZbP7qrQId9q10I1uL808ma%2F2ejnAccegJGGfxC3ekEQco5ApoUaGnetiKe%2B58zxU7wvmRdU2yJJE8siM%2FWrxz9ps5jgyZlZch01UTePkwdK7z%2FcDF6kck83oBX5jb6iElBNF9mcLwufMRNp2CPN7iQHa60Qss0RhqTNBoOO7kpO%2B68Xa%2FvVxo9pqPt85HuC4q21GxKD9t2qDEXMu%2Fbl%2ByPEAoULPNMBpPa5C%2BvCsbRJnnXProUI7oKADopQ4IdfBZCjTRmE9bLpNeL5dGbE%2BZ5sIkSvdc9Hkk4awHwKUeQJCCs0qXsetCW%2Fkguyb%2BFDNtg565d5hgkw86b5QD6uGr1Xm0wy4jFBD6aETcdWcE1c05lQNlona9CbG4DUPUfpYA18CANnZGfF5lBtJFtMPu0ocQGOqUBgAOohHQC6krz6qdvvYaj5vPbg7D%2B2ZJZXy%2FPsCXVbb9AbpEM4ftPkUOhMMd7285Gd%2F9YNnHGAmxUB0eLDd2oM%2F8A%2BihVgP7X7aNY2zbBOVFOwHqfK285a7s3A3%2FUAQMZHfQWfwTe3F9I2ye%2FDes1XSyTAXuBwtyEb7cClNVB1O0yYvUQMxyiYwrMBfdZA%2BXdpQ7TvnA4hVJI9uAIoStkNHZPESA8&X-Amz-Signature=c85c80fcfbc4a366a5bb901eaedc7b34da8e6a33acfecb1c26e58a52534f3688&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

RoPE는 백터의 회전을 통해 위치를 표현합니다, 백터의 회전은 복소수( Complex Number) 를 먼저 이해 해야하는데요.

복소수를 A+Bi 형태로 표현하여 2차원 평면에 복소평면을 그리면 위 그림과 같습니다.

실수축과 허수축으로 구성되어있는 형식입니다.

여기서 Euler 공식을 통해 회전시킬 수 있습니다.

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/b351347d-7727-489a-ae89-52f7948111de/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RNNGALM6%2F20250729%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250729T073215Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIQDNsYuOeKvRPkLmAUZKE%2FlUQh1pV9CFbbrf11CSqUj16QIgMW79d8ZQ8s9IvS84C3zXjjuJfNX6ah0uMqmjCQ4ppBUqiAQInv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKszbMSK3VWFtr3n%2BCrcA%2BPX46GAkLSnL%2BSZ44PVQ%2BMHZGKqySaVIBEhLsgB4xEbxooubjAlLFVnItU3Cv9brbIBirQ1MxD9GWMTCjKsBrJ0MkTBuDjru8i89CEUIIeJr0CT1AQtpTe5TEEwnB5F0BzTho8lPkuYYWNCyxt5mjHBtHJhsUoKVWqESLI5oDC1Rs4fPpJZ6GPJGObF9Nk%2FCwMb4mAIl6qRkMrdTnShm7hXrZKDdgiZW6ZmiY6QSZZbP7qrQId9q10I1uL808ma%2F2ejnAccegJGGfxC3ekEQco5ApoUaGnetiKe%2B58zxU7wvmRdU2yJJE8siM%2FWrxz9ps5jgyZlZch01UTePkwdK7z%2FcDF6kck83oBX5jb6iElBNF9mcLwufMRNp2CPN7iQHa60Qss0RhqTNBoOO7kpO%2B68Xa%2FvVxo9pqPt85HuC4q21GxKD9t2qDEXMu%2Fbl%2ByPEAoULPNMBpPa5C%2BvCsbRJnnXProUI7oKADopQ4IdfBZCjTRmE9bLpNeL5dGbE%2BZ5sIkSvdc9Hkk4awHwKUeQJCCs0qXsetCW%2Fkguyb%2BFDNtg565d5hgkw86b5QD6uGr1Xm0wy4jFBD6aETcdWcE1c05lQNlona9CbG4DUPUfpYA18CANnZGfF5lBtJFtMPu0ocQGOqUBgAOohHQC6krz6qdvvYaj5vPbg7D%2B2ZJZXy%2FPsCXVbb9AbpEM4ftPkUOhMMd7285Gd%2F9YNnHGAmxUB0eLDd2oM%2F8A%2BihVgP7X7aNY2zbBOVFOwHqfK285a7s3A3%2FUAQMZHfQWfwTe3F9I2ye%2FDes1XSyTAXuBwtyEb7cClNVB1O0yYvUQMxyiYwrMBfdZA%2BXdpQ7TvnA4hVJI9uAIoStkNHZPESA8&X-Amz-Signature=f78c12be6d9af14fcaf43fbf2a5b8c33f99a7fc4df474ffe04a57a3fc5c8ffcf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

복소수에 eⁱᶿ를 곱하면 각도 θ만큼 회전을 한다는 공식입니다.

예를 들어 A+Bi라는 벡터를 eⁱᶿ로 곱하면, 벡터의 크기는 유지하고 각도만 θ만큼 회전하여 새로운 벡터를 얻을 수 있다는 것 입니다.

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/beb7173f-68a2-43d0-bd38-5fbaca0c978a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RNNGALM6%2F20250729%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250729T073215Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIQDNsYuOeKvRPkLmAUZKE%2FlUQh1pV9CFbbrf11CSqUj16QIgMW79d8ZQ8s9IvS84C3zXjjuJfNX6ah0uMqmjCQ4ppBUqiAQInv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKszbMSK3VWFtr3n%2BCrcA%2BPX46GAkLSnL%2BSZ44PVQ%2BMHZGKqySaVIBEhLsgB4xEbxooubjAlLFVnItU3Cv9brbIBirQ1MxD9GWMTCjKsBrJ0MkTBuDjru8i89CEUIIeJr0CT1AQtpTe5TEEwnB5F0BzTho8lPkuYYWNCyxt5mjHBtHJhsUoKVWqESLI5oDC1Rs4fPpJZ6GPJGObF9Nk%2FCwMb4mAIl6qRkMrdTnShm7hXrZKDdgiZW6ZmiY6QSZZbP7qrQId9q10I1uL808ma%2F2ejnAccegJGGfxC3ekEQco5ApoUaGnetiKe%2B58zxU7wvmRdU2yJJE8siM%2FWrxz9ps5jgyZlZch01UTePkwdK7z%2FcDF6kck83oBX5jb6iElBNF9mcLwufMRNp2CPN7iQHa60Qss0RhqTNBoOO7kpO%2B68Xa%2FvVxo9pqPt85HuC4q21GxKD9t2qDEXMu%2Fbl%2ByPEAoULPNMBpPa5C%2BvCsbRJnnXProUI7oKADopQ4IdfBZCjTRmE9bLpNeL5dGbE%2BZ5sIkSvdc9Hkk4awHwKUeQJCCs0qXsetCW%2Fkguyb%2BFDNtg565d5hgkw86b5QD6uGr1Xm0wy4jFBD6aETcdWcE1c05lQNlona9CbG4DUPUfpYA18CANnZGfF5lBtJFtMPu0ocQGOqUBgAOohHQC6krz6qdvvYaj5vPbg7D%2B2ZJZXy%2FPsCXVbb9AbpEM4ftPkUOhMMd7285Gd%2F9YNnHGAmxUB0eLDd2oM%2F8A%2BihVgP7X7aNY2zbBOVFOwHqfK285a7s3A3%2FUAQMZHfQWfwTe3F9I2ye%2FDes1XSyTAXuBwtyEb7cClNVB1O0yYvUQMxyiYwrMBfdZA%2BXdpQ7TvnA4hVJI9uAIoStkNHZPESA8&X-Amz-Signature=84df18e61e1751baa21a87509548f185bd049155dffe2d3c1c0206fda342cb77&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/ec91cb0a-d924-4728-a8c8-be0ed6b8ea49/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RNNGALM6%2F20250729%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250729T073215Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIQDNsYuOeKvRPkLmAUZKE%2FlUQh1pV9CFbbrf11CSqUj16QIgMW79d8ZQ8s9IvS84C3zXjjuJfNX6ah0uMqmjCQ4ppBUqiAQInv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKszbMSK3VWFtr3n%2BCrcA%2BPX46GAkLSnL%2BSZ44PVQ%2BMHZGKqySaVIBEhLsgB4xEbxooubjAlLFVnItU3Cv9brbIBirQ1MxD9GWMTCjKsBrJ0MkTBuDjru8i89CEUIIeJr0CT1AQtpTe5TEEwnB5F0BzTho8lPkuYYWNCyxt5mjHBtHJhsUoKVWqESLI5oDC1Rs4fPpJZ6GPJGObF9Nk%2FCwMb4mAIl6qRkMrdTnShm7hXrZKDdgiZW6ZmiY6QSZZbP7qrQId9q10I1uL808ma%2F2ejnAccegJGGfxC3ekEQco5ApoUaGnetiKe%2B58zxU7wvmRdU2yJJE8siM%2FWrxz9ps5jgyZlZch01UTePkwdK7z%2FcDF6kck83oBX5jb6iElBNF9mcLwufMRNp2CPN7iQHa60Qss0RhqTNBoOO7kpO%2B68Xa%2FvVxo9pqPt85HuC4q21GxKD9t2qDEXMu%2Fbl%2ByPEAoULPNMBpPa5C%2BvCsbRJnnXProUI7oKADopQ4IdfBZCjTRmE9bLpNeL5dGbE%2BZ5sIkSvdc9Hkk4awHwKUeQJCCs0qXsetCW%2Fkguyb%2BFDNtg565d5hgkw86b5QD6uGr1Xm0wy4jFBD6aETcdWcE1c05lQNlona9CbG4DUPUfpYA18CANnZGfF5lBtJFtMPu0ocQGOqUBgAOohHQC6krz6qdvvYaj5vPbg7D%2B2ZJZXy%2FPsCXVbb9AbpEM4ftPkUOhMMd7285Gd%2F9YNnHGAmxUB0eLDd2oM%2F8A%2BihVgP7X7aNY2zbBOVFOwHqfK285a7s3A3%2FUAQMZHfQWfwTe3F9I2ye%2FDes1XSyTAXuBwtyEb7cClNVB1O0yYvUQMxyiYwrMBfdZA%2BXdpQ7TvnA4hVJI9uAIoStkNHZPESA8&X-Amz-Signature=66f092cb17c825721d06f76d5add163bd2d93a96d50c2bd3fa2f859bb98ed095&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

예를 들어 “애플 애플 애플 애플” 이라는 문장이 있을 때

기존 Transfomer 모델의 경우 Q/K 값이 같습니다, 상대 위치 정보를 파악할 수 없지만

RoPE 방식을 쓴다면 각 토큰의 위치별로 Rotation 값이 다르기 때문에 상대적인 각도(위치)가 반영됩니다.

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/862fb2ea-37e8-45c0-b8ce-bbb78d63f0c3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RNNGALM6%2F20250729%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250729T073215Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIQDNsYuOeKvRPkLmAUZKE%2FlUQh1pV9CFbbrf11CSqUj16QIgMW79d8ZQ8s9IvS84C3zXjjuJfNX6ah0uMqmjCQ4ppBUqiAQInv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKszbMSK3VWFtr3n%2BCrcA%2BPX46GAkLSnL%2BSZ44PVQ%2BMHZGKqySaVIBEhLsgB4xEbxooubjAlLFVnItU3Cv9brbIBirQ1MxD9GWMTCjKsBrJ0MkTBuDjru8i89CEUIIeJr0CT1AQtpTe5TEEwnB5F0BzTho8lPkuYYWNCyxt5mjHBtHJhsUoKVWqESLI5oDC1Rs4fPpJZ6GPJGObF9Nk%2FCwMb4mAIl6qRkMrdTnShm7hXrZKDdgiZW6ZmiY6QSZZbP7qrQId9q10I1uL808ma%2F2ejnAccegJGGfxC3ekEQco5ApoUaGnetiKe%2B58zxU7wvmRdU2yJJE8siM%2FWrxz9ps5jgyZlZch01UTePkwdK7z%2FcDF6kck83oBX5jb6iElBNF9mcLwufMRNp2CPN7iQHa60Qss0RhqTNBoOO7kpO%2B68Xa%2FvVxo9pqPt85HuC4q21GxKD9t2qDEXMu%2Fbl%2ByPEAoULPNMBpPa5C%2BvCsbRJnnXProUI7oKADopQ4IdfBZCjTRmE9bLpNeL5dGbE%2BZ5sIkSvdc9Hkk4awHwKUeQJCCs0qXsetCW%2Fkguyb%2BFDNtg565d5hgkw86b5QD6uGr1Xm0wy4jFBD6aETcdWcE1c05lQNlona9CbG4DUPUfpYA18CANnZGfF5lBtJFtMPu0ocQGOqUBgAOohHQC6krz6qdvvYaj5vPbg7D%2B2ZJZXy%2FPsCXVbb9AbpEM4ftPkUOhMMd7285Gd%2F9YNnHGAmxUB0eLDd2oM%2F8A%2BihVgP7X7aNY2zbBOVFOwHqfK285a7s3A3%2FUAQMZHfQWfwTe3F9I2ye%2FDes1XSyTAXuBwtyEb7cClNVB1O0yYvUQMxyiYwrMBfdZA%2BXdpQ7TvnA4hVJI9uAIoStkNHZPESA8&X-Amz-Signature=f26bbfcdf5cfb0c7a005a1ce326140ab588456ac58bf00cdbbb1952d752fefe5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 참고

- https://medium.com/@hugmanskj/mastering-llama-rotary-positional-embedding-rope-이해하기-9b1963a22852
- https://en.wikipedia.org/wiki/Transformer_(deep_learning_architecture)?utm_source=chatgpt.com
- https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/01584.pdf?utm_source=chatgpt.com
- https://medium.com/ai-insights-cobet/rotary-positional-embeddings-a-detailed-look-and-comprehensive-understanding-4ff66a874d83
- https://karthick.ai/blog/2024/Rotatory-Position-Embedding-(RoPE)/?utm_source=chatgpt.com
- https://newsletter.theaiedge.io/p/all-about-the-modern-positional-encodings?utm_source=chatgpt.com

