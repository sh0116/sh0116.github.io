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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/8ba4f4bb-7f47-4c51-8172-3a0aee492a75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XV33CCQA%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T071455Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJIMEYCIQD9IP2PKJKbL2VFw9LlnZmD2C8VsRQbEafu3iYA5KEKtQIhAKVhLfMTWlNMF7PaCqXqAYJyqgtNDDmn%2FWKVabz7KoXAKv8DCEAQABoMNjM3NDIzMTgzODA1IgxLLGbz48JWYEg9yekq3AOvav1m%2FYok2m4sqIB68kyQ3%2BQIzwX1Yy7uVM18ntk02FhGwg8BoxhPk370nU0Hnz2m2sPSdb%2FCgtLQnwaNEkrtujUP42ZVVqAe9WsFL5Ye43sNEfnifqi2Qm6c7%2F8xf1OMQo1dyzeB9DoESNBazis%2FmhM1TPDHdSMHfjbwihotwsjqlirD0nIb1kibgxuso8W6Wbtt%2F%2BLhgKoVspa2JiUCN3r00rdGyLFiQqdBZQ4htqT7oErMoDugVfWimNwwpwTyhAsdO1%2FMumfXXRS%2BfZV%2Fp8KJD27ouxa6RXGgXnK6BCNOW%2FAn1SUMbOLLn%2FqCCCz%2BtwZksMx6xdZT8LshAgT5IpepSuKgMOYvoO32Fifmc1M8HbH1Jbj2iZbhugIU63k2WMFgqixyNmmdJpOA07QwIlqecyGYtRbeeekE6AWMbTA1pou7fB7ErusgZitBSFnrBI%2BREug4F3I4K8PWe46BPLllqIPF4g9BtTrGQ2Z4BQpey2uKGwjbzow%2BFcn5DWX2ARcGPtocItSnJ1ml2ttDWAWKGfxW5WXXE4R3mHRCoMOKFEMt0SAJA03QPNoDnKnNF8%2BXHDY8U4pmGlsYPfohBoRNi0lkd2OOBivoSoqsKTolBY9hejjI5I7QmTCjt8HEBjqkARIP5cAaYYbesc52E5aiOBMXDL8%2BUlm6v9Dsu0zPI1Lu25R8BFjvDm8qqYz%2Bot691bhp0U%2FB%2FFgl%2FzCpX7z4PAfy1ozefSGfJ0ZuIsjLzEAH90BXgriZ6IEiNUk7IeNnlC4quDt6%2FEklNLYQ9MakQWtg3C2vch6LW9XAWBsNR6f6CcCoK378B3lIxDPO1ezkln03dtzp2Oh3kD83Dh9%2F2P1%2BnCzG&X-Amz-Signature=0b449ad366e07e8dee028f1780415a80438615366c4f25e58cc909655c6400aa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## Reference


