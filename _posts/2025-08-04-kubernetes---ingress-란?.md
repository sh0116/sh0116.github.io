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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/8e23b497-f666-4afc-95a3-bec229baaa4c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X63OFAQG%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T071408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIFFeIecW48Rm59AtUbObtE4vnAcQlpg3rOYi3lmf3eSAAiEAoCswbeCC7pTdLxPsl5av%2BFtSKt4lHx6ffteCUav%2BLqUq%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDHrOBtxGc%2B13XPGVKSrcA2Ip31JKd5GhqeVvJC94X0KIIIY7NHABhK0uOkyxl7UKIKhZos%2B1T12AnJ08KvBgMkbsS9Zih88mKbMJYsVBr1kdIOpU1RCDwHkRZ1O9WHTc7z2azLM8s%2FK%2BUNMp6v3BHOllAQjazcdWuJU5JyceeGK1up9e71bM%2BYmgCk9M5GZbk3aslYT0UvJ32UqC7cuRfpmLneYks1UDxGzE6OBVZgEhBtLqzJxRk5SsI0IZTlwN3wvmg3Gxpg218YTNR1Gd6Fkep%2FfLhvDPFlNMPms7AIvJOVWrkd9UXC6u6MWjRacnNlZ4jD%2FbekVcvOB2GubgsOSJfLI8aKwqVIYERntAzAUKRA2yRBWScBRcb%2BVyYCOjTadXvmSeoMQGN%2Bf5Y6dfg3ZU4HQe2fqUhmOqHHrxnSWf2wmc3Xkbea0L5KYTW%2BRSkvOd46xqp2IoFNuOOso43AJNwB4dpiqj09F4peozXvJ%2BbsbrnZl2yWJQgY0lx1OepW6F7CNDtETBol1pLdidCm7pekOWIzYlMJ1%2BElqLLbj8%2FJQqKHwRlCcAtUPAwZM%2BUXrxDL%2FQt26JvT2xLdcXicjVxnGvzzoqLanV08%2BVouUSb%2Btp8LNFXDlgUkul%2BXkTB7l8wYI1pmA8nTHVMOO3wcQGOqUBXTUvOTdJnWcINJihxiwKV2EFxgGWBwIZHgjh04Y4svZGvFT8sYgbMSQiwBIp7rN2gMSxJYJRUT7CxHBfUXGTTXHfWv5Cmh4QqIuKbIHhMCUnxKvYMl4EHHRepUR%2FKdqcoKn5%2F56VYSxCpLUUUePqusNfuGnxmM3YysgmMG1sCcbIlGaWO0%2Bg8Osnhd8ZYD6z8AQ1yzJK8cJ5%2BzaglIHt90OHOCqN&X-Amz-Signature=fe6ca896c8ff58561760c5adf7d47127e23a9c09355b2901667308e555f5fa86&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


