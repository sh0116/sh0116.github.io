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
![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/62301a90-6c63-42b4-adb7-d05287ad1abc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664EKON5QX%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T064906Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJGMEQCIBLfSTlfYQ0fXX9EXdLMHZCw%2BGW3RWv80UrhbXNtYcqCAiBAck88WLsMQinBEm%2B6PZ0P6wxM7HbCU5a8LLPHbIPEHyr%2FAwg%2FEAAaDDYzNzQyMzE4MzgwNSIMowZ3dUDwMufikreCKtwDcGVndNjBy1usIr75OKoeW4zeZDo15A%2BW6%2FHBxGpvZ5JcFaF63bECAJN3tDroQHUKmcYiMvDnS4Q6olkDp1tAVyfw920e3uEecXkAjBLIegvsCXSxomUh9o%2BT%2FTR%2FAWUdrEYPuXRtT7zTnam2Nz3Vl1%2BFGzhxrLMZIg%2BU%2BDJP%2BPqAIFOstSdaPkBkan3xi1yML71EjmnjK0N5IHt4bq65Hxl7dYPoO3fkyFTKm75zEc66KuDAfX2jfR6Z83%2BpBGk5lp%2FmFTgJgHlQFjDn1AhJpdQAF09cUdrNLRcePiK0aq%2BopkrgT9wsZ1FLcyPG0eh1GuJbnBsYyfqXDjAC4eep67xVb%2BjAX8Pq5AmRKHVfHJe6oK1rKEjaA21AYeorJyWfJWwlH62Dydl6vw%2Bmh5U1ZTQ274CXpHxelDVK9MvFRu2sFaXZhq3Sduv7eDRPYi0wZtOxIv5AzafpAVA65LojFBMwkJYwF%2BcodnuRzLYVnjgJWncycBburxpKNW7RvqAwwyB2AV%2FOUgKj3ZGkJG4r9BxBIpwp2Au8NU6r%2BP8Qr2uAhK14YSRfHEgByY%2FtL%2F1UDov%2BsUYVwINKeFA5JgBXzn3XhVtbjWC4XoYNgpoqESGTnAAupSR8RAcg3how5I3BxAY6pgHYNLqdb%2BG0Sixbfo%2BZ%2BPLEsqTUEjp3rv0aEX588wx8SOHriOTxLNCt6k6OId%2F5qlxknl1GI7G0y5jkiwyUb56s2BMEENRahP0G6oV7Of1U73ff7XksUsiY4j3sGLEuVarpI3DDmVQugj6Yc35WZEZqAv9IKs79GE4zoy%2BKE7mhiOTx%2B2iSzeYhlIeM4MjX384XqSFecChUIDzG1h7tBri8eohwAfMI&X-Amz-Signature=bd42b8ce6d7abae443bca8ae7db0a9e652d7be8cfc5f6f8c3b178d19f33da58d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

 

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
![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/5734a11c-7eb9-439a-94e2-3aa375662766/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664EKON5QX%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T064907Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJGMEQCIBLfSTlfYQ0fXX9EXdLMHZCw%2BGW3RWv80UrhbXNtYcqCAiBAck88WLsMQinBEm%2B6PZ0P6wxM7HbCU5a8LLPHbIPEHyr%2FAwg%2FEAAaDDYzNzQyMzE4MzgwNSIMowZ3dUDwMufikreCKtwDcGVndNjBy1usIr75OKoeW4zeZDo15A%2BW6%2FHBxGpvZ5JcFaF63bECAJN3tDroQHUKmcYiMvDnS4Q6olkDp1tAVyfw920e3uEecXkAjBLIegvsCXSxomUh9o%2BT%2FTR%2FAWUdrEYPuXRtT7zTnam2Nz3Vl1%2BFGzhxrLMZIg%2BU%2BDJP%2BPqAIFOstSdaPkBkan3xi1yML71EjmnjK0N5IHt4bq65Hxl7dYPoO3fkyFTKm75zEc66KuDAfX2jfR6Z83%2BpBGk5lp%2FmFTgJgHlQFjDn1AhJpdQAF09cUdrNLRcePiK0aq%2BopkrgT9wsZ1FLcyPG0eh1GuJbnBsYyfqXDjAC4eep67xVb%2BjAX8Pq5AmRKHVfHJe6oK1rKEjaA21AYeorJyWfJWwlH62Dydl6vw%2Bmh5U1ZTQ274CXpHxelDVK9MvFRu2sFaXZhq3Sduv7eDRPYi0wZtOxIv5AzafpAVA65LojFBMwkJYwF%2BcodnuRzLYVnjgJWncycBburxpKNW7RvqAwwyB2AV%2FOUgKj3ZGkJG4r9BxBIpwp2Au8NU6r%2BP8Qr2uAhK14YSRfHEgByY%2FtL%2F1UDov%2BsUYVwINKeFA5JgBXzn3XhVtbjWC4XoYNgpoqESGTnAAupSR8RAcg3how5I3BxAY6pgHYNLqdb%2BG0Sixbfo%2BZ%2BPLEsqTUEjp3rv0aEX588wx8SOHriOTxLNCt6k6OId%2F5qlxknl1GI7G0y5jkiwyUb56s2BMEENRahP0G6oV7Of1U73ff7XksUsiY4j3sGLEuVarpI3DDmVQugj6Yc35WZEZqAv9IKs79GE4zoy%2BKE7mhiOTx%2B2iSzeYhlIeM4MjX384XqSFecChUIDzG1h7tBri8eohwAfMI&X-Amz-Signature=0399ff56101966997ad6fdb0f3a2200bb10ac289f61883bd378d730f0a6a5a20&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


