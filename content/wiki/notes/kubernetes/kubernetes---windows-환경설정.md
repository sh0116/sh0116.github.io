---
source: knowledge-base
origin: notion
title: "kubernetes - windows 환경설정 "
area: "Kubernetes"
tags: ["area/kubernetes", "tech/kubernetes"]
created: "2025-08-04T06:05:00.000Z"
last_edited: "2025-08-04T06:27:00.000Z"
status: published
public: true
notion_id: "245172a5-56d6-807c-aa01-e85b9f194d36"
notion_url: "https://www.notion.so/kubernetes-windows-245172a556d6807caa01e85b9f194d36"
type: note
updated: 2026-07-07
---

# kubernetes - windows 환경설정 

## 요약

Kubernetes 기초

Kubernetes 큰 주제 아래에서 세부 개념과 실습 절차를 연결하기 위한 노트입니다.

## 핵심 포인트

- Kubernetes 기초
- Windows 로컬에서 쿠버네티스 환경 구축 방법
- Master Node와 Worker Node 구축
- 네트워크 설정
- 각 OS Hostname설정

## 지식 그래프

- [[wiki/mocs/Knowledge Base|Knowledge Base]]
- [[wiki/mocs/Kubernetes|Kubernetes]]

## 정리 내용

### Windows 로컬에서 쿠버네티스 환경 구축 방법
VMware를 사용하여 구축
### Master Node와 Worker Node 구축
vmware에 동일한 os 3개를 만든다.
![[_attachments/notion/kubernetes---windows-환경설정/245172a556d681beaa9dc0b840c04165.png]]
### 네트워크 설정
아래 링크처럼 네트워크 설정을 진행하면 된다.
[Untitled](https://www.notion.so/b38afbf42c2a4c35a4b2706089788550) 
나의 경우는 vmware로 켜놓고 로컬 터미널(파워쉘)에서 ssh로 접속해서 사용중입니당 
(windows11의 경우 터미널 구성이 잘되어있어서 vmware보다 편함)
![[_attachments/notion/kubernetes---windows-환경설정/245172a556d6816bb0c1d3524bcd0bb9.png]]
### 각 OS Hostname설정
아래의 경우 master노드 mater0라는 호스트네임 설정 방법
각 워커노드도 똑같이 설
```bash
sudo hostnamectl set-hostname master0
sudo vim /etc/hosts
	# 기존 호스트 이름에서 바꾼 호스트 이름으로 적용 후 저장
```
![[_attachments/notion/kubernetes---windows-환경설정/245172a556d681c6a49dfeaf6288c522.png]]

## 출처

- 원문: https://www.notion.so/kubernetes-windows-245172a556d6807caa01e85b9f194d36
- Vault path: wiki/notes/kubernetes/kubernetes---windows-환경설정.md
