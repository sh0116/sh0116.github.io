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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/96e960a1-9b1c-4157-ade1-53664e2fca73/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MTTXEAK%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T071358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIQDVe4ju7hvIDUaKE5m71NmKhIF6GPE0vLs%2BHpQvfqoe%2FQIgAqHLanJCHVbfrBxZHaSe1Q0UPF%2FaBoCdXJzWMnzNiUcq%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDIFDpZZEqh%2FYexfojircAxpbH5TmKf9%2B0Q4rnW6pIoGqoBf%2FqTwRce8DtSxD60%2FNaz38ZP6iwPKBCmR%2BI8MykAENQXdtPVJEMc0I%2FzOMqCPDxm%2BgZhGhj4dw9FZqgOZylsf0bFC0n8Tz2cQx%2BY2dTmR7H4Fo516t7XRf%2FWkTFfyV1MhX650XGa8TigCfSnJ46puApOL%2BFQGRcGdcUIbaUjL2PIfFwonuxF%2FWKnVaxKxplHWC%2Fd3pgdL5v%2FokbqjMcpNjiomQKRBqmpRGVtGZ26AwNGp409FhbzYmn5YS2pKZrXZGy655ns51BJQwuJig08e4iLmuk67wlKzJVwjqM37BT%2BuygrfJo1vU4BnP100kUsaVa8MFyhOa8RP0oy0aVU%2FF5V2z4OvnlkZib1Lr4HAYr%2BkY8FWMmklB0txn%2FwvkdK5m1NMLA0m5PqOMspAy8SBEpriXF32GD1h%2F4aOvWPu6SxacxLM7JP0gffKp%2BGt9ionW1zbSlRO7dvm4Q%2Fm%2FBSWN%2F7Al1kvVILeKeVN7D6jJYEz5Q5kVOCKi77SW8LFIrxtN%2BXTuzfT3jm0M7HPKDWuCV32XlxGZYStFMx%2F93rfTrWHbNxJ1sdejdfE5ueuLCRGAhwAfyBSKhJHPDnC0oLlJaZnS9biD%2BL%2BzMMm2wcQGOqUBzQEXVHp98AqpHL9jqR%2Fjn%2B7Uo3YDqLzUH%2FgNh94QoggLiN7K3I4XdLVz%2F0pTkaOTx9H%2B4V3VxSDb0lPQ55x%2FGNc6669NTm15eeJaQDCtapPzyvS3gxWkls9ECcfKx0TLkTztMac1Oib5RSB2R%2F6EpboJ277%2BlwG47lDajGiR6jNIeRYZzGVMTALLD0Zj3R7KZFU5qffpvaB0l4EvS%2FMzGP92SESR&X-Amz-Signature=78f079b10595abfd475a470c38a87927a47fe9f6ddc6c17647b76269afaa4a96&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/96e960a1-9b1c-4157-ade1-53664e2fca73/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MTTXEAK%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T071358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIQDVe4ju7hvIDUaKE5m71NmKhIF6GPE0vLs%2BHpQvfqoe%2FQIgAqHLanJCHVbfrBxZHaSe1Q0UPF%2FaBoCdXJzWMnzNiUcq%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDIFDpZZEqh%2FYexfojircAxpbH5TmKf9%2B0Q4rnW6pIoGqoBf%2FqTwRce8DtSxD60%2FNaz38ZP6iwPKBCmR%2BI8MykAENQXdtPVJEMc0I%2FzOMqCPDxm%2BgZhGhj4dw9FZqgOZylsf0bFC0n8Tz2cQx%2BY2dTmR7H4Fo516t7XRf%2FWkTFfyV1MhX650XGa8TigCfSnJ46puApOL%2BFQGRcGdcUIbaUjL2PIfFwonuxF%2FWKnVaxKxplHWC%2Fd3pgdL5v%2FokbqjMcpNjiomQKRBqmpRGVtGZ26AwNGp409FhbzYmn5YS2pKZrXZGy655ns51BJQwuJig08e4iLmuk67wlKzJVwjqM37BT%2BuygrfJo1vU4BnP100kUsaVa8MFyhOa8RP0oy0aVU%2FF5V2z4OvnlkZib1Lr4HAYr%2BkY8FWMmklB0txn%2FwvkdK5m1NMLA0m5PqOMspAy8SBEpriXF32GD1h%2F4aOvWPu6SxacxLM7JP0gffKp%2BGt9ionW1zbSlRO7dvm4Q%2Fm%2FBSWN%2F7Al1kvVILeKeVN7D6jJYEz5Q5kVOCKi77SW8LFIrxtN%2BXTuzfT3jm0M7HPKDWuCV32XlxGZYStFMx%2F93rfTrWHbNxJ1sdejdfE5ueuLCRGAhwAfyBSKhJHPDnC0oLlJaZnS9biD%2BL%2BzMMm2wcQGOqUBzQEXVHp98AqpHL9jqR%2Fjn%2B7Uo3YDqLzUH%2FgNh94QoggLiN7K3I4XdLVz%2F0pTkaOTx9H%2B4V3VxSDb0lPQ55x%2FGNc6669NTm15eeJaQDCtapPzyvS3gxWkls9ECcfKx0TLkTztMac1Oib5RSB2R%2F6EpboJ277%2BlwG47lDajGiR6jNIeRYZzGVMTALLD0Zj3R7KZFU5qffpvaB0l4EvS%2FMzGP92SESR&X-Amz-Signature=78f079b10595abfd475a470c38a87927a47fe9f6ddc6c17647b76269afaa4a96&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


