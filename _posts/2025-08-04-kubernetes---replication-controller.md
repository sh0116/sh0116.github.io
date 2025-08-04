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
![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/62301a90-6c63-42b4-adb7-d05287ad1abc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665UAG5TCZ%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T072026Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJIMEYCIQCLrGF5vqd2CBZ67oX%2F7AUm9Yy3gGsPmcijGCYGE%2BfikwIhAIRKtHJ8i1BlJ6Olj0zNW6WH8Y9hUFpYY8XPrvc2vCMYKv8DCEAQABoMNjM3NDIzMTgzODA1Igz1%2FBgZFG3OeiPQqz0q3AMP5IpdpQc%2FvtzzMJTSRtI13n6ZOzC1iELnghiY5zWAtyunT42ZS9519vCrMPcr5MJg5Qj7e1rjftScFIUa3yPslOffsuQN4D%2BfHHdzihLPZbtxGvg06bCK8YWlpW2CRYKE5EqPjBQl%2BEjnNXZUCLhCi2uqWdmGFOqZg1gRcXn2qCv3GhTH%2BADDix82wSkHFzpE4R2DoRDRIVFMncRxKRhFz%2Bp4w%2BTtD8q0Bp%2BWsx7jzwmV5AhWmBqfYLXHfC6ZSyWyp7khYl1mPUKxJWMj73c2zZAp57%2F1K45s6qpo6FWffQ1OSppuItIih16ZuUOrfDQKMwWMjwxtPWqupWoNNg2kJV7LCKvmRQ%2F6Oyykq58Q2eCzjGfsVUW0WnqZ%2B6XHKZfPKNMsE0YjMHCCUzsF0F5Y1bDXPLzvzfa9X8vOM50lOY1YwSvzYSY8%2BPYBswkBqrkogX1LU%2B4Djn8iYxt9E5LjAx2dkbEtR7WHmRlhwTybi6OI5dwZiUv0s1x7HOWqRP3whqP1dL5LrRbV%2BRv2c5jkOBNjNloQ1MUAPWoSNifIyILmgdGPS86T%2BIv5i%2Bd%2B9PXP9J%2FvOe5CcyDrxmgYEXVLm5GJqdfJdHGcn%2B9L6K%2BbwSNWBDeTJq4E6KuWtTC5tsHEBjqkAUq061R1%2BY1gFG5DgkHwy9hM0VQfy8bmYdDGc%2B3yCOnKBAv4p%2FS%2BDx6YOkvhe2Mwvk1QKcfzxd%2B07SZ5AJwc9JIYutnITB9%2B33SWQPGso235dkuKZNKwicgZ8onsrqY%2BI8qy8B%2BPrqxk%2Fys8xHRBcxexxtFOB9zalZ98mWrrBORKmjbXpTeQVK6MLIzAZ2J8txl%2FKihsimy9UX4v5Q8r2kvPW%2BhL&X-Amz-Signature=42720d73b70690abd6d8817f6128fdace7fc847ddce691780c055d6c4104ad58&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

 

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
![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/5734a11c-7eb9-439a-94e2-3aa375662766/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665UAG5TCZ%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T072026Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJIMEYCIQCLrGF5vqd2CBZ67oX%2F7AUm9Yy3gGsPmcijGCYGE%2BfikwIhAIRKtHJ8i1BlJ6Olj0zNW6WH8Y9hUFpYY8XPrvc2vCMYKv8DCEAQABoMNjM3NDIzMTgzODA1Igz1%2FBgZFG3OeiPQqz0q3AMP5IpdpQc%2FvtzzMJTSRtI13n6ZOzC1iELnghiY5zWAtyunT42ZS9519vCrMPcr5MJg5Qj7e1rjftScFIUa3yPslOffsuQN4D%2BfHHdzihLPZbtxGvg06bCK8YWlpW2CRYKE5EqPjBQl%2BEjnNXZUCLhCi2uqWdmGFOqZg1gRcXn2qCv3GhTH%2BADDix82wSkHFzpE4R2DoRDRIVFMncRxKRhFz%2Bp4w%2BTtD8q0Bp%2BWsx7jzwmV5AhWmBqfYLXHfC6ZSyWyp7khYl1mPUKxJWMj73c2zZAp57%2F1K45s6qpo6FWffQ1OSppuItIih16ZuUOrfDQKMwWMjwxtPWqupWoNNg2kJV7LCKvmRQ%2F6Oyykq58Q2eCzjGfsVUW0WnqZ%2B6XHKZfPKNMsE0YjMHCCUzsF0F5Y1bDXPLzvzfa9X8vOM50lOY1YwSvzYSY8%2BPYBswkBqrkogX1LU%2B4Djn8iYxt9E5LjAx2dkbEtR7WHmRlhwTybi6OI5dwZiUv0s1x7HOWqRP3whqP1dL5LrRbV%2BRv2c5jkOBNjNloQ1MUAPWoSNifIyILmgdGPS86T%2BIv5i%2Bd%2B9PXP9J%2FvOe5CcyDrxmgYEXVLm5GJqdfJdHGcn%2B9L6K%2BbwSNWBDeTJq4E6KuWtTC5tsHEBjqkAUq061R1%2BY1gFG5DgkHwy9hM0VQfy8bmYdDGc%2B3yCOnKBAv4p%2FS%2BDx6YOkvhe2Mwvk1QKcfzxd%2B07SZ5AJwc9JIYutnITB9%2B33SWQPGso235dkuKZNKwicgZ8onsrqY%2BI8qy8B%2BPrqxk%2Fys8xHRBcxexxtFOB9zalZ98mWrrBORKmjbXpTeQVK6MLIzAZ2J8txl%2FKihsimy9UX4v5Q8r2kvPW%2BhL&X-Amz-Signature=909b010da9bae9d60a48fccd6c74c5cbdbd0c9ff08375329694fe0f21c9cb6db&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


