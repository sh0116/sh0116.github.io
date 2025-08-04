---
title: "**Transformer 모델 - Self-Attention**"
date: 2025-08-04 06:06:00 +0900
categories: [기술소개]
tags: [Transfomer, AI, LLM]
description: Self-Attention 개념
toc: true
comments: true
---

## 개요

2017년 NIPS에서 'Attention Is All You Need’ 라는 논문으로 Transformer 모델이 나왔다.

병렬 처리가 안되던 RNN의 한계를 극복한 알고리즘으로 자연어처리에서 좋은 결과를 보여줬다.

## 내용

### ASIS

17년도에 나온 Attentions Is All You Need 논문에서는 Attention만으로 구현된 모델을 소개한다. RNN 기법을 사용하지 않고 인코더, 디코더 구조로만 설계하고 번역 성능에서 RNN보다 뛰어난 성과를 냈습니다.

기존의 seq2seq 모델도 인코더와 디코더는 있었습니다.

입력  seq 를 하나의 백터로 압축하고 디코더는 이 백터를 기반으로 출력 seq 를 만들었습니다. 

이 과정에서 입력 seq의 정보가 손실되는 점이 문제였습니다.

RNN 구조를 사용하면 먼 단어일 수록 흐려진다는 단점들이 있었습니다. 

또한 병렬 처리가 안된다..

RNN모델은 이전Tn-1에 결과값을 현재Tn 연산에 사용하는 점 때문이다. 

따라서 n의 차이가 크면 흐려지고, 이전 결과값을 재귀적으로 받기 때문에 병렬 연산이 불가능하다.

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/1e7f5e6f-9228-4d68-9d1d-6554327138c3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YHXAF4LN%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T064837Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJIMEYCIQDWiOciZPTgeWI3KqVyTiYc7KfzJh75wa7NVnHhCC4PewIhAIDQoblZE1kHNi9ZpCkxh6HE9DmNMZjhRF9MmhyccemIKv8DCD8QABoMNjM3NDIzMTgzODA1IgzZ7W%2FGqsLQzl1B1Lcq3AOoXsoVbUvpVG43x0sHlIF%2FAlGP89XBw74c7LOrivJTrj5PjUAM1xiRHYaucEZIy09SSFzKKq5bemUMIZfXWC8PXGREJUqT0T9FgK%2FJQjWKVAZ3LEZaypet%2BdknF3DuboFXJPFtGs6Dfx%2B1FzStT0jzgcensRkpTkL%2FsTK1E3C%2B92t2ERPZjEPOn8jhVMtK1QYHAEJ97x1wUo4X4iIbS%2Bp3kQxXsQDYYKHa%2BOfEyo3F1NFj1G7HZQPg0jHruCB%2B7x9wHOVIPyspvIe1OGj%2BYy9iSPaHX2oT8eGHy6natllkb7WYcMFA42Mg0cIksKKgZjzxo4GkxcUYnf1Fs4E80qebYQA0DXhyuNUc7199TsDvbXDx1lPi5hUH6kPQTOLu1y3MtAhWFkBvMjEHQonL17pghk3pgELzkGKdNoJP%2FayLcAnXqkevZVEdoVb2SXGVoqOwxJtrTFzicnKQphVdpvsyRk0FnREmyHeDTEskptho3RidiLHifEy9VLlqkcUzlQSHFhm1VgzUewDI6eVB%2BmvFBV4NsnD03D5%2BMlbiLFQpxePCql%2FoRRJtVt%2FbY0F0s1DKEIgW%2FQ1TS5x%2FA38X9yWYHuKkDgeiwzdugm535DhjUi6vcJ86KebzshQGvjDPjcHEBjqkAduscCBtV6dGV18u6apQTSyOqF79SN5jgLN3PPfuP9%2BJMZiRI%2BFbS6IOa5Xr5o9Ij%2B6hRBs1W4SbJIvAyfcrvmlsb7IcTl6OaJ55Mg1tnCG82dFIVi9HEWR6ga%2BTyFobZXC2pUeP3WgQpTwS5OUekzjD1u%2BFYcvzKrABmZdcULIk1KC4fr5O8OTHVEhV%2FzXvy3S0dFR13%2BlUCT7hEoBbmI2Lpupi&X-Amz-Signature=54f0f24791c6d05014c2a9a1bb47e05c574ea74d646cfe35d4b162d34976e84b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### TOBE

이런 구조를 바꾼게 바로 2017년 NIPS에서 'Attention Is All You Need’ 라는 논문이다. 

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/6e9cd139-802d-46d7-a36a-93043fd1cafc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YHXAF4LN%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T064837Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJIMEYCIQDWiOciZPTgeWI3KqVyTiYc7KfzJh75wa7NVnHhCC4PewIhAIDQoblZE1kHNi9ZpCkxh6HE9DmNMZjhRF9MmhyccemIKv8DCD8QABoMNjM3NDIzMTgzODA1IgzZ7W%2FGqsLQzl1B1Lcq3AOoXsoVbUvpVG43x0sHlIF%2FAlGP89XBw74c7LOrivJTrj5PjUAM1xiRHYaucEZIy09SSFzKKq5bemUMIZfXWC8PXGREJUqT0T9FgK%2FJQjWKVAZ3LEZaypet%2BdknF3DuboFXJPFtGs6Dfx%2B1FzStT0jzgcensRkpTkL%2FsTK1E3C%2B92t2ERPZjEPOn8jhVMtK1QYHAEJ97x1wUo4X4iIbS%2Bp3kQxXsQDYYKHa%2BOfEyo3F1NFj1G7HZQPg0jHruCB%2B7x9wHOVIPyspvIe1OGj%2BYy9iSPaHX2oT8eGHy6natllkb7WYcMFA42Mg0cIksKKgZjzxo4GkxcUYnf1Fs4E80qebYQA0DXhyuNUc7199TsDvbXDx1lPi5hUH6kPQTOLu1y3MtAhWFkBvMjEHQonL17pghk3pgELzkGKdNoJP%2FayLcAnXqkevZVEdoVb2SXGVoqOwxJtrTFzicnKQphVdpvsyRk0FnREmyHeDTEskptho3RidiLHifEy9VLlqkcUzlQSHFhm1VgzUewDI6eVB%2BmvFBV4NsnD03D5%2BMlbiLFQpxePCql%2FoRRJtVt%2FbY0F0s1DKEIgW%2FQ1TS5x%2FA38X9yWYHuKkDgeiwzdugm535DhjUi6vcJ86KebzshQGvjDPjcHEBjqkAduscCBtV6dGV18u6apQTSyOqF79SN5jgLN3PPfuP9%2BJMZiRI%2BFbS6IOa5Xr5o9Ij%2B6hRBs1W4SbJIvAyfcrvmlsb7IcTl6OaJ55Mg1tnCG82dFIVi9HEWR6ga%2BTyFobZXC2pUeP3WgQpTwS5OUekzjD1u%2BFYcvzKrABmZdcULIk1KC4fr5O8OTHVEhV%2FzXvy3S0dFR13%2BlUCT7hEoBbmI2Lpupi&X-Amz-Signature=b4adfdbe0c56ba7db09a3228523f249d7f279c29a11e9cbb403e273b7e82915e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 참조

https://namu.wiki/w/트랜스포머(인공신경망)

https://chonchony.tistory.com/entry/순환신경망-RNN의-문제점-기울기-소실-기울기-폭주-Gradient-Vanishing-Exploding

https://calmmimiforest.tistory.com/110


