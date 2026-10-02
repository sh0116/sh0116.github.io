---
source: knowledge-base
origin: notion
title: "Neural Networks 신경망 : MLP (Multilayer Perceptron) "
area: "아키텍처와 기술 소개"
tags: ["area/architecture", "concept/ai"]
created: "2025-08-04T06:05:00.000Z"
last_edited: "2025-08-04T07:04:00.000Z"
status: published
public: true
notion_id: "245172a5-56d6-8036-b0d8-f3baed7f59f9"
notion_url: "https://www.notion.so/Neural-Networks-MLP-Multilayer-Perceptron-245172a556d68036b0d8f3baed7f59f9"
type: note
updated: 2026-07-07
---

# Neural Networks 신경망 : MLP (Multilayer Perceptron) 

## 요약

MLP (Multilayer Perceptron)  소개

개념, 구현 맥락, 후속 학습거리를 지식 그래프에 연결하기 위한 정리 노트입니다.

## 핵심 포인트

- MLP (Multilayer Perceptron)  소개
- Perceptron 퍼셉트론
- Multilayer Perceptron : MLP 다층 퍼셉트론

## 지식 그래프

- [[wiki/mocs/Knowledge Base|Knowledge Base]]
- [[wiki/mocs/아키텍처와-기술-소개|아키텍처와 기술 소개]]

## 정리 내용

## Perceptron 퍼셉트론
1957년 프랑크 로젠블라트(Frank Rosenblatt)가 제안한 초기 인공신경망이다. 
다수의 입력으로부터 하나의 결과를 내보내는 알고리즘으로 선형 분류 모델이다.
초기의 Perceptron의 경우 단층 퍼셉트론으로 가중치와 Bias를 조정하여 직선으로 데이터를 선형적으로 분류할 수 있는 신경망이다.
다만 XOR와 같은 한 직선으로 분류가 불가능한 문제(복잡한 문제)의 경우 수학적으로 풀 수 없다는 한계점이 있다.  
![[_attachments/notion/Neural-Networks-신경망-MLP-(Multilayer-Perceptron)/245172a556d68110b313f2e65bc5f335.png]]
출처 : [https://ko.wikipedia.org/wiki/파일:Perceptron_moj.png](https://ko.wikipedia.org/wiki/%ED%8C%8C%EC%9D%BC:Perceptron_moj.png)
> [!note] OR과 같은 문제는 풀 수 있지만, XOR을 단층 퍼셉트론 구조로 풀 수 없다
![[_attachments/notion/Neural-Networks-신경망-MLP-(Multilayer-Perceptron)/245172a556d68100b151cae218170cd5.png]]
출처 : [https://dev.to/jbahire/demystifying-the-xor-problem-1blk](https://dev.to/jbahire/demystifying-the-xor-problem-1blk)
## Multilayer Perceptron : MLP 다층 퍼셉트론
MLP는 XOR과 같은 기존 perceptron이 풀지 못하던 구조적 한계를 벗어나기 위한 아키텍처입니다.
선형 분리가 불가능한 경우를 Perceptron을 다층(MultiLayer)로 쌓아 해결하는 구조입니다.
구조
- 입력층 : 모델 입력 벡터
- 은닉층 : 입력층과 출력층 사이의 여러 뉴런 → MLP의 구조
- 출력층 : 최종 분류 또는 회귀 값을 출력하는 층
![[_attachments/notion/Neural-Networks-신경망-MLP-(Multilayer-Perceptron)/245172a556d6819580f1c772f950ff1d.png]]
출처 : [https://commons.wikimedia.org/wiki/File:Multi-Layer_Perceptron_(MLP)_Neural_Network._From_Left_to_right_Inputs,_Weights,_Perceptron_Neurons_in_Hidden_Layer,_Weights_and_Output_Layer.png](https://commons.wikimedia.org/wiki/File:Multi-Layer_Perceptron_%28MLP%29_Neural_Network._From_Left_to_right_Inputs,_Weights,_Perceptron_Neurons_in_Hidden_Layer,_Weights_and_Output_Layer.png)
> [!note] Activation Functions(활성함수)란 일종의 판단 결과값이다. 
  Weight + Bias를 적용한 값에 활성함수를 씌우면 값이 나온다.
![[_attachments/notion/Neural-Networks-신경망-MLP-(Multilayer-Perceptron)/245172a556d681e3a2e7e63bc87f927e.png]]
출처 : [https://wikidocs.net/250622](https://wikidocs.net/250622)
> [!note] 왜 이제 비선형의 활성함수가 필요한진 밑에 사진을 보면 알 수 있다.
![[_attachments/notion/Neural-Networks-신경망-MLP-(Multilayer-Perceptron)/245172a556d681aaab8bc594e416da1f.png]]
![[_attachments/notion/Neural-Networks-신경망-MLP-(Multilayer-Perceptron)/245172a556d681bda5b7d3bda7cf2991.png]]
출처 : [http://aidev.co.kr/deeplearning/7551](http://aidev.co.kr/deeplearning/7551)
> [!note] 아래 사진을 보면 다층퍼셉트론이 어떻게 XOR을 해결하는지 볼 수 있다. 
  파란색과 빨간색선이 초록선을 만들고 최종적으론 초록선이 판단하는 구조
![[_attachments/notion/Neural-Networks-신경망-MLP-(Multilayer-Perceptron)/245172a556d681febfb0f1819145a0a7.png]]
출처 : [https://www.youtube.com/watch?v=J8K7NFbsSIM](https://www.youtube.com/watch?v=J8K7NFbsSIM)

## 출처

- 원문: https://www.notion.so/Neural-Networks-MLP-Multilayer-Perceptron-245172a556d68036b0d8f3baed7f59f9
- Vault path: wiki/notes/architecture/Neural-Networks-신경망-MLP-(Multilayer-Perceptron).md
