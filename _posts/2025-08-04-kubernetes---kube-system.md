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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/b231983e-0ca9-463d-a773-6c60f2c51f50/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663G2AYMQC%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T072120Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIQDvb4xIAn0r7CdlXel9g5sdXbLwDDk4jrmNfUyfSdZHRAIgGNk%2BeKNOAiBVFS1dpfSgsUwNZFpjz%2FlWeqJ2ezHdXFMq%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDJo%2FtB22PehB1Y6AEyrcA%2F9jSqpN1kzcWO9NXAcDJMRguRseKg2r5sa8ts%2F%2BupiqWtjs8%2BH3NlG%2B6ZNtKji4H0lc2abg1j9YkYnIQF1DYHPN3WDqqCnncHh8pkt9iWR4NHU3SmRrBcIY1kMPaeHETuPUjuNhI7A%2FMepHOO%2FkIWDdVlliFV%2BWrGG%2BVTIHTo4bOa65zaUrl3O0HIeKPLWD9aNYgMyIfo1Jrzyu%2BQBvB4rOiqtkp2smhk7oCVyUk%2Bi2BxE5Lv79jjwVmJ2%2BuF935ADnbQh%2B19b%2FACwyfE%2FPoHKOf%2B%2BeMvkevJrD7jLyzdrj2kYxzVmusYHOlpQP53su3HG%2ByxZWYbizWOi4QMeCWkTwf8ZCwhi3YAgH2%2BxdxaLVgO63dby4BbazmlDVH1TEwrpyaOCf2ZzMTunTUaCP9eenY4SNJS%2F9RJGWwDtLOs7tCvtelWuxfQgnJshaq2S9a1Xdg8YskyF1yalJAwInhS%2FtvCzyXvGa1NntjksukTM3%2Bmp8G8xEwt8xkSkH15dPnxevJrfLj4I5gqdJG7%2FdvsRKYyi1gv8JzNLWc%2BZ5zk77%2BkvuymbFRoo%2FaS7SgiXb9OJNlZyeUTpRk53kxYWym29xG2EimsR7l%2BDDGs30CZV%2ByTzhAZv6Mogjg2OYMOu2wcQGOqUBv552hgOOHvfMKoDk9R7nnAW3TG%2FMH%2B%2FiCauh7r4x3kA%2FumVNXqGgZcxeVDoTQDEkHbp3EsmpZItW1tAw5PrvPq%2B3qr3ft4wGTpUx4nEIChcOjOEHXkNAg%2BEGv9FtuJ%2Fmv7dJaJ5pQWPDceTajAgW35MURh1EOPcfrDNCXW7xZbMBaIrF%2BAw7opnaXVVJEsq9zg%2F2kvWbF4y51fABN2q64ouzS8Sb&X-Amz-Signature=0d7bcbf80f96efde93bb0f67a08c170f62cf8523798607cb08108c0eba10dd61&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 큐브 API서버 

- kubernetes System 컴포넌트는 오직 API서버와 통신
- 컴포넌트간 통신 x
- etcd와 통신하는 유일한 컴포넌트 API
- RESTful API를 통해서 클러스터 상태를 쿼리, 수정할 수 있는 기능 제공
- 구체적인 역할
## 큐브 컨트롤러 매니저

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/5ef47069-72a4-43fe-9427-e42fc25b70d8/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663G2AYMQC%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T072120Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIQDvb4xIAn0r7CdlXel9g5sdXbLwDDk4jrmNfUyfSdZHRAIgGNk%2BeKNOAiBVFS1dpfSgsUwNZFpjz%2FlWeqJ2ezHdXFMq%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDJo%2FtB22PehB1Y6AEyrcA%2F9jSqpN1kzcWO9NXAcDJMRguRseKg2r5sa8ts%2F%2BupiqWtjs8%2BH3NlG%2B6ZNtKji4H0lc2abg1j9YkYnIQF1DYHPN3WDqqCnncHh8pkt9iWR4NHU3SmRrBcIY1kMPaeHETuPUjuNhI7A%2FMepHOO%2FkIWDdVlliFV%2BWrGG%2BVTIHTo4bOa65zaUrl3O0HIeKPLWD9aNYgMyIfo1Jrzyu%2BQBvB4rOiqtkp2smhk7oCVyUk%2Bi2BxE5Lv79jjwVmJ2%2BuF935ADnbQh%2B19b%2FACwyfE%2FPoHKOf%2B%2BeMvkevJrD7jLyzdrj2kYxzVmusYHOlpQP53su3HG%2ByxZWYbizWOi4QMeCWkTwf8ZCwhi3YAgH2%2BxdxaLVgO63dby4BbazmlDVH1TEwrpyaOCf2ZzMTunTUaCP9eenY4SNJS%2F9RJGWwDtLOs7tCvtelWuxfQgnJshaq2S9a1Xdg8YskyF1yalJAwInhS%2FtvCzyXvGa1NntjksukTM3%2Bmp8G8xEwt8xkSkH15dPnxevJrfLj4I5gqdJG7%2FdvsRKYyi1gv8JzNLWc%2BZ5zk77%2BkvuymbFRoo%2FaS7SgiXb9OJNlZyeUTpRk53kxYWym29xG2EimsR7l%2BDDGs30CZV%2ByTzhAZv6Mogjg2OYMOu2wcQGOqUBv552hgOOHvfMKoDk9R7nnAW3TG%2FMH%2B%2FiCauh7r4x3kA%2FumVNXqGgZcxeVDoTQDEkHbp3EsmpZItW1tAw5PrvPq%2B3qr3ft4wGTpUx4nEIChcOjOEHXkNAg%2BEGv9FtuJ%2Fmv7dJaJ5pQWPDceTajAgW35MURh1EOPcfrDNCXW7xZbMBaIrF%2BAw7opnaXVVJEsq9zg%2F2kvWbF4y51fABN2q64ouzS8Sb&X-Amz-Signature=2caa9cdd07e7fafdd94e5d7d65e16cb499560304f17c6ec1e76fc9e98ac11558&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 큐브 스케쥴러

- 일반적으로 실행 할 노드를 직접 정해주지 않음
- 요청 받은 리소스를 어느 노드에서 실행할지 결정하는 역할
- 현재 노드의 상태를 점검하고 최상의 노드를 찾아 배치
- 다수의 포드를 배치하는 경우에는 라운드로빈을 사용하여 분산
## kubernetes System컴포넌트 확인

```yaml
kubectl get pod -n kube-system
```

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/a39272d3-e754-49e8-9357-c94342b1bb23/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663G2AYMQC%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T072120Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIQDvb4xIAn0r7CdlXel9g5sdXbLwDDk4jrmNfUyfSdZHRAIgGNk%2BeKNOAiBVFS1dpfSgsUwNZFpjz%2FlWeqJ2ezHdXFMq%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDJo%2FtB22PehB1Y6AEyrcA%2F9jSqpN1kzcWO9NXAcDJMRguRseKg2r5sa8ts%2F%2BupiqWtjs8%2BH3NlG%2B6ZNtKji4H0lc2abg1j9YkYnIQF1DYHPN3WDqqCnncHh8pkt9iWR4NHU3SmRrBcIY1kMPaeHETuPUjuNhI7A%2FMepHOO%2FkIWDdVlliFV%2BWrGG%2BVTIHTo4bOa65zaUrl3O0HIeKPLWD9aNYgMyIfo1Jrzyu%2BQBvB4rOiqtkp2smhk7oCVyUk%2Bi2BxE5Lv79jjwVmJ2%2BuF935ADnbQh%2B19b%2FACwyfE%2FPoHKOf%2B%2BeMvkevJrD7jLyzdrj2kYxzVmusYHOlpQP53su3HG%2ByxZWYbizWOi4QMeCWkTwf8ZCwhi3YAgH2%2BxdxaLVgO63dby4BbazmlDVH1TEwrpyaOCf2ZzMTunTUaCP9eenY4SNJS%2F9RJGWwDtLOs7tCvtelWuxfQgnJshaq2S9a1Xdg8YskyF1yalJAwInhS%2FtvCzyXvGa1NntjksukTM3%2Bmp8G8xEwt8xkSkH15dPnxevJrfLj4I5gqdJG7%2FdvsRKYyi1gv8JzNLWc%2BZ5zk77%2BkvuymbFRoo%2FaS7SgiXb9OJNlZyeUTpRk53kxYWym29xG2EimsR7l%2BDDGs30CZV%2ByTzhAZv6Mogjg2OYMOu2wcQGOqUBv552hgOOHvfMKoDk9R7nnAW3TG%2FMH%2B%2FiCauh7r4x3kA%2FumVNXqGgZcxeVDoTQDEkHbp3EsmpZItW1tAw5PrvPq%2B3qr3ft4wGTpUx4nEIChcOjOEHXkNAg%2BEGv9FtuJ%2Fmv7dJaJ5pQWPDceTajAgW35MURh1EOPcfrDNCXW7xZbMBaIrF%2BAw7opnaXVVJEsq9zg%2F2kvWbF4y51fABN2q64ouzS8Sb&X-Amz-Signature=1beb90d1e4c27c90b6b413a3a30785824c0825e2513cb1779dacbbe063528b35&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


