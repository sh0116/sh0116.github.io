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
![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/50226290-9a5d-44b5-a10d-6e70642e1a84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WYGUYAOE%2F20250805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250805T002736Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJIMEYCIQDlVgF10LweMiAzjFcyt4KO6QehYGNBi5XjahQk11iWWQIhANNZKWait%2FZgBF2cxo2qxSnCqAgATYuliQUB8g3S7QSXKv8DCFAQABoMNjM3NDIzMTgzODA1IgwJ0Vj%2B4JRc8%2BOvpWIq3AP%2FP3oXDZY0zvxil30AxX3huGx%2FNMlYxRkjJnsi8716d4IFqVSg%2F56n3EGNVnaBEOBlPi9Q4a4%2BkNK%2BjlPB7JD3z87GejSvAS8FW5UspXZAbpitrIFQey96bP0eOZzVm%2BaoNwLgtdx%2Fi9fTjV4E80gBEN2MtI5MUJQcyzam3xm0YEHpE6erUvvrX%2B2dYpE5C1PUnLyn0Bd6mpu4Lx3%2Fk5KOKtynVShAjtKj%2FOUpYdHoTF7opYtZJCNUylcxrvWuhs6YKB1vv0tNjAaBpzz9BK3zvDEjCgMAqkdl%2Fa2gYPiI74zOaffyrjNyQZt0DyNiIUwilHdmx5a7%2FuIuywDhMuJTmIY3K8bF1n%2B5iephmBsY3JDXfit3PPVfn7Bl2wUUIEuWF9fJG6S1uRtKkEGOLggVWJahsT0ht73ONd%2Fep9neymqcRqixwTXxOAPnVN9h4H2jl7AuofiRC2ItlBSuJN3SjuHefugFt6nNb71Zdyypt1tKuEzW2QEdY4n21scFM2Tc31XsKvu5b5dH2Dg70AFUz3lWPVHbPBpcbLFce2B7m043rbAdraBI4jp33On1ijKyApfLEQhIx%2BDSPzIaa725oezAc8Xquy86LMvV%2Bu8zEKsyZ48jh4vOLHqELzDB9MTEBjqkAUb6het1ZDZT2BHltiKA0hMnnmNZnc02JNseaLqbC89V089eMF1jIBVPTfCwwtzk9b2BeGjsLVwS0UEt0p5fqeKQNWbthmH%2BKVog%2FyaTs0RE4gZLrthpZP5khWc0C9QQSFdymyKKd2MMuaMmFEp58ngSftqYGNjKf6ceRJY1SS2ydSxNTlzFYqJ1hFE7ZgCoPnJr8N1%2FymecMOZUS7NtDrch7Y5%2F&X-Amz-Signature=d170fb327b48baefa3753ce819305277a6503174986449a3d9e24b9095f3cd62&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

# CoreDNS

- 내부에서 DNS서버 역할을 하는 POD가 조냊
- 각 미들웨어를 통해 로깅, 캐싱, 등의 기능을 가짐
![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/719cb48d-1620-4790-b196-3fc64458fe2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WYGUYAOE%2F20250805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250805T002736Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJIMEYCIQDlVgF10LweMiAzjFcyt4KO6QehYGNBi5XjahQk11iWWQIhANNZKWait%2FZgBF2cxo2qxSnCqAgATYuliQUB8g3S7QSXKv8DCFAQABoMNjM3NDIzMTgzODA1IgwJ0Vj%2B4JRc8%2BOvpWIq3AP%2FP3oXDZY0zvxil30AxX3huGx%2FNMlYxRkjJnsi8716d4IFqVSg%2F56n3EGNVnaBEOBlPi9Q4a4%2BkNK%2BjlPB7JD3z87GejSvAS8FW5UspXZAbpitrIFQey96bP0eOZzVm%2BaoNwLgtdx%2Fi9fTjV4E80gBEN2MtI5MUJQcyzam3xm0YEHpE6erUvvrX%2B2dYpE5C1PUnLyn0Bd6mpu4Lx3%2Fk5KOKtynVShAjtKj%2FOUpYdHoTF7opYtZJCNUylcxrvWuhs6YKB1vv0tNjAaBpzz9BK3zvDEjCgMAqkdl%2Fa2gYPiI74zOaffyrjNyQZt0DyNiIUwilHdmx5a7%2FuIuywDhMuJTmIY3K8bF1n%2B5iephmBsY3JDXfit3PPVfn7Bl2wUUIEuWF9fJG6S1uRtKkEGOLggVWJahsT0ht73ONd%2Fep9neymqcRqixwTXxOAPnVN9h4H2jl7AuofiRC2ItlBSuJN3SjuHefugFt6nNb71Zdyypt1tKuEzW2QEdY4n21scFM2Tc31XsKvu5b5dH2Dg70AFUz3lWPVHbPBpcbLFce2B7m043rbAdraBI4jp33On1ijKyApfLEQhIx%2BDSPzIaa725oezAc8Xquy86LMvV%2Bu8zEKsyZ48jh4vOLHqELzDB9MTEBjqkAUb6het1ZDZT2BHltiKA0hMnnmNZnc02JNseaLqbC89V089eMF1jIBVPTfCwwtzk9b2BeGjsLVwS0UEt0p5fqeKQNWbthmH%2BKVog%2FyaTs0RE4gZLrthpZP5khWc0C9QQSFdymyKKd2MMuaMmFEp58ngSftqYGNjKf6ceRJY1SS2ydSxNTlzFYqJ1hFE7ZgCoPnJr8N1%2FymecMOZUS7NtDrch7Y5%2F&X-Amz-Signature=6c011931beaf2a0dec0e467b5c342b2a171aace485af4a24902a2e0ebc84f08c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

[https://kubernetes.io/ko/docs/concepts/services-networking/dns-pod-service/](https://kubernetes.io/ko/docs/concepts/services-networking/dns-pod-service/)

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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/ecb9b8a2-564a-4d0b-966f-f25233e45fde/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WYGUYAOE%2F20250805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250805T002736Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJIMEYCIQDlVgF10LweMiAzjFcyt4KO6QehYGNBi5XjahQk11iWWQIhANNZKWait%2FZgBF2cxo2qxSnCqAgATYuliQUB8g3S7QSXKv8DCFAQABoMNjM3NDIzMTgzODA1IgwJ0Vj%2B4JRc8%2BOvpWIq3AP%2FP3oXDZY0zvxil30AxX3huGx%2FNMlYxRkjJnsi8716d4IFqVSg%2F56n3EGNVnaBEOBlPi9Q4a4%2BkNK%2BjlPB7JD3z87GejSvAS8FW5UspXZAbpitrIFQey96bP0eOZzVm%2BaoNwLgtdx%2Fi9fTjV4E80gBEN2MtI5MUJQcyzam3xm0YEHpE6erUvvrX%2B2dYpE5C1PUnLyn0Bd6mpu4Lx3%2Fk5KOKtynVShAjtKj%2FOUpYdHoTF7opYtZJCNUylcxrvWuhs6YKB1vv0tNjAaBpzz9BK3zvDEjCgMAqkdl%2Fa2gYPiI74zOaffyrjNyQZt0DyNiIUwilHdmx5a7%2FuIuywDhMuJTmIY3K8bF1n%2B5iephmBsY3JDXfit3PPVfn7Bl2wUUIEuWF9fJG6S1uRtKkEGOLggVWJahsT0ht73ONd%2Fep9neymqcRqixwTXxOAPnVN9h4H2jl7AuofiRC2ItlBSuJN3SjuHefugFt6nNb71Zdyypt1tKuEzW2QEdY4n21scFM2Tc31XsKvu5b5dH2Dg70AFUz3lWPVHbPBpcbLFce2B7m043rbAdraBI4jp33On1ijKyApfLEQhIx%2BDSPzIaa725oezAc8Xquy86LMvV%2Bu8zEKsyZ48jh4vOLHqELzDB9MTEBjqkAUb6het1ZDZT2BHltiKA0hMnnmNZnc02JNseaLqbC89V089eMF1jIBVPTfCwwtzk9b2BeGjsLVwS0UEt0p5fqeKQNWbthmH%2BKVog%2FyaTs0RE4gZLrthpZP5khWc0C9QQSFdymyKKd2MMuaMmFEp58ngSftqYGNjKf6ceRJY1SS2ydSxNTlzFYqJ1hFE7ZgCoPnJr8N1%2FymecMOZUS7NtDrch7Y5%2F&X-Amz-Signature=dff27ad119f807d7f1728c65bc9642aa3436473f9951497cbed8eeba4878ae6c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


