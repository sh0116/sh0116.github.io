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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/8ba4f4bb-7f47-4c51-8172-3a0aee492a75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T4DSVI6Y%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T072234Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIEZTWsEK4r%2FGWlwhICnuCAuD8pYIhP65ndPpStiqQ41jAiEA74SetU%2FK0cGiJJfkdaXeyknPK026wAl34sXUelWXQqUq%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDDEgXDoxilLYnQc9MyrcA9tHKyLUnHpQAY8U6RmBvlzQwF1bjYfdQYM8BKK4H15VvpVTcZy1giR6g5mIgqFiZy4EifB2pO2H7qZDDGwEI8%2FJX7EplqVHzgJ9z4LVCro%2BPZw5zdXKP59A%2BhdAMbL6pCSJTwHcOgJo9B3AYRT%2BVFZ2d1PVr8ePS6g2lC0sI145D7FkdwxROrBu5pqdkt%2F54bBlvNRZtztc1xLN4Ga4nNaxmFq1yTfR%2Bk%2BaXQYI%2B7qGgc%2FjYYuZJmxOkv8KfyZ6dXnQYAdaWP3lyFcR9fOZaXjHKFIbW%2FAe%2BX9em%2F0fvNzGPCqy5GUNtvPxXsBT3aycPd5bUkxWovhD2Qnd45O%2B%2FymRJmaWjRNB95bXSC%2F6a%2Bq53lS6SufXf94Nbya0AG7UEg72ogEvpscw4InooHA2vdZB853J0lhFSaI7sqUNdRpQ4DT4WQ52z0mZPvZ%2FEAE4sMkFdfizCo%2BWxoWh%2FhA%2BBp7GtFyCepfnTsqwBbOPttgJA2HxvP%2BDHD4E0cip%2BvosFYC9L%2FMXgLUnuf45Mlys1LbOjSg%2Bz%2B21q4DxQ7ccBdhrA6Gtxu%2F8PpIp9YFARIj1N12ybzJk3d8BZnB7AVPez8C2hzMugP1LcHVFMfne2uNyLCTP9OdEADKsyON7MKC3wcQGOqUBGaus5NKWtp4pJOMjA2PAJQPZrunKE3y%2Fgg7nJOcUpX5nedG16%2BMAdVrG4%2FuovdVWI7j%2BFmTBmveonTcUqrkiOqvKAZtTgJ9xBc3QWmIsE1NoYtlYxNrnbJNpeXCBzPHy30pid92akwDgDE%2FMZwCSe17nGBD8rTXerTsFwcNgvtFZF9CTkS65XNFQ54K8nCy1qb5tV4TS6ae4w3GcpT%2BRBKjWUeOX&X-Amz-Signature=dd1f14d8b0a7dd1573350833f1c236cd103dea1c942ebf6eb51622dd364d9f53&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## Reference


