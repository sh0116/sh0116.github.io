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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/1e7f5e6f-9228-4d68-9d1d-6554327138c3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SAQQT54J%2F20250805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250805T002632Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJIMEYCIQCQ%2F%2FfO3GgnNebYO5UAbiPg4k6YGD21cgiERs%2Bo5F9LGAIhAMiVO8osQxdWoIRDGN0DbIh5FjgVkMacsc9f7LZFip6uKv8DCFAQABoMNjM3NDIzMTgzODA1IgxB5B14hRFbq9nc4sAq3AN8ZCi%2FFvYLJ4dbFj73IXOlb1ins68A7XXF1h3DV8%2FEbMEJBF4nRBXDM1833PQwZCdMrEeSojv8%2BSY35gkprLWHti%2FIMp8MDBqHxMZMsFVZ%2F7oQP7PmrPkEV%2B%2Bbn9sNTncyAl6dsHUJZtKMk4wwRirNej8uf%2BuXlnBBwA5b9f6NQRBAJvEjuF1vZTd2chujSiKvDCASIHm57GnolaASwV81%2BGGyAxzbqC1znQ2XcGeHEgketRsyD801P%2B%2FJJhPu6dVoRSv%2FgmmyabzfUWH8HmjOv2RlD6HyHkxrHxC3qaxq6Jn8yE41PHJAPPD0EZdDruE2ko6ik3AgL4CZF%2BZUB065iKC%2BziO3gmiOYWRFMir1AAbkZIVHXR8aS%2FgQxS%2BzT4LefMFVGONvCVukXJ%2BdHq%2F6QUcA%2FBq91becJgdNYm2WEj6sDi85ygg7KbdrXF%2Bn0PMt8aDIwwyjGfYNR2LTms78nOMkC2My69SKkPo7IztCirACzOyz54P%2F6FJa9FCOM9yULbByfpSnbD9mMqT4dwCxPIJxhTmhAtdtdHncjd%2FEhL8ivuoGk2sqBX9G8Hksa6fHy1Jy%2FIOiH7kT4fcVDZdmmgksWVhjR5hYoHreSP6Pozxb04ewAtYbCKb1eTCM9MTEBjqkAemf%2BQivJ0H%2F33mX%2FqVuTzvMAMu5BELTa7QGAzyRVEUzx%2ByPDS%2FVAPmt1lrKUjSvuG93r4buvK9yOVCLgrWw9JgYn3K0JS8%2FR5imAWvPWyKO3hfcPm85dGGPhSRaBAy8lHfFK5F3ph%2Bnj4Q7Bha08lqaYZwNB0TxcqsThJo34vOGUyNrFgJKZUVB0bYh%2BNtAOLeo6xztVtgxkrlB4uVw1m0khvYo&X-Amz-Signature=3e6db893ae1b1aae392f41022c535344ddc523582bb9eb97655a8dd6eb06bfe3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### TOBE

이런 구조를 바꾼게 바로 2017년 NIPS에서 'Attention Is All You Need’ 라는 논문이다. 

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/6e9cd139-802d-46d7-a36a-93043fd1cafc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SAQQT54J%2F20250805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250805T002632Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJIMEYCIQCQ%2F%2FfO3GgnNebYO5UAbiPg4k6YGD21cgiERs%2Bo5F9LGAIhAMiVO8osQxdWoIRDGN0DbIh5FjgVkMacsc9f7LZFip6uKv8DCFAQABoMNjM3NDIzMTgzODA1IgxB5B14hRFbq9nc4sAq3AN8ZCi%2FFvYLJ4dbFj73IXOlb1ins68A7XXF1h3DV8%2FEbMEJBF4nRBXDM1833PQwZCdMrEeSojv8%2BSY35gkprLWHti%2FIMp8MDBqHxMZMsFVZ%2F7oQP7PmrPkEV%2B%2Bbn9sNTncyAl6dsHUJZtKMk4wwRirNej8uf%2BuXlnBBwA5b9f6NQRBAJvEjuF1vZTd2chujSiKvDCASIHm57GnolaASwV81%2BGGyAxzbqC1znQ2XcGeHEgketRsyD801P%2B%2FJJhPu6dVoRSv%2FgmmyabzfUWH8HmjOv2RlD6HyHkxrHxC3qaxq6Jn8yE41PHJAPPD0EZdDruE2ko6ik3AgL4CZF%2BZUB065iKC%2BziO3gmiOYWRFMir1AAbkZIVHXR8aS%2FgQxS%2BzT4LefMFVGONvCVukXJ%2BdHq%2F6QUcA%2FBq91becJgdNYm2WEj6sDi85ygg7KbdrXF%2Bn0PMt8aDIwwyjGfYNR2LTms78nOMkC2My69SKkPo7IztCirACzOyz54P%2F6FJa9FCOM9yULbByfpSnbD9mMqT4dwCxPIJxhTmhAtdtdHncjd%2FEhL8ivuoGk2sqBX9G8Hksa6fHy1Jy%2FIOiH7kT4fcVDZdmmgksWVhjR5hYoHreSP6Pozxb04ewAtYbCKb1eTCM9MTEBjqkAemf%2BQivJ0H%2F33mX%2FqVuTzvMAMu5BELTa7QGAzyRVEUzx%2ByPDS%2FVAPmt1lrKUjSvuG93r4buvK9yOVCLgrWw9JgYn3K0JS8%2FR5imAWvPWyKO3hfcPm85dGGPhSRaBAy8lHfFK5F3ph%2Bnj4Q7Bha08lqaYZwNB0TxcqsThJo34vOGUyNrFgJKZUVB0bYh%2BNtAOLeo6xztVtgxkrlB4uVw1m0khvYo&X-Amz-Signature=b61dafe3676496946ca71273e2f0a3e89caa05299845f87874523ae4ed791bf5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 참조

https://namu.wiki/w/트랜스포머(인공신경망)

https://chonchony.tistory.com/entry/순환신경망-RNN의-문제점-기울기-소실-기울기-폭주-Gradient-Vanishing-Exploding

https://calmmimiforest.tistory.com/110


