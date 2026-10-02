---
source: knowledge-base
origin: notion
title: "Kubernetes - POD YAML작성"
area: "Kubernetes"
tags: ["area/kubernetes", "tech/kubernetes"]
created: "2025-08-04T06:05:00.000Z"
last_edited: "2025-08-04T06:27:00.000Z"
status: published
public: true
notion_id: "245172a5-56d6-8000-96b0-fd551293af27"
notion_url: "https://www.notion.so/Kubernetes-POD-YAML-245172a556d6800096b0fd551293af27"
type: note
updated: 2026-07-07
---

# Kubernetes - POD YAML작성

## 요약

Kubernetes 기초

Kubernetes 큰 주제 아래에서 세부 개념과 실습 절차를 연결하기 위한 노트입니다.

## 핵심 포인트

- Kubernetes 기초
- 파드 yaml 디스크립션 작성
- kuberctl 기본 pod yaml파일
- 연습 문제 겸 POD작성 연습
- 문제 내용

## 지식 그래프

- [[wiki/mocs/Knowledge Base|Knowledge Base]]
- [[wiki/mocs/Kubernetes|Kubernetes]]

## 정리 내용

## 파드 yaml 디스크립션 작성
#### kuberctl 기본 pod yaml파일 
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
## 연습 문제 겸 POD작성 연습 
#### 문제 내용
- 모든 리소스 삭제
- Yaml 사용하여 docker images jenkins 로 jenkins-manual pod 생성하기
- jenkins pod에서 curl 명령어로 [localhost](http://localhost/):8080 접속하기
- jenkins pod 8888포트 포워딩하기
- 현재 jenkinss-manual 설정 yaml로 출력하기
### 모든 리소스 삭제
```bash
kubectl delete svc --all
kubectl delete deploy --all
kubectl delete pod --all
```
### Yaml 사용하여 docker images jenkins 로 jenkins-manual pod 생성하기
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
### jenkins pod에서 curl 명령어로 [localhost](http://localhost/):8080 접속하기
```yaml
kubectl exec pod이름  -- curl localhost:8080 -s
```
### jenkins pod 8888포트 포워딩하기
```yaml
kubectl port-forward pod이름 8888:8080
```
### 현재 jenkinss-manual 설정 yaml로 출력하기
```bash
kubectl get pod pod이름 -o yaml
```
#### kubectl YAML 주석 달기
```bash
kubectl annotate pod 파드이름 test123=test123
```
![[_attachments/notion/Kubernetes---POD-YAML작성/245172a556d681c2b189f864398b6298.png]]

## 출처

- 원문: https://www.notion.so/Kubernetes-POD-YAML-245172a556d6800096b0fd551293af27
- Vault path: wiki/notes/kubernetes/Kubernetes---POD-YAML작성.md
