---
title: "Kubernetes - Label & Seletetor"
date: 2025-08-04 06:05:00 +0900
categories: [kubernetes]
tags: [Kubernetes]
description: Kubernetes 기초
toc: true
comments: true
---

## 레이블 Lable

### 레이블이란?

- 모든 리소스를 구성하는 매우 간단하면서도 강력한 쿠버네티스 기능
- 리소스에 첨부하는 임의의 키/값 쌍 (app: test)
- 레이블 셀렉터를 사용하면 각종 리소스를 필터링하여 선택할 수 있음
- 리소스는 한개 이상의 레이블을 가질수 있음
- 리소스를 만드는 시점에 레이블을 첨부
- 기존 리소스에도 레이블의 값 수정, 추가 가능
- 모든 사람이 쉽게 이해할 수 있는 체계적인 시스템을 구축 가능
### 레이블을 이용한 포드 구성 ( 가로 app / 세로 rel )

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/36ef8101-8194-496b-b5ba-d12aeda22c71/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TLPTOU3Q%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T071416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJGMEQCIEQXMm5NrxK52b9pVV8JoP5errQC11VetPuFL9dREfnDAiAnQ26kLh%2FlPKc48u9xAHvr%2BT4Bqg3P%2FNZ3rpXAzn8JfCr%2FAwhAEAAaDDYzNzQyMzE4MzgwNSIMRyakQHoAJsisgx19KtwDeue8GP3fSK7qeSmMw6WFfYdeFURppjoq9MKIH7vpKyEfLq863MgKkLSasdvPEMWWZAWIoih36bUl54b2aucBzALiGS5Fw0vwBIInuieqfdkFLXopcpFXBIooTG6HIOqHQw18%2F5dluIesGxasbFgas6elPY3PrOrntJrmJxOk0VdzHyOvOKya8FaSS3e14ZwNPx42moDJ7HfpclanSCWcjCpQJtWG1LhWt%2F65owth4W3yQfCy2Aiwqq5VKWtC%2BkVfdHxW3noS%2Bh9%2Frlbx%2F699PHx784V934CUyWoB%2F0hcsquX%2BJNiVYwXnJcO4xHUopqe7T%2FKaqmSnlc2uOn75So8kJxMFeXkH0GyZk1Yz%2FvrYIwmU1lR9Zta2eLGJBdhbUmnTCsNO2vUk8fUpZZxts94fT3Bwfe%2BNh5a1vUnG5GkcUUmlIEYWWH9LVYILpwcz4K9MfmmGqFvz3ActI7IyM%2BGL57AWezhdLqcv3nJbayACbZXmHIm0mWZanT1PfUz1A%2BatbdAIqASa033JK0X%2B027G0OJryGmKF9pnsc9wK8ue76Y7qTR5OOAPN3xkbUWnesKGU0R0UmpjC1fPZo3qh0Xv7NL9pvHbAUFKsIep69VM8JMCqSqJmkfnYz7q3Iw2bbBxAY6pgE%2FfEVnp2IeMh0cL%2Fw6K1BGW2WzxP6278wtKYg6VWT6VWR0mZaxwIGXOzu%2B2u1QVjJ9EeSqOiuH0jU6K%2BC7acP95ygfjbRfN%2F7zxHLFksKQX2Qh0O9hFjmIcIbybesgd3y7j4jh2ddMbA9pvuWY31xwluVcGNkGISJaQn44fGUTWHyr5bbYKJ7e0PvnPDNxsgJOKwG9yLtPbx1g6DdDBDRQzkj5lD7f&X-Amz-Signature=a064b9bf136ef29ee1015c3a0548f237483c4af121030a7562422b949786fee0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 레이블 생성 방법

```go
kubectl label pod 파드명 test=pod
```

> 신규 레이블 추가

```go
kubectl label pod 파드명 test=pod --overwrite
```

> 기존 레이블 수정

## 레이블 필터링하여 검색

```bash
kubectl get pod --show-labels   #labels 컬럼 생성
kubectl get pod -L app,rel      #app, rel key값을 컬럼으로 정렬

# 셀렉터를 통해 라벨을 식별하고 조회한다
kubectl get pod --show-labels -l 'env'  # 필터링
kubectl get pod --show-labels -l '!env' # not 필터링
kubectl get pod --show-labels -l 'env!=test' # key/value 비교
kubectl get pod --show-labels -l 'env!=test,rel=beta' # and연산
kubectl get pod --show-labels -l 'env in (test)' # key/value 비교
```

## 확장 가능한 쿠버네티스 레이블 예제 - 네이밍

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/1cdbb02a-3553-46c6-9579-1a21449b0d12/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TLPTOU3Q%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T071416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJGMEQCIEQXMm5NrxK52b9pVV8JoP5errQC11VetPuFL9dREfnDAiAnQ26kLh%2FlPKc48u9xAHvr%2BT4Bqg3P%2FNZ3rpXAzn8JfCr%2FAwhAEAAaDDYzNzQyMzE4MzgwNSIMRyakQHoAJsisgx19KtwDeue8GP3fSK7qeSmMw6WFfYdeFURppjoq9MKIH7vpKyEfLq863MgKkLSasdvPEMWWZAWIoih36bUl54b2aucBzALiGS5Fw0vwBIInuieqfdkFLXopcpFXBIooTG6HIOqHQw18%2F5dluIesGxasbFgas6elPY3PrOrntJrmJxOk0VdzHyOvOKya8FaSS3e14ZwNPx42moDJ7HfpclanSCWcjCpQJtWG1LhWt%2F65owth4W3yQfCy2Aiwqq5VKWtC%2BkVfdHxW3noS%2Bh9%2Frlbx%2F699PHx784V934CUyWoB%2F0hcsquX%2BJNiVYwXnJcO4xHUopqe7T%2FKaqmSnlc2uOn75So8kJxMFeXkH0GyZk1Yz%2FvrYIwmU1lR9Zta2eLGJBdhbUmnTCsNO2vUk8fUpZZxts94fT3Bwfe%2BNh5a1vUnG5GkcUUmlIEYWWH9LVYILpwcz4K9MfmmGqFvz3ActI7IyM%2BGL57AWezhdLqcv3nJbayACbZXmHIm0mWZanT1PfUz1A%2BatbdAIqASa033JK0X%2B027G0OJryGmKF9pnsc9wK8ue76Y7qTR5OOAPN3xkbUWnesKGU0R0UmpjC1fPZo3qh0Xv7NL9pvHbAUFKsIep69VM8JMCqSqJmkfnYz7q3Iw2bbBxAY6pgE%2FfEVnp2IeMh0cL%2Fw6K1BGW2WzxP6278wtKYg6VWT6VWR0mZaxwIGXOzu%2B2u1QVjJ9EeSqOiuH0jU6K%2BC7acP95ygfjbRfN%2F7zxHLFksKQX2Qh0O9hFjmIcIbybesgd3y7j4jh2ddMbA9pvuWY31xwluVcGNkGISJaQn44fGUTWHyr5bbYKJ7e0PvnPDNxsgJOKwG9yLtPbx1g6DdDBDRQzkj5lD7f&X-Amz-Signature=00f77d576b0f62759050070a95fc30bf0f6313c026c8636b166b9a2e74eb2e54&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 셀렉터 공식 문서 (일치성 기준 요건)

## 레이블과 셀렉터 연습문제

- YAML 파일을 사용하여 app=nginx 레이블을 가진 포드를 생성하라.
- app=nginx를 가진 포드를 get하라
- get된 포드의 레이블의 app을 확인하라
- app=nginx레이블을 가진 포드에 team=dev1레이블을 추가하라
### YAML 파일을 사용하여 app=nginx 레이블을 가진 포드를 생성하라.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: practice-labels
  labels:
    app: nginx
spec:
  containers:
  - name: prac-nginx
    image: nginx
    ports:
    - containerPort: 8080
      protocol: TCP
```

### app=nginx를 가진 포드를 get하라

```bash
kubectl get pod --show-labels -l 'app=nginx'
```

### get된 포드의 레이블의 app을 확인하라

```bash
kubectl get pod -L app
```

### app=nginx레이블을 가진 포드에 team=dev1레이블을 추가하라

```bash
kubectl label pod pod명 team=dev1 (만약 덮어쓰기면 --overwrite)
kubectl get pod -L app,team
```


