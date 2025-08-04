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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/1e7f5e6f-9228-4d68-9d1d-6554327138c3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RWDQ326Y%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T070454Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCIE4pYH%2BZLSdCSMjxr9JnBhettTNmuoebymI1aMwuPX%2BcAiEAlHuOJhJRY20i5y%2BpDTsR%2FFxCIHRfLNhNEj8S30N4dT0q%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDNgm3XLMhs4LXCbEvyrcA%2BXKM9V%2BKJfeW3nYLN1yapS%2BtgHCQbT2ZC0Vo5WW8eXSVJHyFTCf7M7GMT1JKpRK9VdevGI7OPynvRKaa8qzaYSy67T8AoXOBQP3nYtnbAz3QdtELbyWd6kQAyAoPTAwOqxK4sNYa4NkrS6fbbCLSWCSKvEUUeUfdoOhxdJKkCHcT0BD3aOmGORTHcVn6npoG%2BjOGqmCbC3Q52bv%2F78D5mCiRHmz5p4Y0HdHPEMPpMyUC5m1SkZdA8t1aRO7wGZZcNJiS0Ls2EKKA0TpJ%2F2wFRDJ2mnLoKjBhCnfRmR2tmSS564sUrjb%2FMwWj1KcugUjHvTbCUx4Y0ZU4dHujiTZ6uxoeFx6MxzHYUHtJa18r1aAPCy6AFex%2FrPfI9J48uF4Fl%2FLrh8owq%2BWKu0PweqFFsqHwdaUtrXCbUV%2FyxpzP4hBHKj%2F4hE70ZBgl2s8OVaNLuqczdspUODT7%2FfapLjwLqk%2BFe7eUkGw91nW8sIcU3IfKERydZAHNnsSa2T8HhNVPwqhWDB8KhQA8S4%2FGxl0M5njHjInuzwspi7lGgQc7NEktyILzMMo3vWLHrC4tHEnIRz98i9K%2Bocc%2FjhZxuD5bEOmN%2BNkJ07qmSuG2%2BZoxzwpzPbk77YkghpV8IUUMM%2BNwcQGOqUBp0kt2yJADj7XfguOB4%2FXfimS084wVG%2FX9rL%2FF2lGMt%2ByPeerFPP3je8JDUHlJ6xHkM1Mv%2BN8qvhUbZZ7Y2wq3QbMX5%2BbikwWmDqej4cU%2Fz4Hy9QMVytzd4a1qi3nqWJ%2FY4VTs8dXuJTV5wGy1KbqaS1FWX%2BDwr6gZYdL%2FlPqCTmdk%2BCr9AXuWRT%2F6Kkbx%2BpZV1b%2FXazcvjItnww6ywN3oxqx4Oxo&X-Amz-Signature=7c5c9739bf9afba8710881782f21a30bc67e4fad5fc133968f749ac55beda2eb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### TOBE

이런 구조를 바꾼게 바로 2017년 NIPS에서 'Attention Is All You Need’ 라는 논문이다. 

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/6e9cd139-802d-46d7-a36a-93043fd1cafc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RWDQ326Y%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T070454Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCIE4pYH%2BZLSdCSMjxr9JnBhettTNmuoebymI1aMwuPX%2BcAiEAlHuOJhJRY20i5y%2BpDTsR%2FFxCIHRfLNhNEj8S30N4dT0q%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDNgm3XLMhs4LXCbEvyrcA%2BXKM9V%2BKJfeW3nYLN1yapS%2BtgHCQbT2ZC0Vo5WW8eXSVJHyFTCf7M7GMT1JKpRK9VdevGI7OPynvRKaa8qzaYSy67T8AoXOBQP3nYtnbAz3QdtELbyWd6kQAyAoPTAwOqxK4sNYa4NkrS6fbbCLSWCSKvEUUeUfdoOhxdJKkCHcT0BD3aOmGORTHcVn6npoG%2BjOGqmCbC3Q52bv%2F78D5mCiRHmz5p4Y0HdHPEMPpMyUC5m1SkZdA8t1aRO7wGZZcNJiS0Ls2EKKA0TpJ%2F2wFRDJ2mnLoKjBhCnfRmR2tmSS564sUrjb%2FMwWj1KcugUjHvTbCUx4Y0ZU4dHujiTZ6uxoeFx6MxzHYUHtJa18r1aAPCy6AFex%2FrPfI9J48uF4Fl%2FLrh8owq%2BWKu0PweqFFsqHwdaUtrXCbUV%2FyxpzP4hBHKj%2F4hE70ZBgl2s8OVaNLuqczdspUODT7%2FfapLjwLqk%2BFe7eUkGw91nW8sIcU3IfKERydZAHNnsSa2T8HhNVPwqhWDB8KhQA8S4%2FGxl0M5njHjInuzwspi7lGgQc7NEktyILzMMo3vWLHrC4tHEnIRz98i9K%2Bocc%2FjhZxuD5bEOmN%2BNkJ07qmSuG2%2BZoxzwpzPbk77YkghpV8IUUMM%2BNwcQGOqUBp0kt2yJADj7XfguOB4%2FXfimS084wVG%2FX9rL%2FF2lGMt%2ByPeerFPP3je8JDUHlJ6xHkM1Mv%2BN8qvhUbZZ7Y2wq3QbMX5%2BbikwWmDqej4cU%2Fz4Hy9QMVytzd4a1qi3nqWJ%2FY4VTs8dXuJTV5wGy1KbqaS1FWX%2BDwr6gZYdL%2FlPqCTmdk%2BCr9AXuWRT%2F6Kkbx%2BpZV1b%2FXazcvjItnww6ywN3oxqx4Oxo&X-Amz-Signature=72424eddc9de2b1d58b17bf147bbfdfdbbddce96263d917187921a0f76350fc1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 참조

https://namu.wiki/w/트랜스포머(인공신경망)

https://chonchony.tistory.com/entry/순환신경망-RNN의-문제점-기울기-소실-기울기-폭주-Gradient-Vanishing-Exploding

https://calmmimiforest.tistory.com/110


