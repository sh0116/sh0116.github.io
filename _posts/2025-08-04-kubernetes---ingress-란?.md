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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/8e23b497-f666-4afc-95a3-bec229baaa4c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QM32WZCP%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T072142Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJIMEYCIQC%2BnxW1T4%2BtJt%2FYRyeTW4Oh%2FUWhqwOW98apQF3VUp6leQIhAPforZi50or8HoJ%2BCS1SUHzuY5HDWdG9bxygIL26QXkwKv8DCEAQABoMNjM3NDIzMTgzODA1IgyfXpd2yGjE%2FR%2Fiv94q3APAPNpU0YKL0TTGUeBPKt8nH1PcQav5Dk4oP621ZqGeA6l4bxPJOyCJ1YLdMs0%2BFaH23MlBwTcsR1mTii4Dyme0tI8lJ24wQ97ULqUp6qR5ECIRvUBz%2BGMVZfpQKmrTW5nW9UQLltVReiD%2BKFudrx4x58FMzfj9Dv7UeCFJb7KdoBmVQzaNy8tALo4QOVtmjB5Ofg96ZPfMdjfUrGQkATmfMU%2FVq4yzgI%2FkvZtjsNxGGn4Ji1GZ2yNwON0OSsiKgi%2BESgCtEwKSf0zFc4luNgjHaM%2F3XjgHr11k3r%2FMkyLXyCOklj6E18yhGRvrLCOR8LZJMHR5slxplcCEzdcaf0DrVZxJ3gzceK%2FTS0QZmW6fVbmrOidkdoWykrW3wZUo92nu%2B%2BaZV1UyQVKkuHZaUESEkg%2BEsfSF2dFU%2FDTrzVXk6JQjHFSdf6xYCuHyoqjmjwwZCeq0Ci3Z%2Bv1CCR6fquwJnQZmSaGfvDgNgZ2%2FHmIOdoKjJNa8SLKKYmFewyiHk8jB0UxR826yIFlr%2FCRZmmTCAM40%2B6Kuv7JRpf5IDe2d2%2FYvwuExhhnUiSvqRcZD%2Fs1rLMDddmh%2BRqORPsg9Y%2ForXfixY34GQ7rtRVItLdPrOAq6Z0lcsmYNtRoEpTCztsHEBjqkAZTFhns8GBCVeIGWiYya%2FFlIfkhmywQusCNFdQOgfQYwFEAk4PZ%2BH5b8rUzkSAtbGQAfQKD0ILkhaDRqNSgUWdKNDuXofylJk%2BEikPb2XrzF5HpgnzGfF6OID3VZ%2BG2jpmoqCxn08eYR%2FkxDxy66S9SRJPc5SB6KW%2FFym6a1ccw1ASMFJUsnIaBZJiyg4YtntqYIKIXaN1c03Okx22vh85vBNz6M&X-Amz-Signature=a38a8bb759eab74a47173ae3c93daa8135dd2867d1c1cdda2bdbeab5c9c77c7f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


