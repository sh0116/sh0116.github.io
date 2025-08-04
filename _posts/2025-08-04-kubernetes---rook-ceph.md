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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/cbb8b20f-f959-4b43-b1d7-dffd346657f5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VDJEDSBP%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T071433Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCICCfuuNmFevqEvFpazchqNtyru%2BpQbdIlBFaOyLAgzbcAiEAwQ1jRT5Juv1PhELmZUWie6G9XexQoWt1J6rSnogxg7gq%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDLF7RccN%2FNRb2K0RSCrcA760%2BnKEKfs5dobrgQYoE2jE9zzh%2B3daTRFokzdf5ZWHA1TSnQz7sIRlio8Sc3JQ9NIC663PheCFxidCCIzac3vwr7kEQ1qtlryX0xfo%2FlWNVo5Mpa%2FqaYqGD0YZBk8NrQ1PmmD7e5oW0r9iMuruh7C0cRmCJOcfg23BObH4vjszCbcGnlMebKu%2F6HFDanFeEpyR%2BuPV0G7eYepelf%2BPp5O3jufhEIPg2MDqHx611pMqdUn6cfShm83KJFjhmag3a4hmtWdPaoe6Efw7GHwvUGTIveLN8N1451Dsw%2Fdg%2FBaJRqetcIF%2FGZzrVYcfAlwUoSEiZi7Nl194tE70q%2FyxqjbH62zlCFAypsHZoFnhR8c022zts3awDM5agen6Yzf3whAx%2B6YOm8z0RI8H%2FO8IKI04RTgULG%2FBWLzpfbHN5Lk9UmsdX64rbV7vt3uvYctociSxnlX50tJcfpeDyZYhZ%2B8ThZIK%2BiY9Nz%2FPooex6FYNhtZHlwoCJxGZd6Q14MvJ4it4mOdEllXQMyNTHr2xJLFTMpfWOOxe0F0%2FpazLyQdRHf0Ph1i2fQa%2FnA3qZuUEm4gE83EELxNNFMYG19dFJfPk%2Fh%2FAtyfGvlPW9AwCqPQ5dYneb4rVAmUDsTitMKy4wcQGOqUBwcYvZ5XJdXfvJqSho9WUFCSRScHK5ZZCkqEZa7S%2FuN9WRInrBFZx0DtChGVqme5gMTANDqcJ8XsbZWUt2l8B57vsnJrFsYsrw4iWScDoab6%2FmzXfzRMrv35dWh21JlSQE0x1hVK8j%2FNEBOSQkEIB7oEKoYQrWKL8OTkilXvy7YwK8VUbEnexwzOJr3YqZjFwros%2Faz69FBtuRazGDd1VWG31bk8h&X-Amz-Signature=f5dec8b312f255e712d7f8cd8f69093f3c05a8b9bb924feba9363f85f13bb9d8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 로컬 실습

### 요구 사항 

- Worker노드 3대 필요
- 각 Worker노드에 빈디스크가 필요

