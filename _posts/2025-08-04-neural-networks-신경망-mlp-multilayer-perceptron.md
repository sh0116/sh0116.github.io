---
title: "Neural Networks 신경망 : MLP (Multilayer Perceptron)"
date: 2025-08-04 06:05:00 +0900
categories: [기술소개]
tags: [AI]
description: MLP (Multilayer Perceptron)  소개
toc: true
comments: true
redirect_from:
  - /posts/neural-networks-신경망-:-mlp-(multilayer-perceptron)/
---

# Perceptron 퍼셉트론

1957년 프랑크 로젠블라트(Frank Rosenblatt)가 제안한 초기 인공신경망이다. 

다수의 입력으로부터 하나의 결과를 내보내는 알고리즘으로 선형 분류 모델이다.

초기의 Perceptron의 경우 단층 퍼셉트론으로 가중치와 Bias를 조정하여 직선으로 데이터를 선형적으로 분류할 수 있는 신경망이다.

다만 XOR와 같은 한 직선으로 분류가 불가능한 문제(복잡한 문제)의 경우 수학적으로 풀 수 없다는 한계점이 있다.  

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/8a23f1f7-7f5b-4dd7-a5c0-2b667ed62360/image.png)

출처 : https://ko.wikipedia.org/wiki/파일:Perceptron_moj.png

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/2ffaeede-35f4-4628-a3c3-e21b9f48544a/image.png)

출처 : https://dev.to/jbahire/demystifying-the-xor-problem-1blk

# Multilayer Perceptron : MLP 다층 퍼셉트론

MLP는 XOR과 같은 기존 perceptron이 풀지 못하던 구조적 한계를 벗어나기 위한 아키텍처입니다.

선형 분리가 불가능한 경우를 Perceptron을 다층(MultiLayer)로 쌓아 해결하는 구조입니다.

**구조**

- 입력층 : 모델 입력 벡터
- 은닉층 : 입력층과 출력층 사이의 여러 뉴런 → MLP의 구조
- 출력층 : 최종 분류 또는 회귀 값을 출력하는 층
![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/580d271f-5f90-449f-be2c-6a1309f0f42a/image.png)

출처 : https://commons.wikimedia.org/wiki/File:Multi-Layer_Perceptron_(MLP)_Neural_Network._From_Left_to_right_Inputs,_Weights,_Perceptron_Neurons_in_Hidden_Layer,_Weights_and_Output_Layer.png

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/f80928a6-1073-4ca2-a511-72746a9a5cd0/image.png)

출처 : [RAW: {"type": "mention", "mention": {"type": "link_mention", "link_mention": {"href": "https://wikidocs.net/250622", "title": "3. 활성화 함수: 종류와 선택 기준", "icon_url": "https://wikidocs.net/static/img/favicon.ico", "description": "활성화 함수는 인공신경망에서 입력 신호를 출력 신호로 변환하는 역할을 한다. 활성화 함수는 신경망의 비선형성을 도입하여 복잡한 문제를 해결할 수 있도록 도와준다. 이 장에서는 …", "link_provider": "위키독스", "thumbnail_url": "https://wikidocs.net/images/book/resized_image_1.webp"}}, "annotations": {"bold": false, "italic": false, "strikethrough": false, "underline": false, "code": false, "color": "default"}, "plain_text": "https://wikidocs.net/250622", "href": "https://wikidocs.net/250622"}]

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/2b73a077-f0e3-410a-b669-1c2dc3d39b72/image.png)

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/bf377452-8d53-4500-a7b5-8a50569fee19/image.png)

출처 : [RAW: {"type": "mention", "mention": {"type": "link_mention", "link_mention": {"href": "http://aidev.co.kr/deeplearning/7551", "title": "딥러닝 - 신경망에 활성화 함수가 필요한 이유", "description": "https://www.facebook.com/groups/TensorFlowKR/permalink/900098033664589/ 신경망에서 활성화 함수가 필요한 이유를 잘 설명한 글입니다. 과거 단층신경망인 퍼셉트론은 XOR 연산을 할 수가 없었습니다. 당시 기호주의 인공지능의 대가인 마빈 민스키가 이를 공격했고, 그후 신경망의 첫 번째 겨울이 시작되었습니다. XOR 연산을 풀기 ...", "thumbnail_url": "http://aidev.co.kr/files/attach/images/186/551/007/a282d7d2143361488aa7de11e0441be7.jpg"}}, "annotations": {"bold": false, "italic": false, "strikethrough": false, "underline": false, "code": false, "color": "default"}, "plain_text": "http://aidev.co.kr/deeplearning/7551", "href": "http://aidev.co.kr/deeplearning/7551"}]

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/3be23704-c3ca-4d01-b7fa-4033a0b32125/image.png)

출처 : https://www.youtube.com/watch?v=J8K7NFbsSIM


