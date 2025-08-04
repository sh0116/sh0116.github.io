---
title: "Kubernetes - 네트워크"
date: 2025-08-04 06:05:00 +0900
categories: [kubernetes]
tags: [Kubernetes]
description: Kubernetes 기초
toc: true
comments: true
---

# 서비스를 노출하는 세가지 방법

- ClusterIP(기본형태) : pod드링 클러스터 내부의 다른 리소스들과 통신할 수 있도록 가상의 클러스터 전용IP
- Nodeport : 노드의 자체 포트를 사용하여 pod로 리다이렉션 
- LoadBalancer : 외부 게이트웨이를 사용하여 노드 포트로 리다이렉션
# 인그레스 Ingress 개념

만약 여러개의 서비스가 있는 실제 서비스라고 가정하자.

각 기능마다 로드밸런스를 각각 정의를 해야하는 것인가?

Ingress는 서비스의 종류가 아닌 서비스를 하나로 묶는 스마트 라우터 역할을 수행한다.

즉 하나의 LoadBalancer에서 여러 서비스를 노출할 수 없는 한계를 해결하는 것이 Ingress이다.

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/8ba4f4bb-7f47-4c51-8172-3a0aee492a75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNRD24QF%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T072105Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCID0o8S2yvvPE4e5cWbP1%2BS%2FWwLPJxChpgUopAT3oXHszAiEA9HLtGOMnbguNyHL9aNcLu7vVj7ryDwxqtJpgGUifzzIq%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDCClnRWeh%2BB8IMGwtCrcA1ZCEUjQdSs%2F%2F7MkO2DBUKcPMJOPIYLNiDeYtxhPBdkepC4PS2x%2FsgZPTsLWfh24mSruoUHLzEOm1VjAw2OOkrRVSF6%2FHMkLlNLiwRcs15j7HDxbh34rrMUZEvl5gKFvs1%2BlHXbj44a5U25eWraPyiY8fAPWCGfZk6aLHDHDcV%2FKTQ2HOLU3oolvGNZfzKctBWq5RfBHFfl9dUG%2BGkzaHaM3pxg0LPi9ooCQV9MmJmDuucLTW5rVZYv5F1WMRkFKd7lKtYnYNKKOdNrxKSKb3uOo9QGIkIJ9SO51hhPc9Y%2BTZtNCoK3OPpjWFNhos%2BBh9mrUDyuy1JfZ85%2FZGEJX0nAoaROyPYRZ72NJX9KH0SGvM5fRaxaMsvzPRQyiYw%2FkLpEueZ1vqtVjreVqBqCEdsyIGvYYJjaVGAp%2FdWZwfYhh%2Fdg9BcoUIWdPvpySz6OFEWHDvQBffyOeuOThO0%2FldD%2BhWgTTRBrXS8RktF91XNZS8TM3pNUXYhOLZ9AO%2B3fYvmyrLQUQ2lDo4iil5j6T7fQlH%2FvVq%2Bbk7iy2yTQT61Wwaj43evEuwvQQVMdODvAqiglouLZjLU8349FbFA6JOst78KzjDIyx4cfgO0yOwFsIfVGwBxlRG%2Fsad3LjMJm3wcQGOqUBJi6H1%2B19DtkMYqvghaMvsmubDwq89ho0d9TC7ThTxAMKJiQresAjpeTxlFrbWb8K4fZeoC0bTrO2qZOYR0V%2BWSR32D7rJ2W40dMfiURxcPJ6pJGCtjzI1aeZfblP%2BRuh7OJG%2F17mgiLAGF2vX7qMIDAxgTl3zG23fuCUfJBHSnVrcQw7yy7XSp7OJncoSqn5IBaxuVqqr5F%2FitU0hP%2FGwdQn%2BwsX&X-Amz-Signature=4fab4d719b90f423f72522e0afd97e9ec518910a31d51c3bdd8ef0f1a543e199&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## Reference


