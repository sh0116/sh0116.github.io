---
source: knowledge-base
origin: notion
title: "Kubernetes - Kube-Proxy "
area: "Kubernetes"
tags: ["area/kubernetes", "tech/kubernetes"]
created: "2025-08-04T06:05:00.000Z"
last_edited: "2025-08-04T06:27:00.000Z"
status: published
public: true
notion_id: "245172a5-56d6-809b-8200-c04b44cc3481"
notion_url: "https://www.notion.so/Kubernetes-Kube-Proxy-245172a556d6809b8200c04b44cc3481"
type: note
updated: 2026-07-07
---

# Kubernetes - Kube-Proxy 

## 요약

Kubernetes 기초

Kubernetes 큰 주제 아래에서 세부 개념과 실습 절차를 연결하기 위한 노트입니다.

## 핵심 포인트

- Kubernetes 기초
- Kube Proxy
- Kube-Proxy란

## 지식 그래프

- [[wiki/mocs/Knowledge Base|Knowledge Base]]
- [[wiki/mocs/Kubernetes|Kubernetes]]

## 정리 내용

## Kube Proxy
![[_attachments/notion/Kubernetes---Kube-Proxy/245172a556d681a6a644dffd339c97a2.png]]
각 Node 안쪽에 Kube-proxy가 위치한것을 볼 수 있다.
#### Kube-Proxy란
K8s에서 Network를 담당하는 컴포넌트이다.
각 Node에 Proxy가 하나씩 있고, DaemonSet형태로 Kubernetes에 존재한다.
![[_attachments/notion/Kubernetes---Kube-Proxy/245172a556d68154a2bbed32d8ab6583.png]]
![[_attachments/notion/Kubernetes---Kube-Proxy/245172a556d68157914aca4d21280c56.png]]
클라이언트(사용)가 쿠버네티스 API로 정의한 서비스에 연결할 수 있도록 해주는 역할을 한다. 서비스의 IP와 Port로 들어온 접속을 서비스를 지원하는 POD중 하나로 연결해 준다.
![[_attachments/notion/Kubernetes---Kube-Proxy/245172a556d6812d8647c4105a66d2f7.png]]
커널 iptables를 활용하여 연결한다.
![[_attachments/notion/Kubernetes---Kube-Proxy/245172a556d6814f87f7d9e9ea50a25c.png]]

## 출처

- 원문: https://www.notion.so/Kubernetes-Kube-Proxy-245172a556d6809b8200c04b44cc3481
- Vault path: wiki/notes/kubernetes/Kubernetes---Kube-Proxy.md
