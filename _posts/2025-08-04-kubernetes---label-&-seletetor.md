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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/36ef8101-8194-496b-b5ba-d12aeda22c71/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ZP4KDYK%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T063255Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCIQDzmR3KMuKhLfu6r3fHdjewXu%2FWNesFFzkTHBNUIEt8qgIgHFQdyyj9yooGUgkhFqQhPnYT3QNhcIDw%2BcdoOLxCBKsq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDOM8X85p6pvcMG7GmSrcA%2FQ1Fx1k%2BkM2%2FQZpBlhb5sTQELCT6C%2B6ex9xKWxWvDkGwDySRtC1jSrv0G%2FGuz9lcVocLoyRpQ%2BB%2FmxX4MuUYsXVobXy5Q0Vfv02G5Yh%2FX52TEX8WuUkgoUgpKrDNak2qYmOqSWDZNY2ZZVlX4NibXA9KNjj%2BdSKKC99kncNtnZFGS5zPUUCpDbE6v3gbXujB7%2B%2FpGjh%2BlvqwDHu7tN8P0mO3fjSIlJOJr0YeLBNa2g0JShuqaIHcuSGLaqfM%2FFvYOZZjoqKAmUuMQ9uPUPr9o2OzGP%2BhGJ2EPtZrUdURinZSnqx9jr22Qntd9X44L6AuZ8tfhghlksH7J8RfBtKdlETCeMpfC%2BoNf0Qhxj5XlH2Zt9WgI3hoUqNwLqzELeUGc%2B4iwWic6bWHF8U%2BgPBBhHarcpPSq7%2B37ALO1SMkhmUgD3mwX36ln2DgxTalZC1jUN%2BtvIknRBVOufzfBvwNcPiIgaS2AURA4a3EVUFLisjq%2F5SuM1jXPmrOTaVXUOyifci9McmyvaCgWavOz45Lk1hE1QQ9yjk2KZ%2F8%2BWHNXtm8hYEAdoJFbMEq6r%2B%2Fv%2FJjLBwZGJHs2FJ6SUXxRUAX9VUSMWMz%2FdlQ%2FFE1Cv9nLFs3SNwPVi6behGvirXMK6NwcQGOqUBVXy%2FtcmkouALLS5D9P%2Ft6Qk1QzS1atAof4nVSEaJDlsVKBbMhUoh97jSwjssc8LhzIe1LSjHXroV345SQ0FEgSwA5057huHONQv5DJLtZF6oTyLwDCH8BnBcTZur5gBq5DihuNNrJAexZcbWxb2mOOX0aNeXb1T4ES5m3iESeyDJ%2BTlLiCa9QCkxanQQv3T4ooOl3uwAJa205fL8Pn23RFUt91GN&X-Amz-Signature=0c9fe160aaaa11d8c040ef044df5e298cede0fe332e4690e031bee87dc1ef692&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/1cdbb02a-3553-46c6-9579-1a21449b0d12/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ZP4KDYK%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T063255Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCIQDzmR3KMuKhLfu6r3fHdjewXu%2FWNesFFzkTHBNUIEt8qgIgHFQdyyj9yooGUgkhFqQhPnYT3QNhcIDw%2BcdoOLxCBKsq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDOM8X85p6pvcMG7GmSrcA%2FQ1Fx1k%2BkM2%2FQZpBlhb5sTQELCT6C%2B6ex9xKWxWvDkGwDySRtC1jSrv0G%2FGuz9lcVocLoyRpQ%2BB%2FmxX4MuUYsXVobXy5Q0Vfv02G5Yh%2FX52TEX8WuUkgoUgpKrDNak2qYmOqSWDZNY2ZZVlX4NibXA9KNjj%2BdSKKC99kncNtnZFGS5zPUUCpDbE6v3gbXujB7%2B%2FpGjh%2BlvqwDHu7tN8P0mO3fjSIlJOJr0YeLBNa2g0JShuqaIHcuSGLaqfM%2FFvYOZZjoqKAmUuMQ9uPUPr9o2OzGP%2BhGJ2EPtZrUdURinZSnqx9jr22Qntd9X44L6AuZ8tfhghlksH7J8RfBtKdlETCeMpfC%2BoNf0Qhxj5XlH2Zt9WgI3hoUqNwLqzELeUGc%2B4iwWic6bWHF8U%2BgPBBhHarcpPSq7%2B37ALO1SMkhmUgD3mwX36ln2DgxTalZC1jUN%2BtvIknRBVOufzfBvwNcPiIgaS2AURA4a3EVUFLisjq%2F5SuM1jXPmrOTaVXUOyifci9McmyvaCgWavOz45Lk1hE1QQ9yjk2KZ%2F8%2BWHNXtm8hYEAdoJFbMEq6r%2B%2Fv%2FJjLBwZGJHs2FJ6SUXxRUAX9VUSMWMz%2FdlQ%2FFE1Cv9nLFs3SNwPVi6behGvirXMK6NwcQGOqUBVXy%2FtcmkouALLS5D9P%2Ft6Qk1QzS1atAof4nVSEaJDlsVKBbMhUoh97jSwjssc8LhzIe1LSjHXroV345SQ0FEgSwA5057huHONQv5DJLtZF6oTyLwDCH8BnBcTZur5gBq5DihuNNrJAexZcbWxb2mOOX0aNeXb1T4ES5m3iESeyDJ%2BTlLiCa9QCkxanQQv3T4ooOl3uwAJa205fL8Pn23RFUt91GN&X-Amz-Signature=1c3862eb76beebed202f23c22f37e24abf441399f81af70642982d077e9c450d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


