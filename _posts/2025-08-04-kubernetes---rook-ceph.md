---
title: "Kubernetes - rook-ceph"
date: 2025-08-04 06:05:00 +0900
categories: [kubernetes]
tags: [Kubernetes]
description: Kubernetes 기초
toc: true
comments: true
---

# rook-ceph이란

온프레미스 환경에서  storage-class를 구성하는 도구

ceph은 파일 스토리지를 가상화시키는 클러스터를 구성할 수 있는 소프트웨어

직접 설치하는 방법도 있지만 rook패키지를 활용하면 쿠버네티스에서 보다 편히하게 ceph을 설치하고 관리할 수 있다.

## Rook-ceph Architecture

아래 회색의 Application이 Ceph Application이고 Rook을 통해서 pod화 하고 연결하는 과정

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/cbb8b20f-f959-4b43-b1d7-dffd346657f5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663V3LISGR%2F20250805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250805T061026Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJGMEQCIEY886qM5ZjYoWb4d%2B1Nz6T%2F5gLdTVLVSvcNbRIcjLEcAiAam3ecwVVYDSgvFEqhzxqXf94K7W8Dpr4%2FIVQfW48wWir%2FAwhXEAAaDDYzNzQyMzE4MzgwNSIM78fHGMBuO7zYkOvBKtwD7HUKj4c8B6QMOZ%2BdjxPvmP4et4o4iwAMC0D8VmAidxvo1PTcQFwBzOu%2FCnTXRbYZpemz8JcHZpytWbXQs7y7pbb%2F7YsCBSEdEscN8qRIKPc6lnpb6vIglGhiJfugOP5J2L5%2BAsggkjtL6YFOHTgleXOCt5%2FXJKmwwlvxx9On%2BB08jCn09hlkH2z%2FSJLk5AQT%2F2UR82X7ibb6dmz%2BPc74a%2Fkv628AyWufDuuHL%2F9Dwx%2BkaDHZYAjZcnKdLUbaJHPWWOEKG0%2BzgZaEPAexeqv7m2I4inhBnL1UcOweiKbirXi3KjqhfxZONjp0WsjjPUtU6a8NCcFDjofJjSMvi9cqM9qPR95aIymXAkkU23T4feTM1wvxF7kepntza45wWB5AEKF0OhQI%2BJT5KG4OURoAhwEIJw2pU4Xu%2BwyAYRflPkKdlekjoJnb319ov3SX4bf2UmVSN28j%2BLl8oP1cqpVQhJieqtim7SE8mYn9jh%2BcOTpKtHboJ4%2BoEgC9ydDdAAwmbm2Q2LqBdFsE%2Bv44quRPSH5nnJcoiXZhhlEdZHUh3lSc8r3cm2cXD0EMTvL6t98EITTDoYvGaD%2FmNBOTbCTclmZUeNiFKXcCPWLiFvOIrLjYMpwVxBNuDCyTD8QwmLPGxAY6pgFQNAZHaPqoChprktlqVq76GIRkK%2B5za27qcBwlcAWHjRaZo7RZ6cS8CL7rdrYfyNyCtPxlMJaLM0c5AUZwjDb9IU2lGwQ7aJ53%2FiMf5hyQgCFopyIVAIX%2FbwcK4qAzvwjTm6a8T%2F8i%2BWcuN6rNu1FzIP9fwUYlA1wHD7nKm%2B7EeJndb2FKeJs3CZQbVvZnY24niaSD%2FU1gb6nOxRnb8jNbPfjspo6Q&X-Amz-Signature=64b6b1f4dc019372159ee4e47ac77f90666e75370b244819bb44266364c5c555&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 로컬 실습

### 요구 사항 

- Worker노드 3대 필요
- 각 Worker노드에 빈디스크가 필요

