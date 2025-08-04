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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/36ef8101-8194-496b-b5ba-d12aeda22c71/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YWOLSPJU%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T064902Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJIMEYCIQD554oj16hFX6%2BqwYd9JTpYk%2FGptT53od1VG9342kp18wIhAOJXv3hwveDXQ5DXiMpi1OXQCUtrj%2B%2FYVvTVp%2BFa4PcwKv8DCD8QABoMNjM3NDIzMTgzODA1Igz4GI9E1cOXIqAKNZQq3AOHV7UUFdfUDrZKNBewWJu60mL2Owu5b8oHRK%2ByrtJuL44KIzM77v5dmAoxIMmEwWoeUQSfa1PPOaEU3NsvxSngjs7xnK1sW8mtyctmQrlfWbv61vxHMoCtkY4qI75Y3yBHHpEmCKaHRJ33qzYjaBGfXhe4QeBbCdA9COD6OZ%2BhYN24nX30SE%2FAEZWbKhYLKVmmLZhycPvcoqUr13FCRbny8YnE5wEChKoPK2GIyXTUE%2FhGrty3h9SpU687KDcLKr1yKMH84cbeUXx2vjyUwwGSvUH2mLSlzEmwg98OQQ9LILGt2mqdSN2ssJ9zxSu4A%2B6B34K2vFFArl%2B3Tdk01grlpU%2B%2Bc%2BhQ7rr9mC91n3K%2BNzLrq6SKYc84DFkpJaqTiYsxWf%2FA1uGaxxWptI%2FexUYLQC5L3lmJb2er%2FJqaVOdkrcdhdCtoOUvg7xuu%2BUP0xA9QGbFqd9%2FmKQmKGIYUHPUmOKsr9DotFnkdNmH6q6B3wXxjCxFtyBTcN1ecIxNH%2Bn%2B%2FKqLlcLfwLDv7VUrqMo50TPonr7h98MX9MxNqWcWN7ONNrXwMsB8bRu2F%2F5NZV2dI0hC9f3sn%2Fe%2FAKuoZhDYquBtMvUCZcaitzrMv7XoLsTJpBkw2cLEKBaO3dTDajcHEBjqkAYDrYapwNEYxlqL5d6uCyvIqYD7zVFhNr8iHmjn9NvQoT4uOuxJiDGEZlxpsSCojNwinAo0psHeeCFz92ddN%2Bl%2BJvEg3iJsfCO%2FQBc1qtZKuXLQQbjg3sR5oBsyT0ukUVY4qA6j2S6t%2F6KFqcekz0S7ULqJJbAB8VYC0qCt%2BZxg8fPy5%2FHC%2FWlWei2rWqQV%2FYZ9u5C%2BTDFlBqmUSMQwACJ5XvjSD&X-Amz-Signature=c32c0a4cd79f9a3b91e036f3b82638aabdd9d15249a3739b04d80edeac800a1f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/1cdbb02a-3553-46c6-9579-1a21449b0d12/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YWOLSPJU%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T064902Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJIMEYCIQD554oj16hFX6%2BqwYd9JTpYk%2FGptT53od1VG9342kp18wIhAOJXv3hwveDXQ5DXiMpi1OXQCUtrj%2B%2FYVvTVp%2BFa4PcwKv8DCD8QABoMNjM3NDIzMTgzODA1Igz4GI9E1cOXIqAKNZQq3AOHV7UUFdfUDrZKNBewWJu60mL2Owu5b8oHRK%2ByrtJuL44KIzM77v5dmAoxIMmEwWoeUQSfa1PPOaEU3NsvxSngjs7xnK1sW8mtyctmQrlfWbv61vxHMoCtkY4qI75Y3yBHHpEmCKaHRJ33qzYjaBGfXhe4QeBbCdA9COD6OZ%2BhYN24nX30SE%2FAEZWbKhYLKVmmLZhycPvcoqUr13FCRbny8YnE5wEChKoPK2GIyXTUE%2FhGrty3h9SpU687KDcLKr1yKMH84cbeUXx2vjyUwwGSvUH2mLSlzEmwg98OQQ9LILGt2mqdSN2ssJ9zxSu4A%2B6B34K2vFFArl%2B3Tdk01grlpU%2B%2Bc%2BhQ7rr9mC91n3K%2BNzLrq6SKYc84DFkpJaqTiYsxWf%2FA1uGaxxWptI%2FexUYLQC5L3lmJb2er%2FJqaVOdkrcdhdCtoOUvg7xuu%2BUP0xA9QGbFqd9%2FmKQmKGIYUHPUmOKsr9DotFnkdNmH6q6B3wXxjCxFtyBTcN1ecIxNH%2Bn%2B%2FKqLlcLfwLDv7VUrqMo50TPonr7h98MX9MxNqWcWN7ONNrXwMsB8bRu2F%2F5NZV2dI0hC9f3sn%2Fe%2FAKuoZhDYquBtMvUCZcaitzrMv7XoLsTJpBkw2cLEKBaO3dTDajcHEBjqkAYDrYapwNEYxlqL5d6uCyvIqYD7zVFhNr8iHmjn9NvQoT4uOuxJiDGEZlxpsSCojNwinAo0psHeeCFz92ddN%2Bl%2BJvEg3iJsfCO%2FQBc1qtZKuXLQQbjg3sR5oBsyT0ukUVY4qA6j2S6t%2F6KFqcekz0S7ULqJJbAB8VYC0qCt%2BZxg8fPy5%2FHC%2FWlWei2rWqQV%2FYZ9u5C%2BTDFlBqmUSMQwACJ5XvjSD&X-Amz-Signature=d38d888197a063a633f08f5fcfd60b68e557c7f685ad8ebf819413f3c066b8ee&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


