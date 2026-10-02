---
source: knowledge-base
origin: notion
title: "Kubernetes - NameSpace "
area: "Kubernetes"
tags: ["area/kubernetes", "tech/kubernetes"]
created: "2025-08-04T06:05:00.000Z"
last_edited: "2025-08-04T06:27:00.000Z"
status: published
public: true
notion_id: "245172a5-56d6-8079-be03-edf4387b3635"
notion_url: "https://www.notion.so/Kubernetes-NameSpace-245172a556d68079be03edf4387b3635"
type: note
updated: 2026-07-07
---

# Kubernetes - NameSpace 

## 요약

Kubernetes 기초

Kubernetes 큰 주제 아래에서 세부 개념과 실습 절차를 연결하기 위한 노트입니다.

## 핵심 포인트

- Kubernetes 기초
- NameSpace
- Namespace 생성
- NameSpace 연습문제

## 지식 그래프

- [[wiki/mocs/Knowledge Base|Knowledge Base]]
- [[wiki/mocs/Kubernetes|Kubernetes]]

## 정리 내용

## NameSpace
- 리소스를 각각의 분리된 영역으로 나누기 좋은 방법
- 여러 네임스페이스를 사용하면 복잡한 쿠버네티스 시스템을 더 작은 그룹으로 분할
- 멀티 테넌트(multi-tenant) 환경을 분리하여 리소스를 생산, 개발, QA환경 등으로 사용
- 리소스 이름은 네임스페이스 내에서만 고유 명칭 사용
```yaml
kubectl get namespace
kubectl get ns
```
## Namespace 생성
```yaml
kubectl create ns ns이름 --dry-run -o yaml > yaml파일 이름
# yaml수정 
kubectl create -f yaml파일 이름
```
> [!note] k get pod → default ns가 기본값 → 기본값 바꾸고 싶으면 
~/.kube/config에서 namespace추가
![[_attachments/notion/Kubernetes---NameSpace/245172a556d6810d9c53fb18776b71f9.png]]
## NameSpace 연습문제
- 현재 시스템에는 몇 개의 Namespace가 존재하는가?
  ```yaml
kubectl get ns
  ```
  ![[_attachments/notion/Kubernetes---NameSpace/245172a556d681db9383f83a27b722c3.png]]
- Kube-system에는 몇 개의 포드가 존재하는가?
  ```yaml
kubectl get pod -n kube-system
  ```
  ![[_attachments/notion/Kubernetes---NameSpace/245172a556d681dfb5d6def7494a4a60.png]]
- ns-jenkins 네임스페이스를 생성하고 jenkins포드를 배치하라
  - pod image: jenkins
  - pod name : jenkins
  ```yaml
kubectl  create ns ns-jenkins --dry-run -o yaml > ns.yaml
kubectl  create -f ns.yaml --record=true

kubectl run jenkins --image=jenkins/jenkins --port 80 -n ns-jenkins
  ```
- coredns 는 어는 네임스페이스에 속해있는가?
  - Kube-system Namespace에 속함
  ![[_attachments/notion/Kubernetes---NameSpace/245172a556d6814c9fe0eefd0be23ccb.png]]

## 출처

- 원문: https://www.notion.so/Kubernetes-NameSpace-245172a556d68079be03edf4387b3635
- Vault path: wiki/notes/kubernetes/Kubernetes---NameSpace.md
