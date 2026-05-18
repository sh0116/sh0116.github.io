---
title: "Kubernetes - Kube-Proxy"
date: 2025-08-04 06:05:00 +0900
categories: [kubernetes]
tags: [Kubernetes]
description: Kubernetes 기초
toc: true
comments: true
---

# Kube Proxy

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/09fe6073-4730-4f06-b1f3-ec4d1c892eb3/Untitled.png)

각 Node 안쪽에 Kube-proxy가 위치한것을 볼 수 있다.

### Kube-Proxy란

K8s에서 Network를 담당하는 컴포넌트이다.

각 Node에 Proxy가 하나씩 있고, DaemonSet형태로 Kubernetes에 존재한다.

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/5523f286-c968-486e-bca5-1b7149e1bab4/Untitled.png)

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/7d447a12-8224-41fc-b731-32344196224a/Untitled.png)

클라이언트(사용)가 쿠버네티스 API로 정의한 서비스에 연결할 수 있도록 해주는 역할을 한다. 서비스의 IP와 Port로 들어온 접속을 서비스를 지원하는 POD중 하나로 연결해 준다.

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/dcc268b3-5716-45ac-bf0b-63631615eda6/Untitled.png)

커널 iptables를 활용하여 연결한다.

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/6019cdb1-f915-4906-990b-fe49a1f5b1b0/Untitled.png)


