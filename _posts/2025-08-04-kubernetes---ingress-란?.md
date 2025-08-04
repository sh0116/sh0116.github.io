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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/8e23b497-f666-4afc-95a3-bec229baaa4c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XH2LU6U3%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T063241Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJIMEYCIQD%2B%2FiP4zz1H7Bm7NyjJar%2FscpyFbV6kIbRn2xzKgecu%2BQIhAJNzVhBs%2F8rLli4kISyRhB%2B%2FxwKdHPrPwZJ0vX9%2FkfX4Kv8DCD8QABoMNjM3NDIzMTgzODA1IgxXz7XooseGljadtfQq3ANXKUn3Q6LkZGRZx7KKmPpEzprlXwiWMhgXqvnkruCIyWn%2F1pFID94IdAfbi2hkCjfHbgKk7QHhkNecoRHJaelCqfkld7gQNeGXa7HB63%2Bw9fig3PrZMjkEQiGBDiTP8KYDLx6l%2BI0Ezk65khRGKH2ksVx5WmMbfHwWOds45aETkbgYdc8GoEO3I4VPlRBqb1xytcuA6PhvbL3yXd9itFs8%2BaLaPt4ojaU1tJHIbpyehUN%2BxGFksRFgfdStFHSC7LGTOIJU%2BPHQHcAsiu%2FaCGtRsZkyOzMEcgLiv2qNNubPxpFIlaKa3uqaZYqzeJ0lUKJnsStKxXPViDPjIUcRAjU%2FKbWtCW1glerqwqbyf2WgjgvVDD5FTZom7mA1ULxGeApd9IIbTtlv9c0FDNDUVR%2BMS18iqkb9eW7RrHEMTbFl1zFVSjaAMuzIgFJAmCDZXlmfaDPT9%2FID6K8EsD8ATJCbuVRSo6ryJigSyfRHIHzh%2FHqed6c8bfcSqrxN94FuJ9stD8SqWd5XL%2F%2FlXp9WKXQKYImn81wvBIl6ApYUztz%2FJo853DJXICWoCkLbPi3kZgjoTX1BEgP1O526quCH%2BLjHTYoRC0JOch1MiNYEm86B0RLCNakXvSl3MBgEYDCbjcHEBjqkAdtHkoPAg43kWM7EqrHj6gRCOIa5zGi9ZrmCJ%2FCYywTuuDxK1ISAK%2Flyr%2FESLuA1hfu5SJkEh7EFkFezv9PXQLohiKoVtgIcZMhNL0wK06cXGgWXB7FuF7Vx35aw5IhCM2BSFhTr3w4%2B7v74T2Na4pmHGRLtFdcceTcrOypCnyG0rlKHLEMjHjh12OhA5r0WfJ2270GNXAJ0qP%2FugDZlUfR%2FxIxs&X-Amz-Signature=4cd87a858edaaed9e577f447ca6d454b7dd812ffe9892726eaf7fc9bc3d32c66&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


