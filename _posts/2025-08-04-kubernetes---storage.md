---
title: "Kubernetes - Storage"
date: 2025-08-04 06:05:00 +0900
categories: [kubernetes]
tags: [Kubernetes]
description: Kubernetes 기초
toc: true
comments: true
---

# 쿠버네티스 Storage 개념

### 불륨(Volume)

- 컨테이너가 외부 스토리지에 엑세스하고 공유하는 방법
- POD의 컨테이너에는 고유의 분리된 파일 시스템이 존재
- Volume은 POD의 컴포넌트이며 POD의 스펙에 의해 정의
- 독립적인 쿠버네티스의 오브젝트가 아니며 스스로 생성, 삭제 불가
- 각 컨테이너의 파일 시스템의 불륨을 마운트하여 생성
![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/d08779ff-3c8c-4b96-8118-7844ca4a7e40/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662IP7I3ZV%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T063303Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCIQDHHNYIIbJa618QoXXCKskCCwJy%2ByXdxEh5utzR4Azd%2BAIgasBwl5yAEen5NS9p1%2FSNB1cjgudP4SNtGo9yeSKRQIwq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDPsboIAr3g0WMxyc3yrcA%2FsC2%2F6QLJG4wnuVYr%2FmvXtYy%2FbRansG%2B%2BRvpq9pVNqpDviBhinhc7NCknzDQWe%2BPJKaHJUv1WnpyeLdFSvlNcILCaCZi%2BEWdGk7UUSzAfo28i2R%2Bu66MMbROQu81AMQAhmE5YeUjW4zQrNifh9Hl1joG6ip36UFWpNJ%2BZYC3qN0Yc0lnmiEjppK3w8t3Cdwe%2B%2FQX4tiXMx5QTUivyQDGZc6x%2FGTQt8W%2F1LiG8M9bBArOW%2F%2FT6rzYpmi4fS9wzc6i0uafBeR5yFAvA9YPXnxH1xt3Fm%2F9WZf2dRUQpl7HJAqh4OoNHqp2ANTJvSitQK%2BFx5KkmRYFHa%2BS8O0iG3%2FY5inI14kvX6sdjn%2BNKtpcfiuPTY9qcgarTNEhKnOlJkO4plHrsxDHkXqunicIeWedpKT3bIcAqofau1RHCD9XzYY4LQifIigagLB0Jh4JZKSs9Tc9QATWqolMpDfNZmIebRYjMpk6nqD5JbIr5jBXhbJeYG2LY%2BdHzr%2Bs1YhkJ9eE7iG50TxUAXv348iVZtJl5XepEQphgmAGub1sZY%2BqvAZbdq3t2%2ByU35s6iaRqrfJZkPHNNmAG9e3FhNnwMPlXrMza76ZALK5pgUHxTk6fu5elTd963n%2B79bTSL19MOSNwcQGOqUBXUiFfeNYbhv86p7ahPBKOJAhsgx4VLUS8K8g0TQvcbVA3UngeTnbn9T0bg2Rsw0c0N45%2BZwEvWl3a0LZ3%2BUv7dPQk9QEValzA4l9G5bTNBOeE9DjKgpa16%2Fiqd4f44Pb2BrTzJNEJ3eHO7DeFf6iVe%2FCIh92mfJstjpSWlJQX4Tr44TShiD%2FNXexDPUq3wDj5iwgktgt5sRf87546SpN1HSvWjB1&X-Amz-Signature=058f1aff169316ec9f46d893099c427f211abd538e5aebda3d600cf676692a8c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 임시 볼륨 : 
- 로컬 볼륨 :
- 네트워크 볼륨 :
- 네트워크 볼륨 (클라우드 종속) :
# EmptyDir 을 활용한 파일 시스템 공유

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/0fd040f0-b611-4ac4-887d-76487068320b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662IP7I3ZV%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T063303Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCIQDHHNYIIbJa618QoXXCKskCCwJy%2ByXdxEh5utzR4Azd%2BAIgasBwl5yAEen5NS9p1%2FSNB1cjgudP4SNtGo9yeSKRQIwq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDPsboIAr3g0WMxyc3yrcA%2FsC2%2F6QLJG4wnuVYr%2FmvXtYy%2FbRansG%2B%2BRvpq9pVNqpDviBhinhc7NCknzDQWe%2BPJKaHJUv1WnpyeLdFSvlNcILCaCZi%2BEWdGk7UUSzAfo28i2R%2Bu66MMbROQu81AMQAhmE5YeUjW4zQrNifh9Hl1joG6ip36UFWpNJ%2BZYC3qN0Yc0lnmiEjppK3w8t3Cdwe%2B%2FQX4tiXMx5QTUivyQDGZc6x%2FGTQt8W%2F1LiG8M9bBArOW%2F%2FT6rzYpmi4fS9wzc6i0uafBeR5yFAvA9YPXnxH1xt3Fm%2F9WZf2dRUQpl7HJAqh4OoNHqp2ANTJvSitQK%2BFx5KkmRYFHa%2BS8O0iG3%2FY5inI14kvX6sdjn%2BNKtpcfiuPTY9qcgarTNEhKnOlJkO4plHrsxDHkXqunicIeWedpKT3bIcAqofau1RHCD9XzYY4LQifIigagLB0Jh4JZKSs9Tc9QATWqolMpDfNZmIebRYjMpk6nqD5JbIr5jBXhbJeYG2LY%2BdHzr%2Bs1YhkJ9eE7iG50TxUAXv348iVZtJl5XepEQphgmAGub1sZY%2BqvAZbdq3t2%2ByU35s6iaRqrfJZkPHNNmAG9e3FhNnwMPlXrMza76ZALK5pgUHxTk6fu5elTd963n%2B79bTSL19MOSNwcQGOqUBXUiFfeNYbhv86p7ahPBKOJAhsgx4VLUS8K8g0TQvcbVA3UngeTnbn9T0bg2Rsw0c0N45%2BZwEvWl3a0LZ3%2BUv7dPQk9QEValzA4l9G5bTNBOeE9DjKgpa16%2Fiqd4f44Pb2BrTzJNEJ3eHO7DeFf6iVe%2FCIh92mfJstjpSWlJQX4Tr44TShiD%2FNXexDPUq3wDj5iwgktgt5sRf87546SpN1HSvWjB1&X-Amz-Signature=d8ab3b7fffeeb8302087c267c4df3f25f700f623b25124c10e08ec502c4e4475&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## EmptyDir 연습문제

- 하나의 프로세스는 랜덤한 값을 생성 (count 이미지 사용)
- 하나의 프로세스는 랜덤한 값을 출력 (httpd이미지 사용)

