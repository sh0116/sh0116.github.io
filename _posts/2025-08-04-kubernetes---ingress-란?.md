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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/8e23b497-f666-4afc-95a3-bec229baaa4c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663MOEE22S%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T070510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCIQDw7jPlUeFyQazJ6Sw7uv3xbrFxeLC%2B%2BD8ykPE5ZxglLwIgKHqogNZ%2BONk5Cr17prkJy9D4xnha9jha4L1p8KaZ4OYq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDMF6l0GNTFXRaChhPSrcA4qMc3Hq5h4rWStL%2FNC6isG87kchbVF1X%2By8WrLLEQYV2fd6AhE%2BRFd%2BCxNEgHhz7d91%2B77YSN6hMY1RQT2Tk%2Bkk%2ByGaXQoThasqXC4oksuDnyQdinu2Oh7KFMK%2F57vEGkamWnoNOqQ%2Bc%2BaalFXqxAT0BH8tPRV8pdwlgB4tcGUKIaEw9jn5JYBTkGP1XqmOF8OyOXySLGzjKctUKoc2dV1UGT3%2BlRZR05zve5AAbHiYrswnDTq1boosirgRJrY%2FOnh9qLhKNDs0UOtJhEz5Z1J5JxsrbTdwdbzd3SSJ3QSZSZEI6VSNOQvvjt1BvkjOAzeSxLiE4SgK1Zj2NmCMMxt2yZ6JH89DDnR3hGym32xXYlYjuR1EHuMh0J7UhrAmfz9fPBP44h9i6guIlFzI9ZgGqdOuGzMSa7Z39vv5O6oNI08tZLf5sOiWgjWdZg9Y5COr5OYcyxkHiX%2BoPT4hsRDxFOvFQvMfsWWWy13fBQChIwPD6GbpI5OYOMyuGOF0s%2BxQ0Y1dj8MUD4AD8LmhkxnBlFku1gkuXvuiG8nEIqMPMHRfhm794YxC1P32P7wnh4mbRylxXpoFY2dVmS%2BZLf8BocLzT8AXjeNHfK7HEEfN%2FbFFtb0UUf8zffQ7MK2NwcQGOqUBRDZobh%2F5kZ%2BgxJshntVQ1u%2BkpFXYVkFoDml40EyHGZqFixVrnp93Ls5UyMSmt2uxPI4pDk13BcohScJeINNOUS6kUhWRFgiF%2BmKtpiL3%2BDE0yH%2Fp6BQe8sgqUO%2BT9E5IpcOj1XA17VdOpY1LjOYXA85aTG16saSKld6j1V%2BatJD4TJ89Vba9v4ETya3JB8pOD%2F7kejCtD7tUZXFbqsG15CmL8ZZU&X-Amz-Signature=06672330bc827f1972d59a586d3125490f34757d0a956d9183bfbee5c5659d97&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


