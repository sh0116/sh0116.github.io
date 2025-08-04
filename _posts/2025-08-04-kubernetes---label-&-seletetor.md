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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/36ef8101-8194-496b-b5ba-d12aeda22c71/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46665SBWVMW%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T072151Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIFLRE08C3utYo8EBmd3uLc%2BYFx07lgDwsSNHmrhKfrqSAiEA0aw8uHhEXvucv75MLtexwzruUrcns0PEaHcovJqTge8q%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDH4T6nqF4plGa6uRLircA041O0OlK4W5%2FD2xvt84jFUsBQcZ2%2FbBKGj8WI0dUHgBBoJ5xq2skfb6OAMN54a5CUTaygs4DDZU70wGezY3Fd99UQSKe4W7oHID1FQoeyqU7hAduSeLC5QD2st2%2Fqp3y1ZwSSMv2QpZl0EtA775Yu0Z%2FMot38ZbRaTrc8EICkfMcKcz55ilZXgbkRMvx57PbKUuM4Hrbi3auum1Q8fGQLGFjlnm0lYRdPld5D%2BXb059IIpNpdzVA19gY6Imy1nYxDODAoKtQvfIvnD7vzTwptlwv5amz16B478NiJOYpZzd4d%2Fb%2F5PwN2Jwx48lXNXIeb1%2B1hmx7rmGQQuJc0wd7l9EgbLLULktva%2FgPXrzY4JXVrxiyYqV3e9UAP%2Fi4Eu4ggKVlanZoGb4Jl0ngYEDOofyKKKf2NSU3YqMXdcGu4i56QxisHCy01QM%2FrX%2F2Jgc1oaBg75w%2Bj5t9dCo1k%2FFPzqohtOF4GTulnxCCGitl9SrSMzFlCSHGN8%2B9WEWzu4GE7DeOkuJ%2BrIxDs%2BCs17tgEdxt0oD0%2BbOBbJNJlDeNKD8unEVxfgZVWsuqTVXcC8mJZpzWJvIyS3LCMBmF7LCJbIyM%2Bbaf7jpoJ%2FbHwxtqVQuujHv4ZZBBfy%2BpqhaMJ23wcQGOqUBjzD5tuIeaiQFKYhAjRfo4sRglkNVACPh%2FQpvpa3nKV5wcPd34QebCeGv%2BioRjkjejGdI4goiULOzbeV7ZRCS2c6CSomN3BzhrwRPMRDi6mTDbekpJ8YNCbK8wRuaoRg9U8PmBEbUFKQe1aANgD8pa%2FKYAwDXwobl4EjBHkx8lDCvfCONeZVSr4mEqSe5fUHmg4R%2FbWSGPdBkGrPlEeC2zmHma7Be&X-Amz-Signature=e0a6efe7f35dd30f0673e641ad9a6119828957d0ee0b574de606de35b87a8726&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/1cdbb02a-3553-46c6-9579-1a21449b0d12/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46665SBWVMW%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T072152Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIFLRE08C3utYo8EBmd3uLc%2BYFx07lgDwsSNHmrhKfrqSAiEA0aw8uHhEXvucv75MLtexwzruUrcns0PEaHcovJqTge8q%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDH4T6nqF4plGa6uRLircA041O0OlK4W5%2FD2xvt84jFUsBQcZ2%2FbBKGj8WI0dUHgBBoJ5xq2skfb6OAMN54a5CUTaygs4DDZU70wGezY3Fd99UQSKe4W7oHID1FQoeyqU7hAduSeLC5QD2st2%2Fqp3y1ZwSSMv2QpZl0EtA775Yu0Z%2FMot38ZbRaTrc8EICkfMcKcz55ilZXgbkRMvx57PbKUuM4Hrbi3auum1Q8fGQLGFjlnm0lYRdPld5D%2BXb059IIpNpdzVA19gY6Imy1nYxDODAoKtQvfIvnD7vzTwptlwv5amz16B478NiJOYpZzd4d%2Fb%2F5PwN2Jwx48lXNXIeb1%2B1hmx7rmGQQuJc0wd7l9EgbLLULktva%2FgPXrzY4JXVrxiyYqV3e9UAP%2Fi4Eu4ggKVlanZoGb4Jl0ngYEDOofyKKKf2NSU3YqMXdcGu4i56QxisHCy01QM%2FrX%2F2Jgc1oaBg75w%2Bj5t9dCo1k%2FFPzqohtOF4GTulnxCCGitl9SrSMzFlCSHGN8%2B9WEWzu4GE7DeOkuJ%2BrIxDs%2BCs17tgEdxt0oD0%2BbOBbJNJlDeNKD8unEVxfgZVWsuqTVXcC8mJZpzWJvIyS3LCMBmF7LCJbIyM%2Bbaf7jpoJ%2FbHwxtqVQuujHv4ZZBBfy%2BpqhaMJ23wcQGOqUBjzD5tuIeaiQFKYhAjRfo4sRglkNVACPh%2FQpvpa3nKV5wcPd34QebCeGv%2BioRjkjejGdI4goiULOzbeV7ZRCS2c6CSomN3BzhrwRPMRDi6mTDbekpJ8YNCbK8wRuaoRg9U8PmBEbUFKQe1aANgD8pa%2FKYAwDXwobl4EjBHkx8lDCvfCONeZVSr4mEqSe5fUHmg4R%2FbWSGPdBkGrPlEeC2zmHma7Be&X-Amz-Signature=b323b6530b50086d4768b9e24a83dda8371727342214f2cb1b565acec95eceae&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


