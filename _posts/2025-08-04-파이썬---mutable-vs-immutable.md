---
title: "파이썬 - Mutable vs Immutable"
date: 2025-08-04 06:06:00 +0900
categories: [Python]
tags: [python]
description: Python Language
toc: true
comments: true
---

# Mutable & Immutable

- Mutable이란 변경 가능한 이라는 의미이고, Immutable은 변경 불가능한 이라는 의미이다.
- 파이썬의 각 객체 타입에 따라 변경이 가능하고 불가능한 것으로 나뉜다
### 예시) immutable - string Type

str 객체는 변경 불가능한 객체로 한번 할당되면 변경이 불가능합니다.

```python
str_name = "Hello"
str_name[1] = "A"
>>> # TypeError: 'str' object does not support item assignment
```

### 예시) mutable - List Type

반대로 List의 경우는 변경 가능한 객체로 언제든 요소를 변경할 수 있습니다

```python
list_name = [1,2,3,4,5]
list_name[1] = 1
>>> [1,1,3,4,5]

# 오류1 -> 아래 설명 참조
list_name_copy = list_name
list_name[1] = 2
>>> [1,2,3,4,5]

# 오류 해결 방법
list_name_copy = list_name.copy()
list_name_copy  = list(list_name)
list_name_copy  = list_name[:]
import copy
list_name_copy  = copy.deepcopy(list_name)
```

### 오류1 - 얕은 복사와 깊은 복사

list1 = list2 를 한다고 list1에 list2가 복사가 되는 것이 아닙니다.

list2가 가진 객체의 주소(namespace)를 옮기게 되어 같은 주소를 가르키는 객체가 생성되는 것 입니다.

list1과 list2가 모두 같은 객체를 바라보고 있기 때문에 둘 줄 하나를 수정하더라도 두 list가 모두 바뀌게 되어버립니다. 이런 경우는 DeepCopy를 통해 LIST의 값을 복사하는 작업을 수행해야 합니다.


