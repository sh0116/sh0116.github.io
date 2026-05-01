---
title: "Kubernetes - Ingress 란?"
date: 2025-08-04 06:05:00 +0900
categories: [kubernetes]
tags: [Kubernetes]
description: Kubernetes 기초
toc: true
comments: true
---

# Ingress 

인그레스는 클러스터 외부에서 클러스터 내부 서비스로 HTTP와 HTTPS 경로를 노출한다. 트래픽 라우팅은 인그레스 리소스에 정의된 규칙에 의해 컨트롤된다.

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/8e23b497-f666-4afc-95a3-bec229baaa4c/Untitled.png)

## Ingress-nginx 

프라이빗 환경에서 인그레스를 사용할 수 있도록 Nginx설치

쿠버네티스에 pod형식으로 띄워서 설정

## 인그레스 룰

| 종류 | 경로 | 요청 경로 | 일치 여부 |
| --- | --- | --- | --- |
| Prefix | `/` | (모든 경로) | 예 |
| Exact | `/foo` | `/foo` | 예 |
| Exact | `/foo` | `/bar` | 아니오 |
| Exact | `/foo` | `/foo/` | 아니오 |
| Exact | `/foo/` | `/foo` | 아니오 |
| Prefix | `/foo` | `/foo`, `/foo/` | 예 |
| Prefix | `/foo/` | `/foo`, `/foo/` | 예 |
| Prefix | `/aaa/bb` | `/aaa/bbb` | 아니오 |
| Prefix | `/aaa/bbb` | `/aaa/bbb` | 예 |
| Prefix | `/aaa/bbb/` | `/aaa/bbb` | 예, 마지막 슬래시 무시함 |
| Prefix | `/aaa/bbb` | `/aaa/bbb/` | 예, 마지막 슬래시 일치함 |
| Prefix | `/aaa/bbb` | `/aaa/bbb/ccc` | 예, 하위 경로 일치함 |
| Prefix | `/aaa/bbb` | `/aaa/bbbxyz` | 아니오, 문자열 접두사 일치하지 않음 |
| Prefix | `/`, `/aaa` | `/aaa/ccc` | 예, `/aaa` 접두사 일치함 |
| Prefix | `/`, `/aaa`, `/aaa/bbb` | `/aaa/bbb` | 예, `/aaa/bbb` 접두사 일치함 |
| Prefix | `/`, `/aaa`, `/aaa/bbb` | `/ccc` | 예, `/` 접두사 일치함 |
| Prefix | `/aaa` | `/ccc` | 아니오, 기본 백엔드 사용함 |
| Mixed | `/foo` (Prefix), `/foo` (Exact) | `/foo` | 예, Exact 선호함 |


