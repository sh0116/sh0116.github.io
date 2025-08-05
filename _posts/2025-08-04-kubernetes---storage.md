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
![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/d08779ff-3c8c-4b96-8118-7844ca4a7e40/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T7HDHXUC%2F20250805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250805T061015Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJGMEQCIBrcOEg8RoWTDJMBSfdoPhIcBm3Vml4OPPDlzTL7fGCHAiAIfw%2BuYk3mR16EXI2QxrlfFdzUzIjet9jjoD3YHWtaSir%2FAwhXEAAaDDYzNzQyMzE4MzgwNSIMOZGpOUxxrJprK4gBKtwD9AbciUUfBaqM03aJ4Uljz9NoSuxJ6dB4irOTK94t1LdPx50Q2WBqtXdnrx05fF9sWsLuEAczTcu4PUwxKLX9wyTDGdYHDBbJheddVVh2pk1%2BuTvyxUZzG8MPFj1XGRE4qZNFTQg%2BOD9nAfblpk3lM8sRsBY85TNONYVSmQa32X%2BwKzLvWy8%2FDtqpY3sacztO2iuc88Bz%2BbUBV1LPFAwjqXQh7M%2BWg0LbNW3Ij1WRfTHxR4eqVgccqGbYDwSCacw1gY8RZJue4MAmEMCn2g6Q%2BLn1aIWgVSYhuLoKT9Rz%2FosrMCumD4cPPJJ6dpDrMXDWOMoOhbAQSZPXw%2FBEWP3LoVk5m%2BDJMEpD8eQO0in9T9VG5PQBJ%2FW6Kt%2Fw9%2F8PusWD2jb9ElswwdTM06t%2F7ShhwxEMs99S8p4BWmqeXbR6R2nq2LP%2FgqaHbrP91%2BNI8m%2Bhkjlnqx1ajQsvdJ%2FsUZthOwN1reOft8Jom22a53GHIWr1JiiJn0ZjHLUZdcKKnE00fbhJEKgqXjaQYFjMHgYEaqOpMXwueDsviMi34weCzY%2BUTMf3byjiH6GpWCkbi7hETTCwb1NbVOWI8SfMxE%2FrOkNX21HiFPY4gsgys6rOvnfFUzx4FDXprWhZMuAwq7PGxAY6pgFNn9jQckCRe5LMz2vfvU7I0jegrc1PY5AAQMf27yQYOZPejIA5nBwKaZ%2FcT6ludbGRN3TdtZTM9%2B8rY5%2BKGnpm3a5mJDLZ2nUcQCwlnqPxcHZsPhipiHcjW5wMpZMbpCMZzgR6Ggf4W8V5noqOLX8%2BqFv3x6Eo%2BYUnC0MwpfDmK%2BFec2YJG7Vnfs3AGIj2drIJ7Csf3GbV0KG4cdtvaHkZ45SUY15n&X-Amz-Signature=880ee32dc4cb993c84a2146724a789d7216363b020091f1e8817a69829403fa1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 임시 볼륨 : 
- 로컬 볼륨 :
- 네트워크 볼륨 :
- 네트워크 볼륨 (클라우드 종속) :
# EmptyDir 을 활용한 파일 시스템 공유

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/0fd040f0-b611-4ac4-887d-76487068320b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T7HDHXUC%2F20250805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250805T061015Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJGMEQCIBrcOEg8RoWTDJMBSfdoPhIcBm3Vml4OPPDlzTL7fGCHAiAIfw%2BuYk3mR16EXI2QxrlfFdzUzIjet9jjoD3YHWtaSir%2FAwhXEAAaDDYzNzQyMzE4MzgwNSIMOZGpOUxxrJprK4gBKtwD9AbciUUfBaqM03aJ4Uljz9NoSuxJ6dB4irOTK94t1LdPx50Q2WBqtXdnrx05fF9sWsLuEAczTcu4PUwxKLX9wyTDGdYHDBbJheddVVh2pk1%2BuTvyxUZzG8MPFj1XGRE4qZNFTQg%2BOD9nAfblpk3lM8sRsBY85TNONYVSmQa32X%2BwKzLvWy8%2FDtqpY3sacztO2iuc88Bz%2BbUBV1LPFAwjqXQh7M%2BWg0LbNW3Ij1WRfTHxR4eqVgccqGbYDwSCacw1gY8RZJue4MAmEMCn2g6Q%2BLn1aIWgVSYhuLoKT9Rz%2FosrMCumD4cPPJJ6dpDrMXDWOMoOhbAQSZPXw%2FBEWP3LoVk5m%2BDJMEpD8eQO0in9T9VG5PQBJ%2FW6Kt%2Fw9%2F8PusWD2jb9ElswwdTM06t%2F7ShhwxEMs99S8p4BWmqeXbR6R2nq2LP%2FgqaHbrP91%2BNI8m%2Bhkjlnqx1ajQsvdJ%2FsUZthOwN1reOft8Jom22a53GHIWr1JiiJn0ZjHLUZdcKKnE00fbhJEKgqXjaQYFjMHgYEaqOpMXwueDsviMi34weCzY%2BUTMf3byjiH6GpWCkbi7hETTCwb1NbVOWI8SfMxE%2FrOkNX21HiFPY4gsgys6rOvnfFUzx4FDXprWhZMuAwq7PGxAY6pgFNn9jQckCRe5LMz2vfvU7I0jegrc1PY5AAQMf27yQYOZPejIA5nBwKaZ%2FcT6ludbGRN3TdtZTM9%2B8rY5%2BKGnpm3a5mJDLZ2nUcQCwlnqPxcHZsPhipiHcjW5wMpZMbpCMZzgR6Ggf4W8V5noqOLX8%2BqFv3x6Eo%2BYUnC0MwpfDmK%2BFec2YJG7Vnfs3AGIj2drIJ7Csf3GbV0KG4cdtvaHkZ45SUY15n&X-Amz-Signature=af69625a8a61b152931a9a6bef50c3ad6b83a2c6e5a52c8d952806f87fef273b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## EmptyDir 연습문제

- 하나의 프로세스는 랜덤한 값을 생성 (count 이미지 사용)
- 하나의 프로세스는 랜덤한 값을 출력 (httpd이미지 사용)

