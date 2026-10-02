---
source: knowledge-base
origin: notion
title: "Kubernetes - POD란? "
area: "Kubernetes"
tags: ["area/kubernetes", "tech/kubernetes"]
created: "2025-08-04T06:05:00.000Z"
last_edited: "2025-08-04T06:27:00.000Z"
status: published
public: true
notion_id: "245172a5-56d6-8010-81a8-df4be27b44c0"
notion_url: "https://www.notion.so/Kubernetes-POD-245172a556d6801081a8df4be27b44c0"
type: note
updated: 2026-07-07
---

# Kubernetes - POD란? 

## 요약

Kubernetes 기초

Kubernetes 큰 주제 아래에서 세부 개념과 실습 절차를 연결하기 위한 노트입니다.

## 핵심 포인트

- Kubernetes 기초
- 포드, 팟, 파드 == pod의 특징
- POD 관리
- 네트워크 구조
- 컨테이너를 POD 전체에 적절하게 구성하는 방법

## 지식 그래프

- [[wiki/mocs/Knowledge Base|Knowledge Base]]
- [[wiki/mocs/Kubernetes|Kubernetes]]

## 정리 내용

### 포드, 팟, 파드 == pod의 특징
- 컨테이너의 공동 배포된 그룹이며 k8s 기본 빌딩 블록
- k8s 컨테이너를 개별적으로 배포하지 않고 컨테이너의 pod를 항상 배포하고 운영
- 일반적으로 단일 컨테이너지만 다수 컨테이너 포함도 가능
- 다수의 노드에서 실행되는것이 아니라 한 Node에서 독립적으로 실행
### POD 관리
- 장점
  - 밀접하게 연관된 프로세스를 함께 실행하고 마치 하나의 환경에서 동작하는 것 처럼 보임
  - 동일한 환경을 제공하면서 격리된 상태로 유지
- 동일한 pod의 컨테이너 사이의 부분 격리
  - pod의 모든 컨테이너는 동일한 네트워크 및 NameSpace에서 실행
  - 같은 호스트 이름 및 네트워크 인터페이스 공유(포트 충돌 주의)
  - POD의 모든 컨테이너는 동일한 IPC Namespace를 공유 IPC를 통해서 통신 가능
### 네트워크 구조
![[_attachments/notion/Kubernetes---POD란/245172a556d6817199bbd0e8a688d1b9.png]]
### 컨테이너를 POD 전체에 적절하게 구성하는 방법
![[_attachments/notion/Kubernetes---POD란/245172a556d6815b95bee1e0e491c24b.png]]
## POD 구성 Yaml파일
#### 파일 구성 요소
- apiVersion : Kubernetes API버전을 가르킴
- Kind : 어떤 리소스 유형인지 (pod, service, replica) 
- MetaData : pod와 관련된 이름, NameSpace, label 그 밖의 정보 존재
- Spec : 컨테이너 볼륨 정보 등등
- 상태 : pod상태, 컨테이너 설명, IPC 등등
```yaml
apiVersion: v1
kind: Pod
metadata:
name: memory-demo
namespace: mem-example
spec:
containers:
  -name: memory-demo-ctr
image: polinux/stress
resources:
requests:
memory: "100Mi"
limits:
memory: "200Mi"
command: ["stress"]
args: ["--vm", "1", "--vm-bytes", "150M", "--vm-hang", "1"]
```

## 출처

- 원문: https://www.notion.so/Kubernetes-POD-245172a556d6801081a8df4be27b44c0
- Vault path: wiki/notes/kubernetes/Kubernetes---POD란.md
