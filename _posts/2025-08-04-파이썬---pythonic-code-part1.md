---
title: "파이썬 - Pythonic Code Part1"
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

# Python PEP8 - Pythonic 가이드

### 네이밍 

- 변수와 클래스 이름은 코드 내 가독성에 있어 매우 중요합니다.
**파이썬 스타일 네이밍**을 꼭 숙지하시기 바랍니다.

1. **함수, 변수, 애트리뷰트는 snake_case**를 사용합니다.
1. **클래스는 PascalCase**를 사용합니다.
1. **모듈 수준의 상수**는 모든 글자를 **대문자**로 하여 snake_case를 사용합니다.
- **보호해야 하는 인스턴스 애트리뷰트**는 밑줄 한개(_)로 시작합니다.
- **private 인스턴스 애트리뷰트**는 밑줄 두개 (__)로 시작합니다.
### 들여쓰기 - Indentation

- 한 줄의 코드를 여러 줄로 나워 쓰는 경우
```python
# GOOD
foo = long_function_name(
    var_one, var_two,
    var_three, var_four)

foo = long_function_name(var_one, var_two,
                         var_three, var_four)

# BAD
foo = long_function_name(var_one, var_two,
    var_three, var_four)

# if문에서 들여쓰기를 하지 않은 경우
if (this_is_one_thing and
    that_is_another_thing):
    do_something()

# if문에서 들여쓰기를 하여 다음행과 구분을 준 경우
if (this_is_one_thing
        and that_is_another_thing):
    do_something()
```

- {}, (), [] 괄호에 대한 들여쓰기
```python
# 마지막 줄의 첫번째 아이템에 정렬하여 괄호를 닫은 경우
my_list = [
    1, 2, 3,
    4, 5, 6,
    ]
result = some_function_that_takes_arguments(
    'a', 'b', 'c',
    'd', 'e', 'f',
    )

# 첫번째 줄에 정렬하여 괄호를 닫은 경우
my_list = [
    1, 2, 3,
    4, 5, 6,
]
result = some_function_that_takes_arguments(
    'a', 'b', 'c',
    'd', 'e', 'f',
)
```

- **Tab or Space**
### Line의 최대 길이

- 코드 한 줄은 79자 이내로 작성하기를 권장합니다.
- 코드가 길어지는 경우 \ 로 줄 바꿈이 가능합니다.
```python
with open('/path/to/some/file/you/want/to/read') as file_1, \
     open('/path/to/some/file/being/written', 'w') as file_2:
    file_2.write(file_1.read())

# 연산자 이전에 줄바꿈하여 연산자와 이어지는 코드가 보기 좋음
income = (gross_wages
          + taxable_interest
          + (dividends - qualified_dividends)
          - ira_deduction
          - student_loan_interest)

# 연산자 이후에 줄바굼하여 이어지는 코드를 보기 어려움
income = (gross_wages +
          taxable_interest +
          (dividends - qualified_dividends) -
          ira_deduction -
          student_loan_interest)
```

### 빈 줄 ( Blank Lines )

- 빈 줄은 클래스 또는 함수 간의 정의를 구분할 때 사용하고, 코드 내에서 연관성이 있는 코드 블록을 묶는데 사용합니다.
```python
def get_extractor():
  pass


class YoutubePlaylistsBaseInfoExtractor(YoutubeEntryListBaseInfoExtractor):

    def _process_page(self, content):
        pass

    def _real_extract(self, url):
        pass


class YoutubeIE(YoutubeBaseInfoExtractor):

    def _real_extract(self, url):
        pass
```

### import, from import

- 한 줄에 두개의 모듈을 임포트 하는 것은 바람직하지 않습니다.
```python
# GOOD
import os
import sys

from subprocess import Popen, PIPE

# BAD
import os, sys

from subprocess import Popen
from subprocess import PIPE

# wildCard(*)는 최대한 자제해야한다. 
from <module> import *
```

### **Whitespace in Expressions and Statesment**

- Expression 연산자 1+1 수식 같은 것을 의미합니다.
- 이런 코드 안에서 띄어쓰기를 어떻게 할 것인지에 대한 전략입니다.
```python
Yes: spam(ham[1], {eggs: 2})
No:  spam( ham[ 1 ], { eggs: 2 } )
### 괄호에 붙어있는 코드는 띄울 필요 없습니다

# 좋은 예:
ham[1:9], ham[1:9:3], ham[:9:3], ham[1::3], ham[1:9:]
ham[lower:upper], ham[lower:upper:], ham[lower::step]
ham[lower+offset : upper+offset]
ham[: upper_fn(x) : step_fn(x)], ham[:: step_fn(x)]
ham[lower + offset : upper + offset]

# 나쁜 예:
ham[lower + offset:upper + offset]
ham[1: 9], ham[1 :9], ham[1:9 :3]
ham[lower : : upper]
ham[ : upper]

# 좋은 예:
x = 1
y = 2
long_variable = 3

# 나쁜 예:
x             = 1
y             = 2
long_variable = 3
```

### **Other Recommendations**

- 할당(=), 증감연산자(+=, -=), 비교연산자(==, <, >, !=, <>, <=, >=, in, not in, is, is not), Boolean연산자(and, or, not)를 사용할 때 스페이스 한칸씩 넣어주세요.
- 우선순위가 다른 연산자들을 함께 쓸 때, 우선순위가 가장 낮은 연산자 주위로 스페이스 한칸씩 넣어 구분을 해주세요. 어떤게 먼저 연산이 되는지 읽기 쉬워집니다.
```python
# 좋은 예:
i = i + 1
submitted += 1 # 증감 연산
x = x*2 - 1    # 우선 순위가 다른 연산
hypot2 = x*x + y*y # 우선 순위가 다른 연산 구분
c = (a+b) * (a-b)

# 나쁜 예:
i=i+1
submitted +=1
x = x * 2 - 1
hypot2 = x * x + y * y
c = (a + b) * (a - b)
```

### Function annotations

```python
# :과 ->를 사용할 때 아래처럼 스페이스를 넣어주어야 합니다.

# 좋은 예:
def munge(input: AnyStr): ...
def munge() -> AnyStr: ...

# 나쁜 예:
def munge(input:AnyStr): ...
def munge()->PosInt: ...

# 좋은 예:
def complex(real, imag=0.0):
    return magic(r=real, i=imag)

# 나쁜 예:
def complex(real, imag = 0.0):
    return magic(r = real, i = imag)
```

### 주석

```text
# 좋은 예:
"""Return a foobang

Optional plotz says to frobnicate the bizbaz first.
"""

"""Return a foobang"""
```

### 참고자료

[https://codechacha.com/ko/pythonic-and-pep8/](https://codechacha.com/ko/pythonic-and-pep8/)

[https://facerain.club/pythonic-code-guide/](https://facerain.club/pythonic-code-guide/)


