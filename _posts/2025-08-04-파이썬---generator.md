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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/96e960a1-9b1c-4157-ade1-53664e2fca73/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXZE363M%2F20250805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250805T002640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJHMEUCIQDNA2ZNLaMqm9TPmPkFU4Wt6hyGxrF%2F1MYfAyk6preB5QIgMNu7z1M7Z3eXadM8NN3Hgh%2BMNwnDNjOnFgzrFdVG8IQq%2FwMIUBAAGgw2Mzc0MjMxODM4MDUiDCcHEw%2Fv6YNsVXeRoircAzh7B0DeJocYqpfgHdfUk5HstVDbAFql5tU%2BSjjWLSfg%2BPHoALr%2FkQOL37OcBP9YHcB5opEVYdqXMkbq7BlC2zd1ccRunkAAmb2fBdnS%2BnRJGXH%2Bv17jyP7DkePjepPgbLi%2B5xH99RR78Y%2BO0ouUSxRvy%2BvGOcOsq1IfKBJFg1zBRyFU4%2FxJaycwgqsShGDmn4Kl0IranvODpWuz9K5S%2BH9WL7va6TEAtS7ceh%2FOUf0c3puxeaOU0%2BWvngcez%2BBg%2FOQxblxt72c4bLxrF370kBpDYexvugDUttG0vw8ultsMxHMXeSG1AVmjrnbpF7NjOrc%2BkqAzQRJqTjgO0fxz5uTpfLx%2FkfFfGB286qV1Vkx%2FP%2F4Isx7j%2BtneDgJbPNTxmKD%2BxudSMvmTxgiZp7UBCITd6iQ7o59%2FQkJnzj6oMQ5sl5V1hyPef2YyI0d7sNdfmEk%2B9bkDZlsKd2iNAagyq6iEIdaL%2FlwPOH4o4Wdy22ET%2BnHuNYUO87piXsz6xlO3XdG7IckKCgQu%2BYt9J22RpUVZOciF8Zw5kx7NsOn9uxQRbBDI0my6Qy1In8fAbSMRGw4tkFFIN9nBa55seCXVfbo8RdP8KEQDOvRhc%2FEEVczQb%2BU2gEajrg%2FooLkaMPXzxMQGOqUBCnib%2BoWAkbyVmt8PECEPGd0vsY%2BnYyziFjRkGkJnm3SvOOE%2FavQBK6kz7RdDKkrUvyz69xB5wpRzNIBfnOa9zDkPy9XuT%2BYey49AqbFx56zMqj7b3iePdfdeik8x4DBFUYm6VeFbYz3qzcQ%2BwPT%2FfXJyFYNFiesYFR%2BC3hC%2BEwQXu%2Fm2S%2ByRY%2FNqE68xY38ZsC5oqpuv8eSptd6MXWN8uaIDbP88&X-Amz-Signature=b31f8e88b29aff0e68b70c90b75b96685e79970151ba53968cecb87db2fdd5e1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/96e960a1-9b1c-4157-ade1-53664e2fca73/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXZE363M%2F20250805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250805T002640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJHMEUCIQDNA2ZNLaMqm9TPmPkFU4Wt6hyGxrF%2F1MYfAyk6preB5QIgMNu7z1M7Z3eXadM8NN3Hgh%2BMNwnDNjOnFgzrFdVG8IQq%2FwMIUBAAGgw2Mzc0MjMxODM4MDUiDCcHEw%2Fv6YNsVXeRoircAzh7B0DeJocYqpfgHdfUk5HstVDbAFql5tU%2BSjjWLSfg%2BPHoALr%2FkQOL37OcBP9YHcB5opEVYdqXMkbq7BlC2zd1ccRunkAAmb2fBdnS%2BnRJGXH%2Bv17jyP7DkePjepPgbLi%2B5xH99RR78Y%2BO0ouUSxRvy%2BvGOcOsq1IfKBJFg1zBRyFU4%2FxJaycwgqsShGDmn4Kl0IranvODpWuz9K5S%2BH9WL7va6TEAtS7ceh%2FOUf0c3puxeaOU0%2BWvngcez%2BBg%2FOQxblxt72c4bLxrF370kBpDYexvugDUttG0vw8ultsMxHMXeSG1AVmjrnbpF7NjOrc%2BkqAzQRJqTjgO0fxz5uTpfLx%2FkfFfGB286qV1Vkx%2FP%2F4Isx7j%2BtneDgJbPNTxmKD%2BxudSMvmTxgiZp7UBCITd6iQ7o59%2FQkJnzj6oMQ5sl5V1hyPef2YyI0d7sNdfmEk%2B9bkDZlsKd2iNAagyq6iEIdaL%2FlwPOH4o4Wdy22ET%2BnHuNYUO87piXsz6xlO3XdG7IckKCgQu%2BYt9J22RpUVZOciF8Zw5kx7NsOn9uxQRbBDI0my6Qy1In8fAbSMRGw4tkFFIN9nBa55seCXVfbo8RdP8KEQDOvRhc%2FEEVczQb%2BU2gEajrg%2FooLkaMPXzxMQGOqUBCnib%2BoWAkbyVmt8PECEPGd0vsY%2BnYyziFjRkGkJnm3SvOOE%2FavQBK6kz7RdDKkrUvyz69xB5wpRzNIBfnOa9zDkPy9XuT%2BYey49AqbFx56zMqj7b3iePdfdeik8x4DBFUYm6VeFbYz3qzcQ%2BwPT%2FfXJyFYNFiesYFR%2BC3hC%2BEwQXu%2Fm2S%2ByRY%2FNqE68xY38ZsC5oqpuv8eSptd6MXWN8uaIDbP88&X-Amz-Signature=b31f8e88b29aff0e68b70c90b75b96685e79970151ba53968cecb87db2fdd5e1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


