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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/8ba4f4bb-7f47-4c51-8172-3a0aee492a75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RIUFRN3B%2F20250805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250805T061048Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQC1ZPh6HWj2FA9RmQQDnU%2BMN9L4UUJElJhkvvSY73Kv3wIhAMHzO7NpbygpCuLEXKuqv9iV2b3EDmQqnqDF1pDgWmbIKv8DCFcQABoMNjM3NDIzMTgzODA1IgxcFQWqyfGu6hU3soEq3APpGJ16MyDjKNihxQujoJuKtR7lmgd7pmFnRaIkrV0mB0tQKEaQTgnOGNkuL%2BrIyeBAQfPR5HkGM08TfxhUyNVHD2kuh3I4o6okDoVRO63aVn3vH%2FRjt7sp0rdQbUPXdeXhIorB8iGW7JWiG96zERSGtMjxJeZMUxla6sJaWvHQeQ%2BQ3E3at0jGm9qIM4K6cMTk9eZjYHWFmL7VtoU2Vtxg54ruWlWzvoWC7HRIl6wY4Z%2Bv7g88pRY5gi4YTO8JIToMIY2WE9cCUleXX9q384uAg%2BjkF76sgANs5rzxKL6%2F4oMbOpbg%2FPJFjPT7jeW0M6RqpYvpnWcpPFoi88aPCuT%2Fg259zGcwFlOIWA%2F2w600thetReSdAULMK5XQMa3GvpKsTcODQEk5fo870CUydNSkWLoIaOhiwlwDjTwxj%2FXEq%2FCrywOSKrd7nr6grlxiOFW%2FcYPid9nUnYNTu8IAk0YCvwbW4BBRcvW9GvNN3pPNoeWLAF0SsgSZ2v1UFvyO2GpoHqjhdmAWHr0giaGDbITOkN%2BVqw3IZt7JdjhgMQzZMwYNvBautyn1xqq2FiAWbny4DUCPfaP55K6FMhDIAksYPRVN%2Fwd5JAi9wvUwo7pWmT7%2BJt2PqFjXZ5ycNDCWs8bEBjqkAXYlC0TVPnMFXML6emvNObi3FmUjOrsMvJPZz%2B5VAPzXdOOvZnZP09xAeWVWTB%2FtWO0VFNBDUjzyq709Bitwn8%2FbbPLptvg%2B3Yk0Nawt64y4cmQqyCTwOclqph3zVhT0ulN7rZUZCj38skhP5ZzswfEBed27CeuiTOwmgONWgxHE5Sp5Ws4ESOfxF6JQjoSH9RT8OgoFjNSmHp8bQYaj%2B1y1khus&X-Amz-Signature=8b3157a9f757e9442ef5a99a6636d141a12ea94d9827017cdf510dae12346105&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## Reference

[https://velog.io/@hoonki/%EC%BF%A0%EB%B2%84%EB%84%A4%ED%8B%B0%EC%8A%A4-%EC%84%9C%EB%B9%84%EC%8A%A4ClusterIP-NodePort-LoadBalancer%EC%99%80-%EC%9D%B8%EA%B7%B8%EB%A0%88%EC%8A%A4](https://velog.io/@hoonki/%EC%BF%A0%EB%B2%84%EB%84%A4%ED%8B%B0%EC%8A%A4-%EC%84%9C%EB%B9%84%EC%8A%A4ClusterIP-NodePort-LoadBalancer%EC%99%80-%EC%9D%B8%EA%B7%B8%EB%A0%88%EC%8A%A4)


