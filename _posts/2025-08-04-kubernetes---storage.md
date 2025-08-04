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
![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/d08779ff-3c8c-4b96-8118-7844ca4a7e40/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WUYPUWXN%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T070529Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJIMEYCIQDw8bpzZLnQ9WM%2BXoUf1NJ14FEuHImnoJdMtgc2q%2FRPQwIhANxTMkfd17nKz%2F%2B0H%2BuJbMTgywEt6ASMtnJJ4G6RWpgnKv8DCD8QABoMNjM3NDIzMTgzODA1IgyYC3hj6SPvTxI4HDoq3ANplSP65WGB%2Btw1nSbSdE7fkKgXY7CLUimSDWM2eJOHe4XBiJQEnRt1KcBJCS66OXOmX0pP8N9e7%2BvyotlMYmJCW%2FCLaGrS4DJOA6fnC4eR3ejX0UMZRjPHcgqDNev870toZzjdapiyHztZqIWV%2BEZ6UVZwnc491Vbtr4GTlZjh1gTq1C1xNo4AzCkJp%2FHHy9lEFCy3szuIkc2uysDZegenBwa9u%2B976xsoyOGO0G7E2gLtP5KFfRpwGt%2B0TYSXJApPRVslg7MWZtJIuz1sw5vT0shVS8UHwjurwwIB4tg0AjUy%2FwnZm7b2opQNyPcCnyKP%2B1OdrU0pTwc7pn3W13XcNsQ2A8uQk5koGObUyROaREfMtLhscG75sVuu0rtZwAzcR2hLNrTSjvM1gsx62UfJGRylGEs8AhE9aatW8TDbUyDTA5%2BQ3C2TYDMaRoRDQDFdpz3PJB2uwFQ%2F12tAbdjfvGYZU292r74oMj5F3UIZBvhf1T3KMKzBYvVr6iiuMu2zMqYAUYUPHruMg4Bp31IeT0CDvvmFiYGdsaudSDWBW0i5EmHkS0BF4m4900qYFIslxYe%2FwHS9pE0UlTuQhRlJh%2FtNVJc%2B8uAa%2FDZTeYD3RIop2pibpny4XMOeRDC6jcHEBjqkAURo9iDsm9KScakuMn1gkqSzhAdW5%2BQF5eyB8MeHoIvTx2fVUaCjxiJypVAaoxQ%2FJ3ZCo58gq2KVmB3eLFLtLCQSHFYppjGxjZItIjF3epO7pFVBximNrnAZehJsooGgtns6p%2BN70DEDcvUz67cCJn%2BbWwf0bNVicurxwpt91OyMKniKkO%2F2HaKmIHIynL0nFWj9l1%2B4f8gAmOlnmzZ8H0DuUJCm&X-Amz-Signature=ff148b571caffbfc4e88fec198dc0b4c4c822888b8325631703093e17a4ca0f7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 임시 볼륨 : 
- 로컬 볼륨 :
- 네트워크 볼륨 :
- 네트워크 볼륨 (클라우드 종속) :
# EmptyDir 을 활용한 파일 시스템 공유

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/0fd040f0-b611-4ac4-887d-76487068320b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WUYPUWXN%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T070529Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJIMEYCIQDw8bpzZLnQ9WM%2BXoUf1NJ14FEuHImnoJdMtgc2q%2FRPQwIhANxTMkfd17nKz%2F%2B0H%2BuJbMTgywEt6ASMtnJJ4G6RWpgnKv8DCD8QABoMNjM3NDIzMTgzODA1IgyYC3hj6SPvTxI4HDoq3ANplSP65WGB%2Btw1nSbSdE7fkKgXY7CLUimSDWM2eJOHe4XBiJQEnRt1KcBJCS66OXOmX0pP8N9e7%2BvyotlMYmJCW%2FCLaGrS4DJOA6fnC4eR3ejX0UMZRjPHcgqDNev870toZzjdapiyHztZqIWV%2BEZ6UVZwnc491Vbtr4GTlZjh1gTq1C1xNo4AzCkJp%2FHHy9lEFCy3szuIkc2uysDZegenBwa9u%2B976xsoyOGO0G7E2gLtP5KFfRpwGt%2B0TYSXJApPRVslg7MWZtJIuz1sw5vT0shVS8UHwjurwwIB4tg0AjUy%2FwnZm7b2opQNyPcCnyKP%2B1OdrU0pTwc7pn3W13XcNsQ2A8uQk5koGObUyROaREfMtLhscG75sVuu0rtZwAzcR2hLNrTSjvM1gsx62UfJGRylGEs8AhE9aatW8TDbUyDTA5%2BQ3C2TYDMaRoRDQDFdpz3PJB2uwFQ%2F12tAbdjfvGYZU292r74oMj5F3UIZBvhf1T3KMKzBYvVr6iiuMu2zMqYAUYUPHruMg4Bp31IeT0CDvvmFiYGdsaudSDWBW0i5EmHkS0BF4m4900qYFIslxYe%2FwHS9pE0UlTuQhRlJh%2FtNVJc%2B8uAa%2FDZTeYD3RIop2pibpny4XMOeRDC6jcHEBjqkAURo9iDsm9KScakuMn1gkqSzhAdW5%2BQF5eyB8MeHoIvTx2fVUaCjxiJypVAaoxQ%2FJ3ZCo58gq2KVmB3eLFLtLCQSHFYppjGxjZItIjF3epO7pFVBximNrnAZehJsooGgtns6p%2BN70DEDcvUz67cCJn%2BbWwf0bNVicurxwpt91OyMKniKkO%2F2HaKmIHIynL0nFWj9l1%2B4f8gAmOlnmzZ8H0DuUJCm&X-Amz-Signature=0232794d84ecc154a492b99272b343a708ccddf1cb785598965441e4d38852a3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## EmptyDir 연습문제

- 하나의 프로세스는 랜덤한 값을 생성 (count 이미지 사용)
- 하나의 프로세스는 랜덤한 값을 출력 (httpd이미지 사용)

