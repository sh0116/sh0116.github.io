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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/36ef8101-8194-496b-b5ba-d12aeda22c71/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UBYDTZBL%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T070521Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCIQD8MiVK8m%2FX4B9WzcpFh%2BUo%2BTGMs8MNrBel%2FoEd88VQtAIgD0GiDz2UKqhMeQA1OfEJBM3NsIhby23CosZ8JzURfB4q%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDCKHeVNV104icC0OcSrcA8sPSfDizqYx5ZqFFxge28l%2Fa62di162Ail190HhP%2FvFVwWsZYIPdnMQTuSnCnH7jpW0ED5I%2Bbiya%2Fd%2B6U2hyOVlQIL4HTdrfW2qzq9NeZZjgn%2BMUDyUzYd6XoB38aQ6MbRqnas2%2Byw8N60JNdICpvgCQ17s8jXqyjn4RLPC5lKHkSFvxCw2AAfIYn9Bl02jbwfVgsPAmJNd%2B2edoc3qvp6YMF2NdM5G61IwiPf1%2F7Z30zy%2B%2FOC0wrDUiI0RE10u2yUI%2FcxhUwCp3qj29wbtE5XEMymh09aolj9dAE%2BHvEMClP%2FruoOPs3hJVfs0LdmsrnPyE6cW4rg9fzmiZgjRvMuqlUnl5w%2B0DbI0ANBhBBNRTzCr5RTg59kLrIJKsBrHkFAWK%2FKA9tBAXfme7SCf0zylyj%2F%2BdIfXOh8kdeENHmphAItJbhXrYSuOSu60A3xzVvttal270Kd1F2t%2FlFz73NHdTknhHSjboHhfeyIc1PTO%2FazWqdD1a7I4oaJR1pk3fKzIPtG9AsQVvWG94bmOpLCJUGp0VPZsU7PZVv8AyGYvXk6LOi6S%2B0xsdAkbDbZT%2FoTdH1wSfIsqGlw%2F1p2SRT8fl2hXxMDeLW6vNnU5W2nl4RtaxXAkKtioecYHMLaNwcQGOqUB%2B1hPTk4VeKKGEzTHBG9FWUiBcYDF8AVYSMVhsFQ1A4Wqo3CFLa0mYdFQgBtAsH56euyf6WbyMJjthkxd4u9lptoOyhL2pmNqUX2q66LJ3D792I8ztlL0UpLwh1pXTxlKvBYTRQ4JZCjbu%2BiCC8o1cGnyrjk1RWvMoAlt%2B53seZ9rekaXu1y4E6GoUa%2BHpJFa%2Bfv6Xt53hYxy38JePl5rmwB8JtVl&X-Amz-Signature=2204ca5ef6f9c4e7655f828bd8ecc156da6cd61b85c649fffcf78313dc88193d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/1cdbb02a-3553-46c6-9579-1a21449b0d12/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UBYDTZBL%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T070522Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCIQD8MiVK8m%2FX4B9WzcpFh%2BUo%2BTGMs8MNrBel%2FoEd88VQtAIgD0GiDz2UKqhMeQA1OfEJBM3NsIhby23CosZ8JzURfB4q%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDCKHeVNV104icC0OcSrcA8sPSfDizqYx5ZqFFxge28l%2Fa62di162Ail190HhP%2FvFVwWsZYIPdnMQTuSnCnH7jpW0ED5I%2Bbiya%2Fd%2B6U2hyOVlQIL4HTdrfW2qzq9NeZZjgn%2BMUDyUzYd6XoB38aQ6MbRqnas2%2Byw8N60JNdICpvgCQ17s8jXqyjn4RLPC5lKHkSFvxCw2AAfIYn9Bl02jbwfVgsPAmJNd%2B2edoc3qvp6YMF2NdM5G61IwiPf1%2F7Z30zy%2B%2FOC0wrDUiI0RE10u2yUI%2FcxhUwCp3qj29wbtE5XEMymh09aolj9dAE%2BHvEMClP%2FruoOPs3hJVfs0LdmsrnPyE6cW4rg9fzmiZgjRvMuqlUnl5w%2B0DbI0ANBhBBNRTzCr5RTg59kLrIJKsBrHkFAWK%2FKA9tBAXfme7SCf0zylyj%2F%2BdIfXOh8kdeENHmphAItJbhXrYSuOSu60A3xzVvttal270Kd1F2t%2FlFz73NHdTknhHSjboHhfeyIc1PTO%2FazWqdD1a7I4oaJR1pk3fKzIPtG9AsQVvWG94bmOpLCJUGp0VPZsU7PZVv8AyGYvXk6LOi6S%2B0xsdAkbDbZT%2FoTdH1wSfIsqGlw%2F1p2SRT8fl2hXxMDeLW6vNnU5W2nl4RtaxXAkKtioecYHMLaNwcQGOqUB%2B1hPTk4VeKKGEzTHBG9FWUiBcYDF8AVYSMVhsFQ1A4Wqo3CFLa0mYdFQgBtAsH56euyf6WbyMJjthkxd4u9lptoOyhL2pmNqUX2q66LJ3D792I8ztlL0UpLwh1pXTxlKvBYTRQ4JZCjbu%2BiCC8o1cGnyrjk1RWvMoAlt%2B53seZ9rekaXu1y4E6GoUa%2BHpJFa%2Bfv6Xt53hYxy38JePl5rmwB8JtVl&X-Amz-Signature=16e7dfb95f6e76a13a0a37bfcbeed3ad77d4b6a269d17923a091ec584e39c388&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


