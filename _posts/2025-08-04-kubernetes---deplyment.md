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
![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/9faef226-8b82-4d03-b75a-857efb7979b8/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2CE72WG%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T071448Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJIMEYCIQCPIWhZR0HyLFKYr2wS0KcqCxx1cW%2BoiiZD3zOHCb1RmgIhALDGSEAQuDvFuCfT40m4iY1WtnH2yXj%2BJtsvpPaqTjtvKv8DCEAQABoMNjM3NDIzMTgzODA1IgzjR0PwgZHLASZLBPwq3ANrQbTrX1Rx%2Fcaymr1f1pMLJWhip6etPRQWPWwHvSpufANv88sCfZJ7Uao6BzBOIUWFF25w5ZgGw9Nytzg12o0m8UpOz57f1amlFDyB8Xo6BxIBfHJPRPnRMD7h4tf%2BUdSKYNznLlVPLQG4UqeVq4Q5fxW%2Bw2mVamCVJQ1BgCZzLQW91bcxk7oIqePqLbOCbIyuy8XzvDt0zdptm%2BOGTDufRaf1Yr9ixKp2GbhQSiUjQbzd4wWCpRrWLXrt3jmgo%2F8CLR6nGj6CjH27dFtjgZgUgf%2Bm6SAYE%2BE2VyRFK4Y%2BHqzn8%2F77fxiOUu2qkveFyMDWuGIMaTOp6fyNnHrpevCxhcobPvH0DogVvluRqMQHzh0HiP90%2FNh5syl7M6QvdA%2Fie5E%2B6UAPNeJV8%2FOrla2%2BOUg1SEiqDV%2B8b%2ByJeXVvZRucGTfcNRauXjJ0diNcsIZgDIyFlzuLXdMTy9p%2BJU7wZnu4s5MhR5qtqIKIqBvyN602yztKihfaR%2B3J18hzkqtKMY7dvPtFnvm40l00Wcb%2BX%2FP1EpbshkxZSm42U8E6pe6CKf%2F%2BL5KU4LRj3eMLRq7ioZTd5TWvX8%2FODqClAqXkZepuxyhXBGDiDpp4MUdr9uCHYFKGXi2ZzReA%2FzDOtsHEBjqkAdbE64XrprGuJuhRA6FAuu%2B74sP%2FgEDMgVJDU%2B432ZlXRfDi59Igmtd3fM%2BI4S%2BdWY%2BKUMpY2kVWr11EFAhjhuy2wUQbnvIjoFeyO1%2Bpv57k1vWwcotxZZTSKo%2FjXL0tBl98qHe2H1yhIHGweh8pFxUq95z7jO0WN5A1LMEYHKD1N8WzLhYkdExNN6zT7YzjHtIuKxKJvUMf6hJ5WJ0fK%2BEQrTFQ&X-Amz-Signature=fab8138c68c05a04c61b318d9782dbea62633956821570de448f6ed5677bf79b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/162bac64-5cd6-4c19-8588-644a8869155a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2CE72WG%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T071448Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJIMEYCIQCPIWhZR0HyLFKYr2wS0KcqCxx1cW%2BoiiZD3zOHCb1RmgIhALDGSEAQuDvFuCfT40m4iY1WtnH2yXj%2BJtsvpPaqTjtvKv8DCEAQABoMNjM3NDIzMTgzODA1IgzjR0PwgZHLASZLBPwq3ANrQbTrX1Rx%2Fcaymr1f1pMLJWhip6etPRQWPWwHvSpufANv88sCfZJ7Uao6BzBOIUWFF25w5ZgGw9Nytzg12o0m8UpOz57f1amlFDyB8Xo6BxIBfHJPRPnRMD7h4tf%2BUdSKYNznLlVPLQG4UqeVq4Q5fxW%2Bw2mVamCVJQ1BgCZzLQW91bcxk7oIqePqLbOCbIyuy8XzvDt0zdptm%2BOGTDufRaf1Yr9ixKp2GbhQSiUjQbzd4wWCpRrWLXrt3jmgo%2F8CLR6nGj6CjH27dFtjgZgUgf%2Bm6SAYE%2BE2VyRFK4Y%2BHqzn8%2F77fxiOUu2qkveFyMDWuGIMaTOp6fyNnHrpevCxhcobPvH0DogVvluRqMQHzh0HiP90%2FNh5syl7M6QvdA%2Fie5E%2B6UAPNeJV8%2FOrla2%2BOUg1SEiqDV%2B8b%2ByJeXVvZRucGTfcNRauXjJ0diNcsIZgDIyFlzuLXdMTy9p%2BJU7wZnu4s5MhR5qtqIKIqBvyN602yztKihfaR%2B3J18hzkqtKMY7dvPtFnvm40l00Wcb%2BX%2FP1EpbshkxZSm42U8E6pe6CKf%2F%2BL5KU4LRj3eMLRq7ioZTd5TWvX8%2FODqClAqXkZepuxyhXBGDiDpp4MUdr9uCHYFKGXi2ZzReA%2FzDOtsHEBjqkAdbE64XrprGuJuhRA6FAuu%2B74sP%2FgEDMgVJDU%2B432ZlXRfDi59Igmtd3fM%2BI4S%2BdWY%2BKUMpY2kVWr11EFAhjhuy2wUQbnvIjoFeyO1%2Bpv57k1vWwcotxZZTSKo%2FjXL0tBl98qHe2H1yhIHGweh8pFxUq95z7jO0WN5A1LMEYHKD1N8WzLhYkdExNN6zT7YzjHtIuKxKJvUMf6hJ5WJ0fK%2BEQrTFQ&X-Amz-Signature=a0797d4163e1386c6a52a695007c263a33246eef60d13a6d74c30d0ed51eac1e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


