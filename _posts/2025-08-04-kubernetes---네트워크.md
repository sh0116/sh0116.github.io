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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/8ba4f4bb-7f47-4c51-8172-3a0aee492a75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YR6FSBIK%2F20250805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250805T002803Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJHMEUCIQCI%2FwM5lmVr714lmN4ILQADv6OdQwEzpAD%2FW5VpSWG%2FxAIgJiGJXrJD5zafvuI5Yf6EFHHTc014wKqisGXLK%2BN8zKAq%2FwMIUBAAGgw2Mzc0MjMxODM4MDUiDGKTVj0DwtzYmvKc%2ByrcA%2FlrH5r4E3OGxx4iHfR7OCnOkd4DCkMQJdpRejrafhuqVC8%2FUgqPDb45LtQJF1wwk0XMxVNKrmJIe82uarTz2TOl1ldutP7x0cu7Y0hZv82w7oAM841%2Bf4RbsH0F4QvTpI7nOXuONvSEuOSurFJptvqreYGIBGkiqYBFfiUWSoSN8od9G4MMVLbK1zc2MsidLRl6ccvwK0iXJuD9ZudGlIZ72H2z5L315gsL40Z%2B6u76ZUyiMXG37vDmbkELzRmUFwwU6Bt%2BO51MRXZbcW09fg0P5Q%2F1HUFA2TUmV9IvQlr82UncIr2itfG%2FLIlsLsrawk6apCDTtM9gJFMcvvoBLfOnLyWfNf6e1t8%2F3nSLKpIbvrTF8k1Hvw8m3YJJrfrDAm4t40smpjHXliD%2BGUpS5ITLkNVDBiY9wHouA%2FJp2KNBrIROW7KCKhzOKgBJvvxQNXvVIboDd7zSbNigbaO8Sli1FQhA%2Bsc8zaDEFRPDfRwxuYk9BtgfzRXAIOXYHoDHMgA1M47GXgD%2FNcoXvH8MPwJp%2BqVyu%2B2%2FXX6SQcUZn%2BHgvAe%2BtXoOrcsk9eDpPIlchfv6aOp3Azex1IoRwE%2B5ziH4x%2FJNaJTpwmbWi3F23ZydJc3jmTgQdQdgINJjMO70xMQGOqUB%2Bc2uDBVo2o0ta9kiRv156uRdPJn3Rb7Z%2B4FaeOV14Zl%2FKjGSghSqFsN%2F9fSWQYuxhS58xg%2F4nwJLcXCkqmq38Vf6EW1B4EgkErac98tcmIgkfpDfFGIj0JPQPiMYhvJQ5Nz4R5oGCTvLUj%2BTzhoMBo5Ass3yvT1vTG%2Bn5B%2FSmJVjzDrdjK%2F89xcYfcwi%2BR3K2zor6NSo88QVT03n7fzQf2gH2B4Y&X-Amz-Signature=c68905fa63b31456d3408ff4bca2498ecb84d9f15ae382c1bfc5a86f7b159e34&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## Reference

[https://velog.io/@hoonki/%EC%BF%A0%EB%B2%84%EB%84%A4%ED%8B%B0%EC%8A%A4-%EC%84%9C%EB%B9%84%EC%8A%A4ClusterIP-NodePort-LoadBalancer%EC%99%80-%EC%9D%B8%EA%B7%B8%EB%A0%88%EC%8A%A4](https://velog.io/@hoonki/%EC%BF%A0%EB%B2%84%EB%84%A4%ED%8B%B0%EC%8A%A4-%EC%84%9C%EB%B9%84%EC%8A%A4ClusterIP-NodePort-LoadBalancer%EC%99%80-%EC%9D%B8%EA%B7%B8%EB%A0%88%EC%8A%A4)


