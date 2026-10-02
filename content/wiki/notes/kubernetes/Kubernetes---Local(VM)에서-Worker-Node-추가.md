---
source: knowledge-base
origin: notion
title: "Kubernetes - Local(VM)에서 Worker Node 추가 "
area: "Kubernetes"
tags: ["area/kubernetes", "tech/kubernetes"]
created: "2025-08-04T06:05:00.000Z"
last_edited: "2025-08-04T06:27:00.000Z"
status: published
public: true
notion_id: "245172a5-56d6-807b-a34b-d310079ee4bc"
notion_url: "https://www.notion.so/Kubernetes-Local-VM-Worker-Node-245172a556d6807ba34bd310079ee4bc"
type: note
updated: 2026-07-07
---

# Kubernetes - Local(VM)에서 Worker Node 추가 

## 요약

Kubernetes 기초

Kubernetes 큰 주제 아래에서 세부 개념과 실습 절차를 연결하기 위한 노트입니다.

## 핵심 포인트

- Kubernetes 기초
- Master Node와 기존에 이미 Worker Node가 있는 경우입니다

## 지식 그래프

- [[wiki/mocs/Knowledge Base|Knowledge Base]]
- [[wiki/mocs/Kubernetes|Kubernetes]]

## 정리 내용

#### Master Node와 기존에 이미 Worker Node가 있는 경우입니다
VMWare Pro환경
1. 기존 WorkNode의 스냅샵을 복사해서 열어준다
![[_attachments/notion/Kubernetes---Local(VM)에서-Worker-Node-추가/245172a556d681a69129daf4668b3021.png]]
1. Workstation에서 스냅샷을 열어준다
![[_attachments/notion/Kubernetes---Local(VM)에서-Worker-Node-추가/245172a556d68171a83bc28a243243c1.png]]
1. 기존 Node들을 종료하고 새로운 Node를 실행한다.
1. 네트워크 설정이 있었다면 바꿔준다.
  1. 고정 IP를 할당해서 바꿔줘야했다.
  ![[_attachments/notion/Kubernetes---Local(VM)에서-Worker-Node-추가/245172a556d681f6a430f6fd5b4f3d4c.png]]
1. kubeadm 초기화
```yaml
kubeadm reset
```
1. Master Node로 돌아가서 token을 생성한다.
```yaml
kubeadm token create -h #도움말
kubeadm token create --print-join-command #토큰 명령어
--> 결과값을 새로 생성한 Node에 복붙해주면 된다
```
![[_attachments/notion/Kubernetes---Local(VM)에서-Worker-Node-추가/245172a556d681f5a680ff5efab4ac7f.png]]

## 출처

- 원문: https://www.notion.so/Kubernetes-Local-VM-Worker-Node-245172a556d6807ba34bd310079ee4bc
- Vault path: wiki/notes/kubernetes/Kubernetes---Local(VM)에서-Worker-Node-추가.md
