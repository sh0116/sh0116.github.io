---
source: knowledge-base
origin: notion
title: "Kubernetes - Storage "
area: "Kubernetes"
tags: ["area/kubernetes", "tech/kubernetes"]
created: "2025-08-04T06:05:00.000Z"
last_edited: "2025-08-04T06:27:00.000Z"
status: published
public: true
notion_id: "245172a5-56d6-8085-a3b6-c209275e551f"
notion_url: "https://www.notion.so/Kubernetes-Storage-245172a556d68085a3b6c209275e551f"
type: note
updated: 2026-07-07
---

# Kubernetes - Storage 

## 요약

Kubernetes 기초

Kubernetes 큰 주제 아래에서 세부 개념과 실습 절차를 연결하기 위한 노트입니다.

## 핵심 포인트

- Kubernetes 기초
- 쿠버네티스 Storage 개념
- 불륨(Volume)
- EmptyDir 을 활용한 파일 시스템 공유
- EmptyDir 연습문제

## 지식 그래프

- [[wiki/mocs/Knowledge Base|Knowledge Base]]
- [[wiki/mocs/Kubernetes|Kubernetes]]

## 정리 내용

## 쿠버네티스 Storage 개념
#### 불륨(Volume)
- 컨테이너가 외부 스토리지에 엑세스하고 공유하는 방법
- POD의 컨테이너에는 고유의 분리된 파일 시스템이 존재
- Volume은 POD의 컴포넌트이며 POD의 스펙에 의해 정의
- 독립적인 쿠버네티스의 오브젝트가 아니며 스스로 생성, 삭제 불가
- 각 컨테이너의 파일 시스템의 불륨을 마운트하여 생성
![[_attachments/notion/Kubernetes---Storage/245172a556d6813f9afffcc9e5fcf105.png]]
- 임시 볼륨 : 
  - 컨테이너가 파괴되면 불륨도 같이 파괴
  - 컨테이너끼리 데이터 공유를 위한 시스템
- 로컬 볼륨 :
  - 로컬 == Node
  - pod가 위치한 Node에서 파일 시스템을 연동
  - Node가 다르면 데이터가 달라짐
- 네트워크 볼륨 :
  - 클러스터 외부에 있는 볼륨
  - NFS : Network File System 이런 류
- 네트워크 볼륨 (클라우드 종속) :
  - AWS, GCP, 등등
## EmptyDir 을 활용한 파일 시스템 공유
![[_attachments/notion/Kubernetes---Storage/245172a556d6819db664c6936625c733.png]]
### EmptyDir 연습문제
- 하나의 프로세스는 랜덤한 값을 생성 (count 이미지 사용)
- 하나의 프로세스는 랜덤한 값을 출력 (httpd이미지 사용)

## 출처

- 원문: https://www.notion.so/Kubernetes-Storage-245172a556d68085a3b6c209275e551f
- Vault path: wiki/notes/kubernetes/Kubernetes---Storage.md
