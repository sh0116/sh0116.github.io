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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/96e960a1-9b1c-4157-ade1-53664e2fca73/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T7OEEQVR%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T063226Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCIQDDRoGAZuYMhyLKsC2pmN5n8%2FcJ8znFv1fUpunjDEEarAIgKMjXB6%2BH2FxBdSeEjT3aeFmUkH01UKjZZh%2BGV5aVYTcq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDDL744LPvLF3BXXwCCrcAy7zj8PeuHATQSFXYo7J6ieOrKSq5YX30igBmHaLlhQVeWMkeqFFFn1wdvEI%2F7uy7BZOe78DhDqXLaRVmzEjYXaMGPDsskFJlGMUR141Bw%2FhYIoQd9nfKBwN%2BjAV4cd0Tm11MpmfTybOXJaGwRbT66FqXerENJnDmvafoQ4SXKbWb07aGIqUddnIKRjBLrw1bEvY1GOEfXxaqWgyL%2F%2B7WXErllTcnZKBSW11O8O597ov4z3W7kuNjNu9uPgy3I5Oy2jtkb3ewQgvLecSoMBezNFqpJqcZXn2268cRTt7ipf8bN%2BityvdM0f7biW%2F7ImRh3fhOik%2BK0qlQ%2FZeXnrZXGnZW5YvzVhxSzlb1Lw44DbKu%2FbkAzFh%2Fs79gbBiTXapoEoUHBY1KAp%2BF0X2LX4eDXpgDQpo7D5C6qB7cHMBvd1MsHbExDp3GgiHyEQU%2F25xRBSRfI2V%2FJh3GXIwoLfZiH8vfq9LzjHVeR5hU4NavDUpt4mU5o7JHabR4aILE3bjM8LkVksUpr8pdFQ1E5a0fr4YQVkOALFKpoVprpa0FHTBnXOGyc2HKvF7bKJcKdmDtFqWnktBmdSESTW36qDauW22XW457opHuK%2Fe%2FgoYeKoSBi%2Bqm0SFi%2FPkxHRTMK%2BNwcQGOqUBzViVxMC0Vff8spQBnT8sF5PRfg8dLHfEBOyNhY0SLMhHqwZl0vPA2JL7w4LAGUEwFBaJJJC7GML6AzxD7JgVGVgGoXBlWuk6mo%2FKA6%2F60nVGwf%2BT7FVzUqUDVgvc54XvPDAq9nOFc1lccW5vR%2FxNP1adINxXus5yb2n%2FY73J%2B2EXg27sau4qRMSG71TYT4K3t%2FE70VW%2Ff2aHGAXw7hvRJ29O%2FyFX&X-Amz-Signature=087207ea612bb8926e709402164accde24308c1a25e93a0df3e323ef8c6ab910&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/96e960a1-9b1c-4157-ade1-53664e2fca73/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T7OEEQVR%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T063226Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCIQDDRoGAZuYMhyLKsC2pmN5n8%2FcJ8znFv1fUpunjDEEarAIgKMjXB6%2BH2FxBdSeEjT3aeFmUkH01UKjZZh%2BGV5aVYTcq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDDL744LPvLF3BXXwCCrcAy7zj8PeuHATQSFXYo7J6ieOrKSq5YX30igBmHaLlhQVeWMkeqFFFn1wdvEI%2F7uy7BZOe78DhDqXLaRVmzEjYXaMGPDsskFJlGMUR141Bw%2FhYIoQd9nfKBwN%2BjAV4cd0Tm11MpmfTybOXJaGwRbT66FqXerENJnDmvafoQ4SXKbWb07aGIqUddnIKRjBLrw1bEvY1GOEfXxaqWgyL%2F%2B7WXErllTcnZKBSW11O8O597ov4z3W7kuNjNu9uPgy3I5Oy2jtkb3ewQgvLecSoMBezNFqpJqcZXn2268cRTt7ipf8bN%2BityvdM0f7biW%2F7ImRh3fhOik%2BK0qlQ%2FZeXnrZXGnZW5YvzVhxSzlb1Lw44DbKu%2FbkAzFh%2Fs79gbBiTXapoEoUHBY1KAp%2BF0X2LX4eDXpgDQpo7D5C6qB7cHMBvd1MsHbExDp3GgiHyEQU%2F25xRBSRfI2V%2FJh3GXIwoLfZiH8vfq9LzjHVeR5hU4NavDUpt4mU5o7JHabR4aILE3bjM8LkVksUpr8pdFQ1E5a0fr4YQVkOALFKpoVprpa0FHTBnXOGyc2HKvF7bKJcKdmDtFqWnktBmdSESTW36qDauW22XW457opHuK%2Fe%2FgoYeKoSBi%2Bqm0SFi%2FPkxHRTMK%2BNwcQGOqUBzViVxMC0Vff8spQBnT8sF5PRfg8dLHfEBOyNhY0SLMhHqwZl0vPA2JL7w4LAGUEwFBaJJJC7GML6AzxD7JgVGVgGoXBlWuk6mo%2FKA6%2F60nVGwf%2BT7FVzUqUDVgvc54XvPDAq9nOFc1lccW5vR%2FxNP1adINxXus5yb2n%2FY73J%2B2EXg27sau4qRMSG71TYT4K3t%2FE70VW%2Ff2aHGAXw7hvRJ29O%2FyFX&X-Amz-Signature=087207ea612bb8926e709402164accde24308c1a25e93a0df3e323ef8c6ab910&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


