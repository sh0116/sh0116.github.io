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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/36ef8101-8194-496b-b5ba-d12aeda22c71/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667JT7UHV4%2F20250805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250805T002703Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJIMEYCIQD2TW%2F2M4pJ%2B5cYt%2BDKoiqx42Hqmle0zi7XNAeERIfCjgIhAJyWXn2jzdxFl7U0rumgtHo3NCIMzkLfcWpCYv5U%2FnwXKv8DCFAQABoMNjM3NDIzMTgzODA1Igzhe0WjTyf3%2F6vfrxAq3ANot4u36K6HJJwm5YqaIh3wQIopCO1F%2B37Y92aLkRcYR5FWaKMRRzfja25gbGufn34feHWKIuz0FsyJiSt5LzYu4eR9HkJbVL4QkeANx4k1L7i63HsHCQBgDaDllqwetTJYjE2W9my86hSHD69ZXEeTB1AWRDGLNGrUxD5SFHROPNwIAsNmcHcudJWh6fBmNsaJr8hwnySdEQGzaqqm8vLKd6f19RFxbd7X%2BrptzpMycdosjYRm2KLbTeH67wf8XxiAPz2gWbrT27820hkkpIoZiC4Hxz0f5ZdbOhd3TgKoqiThagBwS%2BJV5oE8xcqGatiNZ5MBZdUg8n%2FaXETzPxil34Qdq8ZlqEOvd7jvm%2FjkOH7IPWde5ZXeMU4VaM%2Ba1JsLPXM6%2BszAhv4dGCVk59yeOGZXZEeJTl18qcCynX8jm%2FvidzmdGekGS1rY7c5KX%2BIhikZ5XFwqq6dWEOkOy1qnTqWXQDZAWScGQF%2FrYYWY0MK1VbX1H9e0%2Fpmplop3tNFddvkdAhA%2FDgXYwVthYcj6u%2BBH379oVM5KUjTyG020o40ezWG9ubNRS4UUGiQL8MfO1ZJYozAT%2BstCzPPVyPMAZriyhN87tNO9ROxD7FSb7sUOhwNzUujblGrmbzCs9MTEBjqkAYqcgU9uW8xGIENKM8JuYzanclR%2FWS81vl5%2BTCta6fNAW7rXYAl2SKD4u0tW1iWwopQNGLob4ZC2blv7TaUw4Im1hZrICT2zaYo%2FIyasBFj%2Bpq9euaVUSnPs92DcIFatJwF2K8%2BWyBeV5EgVMd5IYa0TFd3W3HEXNKB21f0q1lf%2FL0v90J7EfsgbxeJvXKi6RbfqNrLLf1uDmzmIeFRXFuxYqf0%2B&X-Amz-Signature=a8ed00e89ec569a84555ac3088e6232576238194432696e195b08653327428ac&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/1cdbb02a-3553-46c6-9579-1a21449b0d12/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667JT7UHV4%2F20250805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250805T002703Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJIMEYCIQD2TW%2F2M4pJ%2B5cYt%2BDKoiqx42Hqmle0zi7XNAeERIfCjgIhAJyWXn2jzdxFl7U0rumgtHo3NCIMzkLfcWpCYv5U%2FnwXKv8DCFAQABoMNjM3NDIzMTgzODA1Igzhe0WjTyf3%2F6vfrxAq3ANot4u36K6HJJwm5YqaIh3wQIopCO1F%2B37Y92aLkRcYR5FWaKMRRzfja25gbGufn34feHWKIuz0FsyJiSt5LzYu4eR9HkJbVL4QkeANx4k1L7i63HsHCQBgDaDllqwetTJYjE2W9my86hSHD69ZXEeTB1AWRDGLNGrUxD5SFHROPNwIAsNmcHcudJWh6fBmNsaJr8hwnySdEQGzaqqm8vLKd6f19RFxbd7X%2BrptzpMycdosjYRm2KLbTeH67wf8XxiAPz2gWbrT27820hkkpIoZiC4Hxz0f5ZdbOhd3TgKoqiThagBwS%2BJV5oE8xcqGatiNZ5MBZdUg8n%2FaXETzPxil34Qdq8ZlqEOvd7jvm%2FjkOH7IPWde5ZXeMU4VaM%2Ba1JsLPXM6%2BszAhv4dGCVk59yeOGZXZEeJTl18qcCynX8jm%2FvidzmdGekGS1rY7c5KX%2BIhikZ5XFwqq6dWEOkOy1qnTqWXQDZAWScGQF%2FrYYWY0MK1VbX1H9e0%2Fpmplop3tNFddvkdAhA%2FDgXYwVthYcj6u%2BBH379oVM5KUjTyG020o40ezWG9ubNRS4UUGiQL8MfO1ZJYozAT%2BstCzPPVyPMAZriyhN87tNO9ROxD7FSb7sUOhwNzUujblGrmbzCs9MTEBjqkAYqcgU9uW8xGIENKM8JuYzanclR%2FWS81vl5%2BTCta6fNAW7rXYAl2SKD4u0tW1iWwopQNGLob4ZC2blv7TaUw4Im1hZrICT2zaYo%2FIyasBFj%2Bpq9euaVUSnPs92DcIFatJwF2K8%2BWyBeV5EgVMd5IYa0TFd3W3HEXNKB21f0q1lf%2FL0v90J7EfsgbxeJvXKi6RbfqNrLLf1uDmzmIeFRXFuxYqf0%2B&X-Amz-Signature=2be08bdcb3be116674e7bdf7b5d68a45e0b7d941b48b975c8079f69388570726&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


