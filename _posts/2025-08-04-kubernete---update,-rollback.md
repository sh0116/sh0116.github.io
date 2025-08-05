---
title: "Kubernete - Update, Rollback"
date: 2025-08-04 06:05:00 +0900
categories: [kubernetes]
tags: [Kubernetes]
description: Kubernetes 기초
toc: true
comments: true
---

## Application Rolling Update & RollBack

# Update 실습

http-go:v1 → v2 → v3 넘어가며 상태 살펴보기

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: http-go-deployment
  labels:
    app: http-go
spec:
  strategy:
    type: RollingUpdate
  replicas: 3
  selector:
    matchLabels:
      app: http-go
  template:
    metadata:
      labels:
        app: http-go
    spec:
      containers:
      - name: http-go
        image: seokhyeon116/http-go:v1
        ports:
        - containerPort: 8080
```

```yaml
kubectl create -f deploy-go.yaml --record=true #record 옵션을 넣어야 히스토리 확인가
```

### 업데이트 

```yaml
kubectl set image deploy http-go-deployment http-go=seokhyeon116/http-go:v2
# set image를 통해서 업데이트
kubectil edit deploy http-go-deployment # image에서 버전 변경
```

업데이트 방식이 RollingUpdate이다

- maxSurge : 최대로 생성할 수 있는 POD의 수를 정한다 (예를 들어 설정값이 30%이면 전체 POD에서 130%까지 만들 수 있다.) 
- maxUnavailable : 사용할 수 없는 최대 POD수를 정한다 (예를 들어 설정값이 30%이면 전체 POD의 70% 이상으로 항상 유지한다.)
```yaml
kubectl get pod -o wide #명령어 실행 시 아래 화면을 볼 수 있다.
# 노드를 하나씩 업데이하고 생성과 제거를 병행한다.
```

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/9c8c0403-7165-46bc-a529-864686459827/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VBXBI5RP%2F20250805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250805T002843Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJIMEYCIQCPGk1YrKY%2FaqV6ToLldfNJhUE2HmAILH%2Fp5BCu8J4QIgIhAKqZ2fNVY3B%2FGugL1qnKh%2F8Pb6YZP1CahA23lrLbUwUrKv8DCFAQABoMNjM3NDIzMTgzODA1IgzG6qTOqw%2FR828ELIIq3APHLOfmQE%2BBbABS2vzH4Uqp7f8O0m041WHjoUOL6WJs5mjcl1pZgMQgIcmmT8mLpJ7YQvBSla%2BL%2B8gBBcxmGS2HTxnynQgjGTSipd0eD%2Ff7UgLBYfVVeoN3wcDnl1G%2Bbr%2FDHrjvtn2Oa09pNTV0BNuB4I27GBIrzKiZp1ZR5iyd8GLbUtkugzsPGFbSfjUAfWuyTIqnFb2E2GzIQkncDVawE2g4hc1YGch3FSip7H5rDqW7WF9UbSXkqa1cgquw7%2Fqf%2BZW56tOGFU6cbMpxVvysjcyE1Ktd%2B3KodK1gAtuY84nHOPpqebdk3faOvYQsYAQ6TMZNaZTN0DAUbsN2weoTA0qxQtg1aCVkntc7isnp4VZJ9vxaFHH%2BhRWisefUmkjPUDBYtBUJa37l5wEjmEylPLv8Dtq6qUwmDzDCXNSSgmHI7GbFMctglxvE6jW066P%2Bmo%2BR7ZKmSTpIJQnLV5Z1HXInrwQJmVvT6cU7Zz%2FI4vQ1e4fDPnkvEQo9SUL4tCZZpiBwvHBLVWZsizl7bLlOuWTewcJqhrWaLObKmBUV9NcowFN5m6Udf7qoOcBYspxNa0pp4ECUIXaBS1OJISNjDyiqVBAeta9tg%2BtZyvh%2FizfFgPb9spwXIBge5zCs9MTEBjqkAbBOK5AAbq1Gv%2BkcIjfwM7wpt%2FOCFZVR5YN3YNMo8IHUkiRsKg5DBjAEtoVsMnFNpXtWWMFkaO8buzgDSvVEYwLvxSXJ22ZSLIlQKkwjkdYs%2FuGu08%2BJl1BcbCSCk6f5zEKCCcLoj0LPaRdfPTOjRi82wRa%2FbYqJS3sdsTW093naoDPsc8QccbVWTvBg9%2F2PZSocZRACKVhw91VZXpTDS22ZP1Zk&X-Amz-Signature=e8d0c1ff288526737f2dc7e4b065554a694c4962062ca204d65dba2e73082cf2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

# 업데이트 결과

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/78a6b4e1-236a-46aa-a2ba-e29ce42f16e9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VBXBI5RP%2F20250805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250805T002843Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJIMEYCIQCPGk1YrKY%2FaqV6ToLldfNJhUE2HmAILH%2Fp5BCu8J4QIgIhAKqZ2fNVY3B%2FGugL1qnKh%2F8Pb6YZP1CahA23lrLbUwUrKv8DCFAQABoMNjM3NDIzMTgzODA1IgzG6qTOqw%2FR828ELIIq3APHLOfmQE%2BBbABS2vzH4Uqp7f8O0m041WHjoUOL6WJs5mjcl1pZgMQgIcmmT8mLpJ7YQvBSla%2BL%2B8gBBcxmGS2HTxnynQgjGTSipd0eD%2Ff7UgLBYfVVeoN3wcDnl1G%2Bbr%2FDHrjvtn2Oa09pNTV0BNuB4I27GBIrzKiZp1ZR5iyd8GLbUtkugzsPGFbSfjUAfWuyTIqnFb2E2GzIQkncDVawE2g4hc1YGch3FSip7H5rDqW7WF9UbSXkqa1cgquw7%2Fqf%2BZW56tOGFU6cbMpxVvysjcyE1Ktd%2B3KodK1gAtuY84nHOPpqebdk3faOvYQsYAQ6TMZNaZTN0DAUbsN2weoTA0qxQtg1aCVkntc7isnp4VZJ9vxaFHH%2BhRWisefUmkjPUDBYtBUJa37l5wEjmEylPLv8Dtq6qUwmDzDCXNSSgmHI7GbFMctglxvE6jW066P%2Bmo%2BR7ZKmSTpIJQnLV5Z1HXInrwQJmVvT6cU7Zz%2FI4vQ1e4fDPnkvEQo9SUL4tCZZpiBwvHBLVWZsizl7bLlOuWTewcJqhrWaLObKmBUV9NcowFN5m6Udf7qoOcBYspxNa0pp4ECUIXaBS1OJISNjDyiqVBAeta9tg%2BtZyvh%2FizfFgPb9spwXIBge5zCs9MTEBjqkAbBOK5AAbq1Gv%2BkcIjfwM7wpt%2FOCFZVR5YN3YNMo8IHUkiRsKg5DBjAEtoVsMnFNpXtWWMFkaO8buzgDSvVEYwLvxSXJ22ZSLIlQKkwjkdYs%2FuGu08%2BJl1BcbCSCk6f5zEKCCcLoj0LPaRdfPTOjRi82wRa%2FbYqJS3sdsTW093naoDPsc8QccbVWTvBg9%2F2PZSocZRACKVhw91VZXpTDS22ZP1Zk&X-Amz-Signature=26f5d779277749cfd86236d63ce914571651f703342dfd4c97a28985cb2e1d24&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## RollBack하기

```yaml
kubectl rollout undo deploy http-go-deployment #한단계전으로 undeo
kubectl rollout undo deploy http-go-deployment --to-revision=1 #history 1번으로 돌아감

kubectl rollout history deploy http-go-deployment #해당 delpoy history 출력
# create할 때 --record=true를 해야 명령줄까지 출력됨
```

ㅏ

# 연습 문제

- alpine이미지 사용하여 업데이트와 롤백을 실행하라, 모든 revision내용은 기록되어야 한다.
- 3.5로 롤링 업데이트 수행
- 3.4로 롤백 수행
```yaml
kubectl create deploy alpine-deploy --image=deploy:3.4 --dry-run -o yaml
```

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  creationTimestamp: null
  labels:
    app: alpine-deploy
  name: alpine-deploy
spec:
  replicas: 1
  selector:
    matchLabels:
      app: alpine-deploy
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 50%
      maxUnavailable: 50%
  template:
    metadata:
      creationTimestamp: null
      labels:
        app: alpine-deploy
    spec:
      containers:
      - image: deploy:3.4
        name: deploy
        resources: {}
status: {}
```

```yaml
kubectl set image deploy alpine-deploy alpine-deploy=alpine:3.5
kubectl rollout undo deploy alpine-deploy
```


