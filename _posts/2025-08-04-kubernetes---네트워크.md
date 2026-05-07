---
title: "Kubernetes - 네트워크"
date: 2025-08-04 06:05:00 +0900
categories: [kubernetes]
tags: [Kubernetes]
description: Kubernetes 기초
toc: true
comments: true
---

# 서비스를 노출하는 세가지 방법

- ClusterIP(기본형태) : pod드링 클러스터 내부의 다른 리소스들과 통신할 수 있도록 가상의 클러스터 전용IP
- Nodeport : 노드의 자체 포트를 사용하여 pod로 리다이렉션 
- LoadBalancer : 외부 게이트웨이를 사용하여 노드 포트로 리다이렉션
# 인그레스 Ingress 개념

만약 여러개의 서비스가 있는 실제 서비스라고 가정하자.

각 기능마다 로드밸런스를 각각 정의를 해야하는 것인가?

Ingress는 서비스의 종류가 아닌 서비스를 하나로 묶는 스마트 라우터 역할을 수행한다.

즉 하나의 LoadBalancer에서 여러 서비스를 노출할 수 없는 한계를 해결하는 것이 Ingress이다.

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/8ba4f4bb-7f47-4c51-8172-3a0aee492a75/Untitled.png)

## Reference

[https://velog.io/@hoonki/%EC%BF%A0%EB%B2%84%EB%84%A4%ED%8B%B0%EC%8A%A4-%EC%84%9C%EB%B9%84%EC%8A%A4ClusterIP-NodePort-LoadBalancer%EC%99%80-%EC%9D%B8%EA%B7%B8%EB%A0%88%EC%8A%A4](https://velog.io/@hoonki/%EC%BF%A0%EB%B2%84%EB%84%A4%ED%8B%B0%EC%8A%A4-%EC%84%9C%EB%B9%84%EC%8A%A4ClusterIP-NodePort-LoadBalancer%EC%99%80-%EC%9D%B8%EA%B7%B8%EB%A0%88%EC%8A%A4)


