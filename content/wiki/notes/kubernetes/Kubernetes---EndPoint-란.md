---
source: knowledge-base
origin: notion
title: "Kubernetes - EndPoint 란? "
area: "Kubernetes"
tags: ["area/kubernetes", "tech/kubernetes"]
created: "2025-08-04T06:05:00.000Z"
last_edited: "2025-08-04T06:27:00.000Z"
status: published
public: true
notion_id: "245172a5-56d6-80cc-860d-d1113224e104"
notion_url: "https://www.notion.so/Kubernetes-EndPoint-245172a556d680cc860dd1113224e104"
type: note
updated: 2026-07-07
---

# Kubernetes - EndPoint 란? 

## 요약

Kubernetes 기초

Kubernetes 큰 주제 아래에서 세부 개념과 실습 절차를 연결하기 위한 노트입니다.

## 핵심 포인트

- Kubernetes 기초
- EndPoint 역할

## 지식 그래프

- [[wiki/mocs/Knowledge Base|Knowledge Base]]
- [[wiki/mocs/Kubernetes|Kubernetes]]

## 정리 내용

## EndPoint 역할
- 쿠버네티스의 서비스 기능을 사용하면 외부 서비스와도 연결 가능
- 외부 서비스와 연결을 수행할 때는 서비스의 endpoint를 레이블을 사용해 지정하는 것이 아니라 외부 IP를 직접 endpoint라는 별도의 자원에서 설정
- https://kubernetes.io/docs/reference/kubernetes-api/service-resources/endpoints-v1/
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

## 출처

- 원문: https://www.notion.so/Kubernetes-EndPoint-245172a556d680cc860dd1113224e104
- Vault path: wiki/notes/kubernetes/Kubernetes---EndPoint-란.md
