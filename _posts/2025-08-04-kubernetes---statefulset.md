---
title: "Kubernetes - Statefulset"
date: 2025-08-04 06:05:00 +0900
categories: [kubernetes]
tags: [Kubernetes]
description: Kubernetes 기초
toc: true
comments: true
---

# 스테이트풀셋 Statefulset

- 안정적이고 고유한 네트워크 식별자가 필요한 경우
- 안정적이고 지속적인 스토리지를 사용해야 하는 경우
- 질서 정연한 포드의 배치와 확장을 원하는 경우
- 포드의 자동 롤링 업데이트를 사용하기 원하는 경우
## Statefulset의 장점

- 스테이트풀셋과 곤련된 볼륨은 삭제되지 않음 (관리필요)
- 포드의 스토리지는 PV나 스토리지 클래스로 프로비저닝 수행해야함
- 롤링 업데이트를 수행하는 경우 수동으로 복구해야 할 수 있음
- 포드 네트워크 ID를 유지하기 위해 헤드레스(headless)서비스 필
## Headless서비스 작성 요령

쿠버네티스 서비스 생성 시 .spec.clusterIP 필드 값을 None으로 설정하면 클러스터 IP가 없는 서비스를 만들 수 있습니다. 이런 서비스를 '헤드리스 서비스(Headless Service)'라고 합니다. 헤드리스 서비스의 경우 클러스터 IP가 할당되지 않고, kube-proxy가 이렇나 서비스를 처리하지 않으며, 로드 밸런싱 또는 프록시 동작을 수행하지 않습니다. DNS가 자동으로 구성되는 방법은 서비스에 셀렉터가 정의되어 있는지 여부에 달려있습니다.

### 정의

- ClusterIP가 없는 서비스로 단일 진입점이 필요 없을 때 사용
- Service와 연결된 Pod의 endpoint로 DNS 레코드가 생성됨
- Pod의 DNS 주소: pod-ip-addr.namespace.pod.cluster.local
```yaml
apiVersion: v1
kind: Service
metadata:
  name: headless-service
spec:
  type: ClusterIP
  clusterIP: None
  selector:
    app: webui
  ports:
  - protocol: TCP
    port: 80
    targetPort: 80
```


