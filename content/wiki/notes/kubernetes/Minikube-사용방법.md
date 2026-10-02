---
source: knowledge-base
origin: notion
title: "Minikube 사용방법 "
area: "Kubernetes"
tags: ["area/kubernetes", "tech/kubernetes"]
created: "2025-08-04T06:05:00.000Z"
last_edited: "2025-08-04T06:27:00.000Z"
status: published
public: true
notion_id: "245172a5-56d6-8025-be5d-f58381572b72"
notion_url: "https://www.notion.so/Minikube-245172a556d68025be5df58381572b72"
type: note
updated: 2026-07-07
---

# Minikube 사용방법 

## 요약

Kubernetes 기초

Kubernetes 큰 주제 아래에서 세부 개념과 실습 절차를 연결하기 위한 노트입니다.

## 핵심 포인트

- Kubernetes 기초
- 개요
- 1. 도커 설치하기
- 2. minikube 설치하기
- 3. 실행하기

## 지식 그래프

- [[wiki/mocs/Knowledge Base|Knowledge Base]]
- [[wiki/mocs/Kubernetes|Kubernetes]]

## 정리 내용

### 개요
Minikube는 VM환경에서 Kubernetes 클러스터를 가상으로 구현한다.
### 1. 도커 설치하기
```bash
sudo apt install docker.io -y
```
### 2. minikube 설치하기
```bash
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube_latest_amd64.deb
sudo dpkg -i minikube_latest_amd64.deb
```
### 3. 실행하기
```bash
minikube start --driver=docker
```
### 4. Kubectl로 pod조회
```bash
kubectl get pods
```
### minikube SSH로 접속하기
```bash
minikube ssh
```
## 아키텍처
![[_attachments/notion/Minikube-사용방법/245172a556d6816da5dbd06d64952f2c.png]]
![[_attachments/notion/Minikube-사용방법/245172a556d681468535ef1d8619c694.png]]
### 출처
- https://blog.naver.com/isc0304/221879359568

## 출처

- 원문: https://www.notion.so/Minikube-245172a556d68025be5df58381572b72
- Vault path: wiki/notes/kubernetes/Minikube-사용방법.md
