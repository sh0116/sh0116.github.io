---
title: "Kubernetes - rook-ceph"
date: 2025-08-04 06:05:00 +0900
categories: [kubernetes]
tags: [Kubernetes]
description: Kubernetes 기초
toc: true
comments: true
---

# rook-ceph이란

온프레미스 환경에서  storage-class를 구성하는 도구

ceph은 파일 스토리지를 가상화시키는 클러스터를 구성할 수 있는 소프트웨어

직접 설치하는 방법도 있지만 rook패키지를 활용하면 쿠버네티스에서 보다 편히하게 ceph을 설치하고 관리할 수 있다.

## Rook-ceph Architecture

아래 회색의 Application이 Ceph Application이고 Rook을 통해서 pod화 하고 연결하는 과정

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/cbb8b20f-f959-4b43-b1d7-dffd346657f5/Untitled.png)

## 로컬 실습

### 요구 사항 

- Worker노드 3대 필요
- 각 Worker노드에 빈디스크가 필요

