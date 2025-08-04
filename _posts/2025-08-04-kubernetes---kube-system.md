---
title: "Kubernetes - kube-system"
date: 2025-08-04 06:06:00 +0900
categories: [kubernetes]
tags: [Kubernetes]
description: Kubernetes 기초
toc: true
comments: true
---

# Kube-system 컴포넌트의 이해

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/b231983e-0ca9-463d-a773-6c60f2c51f50/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667XP7TEDP%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T064835Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJIMEYCIQC6f%2FdiiuVUmZqydd1d5cD3RMYICJB021ObHn%2F7blphyQIhAP%2Bo%2BnGG%2BluuvJy8BWmvfnnRTj%2BoLUMbQR92wTFQfgRNKv8DCD8QABoMNjM3NDIzMTgzODA1IgylplhuCbsdQ7aIyyIq3ANxRJWdHF3YhXV%2FuIh7rxZpl4VEeweJyT8PdmmRDYRXBWQJ54oGn45Gqi4t6mVdPRoMFmAgBGmS1%2FRwYnal5D%2Flt1tu93fGWkKPHNMkjs4BNScyzufaNkUFH%2BV0ql5pAN8BRjGKqFarIKS8T9s%2BJll2K%2BQKDLM70Ezy0r7w%2FIUNckusF3QewaDzkJqQu6hehkf0Vcpo4WxTSeeAP081hHUWUIEAeOk9jILvsLEOFyFnhjLP71ERoXSSPkq5SeQDvt6%2F9Qs%2FGrZTjegGnbVje4adgjbgWjhOjQhaUerQaJvuTOD0JMKQ7VSCEaBF7IK7tkaPAw9t9ANW9yqv6qp4JjfhCt%2BMJd2Lnw0vy1MQ5BQ%2Bp4zrYz6eftEwYtP6P3c6hpDofX2AClQAFLPxsEoT%2FRjuVdNoCy1R29j778Tb3u3xkS9fPVOs1jMamqh9IY7ZwKqIJrwgSOu5kfmsta9%2FxqRwEbdlauXJATK%2Bjr9LN6cbFdOhgQsyelDg9V5k8SfHTlgGBedqAMzsaYBCfoOyq8muk7QFFJoRUfES7uIxggmhWJ9kJw2gDIeRH0neEUfcYQNnfQZe5meN0ZMOK2XqsTXcj5OC8WyoPT0sFUwpvkGz1Fv5xhl1rt%2BquBQsQDDnjcHEBjqkAZkgAG%2B5R0SA0bsWWuhN2ToGmLMwL0AA4TlBvDxDfi3yYjJ1PcCZAbenZvdttYErgH0HvYGHaV9RYCOn58SvO3X8RZtHZHBBS0vxppwAU4y%2B89TIu0Gc5Ikp1mprDrs2aKKiBC6tpXbLQceuvYTD%2FK8me3TYKXjRu01XawAJXnNUoksbB43IQQy%2BtQ2v%2FmfNN26EUFAicWBdAQgMaELgrE2HUuCS&X-Amz-Signature=444ff4755f942461de558593edf601d64bc71f184590d26dbf764a3980bf8cd6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 큐브 API서버 

- kubernetes System 컴포넌트는 오직 API서버와 통신
- 컴포넌트간 통신 x
- etcd와 통신하는 유일한 컴포넌트 API
- RESTful API를 통해서 클러스터 상태를 쿼리, 수정할 수 있는 기능 제공
- 구체적인 역할
## 큐브 컨트롤러 매니저

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/5ef47069-72a4-43fe-9427-e42fc25b70d8/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667XP7TEDP%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T064835Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJIMEYCIQC6f%2FdiiuVUmZqydd1d5cD3RMYICJB021ObHn%2F7blphyQIhAP%2Bo%2BnGG%2BluuvJy8BWmvfnnRTj%2BoLUMbQR92wTFQfgRNKv8DCD8QABoMNjM3NDIzMTgzODA1IgylplhuCbsdQ7aIyyIq3ANxRJWdHF3YhXV%2FuIh7rxZpl4VEeweJyT8PdmmRDYRXBWQJ54oGn45Gqi4t6mVdPRoMFmAgBGmS1%2FRwYnal5D%2Flt1tu93fGWkKPHNMkjs4BNScyzufaNkUFH%2BV0ql5pAN8BRjGKqFarIKS8T9s%2BJll2K%2BQKDLM70Ezy0r7w%2FIUNckusF3QewaDzkJqQu6hehkf0Vcpo4WxTSeeAP081hHUWUIEAeOk9jILvsLEOFyFnhjLP71ERoXSSPkq5SeQDvt6%2F9Qs%2FGrZTjegGnbVje4adgjbgWjhOjQhaUerQaJvuTOD0JMKQ7VSCEaBF7IK7tkaPAw9t9ANW9yqv6qp4JjfhCt%2BMJd2Lnw0vy1MQ5BQ%2Bp4zrYz6eftEwYtP6P3c6hpDofX2AClQAFLPxsEoT%2FRjuVdNoCy1R29j778Tb3u3xkS9fPVOs1jMamqh9IY7ZwKqIJrwgSOu5kfmsta9%2FxqRwEbdlauXJATK%2Bjr9LN6cbFdOhgQsyelDg9V5k8SfHTlgGBedqAMzsaYBCfoOyq8muk7QFFJoRUfES7uIxggmhWJ9kJw2gDIeRH0neEUfcYQNnfQZe5meN0ZMOK2XqsTXcj5OC8WyoPT0sFUwpvkGz1Fv5xhl1rt%2BquBQsQDDnjcHEBjqkAZkgAG%2B5R0SA0bsWWuhN2ToGmLMwL0AA4TlBvDxDfi3yYjJ1PcCZAbenZvdttYErgH0HvYGHaV9RYCOn58SvO3X8RZtHZHBBS0vxppwAU4y%2B89TIu0Gc5Ikp1mprDrs2aKKiBC6tpXbLQceuvYTD%2FK8me3TYKXjRu01XawAJXnNUoksbB43IQQy%2BtQ2v%2FmfNN26EUFAicWBdAQgMaELgrE2HUuCS&X-Amz-Signature=6ab9fa1bdc83fb1017f8e35cf188d1d29b2aaccc25420ec12e7f62438068a58e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 큐브 스케쥴러

- 일반적으로 실행 할 노드를 직접 정해주지 않음
- 요청 받은 리소스를 어느 노드에서 실행할지 결정하는 역할
- 현재 노드의 상태를 점검하고 최상의 노드를 찾아 배치
- 다수의 포드를 배치하는 경우에는 라운드로빈을 사용하여 분산
## kubernetes System컴포넌트 확인

```yaml
kubectl get pod -n kube-system
```

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/a39272d3-e754-49e8-9357-c94342b1bb23/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667XP7TEDP%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T064835Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJIMEYCIQC6f%2FdiiuVUmZqydd1d5cD3RMYICJB021ObHn%2F7blphyQIhAP%2Bo%2BnGG%2BluuvJy8BWmvfnnRTj%2BoLUMbQR92wTFQfgRNKv8DCD8QABoMNjM3NDIzMTgzODA1IgylplhuCbsdQ7aIyyIq3ANxRJWdHF3YhXV%2FuIh7rxZpl4VEeweJyT8PdmmRDYRXBWQJ54oGn45Gqi4t6mVdPRoMFmAgBGmS1%2FRwYnal5D%2Flt1tu93fGWkKPHNMkjs4BNScyzufaNkUFH%2BV0ql5pAN8BRjGKqFarIKS8T9s%2BJll2K%2BQKDLM70Ezy0r7w%2FIUNckusF3QewaDzkJqQu6hehkf0Vcpo4WxTSeeAP081hHUWUIEAeOk9jILvsLEOFyFnhjLP71ERoXSSPkq5SeQDvt6%2F9Qs%2FGrZTjegGnbVje4adgjbgWjhOjQhaUerQaJvuTOD0JMKQ7VSCEaBF7IK7tkaPAw9t9ANW9yqv6qp4JjfhCt%2BMJd2Lnw0vy1MQ5BQ%2Bp4zrYz6eftEwYtP6P3c6hpDofX2AClQAFLPxsEoT%2FRjuVdNoCy1R29j778Tb3u3xkS9fPVOs1jMamqh9IY7ZwKqIJrwgSOu5kfmsta9%2FxqRwEbdlauXJATK%2Bjr9LN6cbFdOhgQsyelDg9V5k8SfHTlgGBedqAMzsaYBCfoOyq8muk7QFFJoRUfES7uIxggmhWJ9kJw2gDIeRH0neEUfcYQNnfQZe5meN0ZMOK2XqsTXcj5OC8WyoPT0sFUwpvkGz1Fv5xhl1rt%2BquBQsQDDnjcHEBjqkAZkgAG%2B5R0SA0bsWWuhN2ToGmLMwL0AA4TlBvDxDfi3yYjJ1PcCZAbenZvdttYErgH0HvYGHaV9RYCOn58SvO3X8RZtHZHBBS0vxppwAU4y%2B89TIu0Gc5Ikp1mprDrs2aKKiBC6tpXbLQceuvYTD%2FK8me3TYKXjRu01XawAJXnNUoksbB43IQQy%2BtQ2v%2FmfNN26EUFAicWBdAQgMaELgrE2HUuCS&X-Amz-Signature=93dcf94e391151376060cfda48c92dd931647144402ef93a3828cbda9abea01e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### yaml파일 저장 위치확

```yaml
ls /etc/kubernetes/manifests/
```

# static pod

- kubelet이 직접 실행하는 포드
- 각각의 노드에서 kubelet에 의해 실행
- pod들을 삭제할 때, apiserver를 통해서 실행되지 않은  static pod는 삭제 불가
- 즉, 노드의 필요에 의해 사용하고자 하는 포드는 static pod로 셋팅
- 다음 명령들을 사용하여 실행하고자 하는  static pod의 위치를 설정 가능
- /etc/kubernetes/manifest/ 폴더 기본 경로
# etcd 란

- etcd는 데이터베이스다!
- Key - value 데이터 셋 형식으로 구성
- 다중 Key - value 가능
- etcdctl 명령어가 필요 → 다운받아야함
```yaml
wget https://github.com/etcd-io/etcd/releases/download/v3.5.6/etcd-v3.5.6-linux-amd64.tar.gz
tar -xf etcd-v3.5.6-linux-amd64.tar.gz

sudo ETCDCTL_API=3 ./etcdctl --endpoints 127.0.0.1:2379 --cacert /etc/kubernetes/pki/etcd/ca.crt --cert /etc/kubernetes/pki/etcd/server.crt --key /etc/kubernetes/pki/etcd/server.key get / --prefix --keys-only
```

### 간단한 key-value put & get

```yaml
sudo ETCDCTL_API=3 ./etcdctl --endpoints 127.0.0.1:2379 --cacert /etc/kubernetes/pki/etcd/ca.crt --cert /etc/kubernetes/pki/etcd/server.crt --key /etc/kubernetes/pki/etcd/server.key  put key1 value1
sudo ETCDCTL_API=3 ./etcdctl --endpoints 127.0.0.1:2379 --cacert /etc/kubernetes/pki/etcd/ca.crt --cert /etc/kubernetes/pki/etcd/server.crt --key /etc/kubernetes/pki/etcd/server.key get key1
```


