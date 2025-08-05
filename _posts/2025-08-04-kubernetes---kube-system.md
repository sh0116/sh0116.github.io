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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/b231983e-0ca9-463d-a773-6c60f2c51f50/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RP6P43DB%2F20250805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250805T060945Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQCYcGQdhjuVsHne7CZV09AsvlmtPoR4MoE7qxxKS7qDYQIhALbIXhOBjTfpw2HhbaPSVHK3zu59Ta9BFt9E4%2BxodtD5Kv8DCFcQABoMNjM3NDIzMTgzODA1Igyj%2Blte2pDncx9TqQMq3ANzHTeHrSPkj2f%2BTExnaeWAmMk5%2BtdI4mGWRE7I0BooDWTejGGmK2UauYrU2ioaOybG82dQuTKcd%2FHStQxSyoCot%2Bk0f9p9kImimKp6n4Ey%2BE6bn87L%2FRosI81wGKg1ZfhXqbafdjkOZojtZHm0Pdkv2PZUjTtGEaqAWXlsKIFJ9xW9TEG57rhvrn17HOltFp%2FHKnuO0GTzGUJj%2FefmDzuDYfrpNSZhaCHIzOsPijvKTiBMNfLXlIayOuK%2B4RKuNrhNVlMm53POH4pL0s7eSbYu2KpcOmpAeLr66M%2BeriMYyWLmVafkPx2IHZq1htKe3wzLKhDgKJnakcsLp8Hfckob3J3SR5AeL9dSFz554rHe7Qkluwnw051PS2eJT08RrnnhZUvOBEwPs892eJbn5bi3fvcyLHWKm%2BdfWE27%2B2vSOJo4NtlrmPKVAJTeyrpNMqjbMP%2BBbAwrH6ZAkjEvmMijAoVuTFLiMNNYYMiWI4wgc1NG790t6U99ekhR5mvNKUpa9NWU4YPTGX1Z%2F1YAIenOpnaCkl1udwKwGTiUCYgIFIwAwykuUp6FwqoLGH41Fqwm3pJXnaIEQJt5OvKERzLBjvE0724Bj%2FrrzRowVuIIUmtGks5F6YgErfgsFjCrs8bEBjqkAbCqqwKWykTyrQod81TlBIBXpY5Nfji%2FOeja1iXdr8%2FLVXztsA1U0sCfNbaPy5Zkg7EPP4lKodNLkqtD1KJ1oPPxA%2FjsWLvHlVbV94Ii7Z2nussBJU5gsGjWRgKILhKzSs9TPascdyQSRNFKDQtOcUwPOhLBZSdPlJ2WKSq17vI2f1HWsC%2BW6%2BlbDA%2B4i98mqmrNyWLckH%2BWh4UURlU3urfhqfuE&X-Amz-Signature=1d0f54bb4eeb6bb034d92107acb1c84bc4c5abc8b419cd79a22e0a6182dbbb97&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 큐브 API서버 

- kubernetes System 컴포넌트는 오직 API서버와 통신
- 컴포넌트간 통신 x
- etcd와 통신하는 유일한 컴포넌트 API
- RESTful API를 통해서 클러스터 상태를 쿼리, 수정할 수 있는 기능 제공
- 구체적인 역할
## 큐브 컨트롤러 매니저

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/5ef47069-72a4-43fe-9427-e42fc25b70d8/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RP6P43DB%2F20250805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250805T060945Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQCYcGQdhjuVsHne7CZV09AsvlmtPoR4MoE7qxxKS7qDYQIhALbIXhOBjTfpw2HhbaPSVHK3zu59Ta9BFt9E4%2BxodtD5Kv8DCFcQABoMNjM3NDIzMTgzODA1Igyj%2Blte2pDncx9TqQMq3ANzHTeHrSPkj2f%2BTExnaeWAmMk5%2BtdI4mGWRE7I0BooDWTejGGmK2UauYrU2ioaOybG82dQuTKcd%2FHStQxSyoCot%2Bk0f9p9kImimKp6n4Ey%2BE6bn87L%2FRosI81wGKg1ZfhXqbafdjkOZojtZHm0Pdkv2PZUjTtGEaqAWXlsKIFJ9xW9TEG57rhvrn17HOltFp%2FHKnuO0GTzGUJj%2FefmDzuDYfrpNSZhaCHIzOsPijvKTiBMNfLXlIayOuK%2B4RKuNrhNVlMm53POH4pL0s7eSbYu2KpcOmpAeLr66M%2BeriMYyWLmVafkPx2IHZq1htKe3wzLKhDgKJnakcsLp8Hfckob3J3SR5AeL9dSFz554rHe7Qkluwnw051PS2eJT08RrnnhZUvOBEwPs892eJbn5bi3fvcyLHWKm%2BdfWE27%2B2vSOJo4NtlrmPKVAJTeyrpNMqjbMP%2BBbAwrH6ZAkjEvmMijAoVuTFLiMNNYYMiWI4wgc1NG790t6U99ekhR5mvNKUpa9NWU4YPTGX1Z%2F1YAIenOpnaCkl1udwKwGTiUCYgIFIwAwykuUp6FwqoLGH41Fqwm3pJXnaIEQJt5OvKERzLBjvE0724Bj%2FrrzRowVuIIUmtGks5F6YgErfgsFjCrs8bEBjqkAbCqqwKWykTyrQod81TlBIBXpY5Nfji%2FOeja1iXdr8%2FLVXztsA1U0sCfNbaPy5Zkg7EPP4lKodNLkqtD1KJ1oPPxA%2FjsWLvHlVbV94Ii7Z2nussBJU5gsGjWRgKILhKzSs9TPascdyQSRNFKDQtOcUwPOhLBZSdPlJ2WKSq17vI2f1HWsC%2BW6%2BlbDA%2B4i98mqmrNyWLckH%2BWh4UURlU3urfhqfuE&X-Amz-Signature=7153dcf9f0fa3f5752f391bb58fe0bc7913d44d56a99d6e4e244683666ca1f26&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 큐브 스케쥴러

- 일반적으로 실행 할 노드를 직접 정해주지 않음
- 요청 받은 리소스를 어느 노드에서 실행할지 결정하는 역할
- 현재 노드의 상태를 점검하고 최상의 노드를 찾아 배치
- 다수의 포드를 배치하는 경우에는 라운드로빈을 사용하여 분산
## kubernetes System컴포넌트 확인

```yaml
kubectl get pod -n kube-system
```

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/a39272d3-e754-49e8-9357-c94342b1bb23/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RP6P43DB%2F20250805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250805T060945Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQCYcGQdhjuVsHne7CZV09AsvlmtPoR4MoE7qxxKS7qDYQIhALbIXhOBjTfpw2HhbaPSVHK3zu59Ta9BFt9E4%2BxodtD5Kv8DCFcQABoMNjM3NDIzMTgzODA1Igyj%2Blte2pDncx9TqQMq3ANzHTeHrSPkj2f%2BTExnaeWAmMk5%2BtdI4mGWRE7I0BooDWTejGGmK2UauYrU2ioaOybG82dQuTKcd%2FHStQxSyoCot%2Bk0f9p9kImimKp6n4Ey%2BE6bn87L%2FRosI81wGKg1ZfhXqbafdjkOZojtZHm0Pdkv2PZUjTtGEaqAWXlsKIFJ9xW9TEG57rhvrn17HOltFp%2FHKnuO0GTzGUJj%2FefmDzuDYfrpNSZhaCHIzOsPijvKTiBMNfLXlIayOuK%2B4RKuNrhNVlMm53POH4pL0s7eSbYu2KpcOmpAeLr66M%2BeriMYyWLmVafkPx2IHZq1htKe3wzLKhDgKJnakcsLp8Hfckob3J3SR5AeL9dSFz554rHe7Qkluwnw051PS2eJT08RrnnhZUvOBEwPs892eJbn5bi3fvcyLHWKm%2BdfWE27%2B2vSOJo4NtlrmPKVAJTeyrpNMqjbMP%2BBbAwrH6ZAkjEvmMijAoVuTFLiMNNYYMiWI4wgc1NG790t6U99ekhR5mvNKUpa9NWU4YPTGX1Z%2F1YAIenOpnaCkl1udwKwGTiUCYgIFIwAwykuUp6FwqoLGH41Fqwm3pJXnaIEQJt5OvKERzLBjvE0724Bj%2FrrzRowVuIIUmtGks5F6YgErfgsFjCrs8bEBjqkAbCqqwKWykTyrQod81TlBIBXpY5Nfji%2FOeja1iXdr8%2FLVXztsA1U0sCfNbaPy5Zkg7EPP4lKodNLkqtD1KJ1oPPxA%2FjsWLvHlVbV94Ii7Z2nussBJU5gsGjWRgKILhKzSs9TPascdyQSRNFKDQtOcUwPOhLBZSdPlJ2WKSq17vI2f1HWsC%2BW6%2BlbDA%2B4i98mqmrNyWLckH%2BWh4UURlU3urfhqfuE&X-Amz-Signature=33b419872ff2aa2c5d167102239f1221ccf4038a252377a4326dbddf5b908746&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


