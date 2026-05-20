---
title: "Kubernetes - Service 란?"
date: 2025-08-04 06:05:00 +0900
categories: [kubernetes]
tags: [Kubernetes]
description: Kubernetes 기초
toc: true
comments: true
---

# Services

-  외부 클라이언트가 몇 개이든지 프론트엔드 pod로 연결
- 프론트엔드는 다시 백엔드 데이터베이스로 연결
- pod의 IP가 변결 될 때마다 재설정 하지 않도록 해야함
- → 결론 : 로드벨런싱 기
![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/9fcd1a32-c9d7-4113-a3f6-39e112bc3ed8/Untitled.png)

## 서비스 세션 고정하기✨

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/3df2994b-94f2-4401-bdfd-c3392b085c5d/Untitled.png)


