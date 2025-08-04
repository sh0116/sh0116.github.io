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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/8e23b497-f666-4afc-95a3-bec229baaa4c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GBCG5P6%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T072011Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIQCp0l8FEGZhuWkBdD229UTW11g0F0QZZ4Lw9r%2BYAwQ2KAIgD492twHILI7V56TzBOGm7rmEf4NhZ5KZsOSjIegbR38q%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDLh1DQ4eKE928%2FtQQCrcA91UAqNaJHV9KBZdm9oyn%2BibE5%2ByhWjfSTGOi0FZUx%2B3pZmvQ1ktqwfYrb93tvt%2FBdy76Tn6wHdnFogPMvWalZnjQ%2BOY7SSfUJaeZPBnJbG%2FuFa12I6rqIQlbrZppfYWTmJGtg76DgMCFjnxuUBCmdMvULjoBPilA%2BkjvRhlr8xqleAPzgTuT6nXlIJsQ%2FBYLR1Hzr59IfYnoVRgrfEBMGwwIqAxlYejr8dYrzHCJS65sQp0gKgUk8gesuec9Zgm6ZxI1i5c%2BWMMbaUk%2F89LMG7SqFqIeLmyEgELb5RNiaX8Uicytwq%2B0FOJwSKtzBjCza9u0TVDlz%2FSZiVO50%2FSBjYgyBTZk%2BwBBMFCkNOjgGNsBwS%2B0gTWiNFqfgtKMAowzXckCE2RGFGd4y%2BVk7dTFklFtIAQvrfXecVIrQmxP59t5k%2BvTqd9Y03HjiVuk%2B71%2Bu6%2FEVLWZAMQZ8yE2P27fNASwgZg53ETOlPIZONuY46vkNgNbXegTfYaRlhKRGNsT3hzz%2FK%2Bo8wIg7jFl0HIPOiXRU5GrlWXrLdfLc12ay697pZZgamc%2BzlCWE7%2FZC2Er5ud60qBUHfeVOSiGY0UpPnTFT4Q3C9Hb%2FOlcsBZqFQWLK8y6XdqNZYL39HjMKa3wcQGOqUBdmc4FlVYJ60d0AhfPBtD4LUFZxpGrRQ%2FOmfEgd2YDvYZjoQ62MjVb%2Brfbgr54ukGd8JbXvd23ZWh7hF9OBkolOPrpUSFagMnOLKA1FjOyghGP05cxcHGg%2Fm1IDE5sJqU4vCKw4fSGFdfpn4xiWEeBj273H%2F8euRcF0vJ4x3MvDjxgJXhiP2r7d1YF2JU0U%2FHKM8BhFPPrGLCYMaWJdjRIotV%2BiGK&X-Amz-Signature=2f5f1889c327b6b15c1c7b594ca1e4a20e4fb02a29ab4511270963a97ed00eb0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


