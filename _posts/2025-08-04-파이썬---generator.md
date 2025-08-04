---
title: "파이썬 - Generator"
date: 2025-08-04 06:05:00 +0900
categories: [Python]
tags: [python]
description: Python Language
toc: true
comments: true
---

# 제너레이터 - Generator 란?

영단어 generate는 사전적으로 "생성하다, 생산하다"라는 의미이다.

**제네레이터는 한 번에 하나씩 구성요소를 반환해주는 이터러블을 생성해주는 객체**이다.

### 목적 

가장 큰 목적은 메모리를 절약하는 것이다.

거대한 요소를 한꺼번에 메모리에 저장하는 대신 특정 요소를 어떻게 만드는지 아는 객체를 만들어서 필요할 때마다 하나씩만 가져오도록 한다.

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/96e960a1-9b1c-4157-ade1-53664e2fca73/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XYC2Y4HF%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T064841Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCIAa7mK6gGMO%2B%2Fr41L1zzzoS0lOAHHr7zjpjYgAgjrTp9AiEAgHwbgmVF8rHv8pdAzlaMKRB9u8tzOvSym3w7Z5pLgG0q%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDMXgt1xTsng7gmMlNircA48b0MXGcibVohoJO2qElEtI5prLqH5ugQq0gya%2BLSt37%2Bi%2BxKT0%2Bj%2BXCWlgyXcT%2FfjDqzJEeoQnGOJwrbGmnahFGHcsIFgyFevt5xyd8Si%2BK4EzvPIXfaoD4YNAYFN%2FcUFog9XI%2B8XNDPwj%2FGonHbr9kx3M66lqPyu3j%2F%2FPfPCU3iPSWSE%2FBRRXLjAi%2F088JlehBhTkEY1KQnlVnsywotWSHiEOVHCQqi5jMoS3v%2FumNKrRxMvKC%2Bb596cAD1Hs0%2FioG%2BF2ebNuwVybeBGwcqKOnvQL35BVU5m7K1sealx414A8B7sU3%2FRMILrWIZjScHhj2AzbvnA%2By0LjnIoTRnjmg0JNuL4BxPUlsEoucfwXCxK6Pb7WgSG%2BlHdbXxmJy6mp6AkSX7InTQQNUChYE8wavCNwqptwomF6a3mL%2FZVK3sNAkj8QrPDkkCats4gc4UCBnvqa2dlv8SZIGYNhj8GUZGrTB4cHxfqVOqZ7nSg70NxTEI5PDTLmJE9P4g%2FgSCUXpSr2rV3Auuj7qTQ%2BOVUhxDIADtpMIVdrXA3FTgcTcpwkaOnOgcSKnmBB86%2FocOWrdXaiS6YCzVYT7BDw6TEgahgi47M0x0grLQXjiQ1n4HE0Jw1knffz6avyMIaNwcQGOqUBUfnbWgptBg6O8BagPPjKYhaMlLIsfdTFjwac%2BeMRpj%2F6CDGfJuy833S7xa51o%2Bk9%2Fjsp%2BZ2pTRmBMCeXXbJgTp4l0UTBOZ9dueAKx1Dp1BdBzrNuN5npSfelx%2FzbSGNCWoqCjalkExpcknnt6cmmaGRCOCZRDEHoeWdvOjAd6hCZVaTuuKdNv1xydKW9Ex95pVMmx4MfgQFBxMlJWAPesHI7rrg9&X-Amz-Signature=1f98c199482d392ed0a842e18bf3c5a3af6d297e38e2546b23f7f4c3e63f8768&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 개념

```python
일반적인 LIST생성 방법
------------------------------

def func_list():
	return ["A","B","C"]

for i in func_list():
	print(i)

------------------------------

Generator를 통한 생성 방
------------------------------

def func_generator():
	yield "A"
  yield "B"
  yield "C"

for i in func_generator():
	print(i)
------------------------------

```

위 두 방식은 똑같은 출력을 한다. 

하지만 메모리의 사용은 전혀 다르다.

### LIST 방식

- 가장 익숙하고 많이 사용하는 방식이다.
- 함수를 실행하면 ["A","B","C"] 생성하고 return한다.
- 메모리 크기는 당연히 ["A","B","C"] 부분의 크기만큼 소모가 될 것 이다.
### Generator 방식

- yield라는 생소한 방식이 사용된다.
- 게으른 반복자라는 별명이 있는 이 방식은 한번에 리스트가 생성되는 방식이 아닌 반복자가 넘어갈 때 마다 생성되는 방식이다. 
- List보다 적은 메모리로 같은 출력을 할 수 있다.
![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/96e960a1-9b1c-4157-ade1-53664e2fca73/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XYC2Y4HF%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T064841Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCIAa7mK6gGMO%2B%2Fr41L1zzzoS0lOAHHr7zjpjYgAgjrTp9AiEAgHwbgmVF8rHv8pdAzlaMKRB9u8tzOvSym3w7Z5pLgG0q%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDMXgt1xTsng7gmMlNircA48b0MXGcibVohoJO2qElEtI5prLqH5ugQq0gya%2BLSt37%2Bi%2BxKT0%2Bj%2BXCWlgyXcT%2FfjDqzJEeoQnGOJwrbGmnahFGHcsIFgyFevt5xyd8Si%2BK4EzvPIXfaoD4YNAYFN%2FcUFog9XI%2B8XNDPwj%2FGonHbr9kx3M66lqPyu3j%2F%2FPfPCU3iPSWSE%2FBRRXLjAi%2F088JlehBhTkEY1KQnlVnsywotWSHiEOVHCQqi5jMoS3v%2FumNKrRxMvKC%2Bb596cAD1Hs0%2FioG%2BF2ebNuwVybeBGwcqKOnvQL35BVU5m7K1sealx414A8B7sU3%2FRMILrWIZjScHhj2AzbvnA%2By0LjnIoTRnjmg0JNuL4BxPUlsEoucfwXCxK6Pb7WgSG%2BlHdbXxmJy6mp6AkSX7InTQQNUChYE8wavCNwqptwomF6a3mL%2FZVK3sNAkj8QrPDkkCats4gc4UCBnvqa2dlv8SZIGYNhj8GUZGrTB4cHxfqVOqZ7nSg70NxTEI5PDTLmJE9P4g%2FgSCUXpSr2rV3Auuj7qTQ%2BOVUhxDIADtpMIVdrXA3FTgcTcpwkaOnOgcSKnmBB86%2FocOWrdXaiS6YCzVYT7BDw6TEgahgi47M0x0grLQXjiQ1n4HE0Jw1knffz6avyMIaNwcQGOqUBUfnbWgptBg6O8BagPPjKYhaMlLIsfdTFjwac%2BeMRpj%2F6CDGfJuy833S7xa51o%2Bk9%2Fjsp%2BZ2pTRmBMCeXXbJgTp4l0UTBOZ9dueAKx1Dp1BdBzrNuN5npSfelx%2FzbSGNCWoqCjalkExpcknnt6cmmaGRCOCZRDEHoeWdvOjAd6hCZVaTuuKdNv1xydKW9Ex95pVMmx4MfgQFBxMlJWAPesHI7rrg9&X-Amz-Signature=1f98c199482d392ed0a842e18bf3c5a3af6d297e38e2546b23f7f4c3e63f8768&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 사용 예제

```python
# 무한
def func_while():
  while True:
    yield "A"
    yield "B"
    yield "C"

# 리스트 형식으로 전달 
def func_from():
  yield from ["A", "B", "C"]

# yield 이외 다른 방식
gener = (i for i in "ABC")
for i in gener:
  print(i)
```


