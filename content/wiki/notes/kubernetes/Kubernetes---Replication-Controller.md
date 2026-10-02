---
source: knowledge-base
origin: notion
title: "Kubernetes - Replication Controller "
area: "Kubernetes"
tags: ["area/kubernetes", "tech/kubernetes"]
created: "2025-08-04T06:05:00.000Z"
last_edited: "2025-08-04T06:27:00.000Z"
status: published
public: true
notion_id: "245172a5-56d6-8088-ae3f-d30f74351dce"
notion_url: "https://www.notion.so/Kubernetes-Replication-Controller-245172a556d68088ae3fd30f74351dce"
type: note
updated: 2026-07-07
---

# Kubernetes - Replication Controller 

## 요약

Kubernetes 기초

Kubernetes 큰 주제 아래에서 세부 개념과 실습 절차를 연결하기 위한 노트입니다.

## 핵심 포인트

- Kubernetes 기초
- ReplicaSet & replication controller
- replication controller 세가지 요소
- replication controller 장점
- replication controller YAML 작성

## 지식 그래프

- [[wiki/mocs/Knowledge Base|Knowledge Base]]
- [[wiki/mocs/Kubernetes|Kubernetes]]

## 정리 내용

### ReplicaSet & replication controller
- pod 가 항상 실행되도록 유지하는 쿠버네티스 리소스
- 노드가 클러스터에서 사라지는 경우 해당 pod를 감지하고 대체 pod생성
- 실행 중인 pod의 목록을 지속적으로 모니터링으로 하고 ‘유형’ 의 실제 pod수가 원하는 수와 항상 일치하는지 확인
![[_attachments/notion/Kubernetes---Replication-Controller/245172a556d681d79f96f3c6f432d774.png]]
> [!note] 장애 발생 후 5분간 지연시간을 주고 대체 노드를 생성
만약 장애가 아닌 경우, 리소스 낭비를 방지하기 위해 지연 시간을 줌
### replication controller 세가지 요소
- 관리하는 pod범위를 결정하는 레이블 셀렉터
- 실행해야하는 pod의 수를 결정하는 복제본 수
- 새로운 pod의 모양을 설명하는 pod템플릿
### replication controller 장점 
- pod가 없는 경우 새 pod 항상 실행
- 노드에 장애 발생 시 다른 노드에 복제본 생성
- 수동, 자동으로 수평 스케일
### replication controller YAML 작성
```yaml
apiVersion: v1
kind: ReplicationController
metadata:
  name: nginx
spec:
  replicas: 3
  selector:
    app: nginx
  template:
    metadata:
      name: nginx
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx
        ports:
        - containerPort: 80
```
### replication controller 조회
```bash
kubectl get  rc #replicationcontrolle 줄임
```
```bash
kubectl describe rc rc이름 #상세 정보 확인 (이벤트 로그 확인 가능)
```
### replication controller 수정
```bash
kubectl scale rc rc이름 --replicas=5 # replica를 5로 늘리는 수정

kubectl edit rc rc이름 # 설정 파일 수정 가능 (vim형태)
```
### replication controller 삭제
```bash
kubectl delete rc rc이름 # rc삭제
kubectl delete rc rc이름 --cascade=false # 실행된 pod는 유지 rc는 삭제
```
### replication controller node 장애 
- 여러 노드에 분산 배치된 pod가 있을 때 만약 한 노드에서 장애가 발생하면 
  다른 노드에 분산 배치한다. (기존 노드는 terminating종료 한다. 하지만 장애 노드이기 때문에 정상 종료는 안되고 명령 대기 상태로 남는다)
![[_attachments/notion/Kubernetes---Replication-Controller/245172a556d681c0ab75e67d9a8e5df2.png]]

## 출처

- 원문: https://www.notion.so/Kubernetes-Replication-Controller-245172a556d68088ae3fd30f74351dce
- Vault path: wiki/notes/kubernetes/Kubernetes---Replication-Controller.md
