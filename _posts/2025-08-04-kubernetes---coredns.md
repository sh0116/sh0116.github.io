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
![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/50226290-9a5d-44b5-a10d-6e70642e1a84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U7EW5W43%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T072045Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIA8DtpL3R5WSH1kqMoUHf9O%2B16EGCwzVR%2BskLXOcilO%2FAiEAvPMTWboQ9RVClpg9xGWOurUyXU3R5876Dku8fJGnMVsq%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDDgnS4EB2LCP7dn9XircA4%2FeUdmGlnKSf3xZKMF8UukyWJ9FRpbD%2BDnqQ1E1AatPiECpULYA2cbblpvRm5Tt9U1J62wjafACm4MjeSHbclfkeInbM04TXsHFsWtuQLjHmJn9iFksYnVK5Hc5tDBWX2sx%2FmHe7DVW7TPQAp2FTyRT9hD8tYpNKdsp53rbzOGaQMVcGt0YpWOBw7WV1WVjkhOHfVYO30ySnC%2BN15ye3yMFJFgn%2FOLof68g3N3gm%2Fg9D%2FRBzbC3036cdkPIjlOj%2BBVM%2Bkmyu2Y2Nvk8G7kQEAEmkXzu7H67mYK1y7OD4ywLKPZy5%2Fv2xGayvZCX34TmHdTtIil%2BXmLxIjOeK6tIdr3VcccuDlbr3Ev7wrmfb0DFdRVXmQ%2FawE%2Br9ISPaAvpvkP5ZXdpRT7N7hznolPe%2BavirGY3MsAPhlZ8CLISRjT2QLgsXf561FihNkMqCFq0FiEHo%2BCWaSuKMiKIFA32ivBpLLs%2Fl6a5C6%2BxWEsp%2FMbppLjvHWmStTffB97AtZNq0kolqK9GS6yKindcKr%2FVoREXtp4b3Z1wrfykH0GDKw5%2FhyhUrtHSigUAx6kXlypMp%2ByxlID%2B6PvLpWNn1tLf1s0zPItcs5r%2Fize3zJQBoNXM1yRDlK40A75iNycNMLm2wcQGOqUBWh%2F9L0xz64GfW5fEqVol9qQ2GbRKiwvwP9GeBUc3%2BUEqBzwUXPnMJeaDKXrU1fyK1xYfxwbx%2BwWwhFpxU9aWX2eaUV8xN2mm5Q0rd741ouly3QLWdqa1cQXT1tvkBrbwQXbgFm5wc4GoYdiQPec2wECXAKWQEXDNtS3uYT7IFIMT32iFO5ejn93Dol7D7F9W7h8iAwC%2BVixaJ3pmui35WKM76YVE&X-Amz-Signature=bf9d43af676fbb806924854d7bde7bb7a3835809c7b859f45c3f3f4d6c1e6415&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

# CoreDNS

- 내부에서 DNS서버 역할을 하는 POD가 조냊
- 각 미들웨어를 통해 로깅, 캐싱, 등의 기능을 가짐
![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/719cb48d-1620-4790-b196-3fc64458fe2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U7EW5W43%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T072045Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIA8DtpL3R5WSH1kqMoUHf9O%2B16EGCwzVR%2BskLXOcilO%2FAiEAvPMTWboQ9RVClpg9xGWOurUyXU3R5876Dku8fJGnMVsq%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDDgnS4EB2LCP7dn9XircA4%2FeUdmGlnKSf3xZKMF8UukyWJ9FRpbD%2BDnqQ1E1AatPiECpULYA2cbblpvRm5Tt9U1J62wjafACm4MjeSHbclfkeInbM04TXsHFsWtuQLjHmJn9iFksYnVK5Hc5tDBWX2sx%2FmHe7DVW7TPQAp2FTyRT9hD8tYpNKdsp53rbzOGaQMVcGt0YpWOBw7WV1WVjkhOHfVYO30ySnC%2BN15ye3yMFJFgn%2FOLof68g3N3gm%2Fg9D%2FRBzbC3036cdkPIjlOj%2BBVM%2Bkmyu2Y2Nvk8G7kQEAEmkXzu7H67mYK1y7OD4ywLKPZy5%2Fv2xGayvZCX34TmHdTtIil%2BXmLxIjOeK6tIdr3VcccuDlbr3Ev7wrmfb0DFdRVXmQ%2FawE%2Br9ISPaAvpvkP5ZXdpRT7N7hznolPe%2BavirGY3MsAPhlZ8CLISRjT2QLgsXf561FihNkMqCFq0FiEHo%2BCWaSuKMiKIFA32ivBpLLs%2Fl6a5C6%2BxWEsp%2FMbppLjvHWmStTffB97AtZNq0kolqK9GS6yKindcKr%2FVoREXtp4b3Z1wrfykH0GDKw5%2FhyhUrtHSigUAx6kXlypMp%2ByxlID%2B6PvLpWNn1tLf1s0zPItcs5r%2Fize3zJQBoNXM1yRDlK40A75iNycNMLm2wcQGOqUBWh%2F9L0xz64GfW5fEqVol9qQ2GbRKiwvwP9GeBUc3%2BUEqBzwUXPnMJeaDKXrU1fyK1xYfxwbx%2BwWwhFpxU9aWX2eaUV8xN2mm5Q0rd741ouly3QLWdqa1cQXT1tvkBrbwQXbgFm5wc4GoYdiQPec2wECXAKWQEXDNtS3uYT7IFIMT32iFO5ejn93Dol7D7F9W7h8iAwC%2BVixaJ3pmui35WKM76YVE&X-Amz-Signature=2bcb1f6de1289c3a57919f237c20ba0c9f78f9884cb0df72716911516a8f6549&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/ecb9b8a2-564a-4d0b-966f-f25233e45fde/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U7EW5W43%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T072045Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIA8DtpL3R5WSH1kqMoUHf9O%2B16EGCwzVR%2BskLXOcilO%2FAiEAvPMTWboQ9RVClpg9xGWOurUyXU3R5876Dku8fJGnMVsq%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDDgnS4EB2LCP7dn9XircA4%2FeUdmGlnKSf3xZKMF8UukyWJ9FRpbD%2BDnqQ1E1AatPiECpULYA2cbblpvRm5Tt9U1J62wjafACm4MjeSHbclfkeInbM04TXsHFsWtuQLjHmJn9iFksYnVK5Hc5tDBWX2sx%2FmHe7DVW7TPQAp2FTyRT9hD8tYpNKdsp53rbzOGaQMVcGt0YpWOBw7WV1WVjkhOHfVYO30ySnC%2BN15ye3yMFJFgn%2FOLof68g3N3gm%2Fg9D%2FRBzbC3036cdkPIjlOj%2BBVM%2Bkmyu2Y2Nvk8G7kQEAEmkXzu7H67mYK1y7OD4ywLKPZy5%2Fv2xGayvZCX34TmHdTtIil%2BXmLxIjOeK6tIdr3VcccuDlbr3Ev7wrmfb0DFdRVXmQ%2FawE%2Br9ISPaAvpvkP5ZXdpRT7N7hznolPe%2BavirGY3MsAPhlZ8CLISRjT2QLgsXf561FihNkMqCFq0FiEHo%2BCWaSuKMiKIFA32ivBpLLs%2Fl6a5C6%2BxWEsp%2FMbppLjvHWmStTffB97AtZNq0kolqK9GS6yKindcKr%2FVoREXtp4b3Z1wrfykH0GDKw5%2FhyhUrtHSigUAx6kXlypMp%2ByxlID%2B6PvLpWNn1tLf1s0zPItcs5r%2Fize3zJQBoNXM1yRDlK40A75iNycNMLm2wcQGOqUBWh%2F9L0xz64GfW5fEqVol9qQ2GbRKiwvwP9GeBUc3%2BUEqBzwUXPnMJeaDKXrU1fyK1xYfxwbx%2BwWwhFpxU9aWX2eaUV8xN2mm5Q0rd741ouly3QLWdqa1cQXT1tvkBrbwQXbgFm5wc4GoYdiQPec2wECXAKWQEXDNtS3uYT7IFIMT32iFO5ejn93Dol7D7F9W7h8iAwC%2BVixaJ3pmui35WKM76YVE&X-Amz-Signature=d8c6af9307d33afc859263a710b93baccaf8cb157e75b17f5745ae7c9356297d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


