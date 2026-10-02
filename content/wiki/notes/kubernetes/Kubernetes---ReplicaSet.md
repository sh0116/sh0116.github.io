---
source: knowledge-base
origin: notion
title: "Kubernetes - ReplicaSet "
area: "Kubernetes"
tags: ["area/kubernetes", "tech/kubernetes"]
created: "2025-08-04T06:05:00.000Z"
last_edited: "2025-08-04T06:27:00.000Z"
status: published
public: true
notion_id: "245172a5-56d6-806d-80dd-f2bbbe31eb56"
notion_url: "https://www.notion.so/Kubernetes-ReplicaSet-245172a556d6806d80ddf2bbbe31eb56"
type: note
updated: 2026-07-07
---

# Kubernetes - ReplicaSet 

## 요약

Kubernetes 기초

Kubernetes 큰 주제 아래에서 세부 개념과 실습 절차를 연결하기 위한 노트입니다.

## 핵심 포인트

- Kubernetes 기초
- ReplicaSet
- ReplicatSet & Replication Controller 차이점
- ReplicaSet 생성
- ReplicaSet 실습

## 지식 그래프

- [[wiki/mocs/Knowledge Base|Knowledge Base]]
- [[wiki/mocs/Kubernetes|Kubernetes]]

## 정리 내용

## ReplicaSet
- ReplicaSet은 차세대 Replication Controller로 완전히 대체 가능함
- 초기 쿠버네티스에서 제공했기 때문에 현장에서는 여전히 계속 사용중인 경우 존재
- 일반적으로 ReplicaSet을 직접 생성하지 않고 상위 수준의 Deployment 리소스를 만들 때 자동으로 생성
### ReplicatSet & Replication Controller 차이점
![[_attachments/notion/Kubernetes---ReplicaSet/245172a556d681b9b4e2df3c434e099b.png]]
### ReplicaSet 생성
replication 보다 업그레이드되었고 metchExp를 추가하여 label 조건에 더 자유롭
![[_attachments/notion/Kubernetes---ReplicaSet/245172a556d6811b9692d61ecbb61deb.png]]
## ReplicaSet 실습
- nginx 3개를 생성하는 rs-nginx 생성하라
- rs-nginx pod의 개수를 10개로 스케일링하라
#### nginx 3개를 생성하는 rs-nginx 생성하라
```yaml
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: rs-nginx
spec:
  # modify replicas according to your case
  replicas: 3
  selector:
    matchLabels:
      app: replica
  template:
    metadata:
      labels:
        app: replica
    spec:
      containers:
      - name: rs-nginx
        image: nginx
```
```yaml
kubectl creat -f yaml이름
```
#### rs-nginx pod의 개수를 10개로 스케일링하라
```yaml
kubectl edit rs rs이름
```
![[_attachments/notion/Kubernetes---ReplicaSet/245172a556d681818236ed37360fc407.png]]

## 출처

- 원문: https://www.notion.so/Kubernetes-ReplicaSet-245172a556d6806d80ddf2bbbe31eb56
- Vault path: wiki/notes/kubernetes/Kubernetes---ReplicaSet.md
