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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/ce5266bb-ffff-4c40-96e1-5a04ccf31630/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TLTFFFIE%2F20250805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250805T002855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJGMEQCIBLV1XA0aKitoQLWQ5NHO%2BcTsFW7OF5VBJVZ0gcbvcioAiABeQSCT7czzeTA2I3Rkv5lC9l3aQ2gAmfmwR94lUmQ3Sr%2FAwhQEAAaDDYzNzQyMzE4MzgwNSIMcoUlIvomMrpF3S5EKtwD2AIbqclcQzI%2FfJr0H49n%2B5JhhtJbPGP1lj8M6YjLZ%2Fv55G7bhIxYdgPV81BUw2LK2P%2BjRRhRoP1GXUUMLZlpQn9%2FpsDJO6SJsCRfGgmlcDwtgGJGnZlwc6HZIby1Ixw0vlG4A27naqGub6CKdXBFNkjAm0ZQEFd1fonDsTs0Z7590NbRAs1B0SEP%2B8TfMAnr4UxfU0NCro8wMNcag1CWpdMD98L0sJdp2qe9lLTHmPlb0kalTDoPUZniDQyEIytMHEJ1tBK1xJZxBYn7Gkmtm5tgy8gj9qi8FlteCtxb2DXF1QXjRWOyfan8GL06yW34Bif6fewne%2FYhv%2FbIXK3H7p8A3ia0MLasD6mY2jQARONT1na0xNPqQqtZBsccnQYcmCS9gaf%2FKOfXd2GCuxAYuyV9Xkl3dd4IaWJ%2BfjyDL3JgyjiXL0xusi4OfECita9cdyqtodqcKAi3HdyfgoRIJaVj0ViuYOJruFvfK%2Bb6mPMBnCTov1NOlUwMRZdeSasoDtWfmJNN1%2FzMzUPKvht35uPqJu1IbMEUOsJlWVsigJU50k6pWZh3wAhnQ6OBmzevV1YwQjXEmzQZH%2ByB75RuQm%2Bs2WANwtr%2BqXpjOES4Hh%2Be6beIb8gPzqQa%2BLYwg%2FTExAY6pgEdN41kD0UDFW%2BqksFw2dUA0giuNHi%2BczexuVBtMfLcyucZQlkX20MVhCtVwCWCLK2ovPUk6JUhFKW7HdPZw%2BDGe9kxMpI54qWuXU%2FUvfDR4doO2YDYglzoQBQJBQ29pjg68W1ngD2eXtDTo0rShHk8r0zK9AT%2B0qurg5S16BnoJOd1uu0uKDTsXKkEe%2FFRqwrID696l3pEie8UlUkWBFPUoar82Y%2Bj&X-Amz-Signature=2fb88b92867ca5c7577fc6734ff12b65e59ffd74ad4156bc16ad773db1280116&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


