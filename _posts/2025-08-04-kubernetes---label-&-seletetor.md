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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/36ef8101-8194-496b-b5ba-d12aeda22c71/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OQUMSIV%2F20250805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250805T061008Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJHMEUCIC2vR605R2YcEbfO8baurnUV9s%2FppAl2Nz7wb4VXaOdSAiEApwIsPFkRRZyxJVWAnIj%2F1L3kNf29iUHjnYVK3iLLJOsq%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDJUXx9HyvMkkWGvhjyrcAz2fY2XlMlKmB68Om2ikrabD4%2BPTz%2Bk%2FtWIghV1P8lt2zRM3LiFppNTp3AKM2RIJaP0nvUnbJKzSLb%2B%2BRMbEZduhY9OEr%2F9jPWHKH9md21AX5qf5UsX2sXJBx8jqbYtGo0S4Qtf%2FDAp6abrUSAaP2ybnA%2B%2BbK0K4lXlSfAUaa920q1DY6Vm4pZg4vO2pXM0vam2N3BRVrdIohpWv0iwdeR%2FrSpUdZyGvGH9oAtW%2BlWwIayRBzOLRcwlFJoY4xwpFXy9mmpBNWysTJf8ME7rkGUzXhQHL7yeL6J6NTInaJcQwMoO5bLiARJ6r1shfvWdYzbuVcPkjr8%2BRHAI0VQr0EnDz4ZdsUVZEtPDyDdNZp7hFqgT86uh3hLUGbXJOBW4CyZZNAwAAMhOHusg%2FTOeBviffL45ws3m7br1nD%2Fn99ST4SefxS26YHgT5elmrp2jhLVyfW%2BarLooPCKYSObjshJ3fMjmdC2SMTRDfEjJ%2BUslvpAcPzz70JUl4oEp5YDYfbUc8HAYRy8w64p2SDe694ZLSUfDXZTb9NvZQptrMU1mhg0WZU2f2QRBJMzzaj%2BGwiTV6xUWy%2BPFfdsc0zgMqAghsbPcuxmiB2U1iyOWdmNR9ax1xHRhj4bKf5Q7zMKu0xsQGOqUB87VBWqSHcJ5CjGI3ruDBhUvgjc6kdNvLAv0CXoLmsC9LlYI%2FZEff7poIlywi8cflP5DlD7tMUnFg%2BjYQ110WVHO7rnPlMw0sRSza7Uj3ge9mY3VMj87sRRgeKvj8vTM72Zksp4cAITJTTPVlKnmnOhSQSSi3c62RcfwdBNyM5I1d%2BHwgBXPkB3i9j0ODfKdEkfoA1zI0Woop5L0ydhpyW6YjCCXr&X-Amz-Signature=1ff5a74182594919c9b1ad52f4a93dce8b3f3ca8232d99e886f00ca83caae12a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/1cdbb02a-3553-46c6-9579-1a21449b0d12/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OQUMSIV%2F20250805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250805T061008Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJHMEUCIC2vR605R2YcEbfO8baurnUV9s%2FppAl2Nz7wb4VXaOdSAiEApwIsPFkRRZyxJVWAnIj%2F1L3kNf29iUHjnYVK3iLLJOsq%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDJUXx9HyvMkkWGvhjyrcAz2fY2XlMlKmB68Om2ikrabD4%2BPTz%2Bk%2FtWIghV1P8lt2zRM3LiFppNTp3AKM2RIJaP0nvUnbJKzSLb%2B%2BRMbEZduhY9OEr%2F9jPWHKH9md21AX5qf5UsX2sXJBx8jqbYtGo0S4Qtf%2FDAp6abrUSAaP2ybnA%2B%2BbK0K4lXlSfAUaa920q1DY6Vm4pZg4vO2pXM0vam2N3BRVrdIohpWv0iwdeR%2FrSpUdZyGvGH9oAtW%2BlWwIayRBzOLRcwlFJoY4xwpFXy9mmpBNWysTJf8ME7rkGUzXhQHL7yeL6J6NTInaJcQwMoO5bLiARJ6r1shfvWdYzbuVcPkjr8%2BRHAI0VQr0EnDz4ZdsUVZEtPDyDdNZp7hFqgT86uh3hLUGbXJOBW4CyZZNAwAAMhOHusg%2FTOeBviffL45ws3m7br1nD%2Fn99ST4SefxS26YHgT5elmrp2jhLVyfW%2BarLooPCKYSObjshJ3fMjmdC2SMTRDfEjJ%2BUslvpAcPzz70JUl4oEp5YDYfbUc8HAYRy8w64p2SDe694ZLSUfDXZTb9NvZQptrMU1mhg0WZU2f2QRBJMzzaj%2BGwiTV6xUWy%2BPFfdsc0zgMqAghsbPcuxmiB2U1iyOWdmNR9ax1xHRhj4bKf5Q7zMKu0xsQGOqUB87VBWqSHcJ5CjGI3ruDBhUvgjc6kdNvLAv0CXoLmsC9LlYI%2FZEff7poIlywi8cflP5DlD7tMUnFg%2BjYQ110WVHO7rnPlMw0sRSza7Uj3ge9mY3VMj87sRRgeKvj8vTM72Zksp4cAITJTTPVlKnmnOhSQSSi3c62RcfwdBNyM5I1d%2BHwgBXPkB3i9j0ODfKdEkfoA1zI0Woop5L0ydhpyW6YjCCXr&X-Amz-Signature=5f188bbb7ff662094687f4b4c9060d136bbd7adc34554c883c8051fdf1d2d792&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


