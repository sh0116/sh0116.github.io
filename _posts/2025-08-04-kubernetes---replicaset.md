---
title: "Kubernetes - ReplicaSet"
date: 2025-08-04 06:05:00 +0900
categories: [kubernetes]
tags: [Kubernetes]
description: Kubernetes 기초
toc: true
comments: true
---

# ReplicaSet

- ReplicaSet은 차세대 Replication Controller로 완전히 대체 가능함
- 초기 쿠버네티스에서 제공했기 때문에 현장에서는 여전히 계속 사용중인 경우 존재
- 일반적으로 ReplicaSet을 직접 생성하지 않고 상위 수준의 Deployment 리소스를 만들 때 자동으로 생성
## ReplicatSet & Replication Controller 차이점

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/35742fe6-0f6d-41c3-a55c-0af6e8de2e29/Untitled.png)

## ReplicaSet 생성

replication 보다 업그레이드되었고 metchExp를 추가하여 label 조건에 더 자유롭

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/e26579b4-01e4-429e-98f4-7aa4d0e3495d/Untitled.png)

# ReplicaSet 실습

- nginx 3개를 생성하는 rs-nginx 생성하라
- rs-nginx pod의 개수를 10개로 스케일링하라
### nginx 3개를 생성하는 rs-nginx 생성하라

```yaml
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: rs-nginx
spec:
  # modify replicas according to your case
  replicas: 3
  selector:
    matchLabels:
      app: replica
  template:
    metadata:
      labels:
        app: replica
    spec:
      containers:
      - name: rs-nginx
        image: nginx
```

```yaml
kubectl creat -f yaml이름
```

### rs-nginx pod의 개수를 10개로 스케일링하라

```yaml
kubectl edit rs rs이름
```

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/c60f5b28-6cbb-4a8f-914e-b940a64e304d/Untitled.png)


