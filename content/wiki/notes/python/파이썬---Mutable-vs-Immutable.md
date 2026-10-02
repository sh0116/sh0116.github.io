---
source: knowledge-base
origin: notion
title: "파이썬 - Mutable vs Immutable "
area: "Python"
tags: ["area/python", "language/python"]
created: "2025-08-04T06:06:00.000Z"
last_edited: "2025-08-04T06:28:00.000Z"
status: published
public: true
notion_id: "245172a5-56d6-80fd-ac44-ec094ade73c0"
notion_url: "https://www.notion.so/Mutable-vs-Immutable-245172a556d680fdac44ec094ade73c0"
type: note
updated: 2026-07-07
---

# 파이썬 - Mutable vs Immutable 

## 요약

Python Language

해결 절차를 블로그 글감으로 발전시키기 위한 트러블슈팅 노트입니다.

## 핵심 포인트

- Python Language
- Mutable & Immutable
- 예시) immutable - string Type
- 예시) mutable - List Type
- 오류1 - 얕은 복사와 깊은 복사

## 지식 그래프

- [[wiki/mocs/Knowledge Base|Knowledge Base]]
- [[wiki/mocs/Python|Python]]

## 정리 내용

## Mutable & Immutable
- Mutable이란 변경 가능한 이라는 의미이고, Immutable은 변경 불가능한 이라는 의미이다.
- 파이썬의 각 객체 타입에 따라 변경이 가능하고 불가능한 것으로 나뉜다
  - Mutable : list(), bytearray(), set(), dict(), classes, class instances 
  - Immutable: int(), float(), complex(), str(), tuple(), frozenset(), bytes()
#### 예시) immutable - string Type
str 객체는 변경 불가능한 객체로 한번 할당되면 변경이 불가능합니다.
```python
str_name = "Hello"
str_name[1] = "A"
>>> # TypeError: 'str' object does not support item assignment
```
#### 예시) mutable - List Type
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
> [!note] 가장 많이 쓰이는 방법으로 파이썬 내장 모듈 copy를 import 하여 deepcopy 메소드를 사용하는 방법이다.
  copy 모듈의 copy() 메소드와의 차이점은 copy() 는 배열의 내부 객체까지 깊은 복사를 해주지 않는 차이점이 있다. (즉, 이중 이상의 배열은 완전한 깊은복사가 이루어지지 않음)
#### 오류1 - 얕은 복사와 깊은 복사
list1 = list2 를 한다고 list1에 list2가 복사가 되는 것이 아닙니다.
list2가 가진 객체의 주소(namespace)를 옮기게 되어 같은 주소를 가르키는 객체가 생성되는 것 입니다.
list1과 list2가 모두 같은 객체를 바라보고 있기 때문에 둘 줄 하나를 수정하더라도 두 list가 모두 바뀌게 되어버립니다. 이런 경우는 DeepCopy를 통해 LIST의 값을 복사하는 작업을 수행해야 합니다.

## 출처

- 원문: https://www.notion.so/Mutable-vs-Immutable-245172a556d680fdac44ec094ade73c0
- Vault path: wiki/notes/python/파이썬---Mutable-vs-Immutable.md
