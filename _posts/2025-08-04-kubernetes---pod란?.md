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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/f38ce897-ad6d-434b-a035-f306e89b207f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XMOU64Z7%2F20250805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250805T061137Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJHMEUCIDU2YRp7ZjeQASWmLQ76IMkSabHarVrl%2FVNYihQjWeUPAiEA4BJUjkdHDTjEdbnI9Kj%2Bn0zdHGdxCA%2BOciaApdVJOF8q%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDAzD7ELMsk5pKTMxISrcAxNeL8wqZZBRmIDMku5AR5g%2BWqm6%2FVHC0I5GTNL3Dk1a%2FEP6vrlE7NcBYeKY9uT9s5WhL9P9TAUk%2FVx4adFQ5ZNifqftulyl0wVPxYMD1f2iY7I6NG6Tbs4M6lhhiwTYka9g2RF2yIBApzbUwawiRcjFbtmbgg3OqDLYR6za04M8noUJgEA0o2jhFg5P2qoEJDwQx%2BrOaFgVU%2FhacQ4ZnGqPIsrnIQiWy53JJW86PuYlEFi%2FjKa%2F4iPcsp%2F34c553o66D4%2BuYbCNLx%2BpBRC0jwyOhV4TZYdK8OLRUHGUByqiGkpYuRG2Zud4J%2Bs%2BvBXOBmh5xFdsf%2BlppzFbTl%2BVmsomehyEq4rut3Wc1uOjry1BW4NV0sgCIPi%2FTkFcoCOCyH%2FRKPZmSzJWvB0Mq5%2BjBP0emTK1ZJtm%2BO0h1urI4OMk%2FEoMljQ0gbt0N%2B5q0G25F5LXSUCLaa1TGU7eFvwm4KPJN1C1yAtXLe59B%2B2WjAnvkz%2FydeMcN66QKVyQtSJ410CcfNo7WUAWvl02HaUvkNS2bgFGil0nODOkmoxdgsTN872vj2ZjMho7MS9BBX7fWyhHpA8zBlrH93f0JIJiGnz0MKExRBtzYEKhjNL9LjyLAc3zrDUraVlMZKEiMKqzxsQGOqUBrPcvDGFETINt65tOkwvY%2FYwx%2F7m32wS9yis5XffqxgFv4y5hrpPlnNXf6FZ0bW702ykTN8bCT%2FN9hil%2FP%2Bm6hanIfsqnRIoWVylFVdQhSSu2howTGLcYcvdDrBTdwCDaWSaC3pP0gYe1BFvDXjDyMv%2FcuLFAFhBw4V7l7cEvC2NLypIx1QiMlCvMeqTT1RxrNStcdXjBCaWfPA6aW9xf41JpkEsB&X-Amz-Signature=7cffadb5c8e9401ea14de94ce2704ff45d1f609b98a883546d3868d7d54dc701&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 컨테이너를 POD 전체에 적절하게 구성하는 방법

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/811279dd-4730-40a6-bff1-b650bb32201c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XMOU64Z7%2F20250805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250805T061137Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJHMEUCIDU2YRp7ZjeQASWmLQ76IMkSabHarVrl%2FVNYihQjWeUPAiEA4BJUjkdHDTjEdbnI9Kj%2Bn0zdHGdxCA%2BOciaApdVJOF8q%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDAzD7ELMsk5pKTMxISrcAxNeL8wqZZBRmIDMku5AR5g%2BWqm6%2FVHC0I5GTNL3Dk1a%2FEP6vrlE7NcBYeKY9uT9s5WhL9P9TAUk%2FVx4adFQ5ZNifqftulyl0wVPxYMD1f2iY7I6NG6Tbs4M6lhhiwTYka9g2RF2yIBApzbUwawiRcjFbtmbgg3OqDLYR6za04M8noUJgEA0o2jhFg5P2qoEJDwQx%2BrOaFgVU%2FhacQ4ZnGqPIsrnIQiWy53JJW86PuYlEFi%2FjKa%2F4iPcsp%2F34c553o66D4%2BuYbCNLx%2BpBRC0jwyOhV4TZYdK8OLRUHGUByqiGkpYuRG2Zud4J%2Bs%2BvBXOBmh5xFdsf%2BlppzFbTl%2BVmsomehyEq4rut3Wc1uOjry1BW4NV0sgCIPi%2FTkFcoCOCyH%2FRKPZmSzJWvB0Mq5%2BjBP0emTK1ZJtm%2BO0h1urI4OMk%2FEoMljQ0gbt0N%2B5q0G25F5LXSUCLaa1TGU7eFvwm4KPJN1C1yAtXLe59B%2B2WjAnvkz%2FydeMcN66QKVyQtSJ410CcfNo7WUAWvl02HaUvkNS2bgFGil0nODOkmoxdgsTN872vj2ZjMho7MS9BBX7fWyhHpA8zBlrH93f0JIJiGnz0MKExRBtzYEKhjNL9LjyLAc3zrDUraVlMZKEiMKqzxsQGOqUBrPcvDGFETINt65tOkwvY%2FYwx%2F7m32wS9yis5XffqxgFv4y5hrpPlnNXf6FZ0bW702ykTN8bCT%2FN9hil%2FP%2Bm6hanIfsqnRIoWVylFVdQhSSu2howTGLcYcvdDrBTdwCDaWSaC3pP0gYe1BFvDXjDyMv%2FcuLFAFhBw4V7l7cEvC2NLypIx1QiMlCvMeqTT1RxrNStcdXjBCaWfPA6aW9xf41JpkEsB&X-Amz-Signature=0329655b90c3a9db0319eb33fc7de31e8b5bddb29ec732e6a095e4abbd864bef&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

 

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


