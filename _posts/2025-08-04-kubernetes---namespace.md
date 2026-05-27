---
title: "Kubernetes - NameSpace"
date: 2025-08-04 06:05:00 +0900
categories: [kubernetes]
tags: [Kubernetes]
description: Kubernetes 기초
toc: true
comments: true
---

# NameSpace

- 리소스를 각각의 분리된 영역으로 나누기 좋은 방법
- 여러 네임스페이스를 사용하면 복잡한 쿠버네티스 시스템을 더 작은 그룹으로 분할
- 멀티 테넌트(multi-tenant) 환경을 분리하여 리소스를 생산, 개발, QA환경 등으로 사용
- 리소스 이름은 네임스페이스 내에서만 고유 명칭 사용
```yaml
kubectl get namespace
kubectl get ns
```

# Namespace 생성

```yaml
kubectl create ns ns이름 --dry-run -o yaml > yaml파일 이름
# yaml수정 
kubectl create -f yaml파일 이름
```

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/7c11461c-1127-4433-ab12-5e84b3fcecaf/Untitled.png)

# NameSpace 연습문제

- 현재 시스템에는 몇 개의 Namespace가 존재하는가?
- Kube-system에는 몇 개의 포드가 존재하는가?
- ns-jenkins 네임스페이스를 생성하고 jenkins포드를 배치하라
- coredns 는 어는 네임스페이스에 속해있는가?

