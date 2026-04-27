---
title: "Kubernetes - EndPoint 란?"
date: 2025-08-04 06:05:00 +0900
categories: [kubernetes]
tags: [Kubernetes]
description: Kubernetes 기초
toc: true
comments: true
---

# EndPoint 역할

- 쿠버네티스의 서비스 기능을 사용하면 외부 서비스와도 연결 가능
- 외부 서비스와 연결을 수행할 때는 서비스의 endpoint를 레이블을 사용해 지정하는 것이 아니라 외부 IP를 직접 endpoint라는 별도의 자원에서 설정
```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-service
spec:
  ports:
    - protocol: TCP
      port: 80
      targetPort: 80

---

apiVersion: v1
kind: Endpoints
metadata:
  name: my-service
subsets:
  - addresses:
      - ip : 199.201.110.204
      - ip : 223.130.195.95
    ports:
      - port: 80
```


