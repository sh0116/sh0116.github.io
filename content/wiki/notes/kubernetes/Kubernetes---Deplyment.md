---
source: knowledge-base
origin: notion
title: "Kubernetes - Deplyment "
area: "Kubernetes"
tags: ["area/kubernetes", "tech/kubernetes"]
created: "2025-08-04T06:05:00.000Z"
last_edited: "2025-08-04T06:27:00.000Z"
status: published
public: true
notion_id: "245172a5-56d6-8040-aec5-e2060fe5fc63"
notion_url: "https://www.notion.so/Kubernetes-Deplyment-245172a556d68040aec5e2060fe5fc63"
type: note
updated: 2026-07-07
---

# Kubernetes - Deplyment 

## 요약

Kubernetes 기초

Kubernetes 큰 주제 아래에서 세부 개념과 실습 절차를 연결하기 위한 노트입니다.

## 핵심 포인트

- Kubernetes 기초
- Deployment
- 업데이트 전략
- Deployment 실습
- Jenkins deployment 생성 - deploy-jenkins

## 지식 그래프

- [[wiki/mocs/Knowledge Base|Knowledge Base]]
- [[wiki/mocs/Kubernetes|Kubernetes]]

## 정리 내용

### Deployment
- Application을 다운 타입 없이 업데이트 가능하도록 도와주는 리소스!
- ReplicaSet과 Replication Controller 상위에 배포되는 리소스
![[_attachments/notion/Kubernetes---Deplyment/245172a556d681f9a84bfc3e4b9e075a.png]]
#### 업데이트 전략
- recreate 
  - Recreate의 경우 기존 파드를 모두 삭제한 다음 새로운 파드를 생성하는 방법입니다. ( 무중단 방식이 아닙니다. 다운타임 발생합니다. )
- Rolling Update :
  - 롤링 업데이트란 새 버전을 배포하면서, 새 버전 파드를 하나씩 늘려가고 기존 버전의 파드를 하나씩 줄여나가는 방식입니다. 무중단 배포 라고도 합니다.
## Deployment 실습
- Jenkins deployment 생성 - deploy-jenkins
- jenkins deployment로 배포되는 앱을 app : jenkins-test로 레이블링
- deployment로 배포된 pod를 하나 삭제하고 이후 생성되는 포드를 관찰
- 새로 생성된 pod의 레이블을 바꿔 deployment 관리영역에서 벗어나게 하라
- scale명령으로 사용할 replica 수 를 5개로 정의
- edit 기능을 사용하여 10로 스켈일링
#### Jenkins deployment 생성 - deploy-jenkins
```yaml
kubectl create -f yaml이름
```
#### jenkins deployment로 배포되는 앱을 app : jenkins-test로 레이블링
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
#### deployment로 배포된 pod를 하나 삭제하고 이후 생성되는 포드를관찰
```bash
kubectl delete pod pod명
kubectl get pod -w --show-labels
```
#### 새로 생성된 pod의 레이블을 바꿔 deployment 관리영역에서 벗어나게 하라
```bash
k label pod deploy-jenkins-69d6b7df8c-mjc2m app-
```
#### scale명령으로 사용할 replica 수 를 5개로 정의
```yaml
kubectl scale deploy deploy이름 --replicas=5
```
#### edit 기능을 사용하여 10로 스켈일링
```yaml
kubectl edit deploy deploy이름
```
![[_attachments/notion/Kubernetes---Deplyment/245172a556d681a099bbda66921bca0a.png]]
### 제목 없음

## 출처

- 원문: https://www.notion.so/Kubernetes-Deplyment-245172a556d68040aec5e2060fe5fc63
- Vault path: wiki/notes/kubernetes/Kubernetes---Deplyment.md
