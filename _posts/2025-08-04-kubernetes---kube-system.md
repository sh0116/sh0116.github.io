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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/b231983e-0ca9-463d-a773-6c60f2c51f50/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MTTXEAK%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T071353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIQDVe4ju7hvIDUaKE5m71NmKhIF6GPE0vLs%2BHpQvfqoe%2FQIgAqHLanJCHVbfrBxZHaSe1Q0UPF%2FaBoCdXJzWMnzNiUcq%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDIFDpZZEqh%2FYexfojircAxpbH5TmKf9%2B0Q4rnW6pIoGqoBf%2FqTwRce8DtSxD60%2FNaz38ZP6iwPKBCmR%2BI8MykAENQXdtPVJEMc0I%2FzOMqCPDxm%2BgZhGhj4dw9FZqgOZylsf0bFC0n8Tz2cQx%2BY2dTmR7H4Fo516t7XRf%2FWkTFfyV1MhX650XGa8TigCfSnJ46puApOL%2BFQGRcGdcUIbaUjL2PIfFwonuxF%2FWKnVaxKxplHWC%2Fd3pgdL5v%2FokbqjMcpNjiomQKRBqmpRGVtGZ26AwNGp409FhbzYmn5YS2pKZrXZGy655ns51BJQwuJig08e4iLmuk67wlKzJVwjqM37BT%2BuygrfJo1vU4BnP100kUsaVa8MFyhOa8RP0oy0aVU%2FF5V2z4OvnlkZib1Lr4HAYr%2BkY8FWMmklB0txn%2FwvkdK5m1NMLA0m5PqOMspAy8SBEpriXF32GD1h%2F4aOvWPu6SxacxLM7JP0gffKp%2BGt9ionW1zbSlRO7dvm4Q%2Fm%2FBSWN%2F7Al1kvVILeKeVN7D6jJYEz5Q5kVOCKi77SW8LFIrxtN%2BXTuzfT3jm0M7HPKDWuCV32XlxGZYStFMx%2F93rfTrWHbNxJ1sdejdfE5ueuLCRGAhwAfyBSKhJHPDnC0oLlJaZnS9biD%2BL%2BzMMm2wcQGOqUBzQEXVHp98AqpHL9jqR%2Fjn%2B7Uo3YDqLzUH%2FgNh94QoggLiN7K3I4XdLVz%2F0pTkaOTx9H%2B4V3VxSDb0lPQ55x%2FGNc6669NTm15eeJaQDCtapPzyvS3gxWkls9ECcfKx0TLkTztMac1Oib5RSB2R%2F6EpboJ277%2BlwG47lDajGiR6jNIeRYZzGVMTALLD0Zj3R7KZFU5qffpvaB0l4EvS%2FMzGP92SESR&X-Amz-Signature=6c024af52aa6b5c96f0bf8afca95e6e09c9a46a85325d4773aa0a113a2e3bd32&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 큐브 API서버 

- kubernetes System 컴포넌트는 오직 API서버와 통신
- 컴포넌트간 통신 x
- etcd와 통신하는 유일한 컴포넌트 API
- RESTful API를 통해서 클러스터 상태를 쿼리, 수정할 수 있는 기능 제공
- 구체적인 역할
## 큐브 컨트롤러 매니저

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/5ef47069-72a4-43fe-9427-e42fc25b70d8/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MTTXEAK%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T071353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIQDVe4ju7hvIDUaKE5m71NmKhIF6GPE0vLs%2BHpQvfqoe%2FQIgAqHLanJCHVbfrBxZHaSe1Q0UPF%2FaBoCdXJzWMnzNiUcq%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDIFDpZZEqh%2FYexfojircAxpbH5TmKf9%2B0Q4rnW6pIoGqoBf%2FqTwRce8DtSxD60%2FNaz38ZP6iwPKBCmR%2BI8MykAENQXdtPVJEMc0I%2FzOMqCPDxm%2BgZhGhj4dw9FZqgOZylsf0bFC0n8Tz2cQx%2BY2dTmR7H4Fo516t7XRf%2FWkTFfyV1MhX650XGa8TigCfSnJ46puApOL%2BFQGRcGdcUIbaUjL2PIfFwonuxF%2FWKnVaxKxplHWC%2Fd3pgdL5v%2FokbqjMcpNjiomQKRBqmpRGVtGZ26AwNGp409FhbzYmn5YS2pKZrXZGy655ns51BJQwuJig08e4iLmuk67wlKzJVwjqM37BT%2BuygrfJo1vU4BnP100kUsaVa8MFyhOa8RP0oy0aVU%2FF5V2z4OvnlkZib1Lr4HAYr%2BkY8FWMmklB0txn%2FwvkdK5m1NMLA0m5PqOMspAy8SBEpriXF32GD1h%2F4aOvWPu6SxacxLM7JP0gffKp%2BGt9ionW1zbSlRO7dvm4Q%2Fm%2FBSWN%2F7Al1kvVILeKeVN7D6jJYEz5Q5kVOCKi77SW8LFIrxtN%2BXTuzfT3jm0M7HPKDWuCV32XlxGZYStFMx%2F93rfTrWHbNxJ1sdejdfE5ueuLCRGAhwAfyBSKhJHPDnC0oLlJaZnS9biD%2BL%2BzMMm2wcQGOqUBzQEXVHp98AqpHL9jqR%2Fjn%2B7Uo3YDqLzUH%2FgNh94QoggLiN7K3I4XdLVz%2F0pTkaOTx9H%2B4V3VxSDb0lPQ55x%2FGNc6669NTm15eeJaQDCtapPzyvS3gxWkls9ECcfKx0TLkTztMac1Oib5RSB2R%2F6EpboJ277%2BlwG47lDajGiR6jNIeRYZzGVMTALLD0Zj3R7KZFU5qffpvaB0l4EvS%2FMzGP92SESR&X-Amz-Signature=d07dd298a3e0bffc1f9c9a366b118cce9590f34e4bebfe4c05517f48cac10dc3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 큐브 스케쥴러

- 일반적으로 실행 할 노드를 직접 정해주지 않음
- 요청 받은 리소스를 어느 노드에서 실행할지 결정하는 역할
- 현재 노드의 상태를 점검하고 최상의 노드를 찾아 배치
- 다수의 포드를 배치하는 경우에는 라운드로빈을 사용하여 분산
## kubernetes System컴포넌트 확인

```yaml
kubectl get pod -n kube-system
```

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/a39272d3-e754-49e8-9357-c94342b1bb23/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MTTXEAK%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T071353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIQDVe4ju7hvIDUaKE5m71NmKhIF6GPE0vLs%2BHpQvfqoe%2FQIgAqHLanJCHVbfrBxZHaSe1Q0UPF%2FaBoCdXJzWMnzNiUcq%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDIFDpZZEqh%2FYexfojircAxpbH5TmKf9%2B0Q4rnW6pIoGqoBf%2FqTwRce8DtSxD60%2FNaz38ZP6iwPKBCmR%2BI8MykAENQXdtPVJEMc0I%2FzOMqCPDxm%2BgZhGhj4dw9FZqgOZylsf0bFC0n8Tz2cQx%2BY2dTmR7H4Fo516t7XRf%2FWkTFfyV1MhX650XGa8TigCfSnJ46puApOL%2BFQGRcGdcUIbaUjL2PIfFwonuxF%2FWKnVaxKxplHWC%2Fd3pgdL5v%2FokbqjMcpNjiomQKRBqmpRGVtGZ26AwNGp409FhbzYmn5YS2pKZrXZGy655ns51BJQwuJig08e4iLmuk67wlKzJVwjqM37BT%2BuygrfJo1vU4BnP100kUsaVa8MFyhOa8RP0oy0aVU%2FF5V2z4OvnlkZib1Lr4HAYr%2BkY8FWMmklB0txn%2FwvkdK5m1NMLA0m5PqOMspAy8SBEpriXF32GD1h%2F4aOvWPu6SxacxLM7JP0gffKp%2BGt9ionW1zbSlRO7dvm4Q%2Fm%2FBSWN%2F7Al1kvVILeKeVN7D6jJYEz5Q5kVOCKi77SW8LFIrxtN%2BXTuzfT3jm0M7HPKDWuCV32XlxGZYStFMx%2F93rfTrWHbNxJ1sdejdfE5ueuLCRGAhwAfyBSKhJHPDnC0oLlJaZnS9biD%2BL%2BzMMm2wcQGOqUBzQEXVHp98AqpHL9jqR%2Fjn%2B7Uo3YDqLzUH%2FgNh94QoggLiN7K3I4XdLVz%2F0pTkaOTx9H%2B4V3VxSDb0lPQ55x%2FGNc6669NTm15eeJaQDCtapPzyvS3gxWkls9ECcfKx0TLkTztMac1Oib5RSB2R%2F6EpboJ277%2BlwG47lDajGiR6jNIeRYZzGVMTALLD0Zj3R7KZFU5qffpvaB0l4EvS%2FMzGP92SESR&X-Amz-Signature=851669588157933e848e9e74498b25124296d33c4efa5a9788122e61a7a47dab&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


