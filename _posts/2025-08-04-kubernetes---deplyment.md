---
title: "Kubernetes - Deplyment"
date: 2025-08-04 06:05:00 +0900
categories: [kubernetes]
tags: [Kubernetes]
description: Kubernetes 기초
toc: true
comments: true
---

## Deployment

- Application을 다운 타입 없이 업데이트 가능하도록 도와주는 리소스!
- ReplicaSet과 Replication Controller 상위에 배포되는 리소스
![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/9faef226-8b82-4d03-b75a-857efb7979b8/Untitled.png)

### 업데이트 전략

- recreate 
- Rolling Update :
# Deployment 실습

- Jenkins deployment 생성 - deploy-jenkins
- jenkins deployment로 배포되는 앱을 app : jenkins-test로 레이블링
- deployment로 배포된 pod를 하나 삭제하고 이후 생성되는 포드를 관찰
- 새로 생성된 pod의 레이블을 바꿔 deployment 관리영역에서 벗어나게 하라
- scale명령으로 사용할 replica 수 를 5개로 정의
- edit 기능을 사용하여 10로 스켈일링
### Jenkins deployment 생성 - deploy-jenkins

```yaml
kubectl create -f yaml이름
```

### jenkins deployment로 배포되는 앱을 app : jenkins-test로 레이블링

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: deploy-jenkins
  labels:
    app: jenkins-test
spec:
  replicas: 3
  selector:
    matchLabels:
      app: jenkins-test
  template:
    metadata:
      labels:
        app: jenkins-test
    spec:
      containers:
      - name: jk
        image: jenkins/jenkins
        ports:
        - containerPort: 8080
```

### deployment로 배포된 pod를 하나 삭제하고 이후 생성되는 포드를관찰

```bash
kubectl delete pod pod명
kubectl get pod -w --show-labels
```

### 새로 생성된 pod의 레이블을 바꿔 deployment 관리영역에서 벗어나게 하라

```bash
k label pod deploy-jenkins-69d6b7df8c-mjc2m app-
```

### scale명령으로 사용할 replica 수 를 5개로 정의

```yaml
kubectl scale deploy deploy이름 --replicas=5
```

### edit 기능을 사용하여 10로 스켈일링

```yaml
kubectl edit deploy deploy이름
```

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/162bac64-5cd6-4c19-8588-644a8869155a/Untitled.png)


