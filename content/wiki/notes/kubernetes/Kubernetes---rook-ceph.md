---
source: knowledge-base
origin: notion
title: "Kubernetes - rook-ceph "
area: "Kubernetes"
tags: ["area/kubernetes", "tech/kubernetes"]
created: "2025-08-04T06:05:00.000Z"
last_edited: "2025-08-04T06:27:00.000Z"
status: published
public: true
notion_id: "245172a5-56d6-805a-a0ad-d71d1bd74b41"
notion_url: "https://www.notion.so/Kubernetes-rook-ceph-245172a556d6805aa0add71d1bd74b41"
type: note
updated: 2026-07-07
---

# Kubernetes - rook-ceph 

## 요약

Kubernetes 기초

Kubernetes 큰 주제 아래에서 세부 개념과 실습 절차를 연결하기 위한 노트입니다.

## 핵심 포인트

- Kubernetes 기초
- rook-ceph이란
- Rook-ceph Architecture
- 로컬 실습
- 요구 사항

## 지식 그래프

- [[wiki/mocs/Knowledge Base|Knowledge Base]]
- [[wiki/mocs/Kubernetes|Kubernetes]]

## 정리 내용

## rook-ceph이란
온프레미스 환경에서  storage-class를 구성하는 도구
ceph은 파일 스토리지를 가상화시키는 클러스터를 구성할 수 있는 소프트웨어
직접 설치하는 방법도 있지만 rook패키지를 활용하면 쿠버네티스에서 보다 편히하게 ceph을 설치하고 관리할 수 있다.
### Rook-ceph Architecture
아래 회색의 Application이 Ceph Application이고 Rook을 통해서 pod화 하고 연결하는 과정
![[_attachments/notion/Kubernetes---rook-ceph/245172a556d681a9b995eeb8fc96af8e.png]]
### 로컬 실습
#### 요구 사항 
- Worker노드 3대 필요
- 각 Worker노드에 빈디스크가 필요
  - 새 disk  추가 및 lsblk확인 필요

## 출처

- 원문: https://www.notion.so/Kubernetes-rook-ceph-245172a556d6805aa0add71d1bd74b41
- Vault path: wiki/notes/kubernetes/Kubernetes---rook-ceph.md
