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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/b231983e-0ca9-463d-a773-6c60f2c51f50/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UCSK7SJ7%2F20250805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250805T002630Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJHMEUCIQCkMFfVuCGLNvQoUwXsfaJgVM4cLH4xB9v03gnk0EsD4gIgX15qxx9g1z5aMSAZzcJuE7ZeCg9S4iujSes7bKkDgLwq%2FwMIUBAAGgw2Mzc0MjMxODM4MDUiDBpkevDQn23X%2B8YveCrcA2R%2FaGdiLfShSh9L1ntDzthzh%2FZNAjBGFelxsJHiOz4nCGHqpvhh7TdRUGezHwbaeFVGss5P7ArbRJNstqZOguFPdFLenZGWzk7FMz7u3EPUevbhQRTMvjyuNg8J8NboI7lVzROfq8zzWWpfo7nJVGWrJlGKRZTbpAXVzdWJMWLc%2Bieu3p253M24nZO9b%2BSusa7mV8%2BWMuuws5NMi1CN91Ptx6JcNwLuaPDHWFjTK%2FoZYeQb0mtFsXDPEm%2Fwm92vCcx5ikxSuHVqrGFv1vr89PGSs3q6uQT4fCUWHEf1DrCI0PQ2%2FrApGb8lx5FdCwbeYMmkmuMyYtuXHWAZwZ7exg4jXN2tCaFI89sbz7OEAuT%2FO%2Be4%2FuIKr0LEEfyrX%2FrWt8XSmY1p0aEtiaDxE7IcK%2BHBj7EK3DERjZnt1i0vUvNwebBtc%2Bi9IjKJe2QlXguaHD0rEk38LNPnZ1iWIqkhMzuCtdZSXoDGkjLrfDBrhJB7YybtVfQfrskiy8VtDSJKA4enS2adV5V2f3DAdx%2FFsLa2h4zFWl0Mio9zp3gCftnAVebnINb61imXG78qNmi2f%2F9dMFR4VL4CtOxp4djLIHVcN52kF%2BTO%2BFvtDke1uIXHl6QIYA2AvbC8BTzeMMD0xMQGOqUBCaJ%2FdCwZPzV%2BkhMGzBbnbIZOLGOKk%2BRfZlJ5LeNdOdAMyvjYHu6PROP5g2I6gdo9Rl%2F%2BoB%2B3HqfKJoGzxM1GXvYy%2FusitJlmGW6xmehC7Lct8m82ivEerMI06nJte2IKGmaZfuiDFrluaGFD5%2FCoyeASn3vQMHyjeB2XxIXpw5TrHT7xSrYir1pqoK9i9b%2FSlk6vQITWrKcAPXQdLJf1ukO634Qn&X-Amz-Signature=727f9d921620c44e9d2409d010d8d5cd280233a72eb3a6affa3e460484cd40ab&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 큐브 API서버 

- kubernetes System 컴포넌트는 오직 API서버와 통신
- 컴포넌트간 통신 x
- etcd와 통신하는 유일한 컴포넌트 API
- RESTful API를 통해서 클러스터 상태를 쿼리, 수정할 수 있는 기능 제공
- 구체적인 역할
## 큐브 컨트롤러 매니저

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/5ef47069-72a4-43fe-9427-e42fc25b70d8/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UCSK7SJ7%2F20250805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250805T002630Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJHMEUCIQCkMFfVuCGLNvQoUwXsfaJgVM4cLH4xB9v03gnk0EsD4gIgX15qxx9g1z5aMSAZzcJuE7ZeCg9S4iujSes7bKkDgLwq%2FwMIUBAAGgw2Mzc0MjMxODM4MDUiDBpkevDQn23X%2B8YveCrcA2R%2FaGdiLfShSh9L1ntDzthzh%2FZNAjBGFelxsJHiOz4nCGHqpvhh7TdRUGezHwbaeFVGss5P7ArbRJNstqZOguFPdFLenZGWzk7FMz7u3EPUevbhQRTMvjyuNg8J8NboI7lVzROfq8zzWWpfo7nJVGWrJlGKRZTbpAXVzdWJMWLc%2Bieu3p253M24nZO9b%2BSusa7mV8%2BWMuuws5NMi1CN91Ptx6JcNwLuaPDHWFjTK%2FoZYeQb0mtFsXDPEm%2Fwm92vCcx5ikxSuHVqrGFv1vr89PGSs3q6uQT4fCUWHEf1DrCI0PQ2%2FrApGb8lx5FdCwbeYMmkmuMyYtuXHWAZwZ7exg4jXN2tCaFI89sbz7OEAuT%2FO%2Be4%2FuIKr0LEEfyrX%2FrWt8XSmY1p0aEtiaDxE7IcK%2BHBj7EK3DERjZnt1i0vUvNwebBtc%2Bi9IjKJe2QlXguaHD0rEk38LNPnZ1iWIqkhMzuCtdZSXoDGkjLrfDBrhJB7YybtVfQfrskiy8VtDSJKA4enS2adV5V2f3DAdx%2FFsLa2h4zFWl0Mio9zp3gCftnAVebnINb61imXG78qNmi2f%2F9dMFR4VL4CtOxp4djLIHVcN52kF%2BTO%2BFvtDke1uIXHl6QIYA2AvbC8BTzeMMD0xMQGOqUBCaJ%2FdCwZPzV%2BkhMGzBbnbIZOLGOKk%2BRfZlJ5LeNdOdAMyvjYHu6PROP5g2I6gdo9Rl%2F%2BoB%2B3HqfKJoGzxM1GXvYy%2FusitJlmGW6xmehC7Lct8m82ivEerMI06nJte2IKGmaZfuiDFrluaGFD5%2FCoyeASn3vQMHyjeB2XxIXpw5TrHT7xSrYir1pqoK9i9b%2FSlk6vQITWrKcAPXQdLJf1ukO634Qn&X-Amz-Signature=89f876c0a60f0ae4ee8a24609fef52321ba499151eecf34a3ac9c829a19b566a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 큐브 스케쥴러

- 일반적으로 실행 할 노드를 직접 정해주지 않음
- 요청 받은 리소스를 어느 노드에서 실행할지 결정하는 역할
- 현재 노드의 상태를 점검하고 최상의 노드를 찾아 배치
- 다수의 포드를 배치하는 경우에는 라운드로빈을 사용하여 분산
## kubernetes System컴포넌트 확인

```yaml
kubectl get pod -n kube-system
```

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/a39272d3-e754-49e8-9357-c94342b1bb23/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UCSK7SJ7%2F20250805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250805T002630Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJHMEUCIQCkMFfVuCGLNvQoUwXsfaJgVM4cLH4xB9v03gnk0EsD4gIgX15qxx9g1z5aMSAZzcJuE7ZeCg9S4iujSes7bKkDgLwq%2FwMIUBAAGgw2Mzc0MjMxODM4MDUiDBpkevDQn23X%2B8YveCrcA2R%2FaGdiLfShSh9L1ntDzthzh%2FZNAjBGFelxsJHiOz4nCGHqpvhh7TdRUGezHwbaeFVGss5P7ArbRJNstqZOguFPdFLenZGWzk7FMz7u3EPUevbhQRTMvjyuNg8J8NboI7lVzROfq8zzWWpfo7nJVGWrJlGKRZTbpAXVzdWJMWLc%2Bieu3p253M24nZO9b%2BSusa7mV8%2BWMuuws5NMi1CN91Ptx6JcNwLuaPDHWFjTK%2FoZYeQb0mtFsXDPEm%2Fwm92vCcx5ikxSuHVqrGFv1vr89PGSs3q6uQT4fCUWHEf1DrCI0PQ2%2FrApGb8lx5FdCwbeYMmkmuMyYtuXHWAZwZ7exg4jXN2tCaFI89sbz7OEAuT%2FO%2Be4%2FuIKr0LEEfyrX%2FrWt8XSmY1p0aEtiaDxE7IcK%2BHBj7EK3DERjZnt1i0vUvNwebBtc%2Bi9IjKJe2QlXguaHD0rEk38LNPnZ1iWIqkhMzuCtdZSXoDGkjLrfDBrhJB7YybtVfQfrskiy8VtDSJKA4enS2adV5V2f3DAdx%2FFsLa2h4zFWl0Mio9zp3gCftnAVebnINb61imXG78qNmi2f%2F9dMFR4VL4CtOxp4djLIHVcN52kF%2BTO%2BFvtDke1uIXHl6QIYA2AvbC8BTzeMMD0xMQGOqUBCaJ%2FdCwZPzV%2BkhMGzBbnbIZOLGOKk%2BRfZlJ5LeNdOdAMyvjYHu6PROP5g2I6gdo9Rl%2F%2BoB%2B3HqfKJoGzxM1GXvYy%2FusitJlmGW6xmehC7Lct8m82ivEerMI06nJte2IKGmaZfuiDFrluaGFD5%2FCoyeASn3vQMHyjeB2XxIXpw5TrHT7xSrYir1pqoK9i9b%2FSlk6vQITWrKcAPXQdLJf1ukO634Qn&X-Amz-Signature=04e25f65187f1e396c39ef7e1cca29dd8acfbd901a0afacf641750f524cb8055&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


