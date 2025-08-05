---
title: "Transformer 모델 - Self-Attention"
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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/1e7f5e6f-9228-4d68-9d1d-6554327138c3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666Q6VRXBV%2F20250805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250805T060947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJHMEUCIAVag6qKvRAExH9IqJiK6SKOatF3%2FWq36B1ydfP6rk7EAiEAgsm1jsws%2BXt%2BBB6w6nenBCzqgsWetxNhniAEziScdb4q%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDC8hJU6DryKRhvIFWSrcA15ngfLGAuPrQLTJSUhtCTNZn6teH%2BAUsUJkN4Rw1sOpgu1%2FV6JWTE8xHgttaccv%2B09ca6t%2Bu%2FHrb8CKaqOI8%2FqH%2B%2FaW1P8N6FgYP%2B06AIHVOP%2FCfg36%2B9YTgUXRut88BDxxYsBLMTbIYq1N53c6Vvxg4%2B9O0Vnc1hsPW3uTRauot%2ByJDvj94RxQcJ4GZCYwZ%2FGuKV3IUAYeajoc9vrYgMF3Du3hUqNS23hbqbHcYBmWkUm5L5Rw1hTdYadxUfsWhR9fJHMcIWEtkJfVdv42%2F6Nd3A54z4taoynGTffqM5RBzfhxHx679%2BYLj0u4yNLPZBD3AGPfH1BZRrffaKy78xIzuUVoqgHjDY6f3lz7pXdiS7UvzFW21BmVWNmUXSMvfYTMz%2FxLJx6MLyiIdtcKDrwjbQ%2FAXAtpEYjbg8Q2QgB9BHhoVOFEPJ0Ky3vIvgsKAGrb4X%2F0Kd9HncxXjFy8YJXwExG3RczqvIKXTMmbrtT5LSlsWbfJ7X%2FgGkHTqIs9WNWWERqLYW1vaKhmF2BLWruII%2FWFyJsnrWUEuPQDQ4d81EA64HtIQFJtAPRJ%2BORx7rQCREkvbiCLhF%2BzAaWjgzT1QYU%2FpY26vAghwhS7VeRimc1cjyMBDTmKePJUMKqzxsQGOqUBckYKkzXocmDjoJjBtTwdrtJVSecOks7AWC5nB%2FxRyZO3bxck%2FNNdZvkCDa5LAhSQO4oImCScLfdNa6HTOoRhp3Qz7%2FURsoWobPN%2B3Gu%2BL1%2F0olFIGd%2BouRMtJpZW%2FsZOxxmARP00C1xJhVDpOoVg9lDqSToirCZFlaYs0ilrZD6dFUFgAPzcHkEeO4A9x2bf2wpHyf5N%2FKvfvTH6BmBiMdcjiSam&X-Amz-Signature=7dcc46fabd0dd04cc1f4fa1f3ae540c751073a7e89585f1d2ef15dce6d48513c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### TOBE

이런 구조를 바꾼게 바로 2017년 NIPS에서 'Attention Is All You Need’ 라는 논문이다. 

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/6e9cd139-802d-46d7-a36a-93043fd1cafc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666Q6VRXBV%2F20250805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250805T060947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJHMEUCIAVag6qKvRAExH9IqJiK6SKOatF3%2FWq36B1ydfP6rk7EAiEAgsm1jsws%2BXt%2BBB6w6nenBCzqgsWetxNhniAEziScdb4q%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDC8hJU6DryKRhvIFWSrcA15ngfLGAuPrQLTJSUhtCTNZn6teH%2BAUsUJkN4Rw1sOpgu1%2FV6JWTE8xHgttaccv%2B09ca6t%2Bu%2FHrb8CKaqOI8%2FqH%2B%2FaW1P8N6FgYP%2B06AIHVOP%2FCfg36%2B9YTgUXRut88BDxxYsBLMTbIYq1N53c6Vvxg4%2B9O0Vnc1hsPW3uTRauot%2ByJDvj94RxQcJ4GZCYwZ%2FGuKV3IUAYeajoc9vrYgMF3Du3hUqNS23hbqbHcYBmWkUm5L5Rw1hTdYadxUfsWhR9fJHMcIWEtkJfVdv42%2F6Nd3A54z4taoynGTffqM5RBzfhxHx679%2BYLj0u4yNLPZBD3AGPfH1BZRrffaKy78xIzuUVoqgHjDY6f3lz7pXdiS7UvzFW21BmVWNmUXSMvfYTMz%2FxLJx6MLyiIdtcKDrwjbQ%2FAXAtpEYjbg8Q2QgB9BHhoVOFEPJ0Ky3vIvgsKAGrb4X%2F0Kd9HncxXjFy8YJXwExG3RczqvIKXTMmbrtT5LSlsWbfJ7X%2FgGkHTqIs9WNWWERqLYW1vaKhmF2BLWruII%2FWFyJsnrWUEuPQDQ4d81EA64HtIQFJtAPRJ%2BORx7rQCREkvbiCLhF%2BzAaWjgzT1QYU%2FpY26vAghwhS7VeRimc1cjyMBDTmKePJUMKqzxsQGOqUBckYKkzXocmDjoJjBtTwdrtJVSecOks7AWC5nB%2FxRyZO3bxck%2FNNdZvkCDa5LAhSQO4oImCScLfdNa6HTOoRhp3Qz7%2FURsoWobPN%2B3Gu%2BL1%2F0olFIGd%2BouRMtJpZW%2FsZOxxmARP00C1xJhVDpOoVg9lDqSToirCZFlaYs0ilrZD6dFUFgAPzcHkEeO4A9x2bf2wpHyf5N%2FKvfvTH6BmBiMdcjiSam&X-Amz-Signature=247836156ad64ca8481bb573b989384c342654b91cf2c3014bb7cb50d7afaf0d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 참조

https://namu.wiki/w/트랜스포머(인공신경망)

https://chonchony.tistory.com/entry/순환신경망-RNN의-문제점-기울기-소실-기울기-폭주-Gradient-Vanishing-Exploding

https://calmmimiforest.tistory.com/110


