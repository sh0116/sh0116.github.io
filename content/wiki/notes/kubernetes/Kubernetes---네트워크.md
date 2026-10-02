---
source: knowledge-base
origin: notion
title: "Kubernetes - 네트워크 "
area: "Kubernetes"
tags: ["area/kubernetes", "tech/kubernetes"]
created: "2025-08-04T06:05:00.000Z"
last_edited: "2025-08-04T06:27:00.000Z"
status: published
public: true
notion_id: "245172a5-56d6-8080-8be4-f391a8c89163"
notion_url: "https://www.notion.so/Kubernetes-245172a556d680808be4f391a8c89163"
type: note
updated: 2026-07-07
---

# Kubernetes - 네트워크 

## 요약

Kubernetes 기초

Kubernetes 큰 주제 아래에서 세부 개념과 실습 절차를 연결하기 위한 노트입니다.

## 핵심 포인트

- Kubernetes 기초
- 서비스를 노출하는 세가지 방법
- ClusterIP
- NodePort
- LoadBalancer

## 지식 그래프

- [[wiki/mocs/Knowledge Base|Knowledge Base]]
- [[wiki/mocs/Kubernetes|Kubernetes]]

## 정리 내용

## 서비스를 노출하는 세가지 방법
- ClusterIP(기본형태) : pod드링 클러스터 내부의 다른 리소스들과 통신할 수 있도록 가상의 클러스터 전용IP
- Nodeport : 노드의 자체 포트를 사용하여 pod로 리다이렉션 
- LoadBalancer : 외부 게이트웨이를 사용하여 노드 포트로 리다이렉션
## ClusterIP
k8s cluster 안쪽에 위치한 Service
클러스터 내부 전용
외부와 통신하려면 Nodeport나 LoadBalancer서비스가 필요함

![[_attachments/notion/Kubernetes---네트워크/245172a556d68175a8f7c20d7e7e1060.png]]
## NodePort
실제 VM 노드의 특정 Port를 뚫는다 
개방된 Port를 통해 Pod에 접근 가능하다.
만약 실제 분산 네트워크 환경을 구축한다고 가정할 때, 만약 VM의 환경이 오토 스케일링된다면, node의 EndPoint를 관리해야하는 문제점이 생긴다. → 로드밸런서가 해결 

![[_attachments/notion/Kubernetes---네트워크/245172a556d681438e61c9989642ad36.png]]
## LoadBalancer 
실제로는 LoadBalancer이 분산 Node들에 정의된 Nodeport를 통해 로드 밸런싱을 한 후 서비스가 pod들 사이에서 로드밸런싱을 수행한다.

![[_attachments/notion/Kubernetes---네트워크/245172a556d6819bb67de824744d7a52.png]]
## 인그레스 Ingress 개념
만약 여러개의 서비스가 있는 실제 서비스라고 가정하자.
각 기능마다 로드밸런스를 각각 정의를 해야하는 것인가?
Ingress는 서비스의 종류가 아닌 서비스를 하나로 묶는 스마트 라우터 역할을 수행한다.
즉 하나의 LoadBalancer에서 여러 서비스를 노출할 수 없는 한계를 해결하는 것이 Ingress이다.
![[_attachments/notion/Kubernetes---네트워크/245172a556d681b982afeab5487030a8.png]]
### Reference
- https://velog.io/@hoonki/%EC%BF%A0%EB%B2%84%EB%84%A4%ED%8B%B0%EC%8A%A4-%EC%84%9C%EB%B9%84%EC%8A%A4ClusterIP-NodePort-LoadBalancer%EC%99%80-%EC%9D%B8%EA%B7%B8%EB%A0%88%EC%8A%A4

## 출처

- 원문: https://www.notion.so/Kubernetes-245172a556d680808be4f391a8c89163
- Vault path: wiki/notes/kubernetes/Kubernetes---네트워크.md
