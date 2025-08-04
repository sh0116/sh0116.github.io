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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/96e960a1-9b1c-4157-ade1-53664e2fca73/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QUVESQDB%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T070459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCIDhyxdsRZ797wvV5cn6B6tCKibw7r3ctWo%2F94gMfpRwWAiEAz2GYO2VDMkcECcP6ZY8D90go2yVQZ%2FGgYdBLlLQtH8Mq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDBGdCiIJvvftDFcj%2BSrcA6JNaxHVl1rzz9pCZzZ3ENkYL9G7aT1WGKzGrSdPAw4I2KbhE%2B9CUnN0gtLgI%2FAM0Y7c%2FlmXAIFXR2ZLQaKUBjuF7j2tiol1xgxIiqrexGBGVubbMQ2H6jGyl69vrcI%2Ba895l9KER8WvxsO9QfVt8tSwGWaCO4h61QOpCQTz60VFYjv8hRremV9cKNX950hKaHRxS%2FPVUZ0WSngnnBKYac7HCWdl9zDWQLy6%2BovoSY%2Bi%2Bky12bkeITR0AhjRGb04GUwEcyYviQAPqvY8HQ4q7cCn%2F%2FnydCzdtJBxmJMY%2FaNVOWIpPKcP2rixA7jq16Shj937QIlRk6UHBoFhBCQNdMR8z4oFOfuj1UVpRAH6i5I4%2F0LH65dPSBE85JR%2FcVwDqzmpPHY93s66S%2BuakpStEXL0R4PywwusQyIvwof%2Bo0WmZmS4LZ9b27lXye9hZnisbZ5d38DNjViMnUMDhhIZvsmJ0Fh3uepSsqNHLCld81loccEpydVu4DV7vVszTXqnsZfOwbi2GLzx9J9koNpvuShx0oatLZUruaig%2Bdr%2FH%2BWkhn9ZuG8FWplcBCjVu%2FCbTQOopc5OFOvktkJwrTDe55YTj3%2BA%2BwhPrc45snoMjne3bL4k9kOwWWzqKzByMNONwcQGOqUB1h8h%2BG8DXhqKu8pnXwJgWJd23Fp5xI%2BgfUPgDDVvZMmc0XJAboOwAZpTxSzXjA9nc5mfzqRysiDN51dwaKtDsDJF3DEuMPz9SKFihJnyEw%2Fe3JiLuXwrdc0sFXlkuIL865A6B4iVK8pJmiW0rBdU9HqkFI2lWfVMOFy9LZAddvsJlnYpZBHYKPrW0EutdoT8v4KATivP9Bk1cKV%2BrGhoCJmfwJyo&X-Amz-Signature=86a51c8e19b112ec87b3e2926eebebc6457051cbcb9e0c6c70e78a8a3a3c1151&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/96e960a1-9b1c-4157-ade1-53664e2fca73/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QUVESQDB%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T070459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCIDhyxdsRZ797wvV5cn6B6tCKibw7r3ctWo%2F94gMfpRwWAiEAz2GYO2VDMkcECcP6ZY8D90go2yVQZ%2FGgYdBLlLQtH8Mq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDBGdCiIJvvftDFcj%2BSrcA6JNaxHVl1rzz9pCZzZ3ENkYL9G7aT1WGKzGrSdPAw4I2KbhE%2B9CUnN0gtLgI%2FAM0Y7c%2FlmXAIFXR2ZLQaKUBjuF7j2tiol1xgxIiqrexGBGVubbMQ2H6jGyl69vrcI%2Ba895l9KER8WvxsO9QfVt8tSwGWaCO4h61QOpCQTz60VFYjv8hRremV9cKNX950hKaHRxS%2FPVUZ0WSngnnBKYac7HCWdl9zDWQLy6%2BovoSY%2Bi%2Bky12bkeITR0AhjRGb04GUwEcyYviQAPqvY8HQ4q7cCn%2F%2FnydCzdtJBxmJMY%2FaNVOWIpPKcP2rixA7jq16Shj937QIlRk6UHBoFhBCQNdMR8z4oFOfuj1UVpRAH6i5I4%2F0LH65dPSBE85JR%2FcVwDqzmpPHY93s66S%2BuakpStEXL0R4PywwusQyIvwof%2Bo0WmZmS4LZ9b27lXye9hZnisbZ5d38DNjViMnUMDhhIZvsmJ0Fh3uepSsqNHLCld81loccEpydVu4DV7vVszTXqnsZfOwbi2GLzx9J9koNpvuShx0oatLZUruaig%2Bdr%2FH%2BWkhn9ZuG8FWplcBCjVu%2FCbTQOopc5OFOvktkJwrTDe55YTj3%2BA%2BwhPrc45snoMjne3bL4k9kOwWWzqKzByMNONwcQGOqUB1h8h%2BG8DXhqKu8pnXwJgWJd23Fp5xI%2BgfUPgDDVvZMmc0XJAboOwAZpTxSzXjA9nc5mfzqRysiDN51dwaKtDsDJF3DEuMPz9SKFihJnyEw%2Fe3JiLuXwrdc0sFXlkuIL865A6B4iVK8pJmiW0rBdU9HqkFI2lWfVMOFy9LZAddvsJlnYpZBHYKPrW0EutdoT8v4KATivP9Bk1cKV%2BrGhoCJmfwJyo&X-Amz-Signature=86a51c8e19b112ec87b3e2926eebebc6457051cbcb9e0c6c70e78a8a3a3c1151&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


