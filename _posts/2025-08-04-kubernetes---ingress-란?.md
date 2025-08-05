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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/8e23b497-f666-4afc-95a3-bec229baaa4c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663RQSGNEZ%2F20250805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250805T002653Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJHMEUCIHqmoyxfAqUeK1%2FrPy3tNrfXB3tce72J3WSvG5P2d7OwAiEAzkKX%2Fgwm6vhLd8zvltSJLJwrzpyPfu93Wgrw2TKI1y4q%2FwMIUBAAGgw2Mzc0MjMxODM4MDUiDD%2FQn5LhSMFoeuDPPSrcA0vE9t4O41B1Xn5S0TmsFcCpri6814fz6xOhQPXxlnANEEr5zhnFSBrrsIbEYq974npcmg%2BWU3Cu6NU%2BKlehO3SS22LvVMouHQ%2FpWxFhohngwOztUxufcKw8S2LOHGwRJqfJWsCNSW7usTVuPUij89ew1WEYWiQXV%2BoP0oPzhGdUh8cUaIRzVvf9iSSSQDKWqTVYIoVA02iIqz4cfUi3NKS1qrfgiST7nUAKk0uzhhgD4j5hKreCztuTfTS%2FVaanjwA6WziccdL%2B880YRBl00z6jNlub3HImiU4%2B6R7KSc3%2B3xMl6XqyHjccZjX%2BYH999ug8599RgnMScjgQIZGL1J5oLVON03FxznCp%2FaosW%2FYqP5cR4zYbiLpzdGuSbIfVKsd5VIWN4RAKLvRsjLI1v1%2FF1NatNuwIlmRMNI8mRBBLDK898VNutlU7zA8umguSRfh6cGAYZbD8r6OIv3eIyW8tLH%2BQkWeKhHY35Tm1itjBcWE9YCYBYoVKKWrmy7HJ60ImFixr4cRhHgHSP7Kis0Q1ifmXFOXfCmn8Fre397SzkG71H%2F0sDZa293ToDPSAIbU9%2FXfyQTbsn8jHt8bcOgxWIISk3OUivYYnVCezQ%2FCyNV%2BcsMceNOChNRDyMJ70xMQGOqUB1O7aQMTeXLZMcOYuApmNrI5Oma32m7MtM3LTySkbgQOTllmCogeYnRzpyX%2B14vGrkcgRyFubQ6EIR%2F%2F7%2BuCL3gdPedJiaZxImSVyNhKEx%2Fb0VKxQq28y5bs%2FQ7UnyuXWS8LyFcq6yAnb%2BWZs4bDdNfPNHhWCQRbw9%2Bkd2%2Bi7kcU46%2F3c%2Bi9GXELPZREsSAuGyeUwh%2F6gcDtxdqALrFVhozpYSEMJ&X-Amz-Signature=e3df579c42949e5cda6a5867b58a655d0c4f4831a6c6fd5ccc9b92c653774823&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


