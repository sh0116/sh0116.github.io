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
![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/50226290-9a5d-44b5-a10d-6e70642e1a84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666FFBGJGV%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T072214Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJGMEQCIAKIjkzloTR6lYnQnzH1vBZ5IaF8aXrlHkgck8jsgLM7AiA8bVPC%2FnmGjkcQlmHl2b95lla3WLz8tbvb6nKv0l5aCyr%2FAwhAEAAaDDYzNzQyMzE4MzgwNSIMlI7Qso5cTMcWYPbeKtwDzQFCpgggjnIjJM6uoqDvF0hrE67Q9SEiIG1IWIJijG81u9wei3GSyQo3qCnyRJ2ajPGp%2FgDh%2F6cd0dvIdHE1NUn44QcaC76ltgvp%2FXA6hBSDEeXJnkDrWriQbIHzR7aXdIENhxmCGOIe3eyd0cdrv%2Ffu1n1b%2BntsDQifS%2BEbfVijnh3hHIZlHiCCST%2FndeZjE1SYhtFTnI8DzdrhYMRpDxxW%2FDuywy3MSBMtnZqFEwaEKoa9yUbusCU1H2ZNa92rFujRi4Pvf%2B1C2uZgLOgB4wq3Svm4398J077fsnYB3imr8OXzQRPXEWCI8l29WrlM6w0HvXmIEAUIvB75iN2dG9vBJ7sOTmqkcjmFcmQ%2FIutyrMLxSgRpxULFmy26LC9zwFtJ2NteT1wC1cQIX4MMpmnxf0xCHCpJD1eBcJz%2FaSGlZ2%2FbVpYMjEzc6a2rRtBhUf62P2S%2Bvyu16mQ8EqaWKfP9oskEdwvRbH2fl0Qt1gU3iJc3wybwgi%2BqrqcZapJtFi6H2Tmy0vVRB5UaXK9wma9iO2F%2FCzgLXJOq9pNVbAmQUXK4dO1XnwJaQpgfsBRGCt%2FzDweingzMQ3auz%2FNMRcqALUbBlOwAbR4kwiTKkJpGv%2Bd7FJ6YufQp6SMwxrfBxAY6pgEqn35vqIkJD3%2BHMkpf6xICdHS3bQ7kkTVFOUDFqBHMouYfc8CGyQrYaDDrOoKJvMOBTvcOQ6buEsPdns4biyPYln7xiKowXp5CDMAVnWf5B%2BzRe47B3TTYZUvebQCF7oTEH7Uvn%2F1TqD9a5de%2Bu1JqvG1q1Vv%2BWFmBE1IimCXVquKaj4iZovV1vVBVtndQi5O4pHQjUvaWfCu9hbk60aCObPxm7nUv&X-Amz-Signature=462b852697ea3ba1b6a5aa3568cea58130f186d26ac207ef2993ae85d245b7b9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

# CoreDNS

- 내부에서 DNS서버 역할을 하는 POD가 조냊
- 각 미들웨어를 통해 로깅, 캐싱, 등의 기능을 가짐
![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/719cb48d-1620-4790-b196-3fc64458fe2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666FFBGJGV%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T072214Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJGMEQCIAKIjkzloTR6lYnQnzH1vBZ5IaF8aXrlHkgck8jsgLM7AiA8bVPC%2FnmGjkcQlmHl2b95lla3WLz8tbvb6nKv0l5aCyr%2FAwhAEAAaDDYzNzQyMzE4MzgwNSIMlI7Qso5cTMcWYPbeKtwDzQFCpgggjnIjJM6uoqDvF0hrE67Q9SEiIG1IWIJijG81u9wei3GSyQo3qCnyRJ2ajPGp%2FgDh%2F6cd0dvIdHE1NUn44QcaC76ltgvp%2FXA6hBSDEeXJnkDrWriQbIHzR7aXdIENhxmCGOIe3eyd0cdrv%2Ffu1n1b%2BntsDQifS%2BEbfVijnh3hHIZlHiCCST%2FndeZjE1SYhtFTnI8DzdrhYMRpDxxW%2FDuywy3MSBMtnZqFEwaEKoa9yUbusCU1H2ZNa92rFujRi4Pvf%2B1C2uZgLOgB4wq3Svm4398J077fsnYB3imr8OXzQRPXEWCI8l29WrlM6w0HvXmIEAUIvB75iN2dG9vBJ7sOTmqkcjmFcmQ%2FIutyrMLxSgRpxULFmy26LC9zwFtJ2NteT1wC1cQIX4MMpmnxf0xCHCpJD1eBcJz%2FaSGlZ2%2FbVpYMjEzc6a2rRtBhUf62P2S%2Bvyu16mQ8EqaWKfP9oskEdwvRbH2fl0Qt1gU3iJc3wybwgi%2BqrqcZapJtFi6H2Tmy0vVRB5UaXK9wma9iO2F%2FCzgLXJOq9pNVbAmQUXK4dO1XnwJaQpgfsBRGCt%2FzDweingzMQ3auz%2FNMRcqALUbBlOwAbR4kwiTKkJpGv%2Bd7FJ6YufQp6SMwxrfBxAY6pgEqn35vqIkJD3%2BHMkpf6xICdHS3bQ7kkTVFOUDFqBHMouYfc8CGyQrYaDDrOoKJvMOBTvcOQ6buEsPdns4biyPYln7xiKowXp5CDMAVnWf5B%2BzRe47B3TTYZUvebQCF7oTEH7Uvn%2F1TqD9a5de%2Bu1JqvG1q1Vv%2BWFmBE1IimCXVquKaj4iZovV1vVBVtndQi5O4pHQjUvaWfCu9hbk60aCObPxm7nUv&X-Amz-Signature=b011f189fe83fe1e45c042107398409282f961c336c50efe600c7881adb9c4e5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/ecb9b8a2-564a-4d0b-966f-f25233e45fde/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666FFBGJGV%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T072214Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJGMEQCIAKIjkzloTR6lYnQnzH1vBZ5IaF8aXrlHkgck8jsgLM7AiA8bVPC%2FnmGjkcQlmHl2b95lla3WLz8tbvb6nKv0l5aCyr%2FAwhAEAAaDDYzNzQyMzE4MzgwNSIMlI7Qso5cTMcWYPbeKtwDzQFCpgggjnIjJM6uoqDvF0hrE67Q9SEiIG1IWIJijG81u9wei3GSyQo3qCnyRJ2ajPGp%2FgDh%2F6cd0dvIdHE1NUn44QcaC76ltgvp%2FXA6hBSDEeXJnkDrWriQbIHzR7aXdIENhxmCGOIe3eyd0cdrv%2Ffu1n1b%2BntsDQifS%2BEbfVijnh3hHIZlHiCCST%2FndeZjE1SYhtFTnI8DzdrhYMRpDxxW%2FDuywy3MSBMtnZqFEwaEKoa9yUbusCU1H2ZNa92rFujRi4Pvf%2B1C2uZgLOgB4wq3Svm4398J077fsnYB3imr8OXzQRPXEWCI8l29WrlM6w0HvXmIEAUIvB75iN2dG9vBJ7sOTmqkcjmFcmQ%2FIutyrMLxSgRpxULFmy26LC9zwFtJ2NteT1wC1cQIX4MMpmnxf0xCHCpJD1eBcJz%2FaSGlZ2%2FbVpYMjEzc6a2rRtBhUf62P2S%2Bvyu16mQ8EqaWKfP9oskEdwvRbH2fl0Qt1gU3iJc3wybwgi%2BqrqcZapJtFi6H2Tmy0vVRB5UaXK9wma9iO2F%2FCzgLXJOq9pNVbAmQUXK4dO1XnwJaQpgfsBRGCt%2FzDweingzMQ3auz%2FNMRcqALUbBlOwAbR4kwiTKkJpGv%2Bd7FJ6YufQp6SMwxrfBxAY6pgEqn35vqIkJD3%2BHMkpf6xICdHS3bQ7kkTVFOUDFqBHMouYfc8CGyQrYaDDrOoKJvMOBTvcOQ6buEsPdns4biyPYln7xiKowXp5CDMAVnWf5B%2BzRe47B3TTYZUvebQCF7oTEH7Uvn%2F1TqD9a5de%2Bu1JqvG1q1Vv%2BWFmBE1IimCXVquKaj4iZovV1vVBVtndQi5O4pHQjUvaWfCu9hbk60aCObPxm7nUv&X-Amz-Signature=36a70761f894937621ced3e0d75ca46460b0a38d4965cf46dbf8b03b967d73b6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


