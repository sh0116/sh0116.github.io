---
title: "**Transformer (Attention is All You Need) 분석**"
date: 2025-08-04 06:05:00 +0900
categories: [논문리뷰]
tags: [AI, Transfomer, LLM]
description: Attention is All You Need 리뷰
toc: true
comments: true
---

# **Transformer (Attention is All You Need)**

## **Transformer Encoder / Decoder**

### Encoder 방식

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/b2e43ef6-e7b5-4858-88bd-11445be5cc29/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667AK7O2KO%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T071959Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIQD4qNT%2F4HSx77nObhxfEmsrlZc0uh%2Fdp97pBSfAbqhVJQIgH3goh%2BHNs67hDwaTQHkqtAmNTsZocnzIsKA20musDB4q%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDLNt3bF2pBbt04nBmyrcA%2FwConbBhDozRFlyhdkKhdR8A%2F1y0BdhlAU9BpGI13BprqR9ontJv4k82fNOwOOAnEqE8ARHefKYy5N3qMAd2lKU5IrN49%2B%2Bn3vGD8T6j%2BnHv2P7qib7lU2Zfx4J3U9ftyjNKcrxz6TP4H7GauNl7tC1u51VLzK4PmMoU3XwUeivgDaeWJRN6wa3Sc97F0u%2FMS5RilN6VIM4f4sy0Zq2Yg%2BsogLwkEnTHlBwAP7T%2BgAV8EwmAcSTqouAkXtycDCZKR7grvP%2BLraG%2FhtshIewbuedSngSO7d9bHnTq7me%2FEEfxIdpjgXsd1mA9VBfGaVErzkisBgPXxgc70%2B8rbn8HHQmPzZNl1%2BS0Y6fnh%2F8Ur0%2BE9muPVj5CF7F2595j8BxHukfaaQz%2B%2BR8%2BlU8tEArcRLeAC26SRD4c%2F3ynck5kTDWonwpBzfpvuM%2Fpg0ZFYjsyTaHieCd%2F%2BM5dDCzAf%2FF6me%2F7J4vFfTQqr5zRdC7DWZASvcRGNCrsihGxjboQEKRaFlqlp0N%2Bturll%2FcEz%2B%2BhE7ayKm8VH4QjEz2E2px%2Bx8q4CJuAvd541Lez9rrw2vss4N02i3sbAjXcNN3GxzypdZ77XzzHuxVfHkeLYXsMfBbtkLlE3BzbA6Od8uzMKe4wcQGOqUB58LFIX%2BrmUZeToJXIpb9lrnb%2FUhb%2Fxnxts1cPKFm9VzMWzowmApJ6PqHzLBTKKNjO%2B8IaDKVrzR5f2nKAhp%2BgTrQtmOAQaZxHVMgYcVCGfgDVasAUf7eF%2FhpNZu%2F1Qd1hg2SD7vMDr8wW0%2F3Sb5MQ81H%2F5Hr97T1LITG2WttpxvJHhA0Xr88MLtZ6jRtKWL%2F0X%2BegCf3%2BwsHXTo30oqxUm01nsLD&X-Amz-Signature=42909cf7b198a8c0f30bed985bdda5aa1454054e70cdce4b971e5eb8ddc40c01&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Encoder 는 N개의 Encoder Block 으로 구성되어 있다.  (논문에서는 N = 6으로 사용했다. )

Encoder Block의 Input/output 형태는 동일하다. 어떤 Matrix 를 Input으로 받는다고 했을 때, output 역시 해당 Matrix와 같은 형태(Shape)를 갖고있다. → Shape이 바뀌지 않는다 (멱등하다.)

각 Encoder 모델은 연결되어 있다. N-1 EB 와 N EB가 연결되어 있다. 각 Input / Output Matrix Shape도 같기 때문에 전체 Encoder의 Shape은 항상 일정하다 (멱등하다.)

Encoder Block을 여러 겹으로 쌓는 것인가? 
Encoder Block은 Input으로 들어오는 문장을 Vector화 하여 Context로 만든다, Context로 만들어진 문장은 추상화되어 더 넓은 관점으로 높은 차원에서 고려될 수 있는 정보로 바뀌고 이 과정을 반복하면 매우 높은 차원의(추상화된 정보) Context가 생성되고 더 많은 관점에서 피처들을 뽑아낼 수 있다.

문장 → 높은 차원의 Context → 보다 더 높은 차원의 Context → …. → Output

일단 이 정도로만 하고 넘어가면 될 것 같다. 

## **Encoder Block**

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/14fc4b24-1f46-437d-80dc-f938777ef95b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667AK7O2KO%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T071959Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIQD4qNT%2F4HSx77nObhxfEmsrlZc0uh%2Fdp97pBSfAbqhVJQIgH3goh%2BHNs67hDwaTQHkqtAmNTsZocnzIsKA20musDB4q%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDLNt3bF2pBbt04nBmyrcA%2FwConbBhDozRFlyhdkKhdR8A%2F1y0BdhlAU9BpGI13BprqR9ontJv4k82fNOwOOAnEqE8ARHefKYy5N3qMAd2lKU5IrN49%2B%2Bn3vGD8T6j%2BnHv2P7qib7lU2Zfx4J3U9ftyjNKcrxz6TP4H7GauNl7tC1u51VLzK4PmMoU3XwUeivgDaeWJRN6wa3Sc97F0u%2FMS5RilN6VIM4f4sy0Zq2Yg%2BsogLwkEnTHlBwAP7T%2BgAV8EwmAcSTqouAkXtycDCZKR7grvP%2BLraG%2FhtshIewbuedSngSO7d9bHnTq7me%2FEEfxIdpjgXsd1mA9VBfGaVErzkisBgPXxgc70%2B8rbn8HHQmPzZNl1%2BS0Y6fnh%2F8Ur0%2BE9muPVj5CF7F2595j8BxHukfaaQz%2B%2BR8%2BlU8tEArcRLeAC26SRD4c%2F3ynck5kTDWonwpBzfpvuM%2Fpg0ZFYjsyTaHieCd%2F%2BM5dDCzAf%2FF6me%2F7J4vFfTQqr5zRdC7DWZASvcRGNCrsihGxjboQEKRaFlqlp0N%2Bturll%2FcEz%2B%2BhE7ayKm8VH4QjEz2E2px%2Bx8q4CJuAvd541Lez9rrw2vss4N02i3sbAjXcNN3GxzypdZ77XzzHuxVfHkeLYXsMfBbtkLlE3BzbA6Od8uzMKe4wcQGOqUB58LFIX%2BrmUZeToJXIpb9lrnb%2FUhb%2Fxnxts1cPKFm9VzMWzowmApJ6PqHzLBTKKNjO%2B8IaDKVrzR5f2nKAhp%2BgTrQtmOAQaZxHVMgYcVCGfgDVasAUf7eF%2FhpNZu%2F1Qd1hg2SD7vMDr8wW0%2F3Sb5MQ81H%2F5Hr97T1LITG2WttpxvJHhA0Xr88MLtZ6jRtKWL%2F0X%2BegCf3%2BwsHXTo30oqxUm01nsLD&X-Amz-Signature=7c73932b86d449455a61bcba77653a31cf4ca73d2cb18c951b8a2916dd692675&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Encoder Block은 크게 Multi-Head Attention Layer, Position-wise Feed-Forward Layer로 구성된다.

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/2934b9e2-c4eb-4789-b583-072f846976a0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667AK7O2KO%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T071959Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIQD4qNT%2F4HSx77nObhxfEmsrlZc0uh%2Fdp97pBSfAbqhVJQIgH3goh%2BHNs67hDwaTQHkqtAmNTsZocnzIsKA20musDB4q%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDLNt3bF2pBbt04nBmyrcA%2FwConbBhDozRFlyhdkKhdR8A%2F1y0BdhlAU9BpGI13BprqR9ontJv4k82fNOwOOAnEqE8ARHefKYy5N3qMAd2lKU5IrN49%2B%2Bn3vGD8T6j%2BnHv2P7qib7lU2Zfx4J3U9ftyjNKcrxz6TP4H7GauNl7tC1u51VLzK4PmMoU3XwUeivgDaeWJRN6wa3Sc97F0u%2FMS5RilN6VIM4f4sy0Zq2Yg%2BsogLwkEnTHlBwAP7T%2BgAV8EwmAcSTqouAkXtycDCZKR7grvP%2BLraG%2FhtshIewbuedSngSO7d9bHnTq7me%2FEEfxIdpjgXsd1mA9VBfGaVErzkisBgPXxgc70%2B8rbn8HHQmPzZNl1%2BS0Y6fnh%2F8Ur0%2BE9muPVj5CF7F2595j8BxHukfaaQz%2B%2BR8%2BlU8tEArcRLeAC26SRD4c%2F3ynck5kTDWonwpBzfpvuM%2Fpg0ZFYjsyTaHieCd%2F%2BM5dDCzAf%2FF6me%2F7J4vFfTQqr5zRdC7DWZASvcRGNCrsihGxjboQEKRaFlqlp0N%2Bturll%2FcEz%2B%2BhE7ayKm8VH4QjEz2E2px%2Bx8q4CJuAvd541Lez9rrw2vss4N02i3sbAjXcNN3GxzypdZ77XzzHuxVfHkeLYXsMfBbtkLlE3BzbA6Od8uzMKe4wcQGOqUB58LFIX%2BrmUZeToJXIpb9lrnb%2FUhb%2Fxnxts1cPKFm9VzMWzowmApJ6PqHzLBTKKNjO%2B8IaDKVrzR5f2nKAhp%2BgTrQtmOAQaZxHVMgYcVCGfgDVasAUf7eF%2FhpNZu%2F1Qd1hg2SD7vMDr8wW0%2F3Sb5MQ81H%2F5Hr97T1LITG2WttpxvJHhA0Xr88MLtZ6jRtKWL%2F0X%2BegCf3%2BwsHXTo30oqxUm01nsLD&X-Amz-Signature=b3787e7d26af4cc024d4fef73eac383a9bd532f1414a35238ea76e2d4a9300a4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Multi-Head Attention은 Attention을 여러 개 수행하는 layer이다. 

Multi-Head Attention을 이해하기 위해서는 Scaled Dot-Product Attention에 대해 먼저 알아야만 한다. Attention이라는 것은 넓은 범위의 전체 data에서 특정한 부분에 집중한다는 의미이다. 

Scaled Dot-Product Attention 자체를 줄여서 Attention 이라고 한다.

> *The animal didn’t cross the street, because it was too tired.*

위 문장에서 *‘it’*은 무엇을 지칭하는 것일까? 

사람이라면 직관적으로 *‘animal’*과 연결지을 수 있지만, 컴퓨터는 *‘it’*이 *‘animal’*을 가리키는지, *‘street’*를 가리키는지 알지 못한다.

Attention은 이러한 문제를 해결하기 위해 두 token 사이의 연관 정도를 계산해내는 방법론이다. 

위의 경우에는 **같은 문장 내**의 두 token 사이의 Attention을 계산하는 것이므로, **Self-Attention**이라고 부른다. 반면, 

**서로 다른 두 문장**에 각각 존재하는 두 token 사이의 Attention을 계산하는 것을 **Cross-Attention**이라고 부른다.


### Attention 모델의 기본 구조

**Q, K, V**

Attention 계산에는 Query, Key, Value라는 3가지 vector가 사용된다. 각 vector의 역할을 정리하면 다음과 같다.

1. Query: 입력 시퀸스에서 관련 부분을 찾으려고하는 현재의 상태 벡터 (소스)
1. Key: 관계의 연관도를 찾기 위해 Query와 비교하는데 사용되는 벡터 (타겟)
1. Value: 특정 Key에 해당하는 입력 시퀸스의 가중치를 구하는데 사용되는 벡터 (벨류)
### Scaled Dot-Product Attention 상세

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/dac62052-f9b4-4944-8208-320b66c9da6e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667AK7O2KO%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T071959Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIQD4qNT%2F4HSx77nObhxfEmsrlZc0uh%2Fdp97pBSfAbqhVJQIgH3goh%2BHNs67hDwaTQHkqtAmNTsZocnzIsKA20musDB4q%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDLNt3bF2pBbt04nBmyrcA%2FwConbBhDozRFlyhdkKhdR8A%2F1y0BdhlAU9BpGI13BprqR9ontJv4k82fNOwOOAnEqE8ARHefKYy5N3qMAd2lKU5IrN49%2B%2Bn3vGD8T6j%2BnHv2P7qib7lU2Zfx4J3U9ftyjNKcrxz6TP4H7GauNl7tC1u51VLzK4PmMoU3XwUeivgDaeWJRN6wa3Sc97F0u%2FMS5RilN6VIM4f4sy0Zq2Yg%2BsogLwkEnTHlBwAP7T%2BgAV8EwmAcSTqouAkXtycDCZKR7grvP%2BLraG%2FhtshIewbuedSngSO7d9bHnTq7me%2FEEfxIdpjgXsd1mA9VBfGaVErzkisBgPXxgc70%2B8rbn8HHQmPzZNl1%2BS0Y6fnh%2F8Ur0%2BE9muPVj5CF7F2595j8BxHukfaaQz%2B%2BR8%2BlU8tEArcRLeAC26SRD4c%2F3ynck5kTDWonwpBzfpvuM%2Fpg0ZFYjsyTaHieCd%2F%2BM5dDCzAf%2FF6me%2F7J4vFfTQqr5zRdC7DWZASvcRGNCrsihGxjboQEKRaFlqlp0N%2Bturll%2FcEz%2B%2BhE7ayKm8VH4QjEz2E2px%2Bx8q4CJuAvd541Lez9rrw2vss4N02i3sbAjXcNN3GxzypdZ77XzzHuxVfHkeLYXsMfBbtkLlE3BzbA6Od8uzMKe4wcQGOqUB58LFIX%2BrmUZeToJXIpb9lrnb%2FUhb%2Fxnxts1cPKFm9VzMWzowmApJ6PqHzLBTKKNjO%2B8IaDKVrzR5f2nKAhp%2BgTrQtmOAQaZxHVMgYcVCGfgDVasAUf7eF%2FhpNZu%2F1Qd1hg2SD7vMDr8wW0%2F3Sb5MQ81H%2F5Hr97T1LITG2WttpxvJHhA0Xr88MLtZ6jRtKWL%2F0X%2BegCf3%2BwsHXTo30oqxUm01nsLD&X-Amz-Signature=8cd2b31937c754e369c092686b23fbc1f4e0ed68e8219fc3a0a89dc91dee2166&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

1. Input에는 Position Encoding + Embeding된 데이터가 들어온다.
1. Linear에서는 1번 Input Matrix에 대해 차원 축소와 출력 Matrix의 모양과 맞춰주는 역할을 한다. 
1. MatMUL에서는 Query와 Key 행렬의 내적을 통해 Attention Score Matrix 를 만든다. 
1. 이후에 Scale과 SoftMax를 통해서 각 유사도의 값의 합(항목별)이 1이 되도록 SoftMax해준다.
![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/c25b2651-1360-4dc3-8392-b5431fd36014/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667AK7O2KO%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T071959Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIQD4qNT%2F4HSx77nObhxfEmsrlZc0uh%2Fdp97pBSfAbqhVJQIgH3goh%2BHNs67hDwaTQHkqtAmNTsZocnzIsKA20musDB4q%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDLNt3bF2pBbt04nBmyrcA%2FwConbBhDozRFlyhdkKhdR8A%2F1y0BdhlAU9BpGI13BprqR9ontJv4k82fNOwOOAnEqE8ARHefKYy5N3qMAd2lKU5IrN49%2B%2Bn3vGD8T6j%2BnHv2P7qib7lU2Zfx4J3U9ftyjNKcrxz6TP4H7GauNl7tC1u51VLzK4PmMoU3XwUeivgDaeWJRN6wa3Sc97F0u%2FMS5RilN6VIM4f4sy0Zq2Yg%2BsogLwkEnTHlBwAP7T%2BgAV8EwmAcSTqouAkXtycDCZKR7grvP%2BLraG%2FhtshIewbuedSngSO7d9bHnTq7me%2FEEfxIdpjgXsd1mA9VBfGaVErzkisBgPXxgc70%2B8rbn8HHQmPzZNl1%2BS0Y6fnh%2F8Ur0%2BE9muPVj5CF7F2595j8BxHukfaaQz%2B%2BR8%2BlU8tEArcRLeAC26SRD4c%2F3ynck5kTDWonwpBzfpvuM%2Fpg0ZFYjsyTaHieCd%2F%2BM5dDCzAf%2FF6me%2F7J4vFfTQqr5zRdC7DWZASvcRGNCrsihGxjboQEKRaFlqlp0N%2Bturll%2FcEz%2B%2BhE7ayKm8VH4QjEz2E2px%2Bx8q4CJuAvd541Lez9rrw2vss4N02i3sbAjXcNN3GxzypdZ77XzzHuxVfHkeLYXsMfBbtkLlE3BzbA6Od8uzMKe4wcQGOqUB58LFIX%2BrmUZeToJXIpb9lrnb%2FUhb%2Fxnxts1cPKFm9VzMWzowmApJ6PqHzLBTKKNjO%2B8IaDKVrzR5f2nKAhp%2BgTrQtmOAQaZxHVMgYcVCGfgDVasAUf7eF%2FhpNZu%2F1Qd1hg2SD7vMDr8wW0%2F3Sb5MQ81H%2F5Hr97T1LITG2WttpxvJHhA0Xr88MLtZ6jRtKWL%2F0X%2BegCf3%2BwsHXTo30oqxUm01nsLD&X-Amz-Signature=62b10cc7cfcb4c6f9dc24dde8c69ef773bf81cb94e27132d172fa0e4779d0ca3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/34305e15-6d2f-4993-a64c-9ef01a463274/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667AK7O2KO%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T071959Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIQD4qNT%2F4HSx77nObhxfEmsrlZc0uh%2Fdp97pBSfAbqhVJQIgH3goh%2BHNs67hDwaTQHkqtAmNTsZocnzIsKA20musDB4q%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDLNt3bF2pBbt04nBmyrcA%2FwConbBhDozRFlyhdkKhdR8A%2F1y0BdhlAU9BpGI13BprqR9ontJv4k82fNOwOOAnEqE8ARHefKYy5N3qMAd2lKU5IrN49%2B%2Bn3vGD8T6j%2BnHv2P7qib7lU2Zfx4J3U9ftyjNKcrxz6TP4H7GauNl7tC1u51VLzK4PmMoU3XwUeivgDaeWJRN6wa3Sc97F0u%2FMS5RilN6VIM4f4sy0Zq2Yg%2BsogLwkEnTHlBwAP7T%2BgAV8EwmAcSTqouAkXtycDCZKR7grvP%2BLraG%2FhtshIewbuedSngSO7d9bHnTq7me%2FEEfxIdpjgXsd1mA9VBfGaVErzkisBgPXxgc70%2B8rbn8HHQmPzZNl1%2BS0Y6fnh%2F8Ur0%2BE9muPVj5CF7F2595j8BxHukfaaQz%2B%2BR8%2BlU8tEArcRLeAC26SRD4c%2F3ynck5kTDWonwpBzfpvuM%2Fpg0ZFYjsyTaHieCd%2F%2BM5dDCzAf%2FF6me%2F7J4vFfTQqr5zRdC7DWZASvcRGNCrsihGxjboQEKRaFlqlp0N%2Bturll%2FcEz%2B%2BhE7ayKm8VH4QjEz2E2px%2Bx8q4CJuAvd541Lez9rrw2vss4N02i3sbAjXcNN3GxzypdZ77XzzHuxVfHkeLYXsMfBbtkLlE3BzbA6Od8uzMKe4wcQGOqUB58LFIX%2BrmUZeToJXIpb9lrnb%2FUhb%2Fxnxts1cPKFm9VzMWzowmApJ6PqHzLBTKKNjO%2B8IaDKVrzR5f2nKAhp%2BgTrQtmOAQaZxHVMgYcVCGfgDVasAUf7eF%2FhpNZu%2F1Qd1hg2SD7vMDr8wW0%2F3Sb5MQ81H%2F5Hr97T1LITG2WttpxvJHhA0Xr88MLtZ6jRtKWL%2F0X%2BegCf3%2BwsHXTo30oqxUm01nsLD&X-Amz-Signature=6e06550bfb7ded5c9cc583a166b4de412f2cab436e864243add74d1843bd79cb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

마지막에 Value Matrix와 내적한다. 

조금 주요 부분을 리즈너블하게 설명을 하자면

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/2a36b0af-a461-4513-9bcc-7d2d30b5a238/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667AK7O2KO%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T071959Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIQD4qNT%2F4HSx77nObhxfEmsrlZc0uh%2Fdp97pBSfAbqhVJQIgH3goh%2BHNs67hDwaTQHkqtAmNTsZocnzIsKA20musDB4q%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDLNt3bF2pBbt04nBmyrcA%2FwConbBhDozRFlyhdkKhdR8A%2F1y0BdhlAU9BpGI13BprqR9ontJv4k82fNOwOOAnEqE8ARHefKYy5N3qMAd2lKU5IrN49%2B%2Bn3vGD8T6j%2BnHv2P7qib7lU2Zfx4J3U9ftyjNKcrxz6TP4H7GauNl7tC1u51VLzK4PmMoU3XwUeivgDaeWJRN6wa3Sc97F0u%2FMS5RilN6VIM4f4sy0Zq2Yg%2BsogLwkEnTHlBwAP7T%2BgAV8EwmAcSTqouAkXtycDCZKR7grvP%2BLraG%2FhtshIewbuedSngSO7d9bHnTq7me%2FEEfxIdpjgXsd1mA9VBfGaVErzkisBgPXxgc70%2B8rbn8HHQmPzZNl1%2BS0Y6fnh%2F8Ur0%2BE9muPVj5CF7F2595j8BxHukfaaQz%2B%2BR8%2BlU8tEArcRLeAC26SRD4c%2F3ynck5kTDWonwpBzfpvuM%2Fpg0ZFYjsyTaHieCd%2F%2BM5dDCzAf%2FF6me%2F7J4vFfTQqr5zRdC7DWZASvcRGNCrsihGxjboQEKRaFlqlp0N%2Bturll%2FcEz%2B%2BhE7ayKm8VH4QjEz2E2px%2Bx8q4CJuAvd541Lez9rrw2vss4N02i3sbAjXcNN3GxzypdZ77XzzHuxVfHkeLYXsMfBbtkLlE3BzbA6Od8uzMKe4wcQGOqUB58LFIX%2BrmUZeToJXIpb9lrnb%2FUhb%2Fxnxts1cPKFm9VzMWzowmApJ6PqHzLBTKKNjO%2B8IaDKVrzR5f2nKAhp%2BgTrQtmOAQaZxHVMgYcVCGfgDVasAUf7eF%2FhpNZu%2F1Qd1hg2SD7vMDr8wW0%2F3Sb5MQ81H%2F5Hr97T1LITG2WttpxvJHhA0Xr88MLtZ6jRtKWL%2F0X%2BegCf3%2BwsHXTo30oqxUm01nsLD&X-Amz-Signature=29033ca4692b3824997cd6a610a9e26680e74dc146293267ac301910470a3403&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

1. Matmul에서 Query와 Key 간의 유사도를 계산한다, 각 단어(토큰) 간의 유사도를 계산해서 관련 있는 부분은 더 많은 정보를, 유사도가 적은 단어(토큰)은 적은 정보를 가져간다. 
1. 마지막에 Value를 내적하여 Attention Score Matrix를 적용한다.
1. 이걸 Multi Head 방식으로 여러 겹 쌓는 이유는 위 그림처럼 다양한 관점에서 더 복잡한 관계성을 파악할 수 있는 장점이 있기 때문이다. 
참조

https://www.blossominkyung.com/deeplearning/transformer-mha

https://tech.scatterlab.co.kr/vllm-implementation-details/

https://cpm0722.github.io/pytorch-implementation/transformer


