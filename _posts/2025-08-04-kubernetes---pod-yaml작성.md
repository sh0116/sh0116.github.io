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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/ce5266bb-ffff-4c40-96e1-5a04ccf31630/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XNM4A6DR%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T072317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIQClmVG3XDEU%2BkhIxDBtqbbcX9Pwzc1I73ojdLZ9vCgnxAIgbQ68et0%2B61AxZUlDkbffqsd1NiwFJ5moSjYSXKXOj54q%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDAAhisofpeOOS4q8PircA%2BwFH65z6nZ8hlmM7n4JoSMwQGaeqDKxq%2F%2BbK4nHtAsbgO7AkM%2BftJF6I8GVFoEHBC%2B%2FrbWv31JJEGvV9DnMWI62uY20c06XN1qHmYXC2uG32lSh%2FE%2B1U6wRW77T50ZnuRw9jxx4lU14%2BI1sjti0Pk1mx7qEQvQ26yatQ2GwbN7oV8CL0a9238N00syXcp0BRtjHAwlqWo0oSROkUxYrP4skskWhBDbraEzyF2pDXaaM%2FFwSSqxb79RvuHFSz8f7e63aSo%2BB%2FpKjMQYPTDhRFaXVuw7vmQli4aqH%2FatH%2B564X1CFwe8TZ5o19iXWpgj4cus9wTUBs5%2BJmlLRYbz4Xep%2B%2F0zgXBhW4xgXG6fAffNOzQ4xQgUMQ7O6UReHezcxetqRDSjwkbxZUX9tCj6TIL9Dly2QDN6ej%2F%2Bb9BVuSeb4hJgJIrbZuXk1g8baDYcp8%2BU%2BVQDaJnfwlx5kV9datBbDvxOSmIop4kYZ0y0l7nPJt0v95Jq8AZ8n6UMKPLXcCPCIRcuUUM75zW3dSg5VWgtXdJx90lOr046mIaPUrqZC8B4T0hfcAUql00KCJnt4jrTb37dGFKWw5t9PlsD9Nbussd6S7Uajp6FD0B57squEZ5YGrAFKgZAOQS5lMOq2wcQGOqUBCKuTzR3xDWbsmLwWLD%2FMuo52L29IYUD3T4iFOtfqJTdxn30p0DZTKlKMOj%2FgTbhQ9XfEYqZfOOiAX%2BikGJDhjoBS6draDp1ZNJxd2jUcVk9L7o2dN9Id7kZH%2FoW28s1OPY07Syjglkca88Mu2Sln7lYBt%2BJPGXBjDsZCSE%2F1Qbi0OARtz9buITUnINsi%2FCmbJmQsqagS0tCt02PLJaMJVcx7aXbw&X-Amz-Signature=8ec6780e8804c1202ea23a26aca780062b330103e49e0cc24bcb62e8f4cd975b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


