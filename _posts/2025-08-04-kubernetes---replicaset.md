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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/35742fe6-0f6d-41c3-a55c-0af6e8de2e29/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663C43W6ZK%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T072215Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJGMEQCICItVpu1%2B3SIgbwVpe3n%2BEhcGrtFXnx5sbsuhlUzkh5IAiAFWNt3S06RXcwYXgIZCgxe729qjsHpe4CXGXqWUpA61Sr%2FAwhAEAAaDDYzNzQyMzE4MzgwNSIMvkrm42mIRpjDTNiOKtwDy0xbY%2B5%2FSjZ3lNtjgOj7ts23nWqWHsceRpap2n2AEBNZGIQ20SjjaLQRNgn0brHPNC2UF9RMyVY6vLGmCDVY8RYFxaXPS3z2MYU%2FeQSNIebrBHdwUdbpWFYaL5VwJ0SH7T9H7jWckHdrfOZb6fZ%2FLmg5Givdr6P6Nk8Q%2BzmHsZGRj%2Bqyx0%2F2bafiYfXkJbbQZBA3hx9a9mM4p6o9oX9wtimDpZuKNEUSClt6r1LItDIEYBfzQh2mPeNlvM8vILESqTS5%2BRecHZNqZMqvKxCfS6i5CvABKpo1Pc5J7aC8cgF4QlwX8iYWpL%2BPZqPAniJcnq1H67AdrLofhGRIbSzJnU6oflw1iKq9gKwfB%2BsOxl8hZaKHEed19qmXwPRvXg4w%2BTV4kMnH7OTbplq%2B7XtnOkhukkc7q0rNmIEERloTYwIxwcVK76sQzk7xgSoKdgsdvmUPwRiTY5R7xeDOrUhyAuHm01DiH2ftgC9uOe1YvJVeZyLgiISh%2BAzJTKLaREudVnn4FRX9P6VnOyPLe%2FhNyg0kea%2F5hVwPCfv5eLqKeqBefm8KHeVHLf4231kdf%2FkUwsXOED%2FaGgR5SS31CyNk9ajoHQ5fac%2BmNzfONZZF6vbBv2hZVoLumV6RA90wprjBxAY6pgGto%2Fmxbmdqw6Lrxh1alrqJru8JTR4QUY6mioVoNPC4RFy%2FRJnRy0EAclRLHFVUm49TgScOELUESO3JIBDcIl9BWpoM1gf9f6nQ0PQHUtiVDVz9N9weZr4pClKkLK3gK8DhJDgS3UZSoWJoLvcP48DvCt1E7Op2VgRhhvWU9f3SEHdRgqL3KOeXmDa4hLHcm50JCx%2B7TY0XRRzY%2Fgpu%2B5mShlKYLqPm&X-Amz-Signature=4d1ea5ffd4bbfbe1da38f4209ab65a66335d0e953be11e403af94dc7085702a0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## ReplicaSet 생성

replication 보다 업그레이드되었고 metchExp를 추가하여 label 조건에 더 자유롭

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/e26579b4-01e4-429e-98f4-7aa4d0e3495d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663C43W6ZK%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T072215Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJGMEQCICItVpu1%2B3SIgbwVpe3n%2BEhcGrtFXnx5sbsuhlUzkh5IAiAFWNt3S06RXcwYXgIZCgxe729qjsHpe4CXGXqWUpA61Sr%2FAwhAEAAaDDYzNzQyMzE4MzgwNSIMvkrm42mIRpjDTNiOKtwDy0xbY%2B5%2FSjZ3lNtjgOj7ts23nWqWHsceRpap2n2AEBNZGIQ20SjjaLQRNgn0brHPNC2UF9RMyVY6vLGmCDVY8RYFxaXPS3z2MYU%2FeQSNIebrBHdwUdbpWFYaL5VwJ0SH7T9H7jWckHdrfOZb6fZ%2FLmg5Givdr6P6Nk8Q%2BzmHsZGRj%2Bqyx0%2F2bafiYfXkJbbQZBA3hx9a9mM4p6o9oX9wtimDpZuKNEUSClt6r1LItDIEYBfzQh2mPeNlvM8vILESqTS5%2BRecHZNqZMqvKxCfS6i5CvABKpo1Pc5J7aC8cgF4QlwX8iYWpL%2BPZqPAniJcnq1H67AdrLofhGRIbSzJnU6oflw1iKq9gKwfB%2BsOxl8hZaKHEed19qmXwPRvXg4w%2BTV4kMnH7OTbplq%2B7XtnOkhukkc7q0rNmIEERloTYwIxwcVK76sQzk7xgSoKdgsdvmUPwRiTY5R7xeDOrUhyAuHm01DiH2ftgC9uOe1YvJVeZyLgiISh%2BAzJTKLaREudVnn4FRX9P6VnOyPLe%2FhNyg0kea%2F5hVwPCfv5eLqKeqBefm8KHeVHLf4231kdf%2FkUwsXOED%2FaGgR5SS31CyNk9ajoHQ5fac%2BmNzfONZZF6vbBv2hZVoLumV6RA90wprjBxAY6pgGto%2Fmxbmdqw6Lrxh1alrqJru8JTR4QUY6mioVoNPC4RFy%2FRJnRy0EAclRLHFVUm49TgScOELUESO3JIBDcIl9BWpoM1gf9f6nQ0PQHUtiVDVz9N9weZr4pClKkLK3gK8DhJDgS3UZSoWJoLvcP48DvCt1E7Op2VgRhhvWU9f3SEHdRgqL3KOeXmDa4hLHcm50JCx%2B7TY0XRRzY%2Fgpu%2B5mShlKYLqPm&X-Amz-Signature=3356947fd803c7ad94c6cd7fc260321828386c0d2189f97d0fbda1482d0f9b2d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/c60f5b28-6cbb-4a8f-914e-b940a64e304d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663C43W6ZK%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T072215Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJGMEQCICItVpu1%2B3SIgbwVpe3n%2BEhcGrtFXnx5sbsuhlUzkh5IAiAFWNt3S06RXcwYXgIZCgxe729qjsHpe4CXGXqWUpA61Sr%2FAwhAEAAaDDYzNzQyMzE4MzgwNSIMvkrm42mIRpjDTNiOKtwDy0xbY%2B5%2FSjZ3lNtjgOj7ts23nWqWHsceRpap2n2AEBNZGIQ20SjjaLQRNgn0brHPNC2UF9RMyVY6vLGmCDVY8RYFxaXPS3z2MYU%2FeQSNIebrBHdwUdbpWFYaL5VwJ0SH7T9H7jWckHdrfOZb6fZ%2FLmg5Givdr6P6Nk8Q%2BzmHsZGRj%2Bqyx0%2F2bafiYfXkJbbQZBA3hx9a9mM4p6o9oX9wtimDpZuKNEUSClt6r1LItDIEYBfzQh2mPeNlvM8vILESqTS5%2BRecHZNqZMqvKxCfS6i5CvABKpo1Pc5J7aC8cgF4QlwX8iYWpL%2BPZqPAniJcnq1H67AdrLofhGRIbSzJnU6oflw1iKq9gKwfB%2BsOxl8hZaKHEed19qmXwPRvXg4w%2BTV4kMnH7OTbplq%2B7XtnOkhukkc7q0rNmIEERloTYwIxwcVK76sQzk7xgSoKdgsdvmUPwRiTY5R7xeDOrUhyAuHm01DiH2ftgC9uOe1YvJVeZyLgiISh%2BAzJTKLaREudVnn4FRX9P6VnOyPLe%2FhNyg0kea%2F5hVwPCfv5eLqKeqBefm8KHeVHLf4231kdf%2FkUwsXOED%2FaGgR5SS31CyNk9ajoHQ5fac%2BmNzfONZZF6vbBv2hZVoLumV6RA90wprjBxAY6pgGto%2Fmxbmdqw6Lrxh1alrqJru8JTR4QUY6mioVoNPC4RFy%2FRJnRy0EAclRLHFVUm49TgScOELUESO3JIBDcIl9BWpoM1gf9f6nQ0PQHUtiVDVz9N9weZr4pClKkLK3gK8DhJDgS3UZSoWJoLvcP48DvCt1E7Op2VgRhhvWU9f3SEHdRgqL3KOeXmDa4hLHcm50JCx%2B7TY0XRRzY%2Fgpu%2B5mShlKYLqPm&X-Amz-Signature=b32e58487e129e538fbc42c5c72b3b3f79e603883e663cd299c98a0bb3d62181&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


