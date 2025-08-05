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
![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/9faef226-8b82-4d03-b75a-857efb7979b8/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UMWMZJFI%2F20250805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250805T002752Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJHMEUCIQCJLSXS%2Fd04xrSCS3QLB6TawKxDZ0l4GWq1Lkj%2B3Kcf%2BgIgMz1yRe8a1YMBiRH2fMDZGkXmQ8g8MWOAigjfJ3Yj6U4q%2FwMIUBAAGgw2Mzc0MjMxODM4MDUiDL98BTVZMFl%2F2M9RZyrcAxvpzdCcMpNbQX5jYXIGhgnqNjJtWp9dS7GsT7eBdqzbsGNynK%2FZkWcSQwWFMtHQiUEAo1tOPd9Vjc3PM9HsqUTcvWnktHBawtFoSTcWmwdUu8c%2FU2%2BQvwEq8soJHGDRG6U8Lx0f%2BR1dm3%2BvsE1V6ejkqx5uyCFT64FifQp1GJLNo7gn2c%2BqgrVq8d0D%2FpDJjO65tkRsohuBX3E6HpMPGIhx2Zc%2Bwd%2F1R6kmdGDD%2Fq2hhPr7giAEYgOg189hctffLf0TOylIcD8hWVNugJkigIjvSjfOECIQ7SHKyRDvDkrYYzHGMBwVvN%2BswxGFyaaUF6GouTQag3POKylqB4Bu7ZdN8bxyQbjIYq3gmiSgyAIMthDHlkUHbHCEFio9MNNlpZ22XL%2FCX5mzThn%2BKyUXxjW7rPbZ%2FsNQqegt35sYPq05c2ne8OzCJI1JaOHC8DBHEL%2FiA0k8JBbARDzId2XK17K48yqVaJTxOgcbD4bq9kg91ZoCd5MBBAIB8bVmLEEyfDuY%2FZU3nXkO8FBy%2Fk850a8%2FUR9IioSjBY5ziiiS%2BX1PH1nRyoG2KcFcJsXLL4rgbE6SdiOZMvFMCbJ%2FuIjyRG3WoIkKl6XRucUbkQvvQC%2BZ%2BTCnLWzourF%2BP9a6MPbzxMQGOqUBWsrcdvr7zOAyLNK3LgtDtO90NYLowvQvDc9zT50ekfI9AGQsbz7XyUWPl0qXMMStPPLvb75MDiMfSLWgXCaD39Cvv9%2Fsj1T6tXZCp4qeKi%2Ff8jdCzEOxSDHyfQSa%2FoTXmivCtMdEMCQiASEYEkCRdKtZTYuTkuBmkODp1z5UvMW9xmNcKxGrkByNt9MnQiDKsaKBLvZWdbWk58IWVFqSfE6elA3v&X-Amz-Signature=f22e6da20c232ae6a7b8ae95a2d184852c192d505d7183ef6b6f78f9a2e5f20d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/162bac64-5cd6-4c19-8588-644a8869155a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UMWMZJFI%2F20250805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250805T002753Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJHMEUCIQCJLSXS%2Fd04xrSCS3QLB6TawKxDZ0l4GWq1Lkj%2B3Kcf%2BgIgMz1yRe8a1YMBiRH2fMDZGkXmQ8g8MWOAigjfJ3Yj6U4q%2FwMIUBAAGgw2Mzc0MjMxODM4MDUiDL98BTVZMFl%2F2M9RZyrcAxvpzdCcMpNbQX5jYXIGhgnqNjJtWp9dS7GsT7eBdqzbsGNynK%2FZkWcSQwWFMtHQiUEAo1tOPd9Vjc3PM9HsqUTcvWnktHBawtFoSTcWmwdUu8c%2FU2%2BQvwEq8soJHGDRG6U8Lx0f%2BR1dm3%2BvsE1V6ejkqx5uyCFT64FifQp1GJLNo7gn2c%2BqgrVq8d0D%2FpDJjO65tkRsohuBX3E6HpMPGIhx2Zc%2Bwd%2F1R6kmdGDD%2Fq2hhPr7giAEYgOg189hctffLf0TOylIcD8hWVNugJkigIjvSjfOECIQ7SHKyRDvDkrYYzHGMBwVvN%2BswxGFyaaUF6GouTQag3POKylqB4Bu7ZdN8bxyQbjIYq3gmiSgyAIMthDHlkUHbHCEFio9MNNlpZ22XL%2FCX5mzThn%2BKyUXxjW7rPbZ%2FsNQqegt35sYPq05c2ne8OzCJI1JaOHC8DBHEL%2FiA0k8JBbARDzId2XK17K48yqVaJTxOgcbD4bq9kg91ZoCd5MBBAIB8bVmLEEyfDuY%2FZU3nXkO8FBy%2Fk850a8%2FUR9IioSjBY5ziiiS%2BX1PH1nRyoG2KcFcJsXLL4rgbE6SdiOZMvFMCbJ%2FuIjyRG3WoIkKl6XRucUbkQvvQC%2BZ%2BTCnLWzourF%2BP9a6MPbzxMQGOqUBWsrcdvr7zOAyLNK3LgtDtO90NYLowvQvDc9zT50ekfI9AGQsbz7XyUWPl0qXMMStPPLvb75MDiMfSLWgXCaD39Cvv9%2Fsj1T6tXZCp4qeKi%2Ff8jdCzEOxSDHyfQSa%2FoTXmivCtMdEMCQiASEYEkCRdKtZTYuTkuBmkODp1z5UvMW9xmNcKxGrkByNt9MnQiDKsaKBLvZWdbWk58IWVFqSfE6elA3v&X-Amz-Signature=40c1d9c4ed50a359bde61334c0616e70d7633271807f7ba07f0c02047ae92cc8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


