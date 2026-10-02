---
source: knowledge-base
origin: notion
title: "파이썬 - Generator "
area: "Python"
tags: ["area/python", "language/python"]
created: "2025-08-04T06:05:00.000Z"
last_edited: "2025-08-04T06:28:00.000Z"
status: published
public: true
notion_id: "245172a5-56d6-803b-8102-f1d566fa353a"
notion_url: "https://www.notion.so/Generator-245172a556d6803b8102f1d566fa353a"
type: note
updated: 2026-07-07
---

# 파이썬 - Generator 

## 요약

Python Language

개념, 구현 맥락, 후속 학습거리를 지식 그래프에 연결하기 위한 정리 노트입니다.

## 핵심 포인트

- Python Language
- 제너레이터 - Generator 란?
- 목적
- 개념
- LIST 방식

## 지식 그래프

- [[wiki/mocs/Knowledge Base|Knowledge Base]]
- [[wiki/mocs/Python|Python]]

## 정리 내용

## 제너레이터 - Generator 란?
영단어 generate는 사전적으로 "생성하다, 생산하다"라는 의미이다.
제네레이터는 한 번에 하나씩 구성요소를 반환해주는 이터러블을 생성해주는 객체이다.
#### 목적 
가장 큰 목적은 메모리를 절약하는 것이다.
거대한 요소를 한꺼번에 메모리에 저장하는 대신 특정 요소를 어떻게 만드는지 아는 객체를 만들어서 필요할 때마다 하나씩만 가져오도록 한다.
![[_attachments/notion/파이썬---Generator/245172a556d6817189f0ce76278baab7.png]]
#### 개념
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
#### LIST 방식
- 가장 익숙하고 많이 사용하는 방식이다.
- 함수를 실행하면 ["A","B","C"] 생성하고 return한다.
- 메모리 크기는 당연히 ["A","B","C"] 부분의 크기만큼 소모가 될 것 이다.
#### Generator 방식
- yield라는 생소한 방식이 사용된다.
- 게으른 반복자라는 별명이 있는 이 방식은 한번에 리스트가 생성되는 방식이 아닌 반복자가 넘어갈 때 마다 생성되는 방식이다. 
- List보다 적은 메모리로 같은 출력을 할 수 있다.
![[_attachments/notion/파이썬---Generator/245172a556d681508039ebeadf82fc22.png]]
#### 사용 예제
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

## 출처

- 원문: https://www.notion.so/Generator-245172a556d6803b8102f1d566fa353a
- Vault path: wiki/notes/python/파이썬---Generator.md
