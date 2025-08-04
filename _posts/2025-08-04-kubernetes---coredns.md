---
title: "Kubernetes - CoreDNS"
date: 2025-08-04 06:05:00 +0900
categories: [kubernetes]
tags: [Kubernetes]
description: Kubernetes 기초
toc: true
comments: true
---

## DNS 도메인 네임 서비스

- 서비스를 생성하면 대응되는 DNS 엔트리가 생성됨 
- 엔트리는 <서비스 이름>.<네임스페이스 이름>.svc.cluster.local 의 형식을 가짐
![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/50226290-9a5d-44b5-a10d-6e70642e1a84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZEW6C6CB%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T071437Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIBjaCDUe6U1ntNlRX4PLLMJsByD%2FaBRm2ycjxvkkH1PeAiEA3ydVVyqK1UGCwx%2F9nL3jfrff62jPlB%2BHs2KXfHK%2BZXwq%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDJ8xurcfXW0JY3PIiCrcA5b6vVa%2FQc6ybVjgW012C7Q7lgYcVkxUziEvB5wJJWBpbPJdvyGlLQaVP%2FTzIADIDxSueWcb4eJJQfaNde6nQV0z9BfmqglAYiDHC4NtoAJ9VbCzZL5fuYp%2FpvpZfiG0XHdWmDgUI0OL1%2BGC7FMn1OAlemvHT9uEQwwJF3tuCbVPcl9QGYGN2aKtbA4q6uBBeri5xazNp5UbNViIfCsi3V9UncdIfBjZ9939NKXO939gkR3J4tH1bQQpNi8azuqDvQJVctmZwmRA08zltWeiYx667U%2Byc8FUyW6qoQgiFobdqH6IpOuEGbVoDu8%2BnhXtImBPoN9Y2bcPw669EaCf17gdBlHanjGEyulZNLG7R0SIQh%2B6FlIg133Na7dwerzbjoTvFIYqrTe1EpnlJOiifL7iCEtzxDoO5wqWXa2n5eHNC9wD%2Fhycoc6nDQ8LNkwdexShuSHpgmDDF7Haqd8t8O%2Bu%2B0BsaRifVcRjciCgq%2BVt3cWIF5plfsXTGTcL%2FgrqVCKsyAD6P8TsMjZkLlPKJWmKH7BL9A7lqEJ%2BUD5z02%2BuCSzKg%2FjH7Wj6E7JcS60iHFlhqOks8rW7iQZCDhDwwkyPWlw%2BrQUZ%2BGKx9n3MoE7Cil85yWEDU5VxosbiMKS4wcQGOqUB9w9Anb%2BwIyGLz1zXkI1Y0DwF%2BrhkW12l1OtNqh%2FEYmwEk%2B2PTvvUKkhsVy82hy4FpT3gLdv32rRxlKHHG5l%2BvmmyKITrT3sfsInwTe3IhUkA8jZetgFcx38BHqOXeOTdDnmkZqkE1ITB4EjoH%2BA57GEiSJLotuUbADiLzZGBv674RPKACF%2BTmwBHJbyjg%2F2WZdUVQyKqeipiVNuOYw5v2fEgRXZS&X-Amz-Signature=f9a706005db343c34b35fed2d53d3fee95a6b28b69ab619664ce238b03d4a0ad&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

# CoreDNS

- 내부에서 DNS서버 역할을 하는 POD가 조냊
- 각 미들웨어를 통해 로깅, 캐싱, 등의 기능을 가짐
![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/719cb48d-1620-4790-b196-3fc64458fe2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZEW6C6CB%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T071437Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIBjaCDUe6U1ntNlRX4PLLMJsByD%2FaBRm2ycjxvkkH1PeAiEA3ydVVyqK1UGCwx%2F9nL3jfrff62jPlB%2BHs2KXfHK%2BZXwq%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDJ8xurcfXW0JY3PIiCrcA5b6vVa%2FQc6ybVjgW012C7Q7lgYcVkxUziEvB5wJJWBpbPJdvyGlLQaVP%2FTzIADIDxSueWcb4eJJQfaNde6nQV0z9BfmqglAYiDHC4NtoAJ9VbCzZL5fuYp%2FpvpZfiG0XHdWmDgUI0OL1%2BGC7FMn1OAlemvHT9uEQwwJF3tuCbVPcl9QGYGN2aKtbA4q6uBBeri5xazNp5UbNViIfCsi3V9UncdIfBjZ9939NKXO939gkR3J4tH1bQQpNi8azuqDvQJVctmZwmRA08zltWeiYx667U%2Byc8FUyW6qoQgiFobdqH6IpOuEGbVoDu8%2BnhXtImBPoN9Y2bcPw669EaCf17gdBlHanjGEyulZNLG7R0SIQh%2B6FlIg133Na7dwerzbjoTvFIYqrTe1EpnlJOiifL7iCEtzxDoO5wqWXa2n5eHNC9wD%2Fhycoc6nDQ8LNkwdexShuSHpgmDDF7Haqd8t8O%2Bu%2B0BsaRifVcRjciCgq%2BVt3cWIF5plfsXTGTcL%2FgrqVCKsyAD6P8TsMjZkLlPKJWmKH7BL9A7lqEJ%2BUD5z02%2BuCSzKg%2FjH7Wj6E7JcS60iHFlhqOks8rW7iQZCDhDwwkyPWlw%2BrQUZ%2BGKx9n3MoE7Cil85yWEDU5VxosbiMKS4wcQGOqUB9w9Anb%2BwIyGLz1zXkI1Y0DwF%2BrhkW12l1OtNqh%2FEYmwEk%2B2PTvvUKkhsVy82hy4FpT3gLdv32rRxlKHHG5l%2BvmmyKITrT3sfsInwTe3IhUkA8jZetgFcx38BHqOXeOTdDnmkZqkE1ITB4EjoH%2BA57GEiSJLotuUbADiLzZGBv674RPKACF%2BTmwBHJbyjg%2F2WZdUVQyKqeipiVNuOYw5v2fEgRXZS&X-Amz-Signature=33e0b9f91cd1a080fcb0fe328c2089ad2ccba9096558712ebb509ad57ddfb48a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

## POD에서도 Subdomain을 사용하면 DNS서비스를 사용가능하다.

- yaml 파일의 호스트 이름은 pod의 metadata.name을 따름
- 필요한 경우 Hostname을 따로 선택 가능
- 서브 도메인을 설정하면 FQDN 사용가능
### 공식문서

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

## 연습문제

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/ecb9b8a2-564a-4d0b-966f-f25233e45fde/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZEW6C6CB%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T071437Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIBjaCDUe6U1ntNlRX4PLLMJsByD%2FaBRm2ycjxvkkH1PeAiEA3ydVVyqK1UGCwx%2F9nL3jfrff62jPlB%2BHs2KXfHK%2BZXwq%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDJ8xurcfXW0JY3PIiCrcA5b6vVa%2FQc6ybVjgW012C7Q7lgYcVkxUziEvB5wJJWBpbPJdvyGlLQaVP%2FTzIADIDxSueWcb4eJJQfaNde6nQV0z9BfmqglAYiDHC4NtoAJ9VbCzZL5fuYp%2FpvpZfiG0XHdWmDgUI0OL1%2BGC7FMn1OAlemvHT9uEQwwJF3tuCbVPcl9QGYGN2aKtbA4q6uBBeri5xazNp5UbNViIfCsi3V9UncdIfBjZ9939NKXO939gkR3J4tH1bQQpNi8azuqDvQJVctmZwmRA08zltWeiYx667U%2Byc8FUyW6qoQgiFobdqH6IpOuEGbVoDu8%2BnhXtImBPoN9Y2bcPw669EaCf17gdBlHanjGEyulZNLG7R0SIQh%2B6FlIg133Na7dwerzbjoTvFIYqrTe1EpnlJOiifL7iCEtzxDoO5wqWXa2n5eHNC9wD%2Fhycoc6nDQ8LNkwdexShuSHpgmDDF7Haqd8t8O%2Bu%2B0BsaRifVcRjciCgq%2BVt3cWIF5plfsXTGTcL%2FgrqVCKsyAD6P8TsMjZkLlPKJWmKH7BL9A7lqEJ%2BUD5z02%2BuCSzKg%2FjH7Wj6E7JcS60iHFlhqOks8rW7iQZCDhDwwkyPWlw%2BrQUZ%2BGKx9n3MoE7Cil85yWEDU5VxosbiMKS4wcQGOqUB9w9Anb%2BwIyGLz1zXkI1Y0DwF%2BrhkW12l1OtNqh%2FEYmwEk%2B2PTvvUKkhsVy82hy4FpT3gLdv32rRxlKHHG5l%2BvmmyKITrT3sfsInwTe3IhUkA8jZetgFcx38BHqOXeOTdDnmkZqkE1ITB4EjoH%2BA57GEiSJLotuUbADiLzZGBv674RPKACF%2BTmwBHJbyjg%2F2WZdUVQyKqeipiVNuOYw5v2fEgRXZS&X-Amz-Signature=d3466affeea173cc1afb709500d367ece0c631eff52cb12fc67cc2d24cea4eee&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


