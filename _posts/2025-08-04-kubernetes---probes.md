---
title: "Kubernetes - Probes"
date: 2025-08-04 06:05:00 +0900
categories: [kubernetes]
tags: [Kubernetes]
description: Kubernetes 기초
toc: true
comments: true
---

## Probe 3가지 - Pod 보조 역

- Libeness Probe
- Readiness Probe
- Startup Probe
## Liveness Command 설정

```yaml
apiVersion: v1
kind: Pod
metadata:
  labels:
    test: liveness
  name: liveness-exec
spec:
  containers:
  - name: liveness
    image: registry.k8s.io/busybox
    args:
    - /bin/sh
    - -c
    - touch /tmp/healthy; sleep 30; rm -f /tmp/healthy; sleep 600
    livenessProbe:
      exec:
        command: # liveness점검 명령어 (실패 시 pod 재시)
        - cat
        - /tmp/healthy
      initialDelaySeconds: 5 # pod 실행 후 5초뒤 liveness 점검
      periodSeconds: 5 # 5초마다 liveness 점검
```

```yaml
apiVersion: v1
kind: Pod
metadata:
  labels:
    test: liveness
  name: liveness-http
spec:
  containers:
  - name: liveness
    image: registry.k8s.io/liveness #go로 짜여진 코드 5초간 200반환, 이후 500반
    args:
    - /server
    livenessProbe:
      httpGet:             # request 200~399까지 정상 범위 나머지 비정상(pod재시작)
        path: /healthz
        port: 8080
        httpHeaders:
        - name: Custom-Header
          value: Awesome
      initialDelaySeconds: 3
      periodSeconds: 3
```

```go
# image registry.k8s.io/liveness

http.HandleFunc("/healthz", func(w http.ResponseWriter, r *http.Request) {
    duration := time.Now().Sub(started)
    if duration.Seconds() > 10 {
        w.WriteHeader(500)
        w.Write([]byte(fmt.Sprintf("error: %v", duration.Seconds())))
    } else {
        w.WriteHeader(200)
        w.Write([]byte("ok"))
    }
})
```

## Readiness 설정

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: goproxy
  labels:
    app: goproxy
spec:
  containers:
  - name: goproxy
    image: registry.k8s.io/goproxy:0.1
    ports:
    - containerPort: 8080
    readinessProbe: # 8080 검사 / 5초 후 검사 시작 -> 서비스 시작 가능 상태 점검
      tcpSocket:
        port: 8080
      initialDelaySeconds: 5
      periodSeconds: 10
    livenessProbe: # 8080 검사 / 15초 후 검사 시작 -> 컨테이너 정상 실행 점검
      tcpSocket:
        port: 8080
      initialDelaySeconds: 15
      periodSeconds: 20
```

## Statup 설정

```yaml
ports:
- name: liveness-port
  containerPort: 8080
  hostPort: 8080

livenessProbe:
  httpGet:
    path: /healthz
    port: liveness-port
  failureThreshold: 1
  periodSeconds: 10

startupProbe: # 30번 검사 -> 10초간격으로 수행 (30*10=300sec) 
  httpGet:    # 300초 동안 포드가 정상 실행되는 시간을 벌어줌, 만약 비정상이면 pod 종료
    path: /healthz
    port: liveness-port
  failureThreshold: 30
  periodSeconds: 10
```


