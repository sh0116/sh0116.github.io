---
title: "Kubernetes - POD YAML작성"
date: 2025-08-04 06:05:00 +0900
categories: [kubernetes]
tags: [Kubernetes]
description: Kubernetes 기초
toc: true
comments: true
---

# 파드 yaml 디스크립션 작성

### kuberctl 기본 pod yaml파일 

```bash
kubectl explain pods
```

```yaml
KIND:     Pod
VERSION:  v1

DESCRIPTION:
     Pod is a collection of containers that can run on a host. This resource is
     created by clients and scheduled onto hosts.

FIELDS:
   apiVersion   <string>
     APIVersion defines the versioned schema of this representation of an
     object. Servers should convert recognized schemas to the latest internal
     value, and may reject unrecognized values. More info:
     https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources

   kind <string>
     Kind is a string value representing the REST resource this object
     represents. Servers may infer this from the endpoint the client submits
     requests to. Cannot be updated. In CamelCase. More info:
     https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds

   metadata     <Object>
     Standard object's metadata. More info:
     https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata

   spec <Object>
     Specification of the desired behavior of the pod. More info:
     https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status

   status       <Object>
     Most recently observed status of the pod. This data may not be up to date.
     Populated by the system. Read-only. More info:
     https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status
```

# 연습 문제 겸 POD작성 연습 

### 문제 내용

- 모든 리소스 삭제
- Yaml 사용하여 docker images jenkins 로 jenkins-manual pod 생성하기
- jenkins pod에서 curl 명령어로 localhost:8080 접속하기
- jenkins pod 8888포트 포워딩하기
- 현재 jenkinss-manual 설정 yaml로 출력하기
## 모든 리소스 삭제

```bash
kubectl delete svc --all
kubectl delete deploy --all
kubectl delete pod --all
```

## Yaml 사용하여 docker images jenkins 로 jenkins-manual pod 생성하기

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod-practice
spec:
  containers:
  - name: jenkins-manuale
    image: jenkins/jenkins:lts-jdk11
    ports:
    -  containerPort: 8080
```

```bash
k create -f jenkins-manual.yaml
```

## jenkins pod에서 curl 명령어로 localhost:8080 접속하기

```yaml
kubectl exec pod이름  -- curl localhost:8080 -s
```

## jenkins pod 8888포트 포워딩하기

```yaml
kubectl port-forward pod이름 8888:8080
```

## 현재 jenkinss-manual 설정 yaml로 출력하기

```bash
kubectl get pod pod이름 -o yaml
```

### kubectl YAML 주석 달기

```bash
kubectl annotate pod 파드이름 test123=test123
```

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/ce5266bb-ffff-4c40-96e1-5a04ccf31630/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X3N4RGRC%2F20250805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250805T061142Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJHMEUCIQCT71U1QwlAl%2F2SYrrEtJMB%2BFzMXBr4i7mcj8uDqMlgXwIgbVmGXZUnF49KWUk2qsqKh6MynaEA810Q%2BFdSU1opzbcq%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDICSSaWcrWKT9ZBvPyrcA2RgvVzUZ2ihWMhe4S%2BFIeRCeUhX6H%2Fh%2BbHWMd8%2Ftg247hNgVgfLkxmBjmNeTG40lNsBOjxdDcn7HjLv%2BdZmIVCyT%2BaaP4MkdhtCvtmu4%2BFbqK8%2FuSFJuU3mBbSLBgCPXFPlTLNnWslq3jD640FdZ02DHW2Gg%2BKSrMhfWv%2Bl6KD1fnF8VIHHsKLspTJOddq42ty1IUo6htHAdYbLtxiwP%2FyjiTxcoFES19ucB%2BGwD8dY3nj%2Fn7L3CjGOSeZeKXQjIo1M3JNQgbDguNNVpIIuHh%2FYdn5Os%2B5TmtW3IxDqcfHtTTSG8f7XTwomdLX78KYxVYf0FMGWNXIMJ4GUsHRPenp2ZlU2vtze01wQrRvvExWIHKo2DWntiqVbrkl1Akd5k4PA2fpxJl%2BjBdTFcHQL%2F0VulJ1HudXafeDJx%2FBkeUI%2FY6POlLMMdeXcjNZ7gRA6I5D83JR1Fl6VdVyjI%2Ffc14XHnSkiSDTYQPEnomu6ZNDhANmvdnzMnUA0VMlirN%2Ff1HfyIfog0Z3GEXvYDizfc3%2B3p2uXrmFtxorJzR9dr0Yu3NvbOO2VCZ0o9tqAmfFVTIqwsPh9K4SQ%2BuJJmQt87KdDN%2Bu52y2siCBo2FiuEyuRE6gC%2BDtXqDRdqhGnMK%2B0xsQGOqUBJAA63HNmXTkO68Z2AIJ%2BY4xJ0cGt7Q%2BFpD8N6NvVUIfVNvwQswf%2BB9tIEloqFFsiwCy2rSjr7d9oi9FIBZ6OP83q1LCvvx25G1ljrJResLzDLZ7DipgW8NWNuwJon3NDggr04RBT2yj4%2BPc6eQy0CWPNr7Nm7g2EKO6rbKmtNskaulj%2FmBRThaqXqwPDmaWnLwZoN5ViVJDr%2BIoGyR1%2BguM6mdpH&X-Amz-Signature=e78811fab811b92955d71bbe61a45bb52c486f666dd776b445d4c3c271d05215&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


