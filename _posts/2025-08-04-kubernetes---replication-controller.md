---
title: "Kubernetes - Replication Controller"
date: 2025-08-04 06:05:00 +0900
categories: [kubernetes]
tags: [Kubernetes]
description: Kubernetes 기초
toc: true
comments: true
---

## ReplicaSet & replication controller

- pod 가 항상 실행되도록 유지하는 쿠버네티스 리소스
- 노드가 클러스터에서 사라지는 경우 해당 pod를 감지하고 대체 pod생성
- 실행 중인 pod의 목록을 지속적으로 모니터링으로 하고 ‘유형’ 의 실제 pod수가 원하는 수와 항상 일치하는지 확인
![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/62301a90-6c63-42b4-adb7-d05287ad1abc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YLLKBRDC%2F20250805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250805T061010Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJHMEUCIQDfWOFwC%2B6CaYclT8v%2BuPK7kq5%2BIaFOy0URwn7hcpr7CAIgFyXc7%2FEQSMPohnXzsMm2vSvTytExeJEdvKr%2FMd7LPGYq%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDFu%2BVbTrYCDsi36VIyrcA97kdeOH0RSER70ClTw7z4ZdbSMxfEhr9fqJBM6t%2BPlEeLrlsqgiTsO2Qyvu13HYrVhRJHvNvdDcf6WR53J8DqzfuL5GoB2Pur5rlh59rgUlvA6r5qnUk6TgBlUjm071zEbcZsdshOSAYjywpKOXMNEglTIaBLykmdqFPjLnhCDhwtAN%2Blb4kulM%2BlzaTuq18o8ACPx6%2FmzBQcrKfKCUm2S9yFo%2FqnqgKXt8hYYrblwAz91ouBqKGhcKSGD1DC30yN0Ai4iJb5MFR9pCRV%2Fh7bRlaf16n5KeGgf68r6ugjIARQ2us1pCX3OiAmTULAbizzHNOc4%2BDepVYEat19a%2Fuum6KvayGNUxyU1Vru1%2FHGKriS2JzCWgdvb0%2B%2Frzw%2BtJ5UBIUGY4GwR7j1oaXWrNfBhg%2FAoBxF7D1DtIWXFcn7Mrvn2D4dEgzEyIueb2cRR23xAkzdiH%2B1zrXWv2ix4C2n2uNEOpHdHHNEPnd0urndNnk5C316yDQJrj6QvrYhfBwGmmmToq3E9rF1OIsdUcPOJ0EEEejhXT7AEVPTKH6vXCki7weLfu3NVwhZ%2FcUknTg9YujvHSe3od2YMueG9DaxdTbVUomQTmotgpkAO4AzsOYIY9SgcycjWBEVSVMJu0xsQGOqUBzYxVczgJcpEmPdM%2FA2vQQU6MFai9PMdQXJRkw2aO4kGZnAHzEcZ3POytOwun1yM55PuaNrCEN2QwDArddtLq40fwuy1G8IRDIaIHjy6xJzQRQunJpXkzMQzVx%2BfpAPpym%2BhSaURZCLwAAonJeUKarfmudHYEz2OX%2BDh0Dfj0HuqE3QdUqworjns%2FXPn0ZQ8p78AIXqAWUIJdlyKs31wC8wmmF%2Fpe&X-Amz-Signature=265924be41564283e9826ee22d66d0bfd1fefc2293d1a4a8fc0edece59a148d9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

 

## replication controller 세가지 요소

- 관리하는 pod범위를 결정하는 레이블 셀렉터
- 실행해야하는 pod의 수를 결정하는 복제본 수
- 새로운 pod의 모양을 설명하는 pod템플릿
## replication controller 장점 

- pod가 없는 경우 새 pod 항상 실행
- 노드에 장애 발생 시 다른 노드에 복제본 생성
- 수동, 자동으로 수평 스케일
## replication controller YAML 작성

```yaml
apiVersion: v1
kind: ReplicationController
metadata:
  name: nginx
spec:
  replicas: 3
  selector:
    app: nginx
  template:
    metadata:
      name: nginx
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx
        ports:
        - containerPort: 80
```

## replication controller 조회

```bash
kubectl get  rc #replicationcontrolle 줄임
```

```bash
kubectl describe rc rc이름 #상세 정보 확인 (이벤트 로그 확인 가능)
```

## replication controller 수정

```bash
kubectl scale rc rc이름 --replicas=5 # replica를 5로 늘리는 수정

kubectl edit rc rc이름 # 설정 파일 수정 가능 (vim형태)
```

## replication controller 삭제

```bash
kubectl delete rc rc이름 # rc삭제
kubectl delete rc rc이름 --cascade=false # 실행된 pod는 유지 rc는 삭제
```

## replication controller node 장애 

- 여러 노드에 분산 배치된 pod가 있을 때 만약 한 노드에서 장애가 발생하면 
![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/5734a11c-7eb9-439a-94e2-3aa375662766/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YLLKBRDC%2F20250805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250805T061010Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJHMEUCIQDfWOFwC%2B6CaYclT8v%2BuPK7kq5%2BIaFOy0URwn7hcpr7CAIgFyXc7%2FEQSMPohnXzsMm2vSvTytExeJEdvKr%2FMd7LPGYq%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDFu%2BVbTrYCDsi36VIyrcA97kdeOH0RSER70ClTw7z4ZdbSMxfEhr9fqJBM6t%2BPlEeLrlsqgiTsO2Qyvu13HYrVhRJHvNvdDcf6WR53J8DqzfuL5GoB2Pur5rlh59rgUlvA6r5qnUk6TgBlUjm071zEbcZsdshOSAYjywpKOXMNEglTIaBLykmdqFPjLnhCDhwtAN%2Blb4kulM%2BlzaTuq18o8ACPx6%2FmzBQcrKfKCUm2S9yFo%2FqnqgKXt8hYYrblwAz91ouBqKGhcKSGD1DC30yN0Ai4iJb5MFR9pCRV%2Fh7bRlaf16n5KeGgf68r6ugjIARQ2us1pCX3OiAmTULAbizzHNOc4%2BDepVYEat19a%2Fuum6KvayGNUxyU1Vru1%2FHGKriS2JzCWgdvb0%2B%2Frzw%2BtJ5UBIUGY4GwR7j1oaXWrNfBhg%2FAoBxF7D1DtIWXFcn7Mrvn2D4dEgzEyIueb2cRR23xAkzdiH%2B1zrXWv2ix4C2n2uNEOpHdHHNEPnd0urndNnk5C316yDQJrj6QvrYhfBwGmmmToq3E9rF1OIsdUcPOJ0EEEejhXT7AEVPTKH6vXCki7weLfu3NVwhZ%2FcUknTg9YujvHSe3od2YMueG9DaxdTbVUomQTmotgpkAO4AzsOYIY9SgcycjWBEVSVMJu0xsQGOqUBzYxVczgJcpEmPdM%2FA2vQQU6MFai9PMdQXJRkw2aO4kGZnAHzEcZ3POytOwun1yM55PuaNrCEN2QwDArddtLq40fwuy1G8IRDIaIHjy6xJzQRQunJpXkzMQzVx%2BfpAPpym%2BhSaURZCLwAAonJeUKarfmudHYEz2OX%2BDh0Dfj0HuqE3QdUqworjns%2FXPn0ZQ8p78AIXqAWUIJdlyKs31wC8wmmF%2Fpe&X-Amz-Signature=32138674e592525a173551931a78e4f42c9b1d57fbb5837f85fba0dc128b7f90&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


