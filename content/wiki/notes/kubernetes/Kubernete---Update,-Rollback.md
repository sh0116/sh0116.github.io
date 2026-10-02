---
source: knowledge-base
origin: notion
title: "Kubernete - Update, Rollback"
area: "Kubernetes"
tags: ["area/kubernetes", "tech/kubernetes"]
created: "2025-08-04T06:05:00.000Z"
last_edited: "2025-08-04T06:27:00.000Z"
status: published
public: true
notion_id: "245172a5-56d6-806b-8b6d-dfc14356d62e"
notion_url: "https://www.notion.so/Kubernete-Update-Rollback-245172a556d6806b8b6ddfc14356d62e"
type: note
updated: 2026-07-07
---

# Kubernete - Update, Rollback

## 요약

Kubernetes 기초

Kubernetes 큰 주제 아래에서 세부 개념과 실습 절차를 연결하기 위한 노트입니다.

## 핵심 포인트

- Kubernetes 기초
- Application Rolling Update & RollBack
- Update 실습
- 업데이트
- 업데이트 결과

## 지식 그래프

- [[wiki/mocs/Knowledge Base|Knowledge Base]]
- [[wiki/mocs/Kubernetes|Kubernetes]]

## 정리 내용

### Application Rolling Update & RollBack
## Update 실습
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
#### 업데이트 
```yaml
kubectl set image deploy http-go-deployment http-go=seokhyeon116/http-go:v2
# set image를 통해서 업데이트
kubectil edit deploy http-go-deployment # image에서 버전 변경
```
업데이트 방식이 RollingUpdate이다
- maxSurge : 최대로 생성할 수 있는 POD의 수를 정한다 (예를 들어 설정값이 30%이면 전체 POD에서 130%까지 만들 수 있다.) 
- maxUnavailable : 사용할 수 없는 최대 POD수를 정한다 (예를 들어 설정값이 30%이면 전체 POD의 70% 이상으로 항상 유지한다.)
  ![[_attachments/notion/Kubernete---Update,-Rollback/245172a556d6814393d6e1e0354b761b.png]]
```yaml
kubectl get pod -o wide #명령어 실행 시 아래 화면을 볼 수 있다.
# 노드를 하나씩 업데이하고 생성과 제거를 병행한다.
```
![[_attachments/notion/Kubernete---Update,-Rollback/245172a556d68130988dd820d7f51189.png]]
## 업데이트 결과
#### v1
![[_attachments/notion/Kubernete---Update,-Rollback/245172a556d681d59b96fcf63a67a1d0.png]]

#### v2
![[_attachments/notion/Kubernete---Update,-Rollback/245172a556d6817998c2f5c35fc7b35e.png]]
> [!note] replicaSet → 유지된다
![[_attachments/notion/Kubernete---Update,-Rollback/245172a556d681038fddcffb11efe316.png]]
### RollBack하기
```yaml
kubectl rollout undo deploy http-go-deployment #한단계전으로 undeo
kubectl rollout undo deploy http-go-deployment --to-revision=1 #history 1번으로 돌아감

kubectl rollout history deploy http-go-deployment #해당 delpoy history 출력
# create할 때 --record=true를 해야 명령줄까지 출력됨
```
ㅏ
## 연습 문제
- alpine이미지 사용하여 업데이트와 롤백을 실행하라, 모든 revision내용은 기록되어야 한다.
  - alpine:3.4 이미지를 사용하여 deployment를 생성하라
  - replicas: 10
  - maxSurge:50%
  - maxUnavailable: 50%
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

## 출처

- 원문: https://www.notion.so/Kubernete-Update-Rollback-245172a556d6806b8b6ddfc14356d62e
- Vault path: wiki/notes/kubernetes/Kubernete---Update,-Rollback.md
