---
source: knowledge-base
origin: notion
title: "Kubernetes - Service 란? "
area: "Kubernetes"
tags: ["area/kubernetes", "tech/kubernetes"]
created: "2025-08-04T06:05:00.000Z"
last_edited: "2025-08-04T06:27:00.000Z"
status: published
public: true
notion_id: "245172a5-56d6-80f5-931a-f3242116e52f"
notion_url: "https://www.notion.so/Kubernetes-Service-245172a556d680f5931af3242116e52f"
type: note
updated: 2026-07-07
---

# Kubernetes - Service 란? 

## 요약

Kubernetes 기초

Kubernetes 큰 주제 아래에서 세부 개념과 실습 절차를 연결하기 위한 노트입니다.

## 핵심 포인트

- Kubernetes 기초
- Services
- 서비스 세션 고정하기✨

## 지식 그래프

- [[wiki/mocs/Knowledge Base|Knowledge Base]]
- [[wiki/mocs/Kubernetes|Kubernetes]]

## 정리 내용

## Services
-  외부 클라이언트가 몇 개이든지 프론트엔드 pod로 연결
- 프론트엔드는 다시 백엔드 데이터베이스로 연결
- pod의 IP가 변결 될 때마다 재설정 하지 않도록 해야함
- → 결론 : 로드벨런싱 기
![[_attachments/notion/Kubernetes---Service-란/245172a556d681a9a2cbc342c02dcbc5.png]]
### 서비스 세션 고정하기✨
> [!note] 여러 POD에 세션이 모두 다르다 따라서 한 IP에서 들어갈 POD를 고정해주는 작업
→ sessionAffinity → 세션 친밀감(?) → ClientIP 를 넣으면 한 POD에 배정된다.
![[_attachments/notion/Kubernetes---Service-란/245172a556d68167a00edafa324fa305.png]]
http-go-5768858844-p99jx로 고정된것을 
확인할 수 있다.

![[_attachments/notion/Kubernetes---Service-란/245172a556d681ea8a98d6004895fddf.png]]

## 출처

- 원문: https://www.notion.so/Kubernetes-Service-245172a556d680f5931af3242116e52f
- Vault path: wiki/notes/kubernetes/Kubernetes---Service-란.md
