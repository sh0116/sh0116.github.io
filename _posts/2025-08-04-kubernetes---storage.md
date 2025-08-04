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
![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/d08779ff-3c8c-4b96-8118-7844ca4a7e40/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667T4YJJ6T%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T071422Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIQCQ%2FbEN6c6jfGjrncBtBiiQ3HMPW5ou9Ef9dajaLcnbOAIgNhAs68D5lzXR6PWED8icP3YD3ClYpE7xsDdbm3zwESwq%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDLKAz6KUeiSKINPswircA6PgfX3KYF12wuq7bpxn4x94%2BQcdYJqN21wS4tRSZs7Dx9dycWWsEqPS25YTwX0xmymTj3LbWoA4CB6vysVO825oiizZE8y5LvUHUCVD3Pt9pYWJFOGvLwgQKnBJ5KiV7eUoYbihTvnDx32YTf3ndQxNTk3MIOk7BCrQiVKJRyJN2msOuPGBOawPL%2Bx%2BSHdmGGzBxbuc23YfHV4KjQSOGCq6K6NOvOM18nG%2FjjcqT0ncq6ZvnyCa0ohzl7GAWtxqCUVbiF%2FIWkns%2FeFF%2FZBwGKmlS5KXopkFJSGNu9LlgnPNvI0BtTbB3HQMWP2RO3BC1Nsl0SP9P5bbxrOezrW6G%2F0QoGWNutv1I2ns3xqTYModALxhnhHUNhL7rp83y7iY6o1OthhyvbyGRiF08ugvpv8eG9tzcpcTxs04STdZ1Po3GPQ%2FMpYX%2B1W%2BiTzhbbaUudh6x5iSsCme758FPM%2BIqUyEeY%2BD0uIIK4riwgvp256y9eo9NDKA3PMA9YUOTy0KhxUXNJ%2Fqxlw4ZlBwr3MxqJUhtj1Jq%2BifU3D0nogbU5HDseerE3BfvG%2FGPKJZOfrb2kDeyNlfAruV7Jh%2FfhdtC%2B39quX7uARatEcCGhJ%2FRTjxnBE4ww1p3sJ4%2FShvMOu2wcQGOqUBV1f4ZgMAO0ubtx562VezCbtLd7DJqre2vkpHtamZOeu%2BGYeov%2BlTBtEaM1BZ7uaZHiq3qEjopu0ZfK8w5SvWoPsVJe%2FU62f1aNC1zExc450t4VMEigYoFJGsX%2Fp0eY8aHjta9ULldYFYLhqmN1UmDnNDxJKqlrhnZdndvCHi%2FRwVR7djZ%2FGzsij6SG7TtiMCh%2BXMQN8DqVlYp3lFk578R3V1rhvz&X-Amz-Signature=68f6edb185f50946d7a78a328e406cf95a898d497ccfc6e30f3d7a07f813ec2e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 임시 볼륨 : 
- 로컬 볼륨 :
- 네트워크 볼륨 :
- 네트워크 볼륨 (클라우드 종속) :
# EmptyDir 을 활용한 파일 시스템 공유

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/0fd040f0-b611-4ac4-887d-76487068320b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667T4YJJ6T%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T071422Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIQCQ%2FbEN6c6jfGjrncBtBiiQ3HMPW5ou9Ef9dajaLcnbOAIgNhAs68D5lzXR6PWED8icP3YD3ClYpE7xsDdbm3zwESwq%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDLKAz6KUeiSKINPswircA6PgfX3KYF12wuq7bpxn4x94%2BQcdYJqN21wS4tRSZs7Dx9dycWWsEqPS25YTwX0xmymTj3LbWoA4CB6vysVO825oiizZE8y5LvUHUCVD3Pt9pYWJFOGvLwgQKnBJ5KiV7eUoYbihTvnDx32YTf3ndQxNTk3MIOk7BCrQiVKJRyJN2msOuPGBOawPL%2Bx%2BSHdmGGzBxbuc23YfHV4KjQSOGCq6K6NOvOM18nG%2FjjcqT0ncq6ZvnyCa0ohzl7GAWtxqCUVbiF%2FIWkns%2FeFF%2FZBwGKmlS5KXopkFJSGNu9LlgnPNvI0BtTbB3HQMWP2RO3BC1Nsl0SP9P5bbxrOezrW6G%2F0QoGWNutv1I2ns3xqTYModALxhnhHUNhL7rp83y7iY6o1OthhyvbyGRiF08ugvpv8eG9tzcpcTxs04STdZ1Po3GPQ%2FMpYX%2B1W%2BiTzhbbaUudh6x5iSsCme758FPM%2BIqUyEeY%2BD0uIIK4riwgvp256y9eo9NDKA3PMA9YUOTy0KhxUXNJ%2Fqxlw4ZlBwr3MxqJUhtj1Jq%2BifU3D0nogbU5HDseerE3BfvG%2FGPKJZOfrb2kDeyNlfAruV7Jh%2FfhdtC%2B39quX7uARatEcCGhJ%2FRTjxnBE4ww1p3sJ4%2FShvMOu2wcQGOqUBV1f4ZgMAO0ubtx562VezCbtLd7DJqre2vkpHtamZOeu%2BGYeov%2BlTBtEaM1BZ7uaZHiq3qEjopu0ZfK8w5SvWoPsVJe%2FU62f1aNC1zExc450t4VMEigYoFJGsX%2Fp0eY8aHjta9ULldYFYLhqmN1UmDnNDxJKqlrhnZdndvCHi%2FRwVR7djZ%2FGzsij6SG7TtiMCh%2BXMQN8DqVlYp3lFk578R3V1rhvz&X-Amz-Signature=3d4854fb043e2bc02991826e27f6d49cfb55e8daab4ce966ade386169316f2d9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## EmptyDir 연습문제

- 하나의 프로세스는 랜덤한 값을 생성 (count 이미지 사용)
- 하나의 프로세스는 랜덤한 값을 출력 (httpd이미지 사용)

