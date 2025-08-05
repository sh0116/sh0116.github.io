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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/f38ce897-ad6d-434b-a035-f306e89b207f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46673SXLGQC%2F20250805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250805T002849Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJHMEUCIEqSZQq8xTnLjeJUw5LOPXZX3cryeeoXqSFWMkMPx8Q2AiEA6FNYdGS4iFxe9SRHCsK4BnoYzvmZzPoyikgDjlw0GTcq%2FwMIUBAAGgw2Mzc0MjMxODM4MDUiDJurcLclqzacBDYL6yrcA4Y1c6ajyZ3uiMCRaV84gYPH9Ev%2BXvfHiZwSi8CYxQgnAEeg3UkWY%2B3WNUNExpxqbcn0E0qPnyx0EAyWkiR93FwaN5JAf3w5kl%2BJ2z3PSjrvYvbQHmvcAA2PIqY2t0tzImdlOBIdVC4AwHB03tRwb7%2FZpfcINqSl3ltjYR9OdWHfZMG2upvzmAvCNy1TP6txjWNXD3miYQzL0vM2ErrqqKXIPZ%2FuvrNIT6fTbJZpaPaYhiWFjaLde8DBwIJjN5l0SLWWbfJ8Jxj%2BzWC569qVq4j66X4%2FIe9oy9Y070ISt0u21OuFJE5w%2FjktZ7BwGF%2BfrNWgxMHJiD6Z3ftkt7g%2FkQFq86GfW6NZJtclxy0GksyKO6up7ht801Hk%2FhbjlLWAZQtlFxN3ggODKHsm%2FWuNrfgYZXnpvtqWFTbWFK7lQe%2BZHXJpbFjAP4QoV8OuKv%2Fr6xgGQ1exZlvGx12vdbFevHc4upa3OuQiK2pIDSEPRCFkZJnGtG33x7c9JHDhgWneqMtrP8Wn57C4b4HtJjFDHnzxxuKLfxuk25WK0xxozwRoeXiL%2Bv9JsrOmAwUNTlqyf%2BcAfjqKotQoC80tMwyKQSFOMrKGdIQmkcfL3YKjMUygtw2pUoIfHL5BgQteMIz0xMQGOqUB2CX2Hzbuxla2czMJYOeFH%2FLABqHsmjpz%2F%2BnYfvbZx1i8q663874dhFM%2BETvtzkHS9Us9vyZ7rRIQJqoiXAU4e7BL6j4N667iTm43xWz6XRJEo6GGSy38OdoPD6Gtgb1UlkgRhuIO%2FoXwdNVojD8agTDqwE1KP9Yv8BNcjDJtZ2lrNnR0mVPAabfCMVxjfNP1ydxxiCqH%2BL1VxoMX40725Mr2klKn&X-Amz-Signature=2b72af1078ed6ce53b9ac6279274ab84a9114d796112c0b98023d4161dd1feaa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 컨테이너를 POD 전체에 적절하게 구성하는 방법

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/811279dd-4730-40a6-bff1-b650bb32201c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46673SXLGQC%2F20250805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250805T002849Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJHMEUCIEqSZQq8xTnLjeJUw5LOPXZX3cryeeoXqSFWMkMPx8Q2AiEA6FNYdGS4iFxe9SRHCsK4BnoYzvmZzPoyikgDjlw0GTcq%2FwMIUBAAGgw2Mzc0MjMxODM4MDUiDJurcLclqzacBDYL6yrcA4Y1c6ajyZ3uiMCRaV84gYPH9Ev%2BXvfHiZwSi8CYxQgnAEeg3UkWY%2B3WNUNExpxqbcn0E0qPnyx0EAyWkiR93FwaN5JAf3w5kl%2BJ2z3PSjrvYvbQHmvcAA2PIqY2t0tzImdlOBIdVC4AwHB03tRwb7%2FZpfcINqSl3ltjYR9OdWHfZMG2upvzmAvCNy1TP6txjWNXD3miYQzL0vM2ErrqqKXIPZ%2FuvrNIT6fTbJZpaPaYhiWFjaLde8DBwIJjN5l0SLWWbfJ8Jxj%2BzWC569qVq4j66X4%2FIe9oy9Y070ISt0u21OuFJE5w%2FjktZ7BwGF%2BfrNWgxMHJiD6Z3ftkt7g%2FkQFq86GfW6NZJtclxy0GksyKO6up7ht801Hk%2FhbjlLWAZQtlFxN3ggODKHsm%2FWuNrfgYZXnpvtqWFTbWFK7lQe%2BZHXJpbFjAP4QoV8OuKv%2Fr6xgGQ1exZlvGx12vdbFevHc4upa3OuQiK2pIDSEPRCFkZJnGtG33x7c9JHDhgWneqMtrP8Wn57C4b4HtJjFDHnzxxuKLfxuk25WK0xxozwRoeXiL%2Bv9JsrOmAwUNTlqyf%2BcAfjqKotQoC80tMwyKQSFOMrKGdIQmkcfL3YKjMUygtw2pUoIfHL5BgQteMIz0xMQGOqUB2CX2Hzbuxla2czMJYOeFH%2FLABqHsmjpz%2F%2BnYfvbZx1i8q663874dhFM%2BETvtzkHS9Us9vyZ7rRIQJqoiXAU4e7BL6j4N667iTm43xWz6XRJEo6GGSy38OdoPD6Gtgb1UlkgRhuIO%2FoXwdNVojD8agTDqwE1KP9Yv8BNcjDJtZ2lrNnR0mVPAabfCMVxjfNP1ydxxiCqH%2BL1VxoMX40725Mr2klKn&X-Amz-Signature=ed778f04dfffc4f43d6623003df51f1db5d04efa0d395ef746cb6fa3325026a9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

 

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


