---
title: "Kubernetes - POD란?"
date: 2025-08-04 06:05:00 +0900
categories: [kubernetes]
tags: [Kubernetes]
description: Kubernetes 기초
toc: true
comments: true
---

## 포드, 팟, 파드 == pod의 특징

- 컨테이너의 공동 배포된 그룹이며 k8s 기본 빌딩 블록
- k8s 컨테이너를 개별적으로 배포하지 않고 컨테이너의 pod를 항상 배포하고 운영
- 일반적으로 단일 컨테이너지만 다수 컨테이너 포함도 가능
- 다수의 노드에서 실행되는것이 아니라 한 Node에서 독립적으로 실행
## POD 관리

- 장점
- 동일한 pod의 컨테이너 사이의 부분 격리
## 네트워크 구조

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/f38ce897-ad6d-434b-a035-f306e89b207f/Untitled.png)

## 컨테이너를 POD 전체에 적절하게 구성하는 방법

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/811279dd-4730-40a6-bff1-b650bb32201c/Untitled.png)

 

# POD 구성 Yaml파일

### 파일 구성 요소

- apiVersion : Kubernetes API버전을 가르킴
- Kind : 어떤 리소스 유형인지 (pod, service, replica) 
- MetaData : pod와 관련된 이름, NameSpace, label 그 밖의 정보 존재
- Spec : 컨테이너 볼륨 정보 등등
- 상태 : pod상태, 컨테이너 설명, IPC 등등
```yaml
apiVersion: v1
kind: Pod
metadata:
name: memory-demo
namespace: mem-example
spec:
containers:
  -name: memory-demo-ctr
image: polinux/stress
resources:
requests:
memory: "100Mi"
limits:
memory: "200Mi"
command: ["stress"]
args: ["--vm", "1", "--vm-bytes", "150M", "--vm-hang", "1"]
```


