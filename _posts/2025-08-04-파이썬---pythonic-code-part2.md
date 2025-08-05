---
title: "파이썬 - Pythonic Code Part2"
date: 2025-08-04 06:05:00 +0900
categories: [Python]
tags: [python]
description: Python Language
toc: true
comments: true
---

# 파이썬스러운 코드 - Pythonic Code

### 파이썬스럽다란?

- 파이썬이 가지고 있는 고유한 메커니즘을 따른 코드를 파이썬스럽다고 표현한다.
### Pythonic의 장점

- 성능이 좋다.
- 코드가 간결하며 이해하기 쉽다.
- 실수를 줄일 수 있다.
## INDEX

# LIST, STRING - split & join

- split : String을 기준값에 따라 나누는 함수
- join : List를 하나로 연결하는 함수
```python
>>> greeting = "Hello my name is Lee"
>>> sp_greeting = greeting.split()
['Hello', 'my', 'name', 'is', 'Lee']

>>> fruits = ['apple', 'banana', 'tomato']
>>> all_fruits = " & ".join(fruits)
apple & banana & tomato
```

# **list comprehension **

for-append보다 빠르게 List를 생성하는 방법

```python
# 기본 방법
>>> List_name = [i for i in range(10]
>>> List_name = [i for i in range(10) if i%2 != 0]

# Nested for loop
>>> word1 = "Hello"
>>> word2 = "World"
>>> result2 = [i+j for i in word1 for j in word2]
>>> print(result2)
['HW', 'Ho', 'Hr', 'Hl', 'Hd', 'eW', 'eo', 'er', 'el', 'ed', 'lW', 'lo', 'lr', 'll', 'ld', 'lW', 'lo', 'lr', 'll', 'ld', 'oW', 'oo', 'or', 'ol', 'od']

# filter if,else
>>> result = [i + j if not(i == j) else "Same alpha!" for i in alpha_1 for j in alpha_2]
>>> print(result)
['AB', 'AC', 'AD', 'Same alpha!', 'BC', 'BD', 'CB', 'Same alpha!', 'CD']
```

# Lambda & map & reduce

```python
# 일반적인 함수
>>> def my_sum(x, y):
        return (x + y)
>>> print(my_sum(40,  2))
42

# lambda 함수
>>> my_lam_sum = lambda x, y : x + y
>>> print(my_lam_sum(40, 2))
42
>>> (lambda x, y: x + y)(40, 2)
42

-------------------------------------------

>>> list_a = [1, 2, 3]

# 한 개의 리스트
>>> my_square = lambda x : x ** 2
>>> print(list(map(my_square, list_a)))
[1, 4, 9]

# 두 개 이상의 리스트
>>> my_sum = lambda x, y : x + y
>>> print(list(map(my_sum, list_a, list_a)))
[2, 4, 6]

-------------------------------------------

>>> from functools import reduce

>>> list_a = [1, 2, 3, 4, 5]
>>> my_sum = lambda x, y : x + y
# x1 = 1, y1 = 2 -> x1 + y1 = 3 = x2
# x2 = 3, y2 = 3 -> x2 + y2 = 6 = x3
# x3 = 6, y3 = 4 -> x3 + y3 = 10 = x4
# x4 = 10, y4 = 5 -> x4 + y4 = 15
>>> print(reduce(my_sum, list_a))
15
```

# variable-length argument

### 가변인자 : variable-length argument (*)

> 개수가 정해지지 않은 변수를 함수의 parameter로 사용.asterisk를 사용하여 함수의 parameter를 표시.입력된 값은 함수 내에서tuple type으로 사용.오직 한 개만 함수의 맨 마지막 parameter 위치에 사용.


```plain text
>>> def sum_all(a, b, *args):
...     print(list(args))
...     print(type(args))
...     return (a + b + sum(args))
...
>>> result = sum_all(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
[3, 4, 5, 6, 7, 8, 9, 10]	# 함수 내에서 가변인자
<class 'tuple'>			# 함수 내에서 가변인자 type
>>> print(result)
55
```

### 키워드 가변인자 : Keyword variable-length argument (**)

> parameter 이름을 따로 지정하지 않고 입력.asterisk를 두개 사용하여 함수의 parameter를 표시.입력된 값은 함수 내에서 dict type으로 사용.오직 한 개만 기존 가변인자 다음에 사용.(순서 지키지 않으면 에러 발생함)


```plain text
# 키워드 가변인자만 사용
>>> def kword_test(**kwargs):
...     print(kwargs)
...     print(type(kwargs))
...
>>> kword_test(one = 24, two = 42, three = 7)
{'one': 24, 'two': 42, 'three': 7}
<class 'dict'>

# 가변인자 뒤에 키워드 가변인자 사용
>>> def sum_all(a, b = 1, *args, **kwargs):
...     print(f"args: {args}")
...     print(f"kwargs: {kwargs}")
...
>>> sum_all(1, 2, 3, 4, 5, 6, 7, eight=8, nine=9, ten=10)
args: (3, 4, 5, 6, 7)
kwargs: {'eight': 8, 'nine': 9, 'ten': 10}
```

### unpacking container

> container에 들어있는 값들을 unpacking하여 함수에 전달할 때 사용할 수 있다.**를 이용하여 dict 자료형을 unpacking 할 수도 있다.

```plain text
>>> def unpacking_test(a, *args):
...     print(a, args)
...     print(type(args))
...
# unpacking_test(1, 2, 3, 4, 5) 와 동일함. *로 unpacking 되었기 때문.
>>> unpacking_test(1, *(2, 3, 4, 5))
# 가변인자는 tuple type으로 받음.
1 (2, 3, 4, 5)
<class 'tuple'>

>>> def unpacking_test2(a, args):
...     print(a, *args)
...     print(type(args))
...
>>> unpacking_test2(1, (2, 3, 4, 5))
# tuple type을 받아서 unpacking 하여 출력.
1 2 3 4 5
<class 'tuple'>
```

# N진법 정리

Python에서 N진법으로 변환하는 알고리즘

### N to 10 - int함수

- int(str, int) 형식으로 int(N진수인 숫자 문자열, N) 형식으로 작성하면 변환이 됩니다.
- ex) int(”FFF”, 16)
### 10 to 2,8,16 - bin, oct, hex 함수

- 2, 8, 16 은 자주 접하는 진법입니다. 파이썬은 내부함수로 변환 알고리즘을 제공합니다.
- print(bin(10)) print(oct(10)) print(hex(10))
### 10 to N - 변환 알고리즘

```yaml
def convert(num, base) :
    q, r = divmod(num, base)
		# num과 base를 나눈 값 q
		# num과 base의 나머지 값 r
    if q == 0 :
        return tmp[r] 
    else :
        return convert(q, base) + tmp[r]
```

### N to M - N to 10 → 10 to M

- 10진수를 변환하고 다시 원하는 M진수로 변환해야한다
# 문자열 왼쪽, 가운데, 오른쪽 정렬

### **ljust, center, rjust 함수 **

```yaml
s = '가나다라'
n = 7

s.ljust(n) # 좌측 정렬
s.center(n) # 가운데 정렬
s.rjust(n) # 우측 정렬
```

## 참고자료

[https://velog.io/@hyungraelee/Pythonic-Code-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%8A%A4%ED%83%80%EC%9D%BC-%EC%BD%94%EB%93%9C](https://velog.io/@hyungraelee/Pythonic-Code-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%8A%A4%ED%83%80%EC%9D%BC-%EC%BD%94%EB%93%9C)


