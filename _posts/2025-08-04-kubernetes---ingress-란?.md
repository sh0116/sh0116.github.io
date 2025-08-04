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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/8e23b497-f666-4afc-95a3-bec229baaa4c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TLDHDPRM%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T064854Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJGMEQCIFDA1i8pG4FF73Za2eaHgrfVbhMJ%2FlagngDjfbpzV%2FK6AiBZi8t04LMjR3NqQNLX3zl1LT5ZLhI6Bz7JS6w5ZWxPTCr%2FAwg%2FEAAaDDYzNzQyMzE4MzgwNSIMVVTCP6Xttx9lhi4wKtwDPT%2BCn40ZjRIzmMJrOmsR6PmkBg%2FO9XULb3lq7jxYsCEI4kM5PP5MeQjPpF8XegCbmFb3MFA2DX%2Bpb8ojOxegmzfUYHwq%2BDOZR79DS0Ca19vHN2hgvKZ%2FGo%2BAIUOLXPQU5%2BDBQ5X9yCYZOqGDMOi0bclo3hNPBZlTUa%2FPnWaJGYmIlpAGRZg%2BYZcqnIsaimRcvWa9wYvcs95dM1Pk1Oms928X1YNMfXOB1Vx51JcugP%2BwPeEzMfc3huSgOLTymaCrcMNz%2FuGh8mQJyFS6DXE7CJUo8MdEgjaoT%2Bc2%2BNUxWDtkpSSJGsxpXKeq7mkhPj9QOvAYWTKHcInHRBV7GmpVMAZE7WI6Zc0NwKpMCyr%2FjFiG1vFs0BTtK02OiA7wpGQz7o9pi8s%2FfA52%2BrMJO%2FK16czpqqHYxTMv8CpgQ1btPUpW%2BVGjpdxOJJsLrHJW6H4ZqK0dEbO4siU16azplRZ9vkmg%2F9i%2BgKzQIkrro5qsWDWx4VQ0DzW%2Fy8QIFRXdNNlYXxYHFGcQP0DilOPup%2FNFX5JxYcvV4WbBHXJG3w7eNGmTRw%2BK7LGL2YOdVX4UjqzLwVby%2F%2BZM%2FS%2BXFrBJYCa732orobJAnkGv%2FUfPJYdFelRyDXR4iWhcxBJ19hAwh43BxAY6pgGqQcROfkRDLPlPyT6Te5YYlXiXx7Vt7wFccPxleNOU5Jhv34iTHzDdjadVgKF3%2FOjf8Wb%2FvMHUVeYddXeKqstQivGi74MgeGPfx4j%2BBq4mdJW69ASnjU%2B%2BqhjNVQbvZzfgYuRjXSLSHWwJpWT3OlsKl4N7MlWyYWj%2BVeHJveFKAhG7eSYCkZQa3XWoTd%2FvIrizbmhU7tbw2IgJSlS4zagnR3jjgKNs&X-Amz-Signature=2e11b19d6304b1e48a172cd4fac78ced62d7154545ab485e96e38498f84b5404&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


