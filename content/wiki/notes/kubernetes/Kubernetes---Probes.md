---
source: knowledge-base
origin: notion
title: "Kubernetes - Probes "
area: "Kubernetes"
tags: ["area/kubernetes", "tech/kubernetes"]
created: "2025-08-04T06:05:00.000Z"
last_edited: "2025-08-04T06:27:00.000Z"
status: published
public: true
notion_id: "245172a5-56d6-8050-b026-fb877f9c4874"
notion_url: "https://www.notion.so/Kubernetes-Probes-245172a556d68050b026fb877f9c4874"
type: note
updated: 2026-07-07
---

# Kubernetes - Probes 

## 요약

Kubernetes 기초

Kubernetes 큰 주제 아래에서 세부 개념과 실습 절차를 연결하기 위한 노트입니다.

## 핵심 포인트

- Kubernetes 기초
- Probe 3가지 - Pod 보조 역
- 쿠버네티스 공식 문서 정리
- Liveness Command 설정
- Readiness 설정

## 지식 그래프

- [[wiki/mocs/Knowledge Base|Knowledge Base]]
- [[wiki/mocs/Kubernetes|Kubernetes]]

## 정리 내용

### Probe 3가지 - Pod 보조 역
- Libeness Probe
  - 컨테이너가 살아있는지 판단하고 다시 시작하는 기능
  - 컨테이너의 상태를 스스로 판단하여 교착상태에 빠진 컨테이너를 재시작
  - 버그가 생겨도 높은 가용성을 보임
- Readiness Probe
  - pod가 준비된 상태에 있는지 확인하고 정상 서비스를 시작하는 기능
  - pod가 적절하게 준비되지 않은 경우 로드벨런싱을 하지 않음
- Startup Probe
  - 애플리케이션의 시작 시기 확인하여 가용성을 높이는 기능
  - Liveness와 Readiness의 기능을 비활성화
### 쿠버네티스 공식 문서 정리
  ![[_attachments/notion/Kubernetes---Probes/245172a556d681d1aab4c19f448c977c.png]]
### Liveness Command 설정
> [!note] 로컬 파일을 통해 Pod가 살아있는지 점검 하는 Probe
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
> [!note] HTTP GET요청을 통 Pod가 살아있는지 점검 하는 Probe
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
### Readiness 설정
> [!note] Readiness & liveness probe설정
readiness는 정상 실행을 검사하고 비정상이면 서비스 로드벨런스에서 제거
libeness는 정상 start를 검사하고 비정상이면 pod restart
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
### Statup 설정
> [!note] 시작할 때까지 검사 → 프로그램 시작을 검사(장시간 걸리는 pod의 경우 필)
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

## 출처

- 원문: https://www.notion.so/Kubernetes-Probes-245172a556d68050b026fb877f9c4874
- Vault path: wiki/notes/kubernetes/Kubernetes---Probes.md
