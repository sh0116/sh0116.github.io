---
source: knowledge-base
origin: notion
title: "Kubernetes - Ingress 란? "
area: "Kubernetes"
tags: ["area/kubernetes", "tech/kubernetes"]
created: "2025-08-04T06:05:00.000Z"
last_edited: "2025-08-04T06:27:00.000Z"
status: published
public: true
notion_id: "245172a5-56d6-803f-b138-d25f2c5cbd35"
notion_url: "https://www.notion.so/Kubernetes-Ingress-245172a556d6803fb138d25f2c5cbd35"
type: note
updated: 2026-07-07
---

# Kubernetes - Ingress 란? 

## 요약

Kubernetes 기초

Kubernetes 큰 주제 아래에서 세부 개념과 실습 절차를 연결하기 위한 노트입니다.

## 핵심 포인트

- Kubernetes 기초
- Ingress
- Ingress-nginx
- 인그레스 룰
- 4 노드포트, 로드밸런서 연습문제

## 지식 그래프

- [[wiki/mocs/Knowledge Base|Knowledge Base]]
- [[wiki/mocs/Kubernetes|Kubernetes]]

## 정리 내용

## Ingress 
인그레스는 클러스터 외부에서 클러스터 내부 서비스로 HTTP와 HTTPS 경로를 노출한다. 트래픽 라우팅은 인그레스 리소스에 정의된 규칙에 의해 컨트롤된다.
![[_attachments/notion/Kubernetes---Ingress-란/245172a556d681ffb75cdcce79081e67.png]]
### Ingress-nginx 
프라이빗 환경에서 인그레스를 사용할 수 있도록 Nginx설치
쿠버네티스에 pod형식으로 띄워서 설정
### 인그레스 룰
| 열 1 | 열 2 | 열 3 | 열 4 |
| --- | --- | --- | --- |
| 종류 | 경로 | 요청 경로 | 일치 여부 |
| Prefix | / | (모든 경로) | 예 |
| Exact | /foo | /foo | 예 |
| Exact | /foo | /bar | 아니오 |
| Exact | /foo | /foo/ | 아니오 |
| Exact | /foo/ | /foo | 아니오 |
| Prefix | /foo | /foo, /foo/ | 예 |
| Prefix | /foo/ | /foo, /foo/ | 예 |
| Prefix | /aaa/bb | /aaa/bbb | 아니오 |
| Prefix | /aaa/bbb | /aaa/bbb | 예 |
| Prefix | /aaa/bbb/ | /aaa/bbb | 예, 마지막 슬래시 무시함 |
| Prefix | /aaa/bbb | /aaa/bbb/ | 예, 마지막 슬래시 일치함 |
| Prefix | /aaa/bbb | /aaa/bbb/ccc | 예, 하위 경로 일치함 |
| Prefix | /aaa/bbb | /aaa/bbbxyz | 아니오, 문자열 접두사 일치하지 않음 |
| Prefix | /, /aaa | /aaa/ccc | 예, /aaa 접두사 일치함 |
| Prefix | /, /aaa, /aaa/bbb | /aaa/bbb | 예, /aaa/bbb 접두사 일치함 |
| Prefix | /, /aaa, /aaa/bbb | /ccc | 예, / 접두사 일치함 |
| Prefix | /aaa | /ccc | 아니오, 기본 백엔드 사용함 |
| Mixed | /foo (Prefix), /foo (Exact) | /foo | 예, Exact 선호함 |
자료모음
## 4 노드포트, 로드밸런서 연습문제
  tomcat-deploy-np-lb.yaml
  ```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  creationTimestamp: null
  labels:
    run: tomcat
  name: tomcat
spec:
  replicas: 1
  selector:
    matchLabels:
      run: tomcat
  strategy: {}
  template:
    metadata:
      creationTimestamp: null
      labels:
        run: tomcat
    spec:
      containers:
      - image: consol/tomcat-7.0
        name: tomcat
        ports:
        - containerPort: 8080
        resources: {}
status: {}
---
apiVersion: v1
kind: Service
metadata:
  name: tomcat-np
spec:
  type: NodePort
  selector:
    run: tomcat
  ports:
    - protocol: TCP
      port: 80
      targetPort: 8080
      nodePort: 30002
---
apiVersion: v1
kind: Service
metadata:
  name: tomcat-lb
spec:
  type: LoadBalancer
  selector:
    run: tomcat
  ports:
    - protocol: TCP
      port: 80
      targetPort: 8080
  ```
## 5 인그레스(ingress) 실습
  인그레스 nginx 설치
  ```bash
git clone https://github.com/kubernetes/ingress-nginx/
kubectl apply -k `pwd`/ingress-nginx/deploy/static/provider/baremetal/
kubectl delete validatingwebhookconfigurations.admissionregistration.k8s.io ingress-nginx-admission
  ```
  ingress 자원을 사용해 룰 생성
  ```yaml
cat <<EOF | kubectl apply -f -
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: http-go-ingress
  annotations:
    kubernetes.io/ingress.class: nginx
    nginx.ingress.kubernetes.io/rewrite-target: /welcome/test
spec:
  rules:
    - http:
        paths:
          - pathType: Exact
            path: /welcome/test
            backend:
              service:
                name: http-go
                port: 
                  number: 80
EOF
  ```
  서비스를 구성할 수 있는 다음 명령어를 실행한다.
  ```yaml
kubectl create deployment http-go --image=gasbugs/http-go:ingress # 인그레스 테스트용 http-go
kubectl expose deployment http-go --port=80 --target-port=8080
  ```
  TLS 인증서 생성
  ```bash
openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
    -out ingress-tls.crt \
    -keyout ingress-tls.key \
    -subj "/CN=ingress-tls"

kubectl create secret tls ingress-tls \
    --namespace default \
    --key ingress-tls.key \
    --cert ingress-tls.crt
  ```
  TLS 인증서를 사용하는 ingress 생성
  ```yaml
cat <<EOF | kubectl apply -f -
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: http-go-ingress
  annotations:
    kubernetes.io/ingress.class: nginx
    nginx.ingress.kubernetes.io/rewrite-target: /welcome/test
    nginx.ingress.kubernetes.io/ssl-redirect: "true"
spec:
  tls:
  - hosts:
    - gasbugs.com
    secretName: ingress-tls
  rules:
    - host: gasbugs.com
      http:
        paths:
          - pathType: Exact
            path: /welcome/test
            backend:
              service:
                name: http-go
                port: 
                  number: 80
EOF
  ```
  ```bash
curl http://gasbugs.com:32049/welcome/test -kv --resolve gasbugs.com:32049:127.0.0.1
ㅊㅕ
curl https://gasbugs.com:31915/welcome/test -kv --resolve gasbugs.com:31915:127.0.0.1

curl https://gasbugs1.com:31915/welcome/test -kv --resolve gasbugs1.com:31915:127.0.0.1
  ```
## 6 인그레스 연습문제
  ```bash
kubectl delete all --all

# http-go 디플로이먼트/서비스 생성
kubectl create deploy http-go --image=gasbugs/http-go 
kubectl expose deploy http-go --port=80 --target-port=8080

# 톰캣 디플로이먼트/서비스 생성
kubectl create deploy tomcat --image=consol/tomcat-7.0 
kubectl expose deploy tomcat --port=80 --target-port=8080

# TLS 인증서 생성
openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
    -out gasbugs-tls.crt \
    -keyout gasbugs-tls.key \
    -subj "/CN=ingress-tls"

# tls 인증서를 통해 secret을 구성
kubectl create secret tls gasbugs-tls \
    --namespace default \
    --key gasbugs-tls.key \
    --cert gasbugs-tls.crt

cat <<EOF | kubectl apply -f -
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: http-go-ingress
  annotations:
    kubernetes.io/ingress.class: nginx
    nginx.ingress.kubernetes.io/rewrite-target: /
    nginx.ingress.kubernetes.io/ssl-redirect: "true"
spec:
  tls:
  - hosts:
    - tomcat.gasbugs.com    
    - http-go.gasbugs.com
    secretName: gasbugs-tls
  rules:
    - host: http-go.gasbugs.com
      http:
        paths:
          - pathType: Prefix
            path: /
            backend:
              service:
                name: http-go
                port: 
                  number: 80
    - host: tomcat.gasbugs.com
      http:
        paths:
          - pathType: Prefix
            path: /
            backend:
              service:
                name: tomcat
                port: 
                  number: 80
EOF
  ```
  ```bash
curl http://tomcat.gasbugs.com:32049/welcome/test -kv --resolve tomcat.gasbugs.com:32049:127.0.0.1

curl https://tomcat.gasbugs.com:31915/ -kv --resolve tomcat.gasbugs.com:31915:127.0.0.1

curl https://http-go.gasbugs.com:31915/ -kv --resolve http-go.gasbugs.com:31915:127.0.0.1
  ```
## 7 서비스 DNS 연습문제
  blue-jenkins-svc-deploy.yaml
  ```yaml
apiVersion: v1
kind: Namespace
metadata:
  creationTimestamp: null
  name: blue
spec: {}
status: {}
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
      - image: jenkins
        name: pod-jenkins
        ports:
        - containerPort: 8080
        resources: {}
status: {}
---
apiVersion: v1
kind: Service
metadata:
  creationTimestamp: null
  labels:
    run: pod-jenkins
  name: srv-jenkins
  namespace: blue
spec:
  ports:
  - port: 8080
    protocol: TCP
    targetPort: 8080
  selector:
    run: pod-jenkins
status:
  loadBalancer: {}
  ```

## 출처

- 원문: https://www.notion.so/Kubernetes-Ingress-245172a556d6803fb138d25f2c5cbd35
- Vault path: wiki/notes/kubernetes/Kubernetes---Ingress-란.md
