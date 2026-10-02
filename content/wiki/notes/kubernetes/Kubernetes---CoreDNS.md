---
source: knowledge-base
origin: notion
title: "Kubernetes - CoreDNS "
area: "Kubernetes"
tags: ["area/kubernetes", "tech/kubernetes"]
created: "2025-08-04T06:05:00.000Z"
last_edited: "2025-08-04T06:27:00.000Z"
status: published
public: true
notion_id: "245172a5-56d6-80d3-8a48-f8521220df77"
notion_url: "https://www.notion.so/Kubernetes-CoreDNS-245172a556d680d38a48f8521220df77"
type: note
updated: 2026-07-07
---

# Kubernetes - CoreDNS 

## 요약

Kubernetes 기초

Kubernetes 큰 주제 아래에서 세부 개념과 실습 절차를 연결하기 위한 노트입니다.

## 핵심 포인트

- Kubernetes 기초
- DNS 도메인 네임 서비스
- CoreDNS
- POD에서도 Subdomain을 사용하면 DNS서비스를 사용가능하다.
- 공식문서

## 지식 그래프

- [[wiki/mocs/Knowledge Base|Knowledge Base]]
- [[wiki/mocs/Kubernetes|Kubernetes]]

## 정리 내용

### DNS 도메인 네임 서비스
- 서비스를 생성하면 대응되는 DNS 엔트리가 생성됨 
- 엔트리는 <서비스 이름>.<네임스페이스 이름>.svc.cluster.local 의 형식을 가짐
![[_attachments/notion/Kubernetes---CoreDNS/245172a556d6817d89a1efc2ab107560.png]]
## CoreDNS
- 내부에서 DNS서버 역할을 하는 POD가 조냊
- 각 미들웨어를 통해 로깅, 캐싱, 등의 기능을 가짐
![[_attachments/notion/Kubernetes---CoreDNS/245172a556d68194a402cf12318dc2fa.png]]
- DNS 에는 configmap저장소를 사용해 설정 파일을 컨트롤함
- CoreFile을 통해 현재 클러스터의 NS를 지정
```yaml
kubectl get configmap coredns -n kube-system -o yaml
------------------------------------------------------------
apiVersion: v1
data:
  Corefile: |
    .:53 {
        errors
        health {
           lameduck 5s
        }
        ready
        kubernetes cluster.local in-addr.arpa ip6.arpa {
           pods insecure
           fallthrough in-addr.arpa ip6.arpa
           ttl 30
        }
        prometheus :9153
        forward . /etc/resolv.conf {
           max_concurrent 1000
        }
        cache 30
        loop
        reload
        loadbalance
    }
```
### POD에서도 Subdomain을 사용하면 DNS서비스를 사용가능하다.
- yaml 파일의 호스트 이름은 pod의 metadata.name을 따름
- 필요한 경우 Hostname을 따로 선택 가능
- 서브 도메인을 설정하면 FQDN 사용가능
  - 예시 : <hostname>.<subdomain>.<Namespace>.svc.cluster-domain.example
  - FQDN이란 Fully Qualified Domain Name 호스트를 도메인에 기술한 주소
    - 예시 www.naver.com (www가 호스트 naver.com 이 도메인)
#### 공식문서
- https://kubernetes.io/ko/docs/concepts/services-networking/dns-pod-service/
```yaml
# sub도메인 생성 및 POD 도메인 생성 YAML파일
apiVersion: v1
kind: Service
metadata:
  name: default-subdomain
spec:
  selector:
    name: busybox
  clusterIP: None
  ports:
  - name: foo # 사실 포트는 필요하지 않다.
    port: 1234
    targetPort: 1234
---
apiVersion: v1
kind: Pod
metadata:
  name: busybox1
  labels:
    name: busybox
spec:
  hostname: busybox-1
  subdomain: default-subdomain
  containers:
  - image: busybox:1.28
    command:
      - sleep
      - "3600"
    name: busybox
---
apiVersion: v1
kind: Pod
metadata:
  name: busybox2
  labels:
    name: busybox
spec:
  hostname: busybox-2
  subdomain: default-subdomain
  containers:
  - image: busybox:1.28
    command:
      - sleep
      - "3600"
    name: busybox
```
### 연습문제
![[_attachments/notion/Kubernetes---CoreDNS/245172a556d68105aec2cf1be2c4fbed.png]]
```yaml
apiVersion: v1
kind: Namespace
metadata:
  creationTimestamp: null
  name: blue

---
apiVersion: v1
kind: Service
metadata:
  name: srv-jenkins
  namespace: blue
spec:
  ports:
    - protocol: TCP
      port: 8080
      targetPort: 8080
  selector:
    run: pod-jenkins

---

apiVersion: apps/v1
kind: Deployment
metadata:
  creationTimestamp: null
  labels:
    run: pod-jenkins
  name: pod-jenkins
  namespace: blue
spec:
  replicas: 1
  selector:
    matchLabels:
      run: pod-jenkins
  strategy: {}
  template:
    metadata:
      creationTimestamp: null
      labels:
        run: pod-jenkins
    spec:
      containers:
      - image: jenkins/jenkins
        name: jenkins
        ports:
        - containerPort: 8080
        resources: {}
status: {}
```
```yaml
k exec http-go -- curl srv-jenkins.blue.svc.cluster.local:8080
k exec http-go -- curl srv-jenkins.blue:8080
```

## 출처

- 원문: https://www.notion.so/Kubernetes-CoreDNS-245172a556d680d38a48f8521220df77
- Vault path: wiki/notes/kubernetes/Kubernetes---CoreDNS.md
