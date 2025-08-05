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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/8e23b497-f666-4afc-95a3-bec229baaa4c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664PJLXAGB%2F20250805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250805T060959Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQCvQy5jmB7%2FZMpl0I4Lv1kX5HW4C7wFJNGIj8ShOOZAbQIhAI467ojfrV5%2FDjWLYsoifkCCy4qcBuYjBotau4H4b2vHKv8DCFcQABoMNjM3NDIzMTgzODA1IgxjTkPk%2FLGav2pvpeMq3AO8bp3sNOve9OsZzn6p6veFa5TRONzW%2BrEdx%2Fdz4ZZzsdx7LxPScvo91XfBNyBtSKyPl1Sbzt9bRHHCA9I8Sd4uKxIHoq%2FY1RnCsiHS6%2BI7Vhu3fiORgEIAsI%2Fru7QDHJj2VMStQTaai%2Bkr3vje8Nz1pmta7aPtrE65Y71hobdY3MYSUctFi%2BhQ5SNHCZydeZ1223i3sVXxgtOeR3jrRPgjA1H%2B40xtPdGm%2BlMBNUyiin93R3WEECilpk6WwWI7PYzuJuZK4DG%2Bp%2B%2B6WE6Nb2kehvjBpQMjdyCwPuk4umLWIhnh4lb70QvdxZqLJzAwAJr0L2FvQ6rt0XRo%2Bg8OG2ObRT6qkO9gn8SJPYS%2FXOA9xt1RJzveM289ZrztQNbotxDgvo4%2FkXr4Unc%2BoEr%2B4XkcPeZGWhC5FlDNfZIVqG1kCngFrucO9rhBWgPTc2JSSpi2WHtt5GCO0ZvIOcVklGq5DeE7eGpLM3nXQc6GsH2fSgL%2BI0K%2BqsZKdPadrdk73kkUGSJn8%2FI46CPr7m7J%2FN28IJ%2BCzKSfOO8vXYYncLx%2F%2BVAR9%2FNNnliqR33tMqdMCFX0u2cB4BBo9oOFWgJZRfxAhnUOJp82ErzpYcxmrihRTZb8X0kL4xBc1bVDLjCQtMbEBjqkAdlkOp%2FsYSgUJZ%2BL3dLQCSGkPu6vsg2SljKc18k7vrmFe5cEt%2FWGYvExKqBLBwDZZytl4NhxCidjoY92DkHta8LZspB8cKa1DpJhxARudvumrgWKn%2FEvZoC8bYXqIEIPshoQ6RjUtAmr%2BfG0b0A9Ebol6KJjCue0LIK9gm5W6c7FHRtz7V%2FTHy%2FOKBYzbKbZlSyetnkKa2r9jXyvSt%2FtQBdhXfu7&X-Amz-Signature=e619698ef7246ffc263a90c1d3c4400f39d719d2ccd09f81d50c3e4869adf93b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


