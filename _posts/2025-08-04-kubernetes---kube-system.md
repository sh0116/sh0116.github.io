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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/b231983e-0ca9-463d-a773-6c60f2c51f50/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YDKHWMUE%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T070452Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJIMEYCIQD6wTV8EqPKVsvK8FNx6VkE5Nv9EnooPdsraBu%2BB7ueewIhALcfXbrAHLPHrvrtV1XyKEkfWrWB7X%2BH7%2Frg%2BrenIE0OKv8DCD8QABoMNjM3NDIzMTgzODA1IgxCuNAfJ01ZaJ%2FnGHMq3APCHes4akaQjeTpjlZzRH9srq%2Bdj8guIx67B39QCkV4GlUZmixwqdCYNmd%2B4HdbRB5APaAtmw4hPjfxMivz7FBfPMwqI5PCShUE1nuYWkAnJIb3c6LWnfHRC1qrjdAx8rDQJerZ3bCMjUHIsRMsrpq98VqDf7bT5aYEGDjeZ38%2BcogcKz2xfw3KZ86h0KtUhgAXcwYCXNiRTYuyl%2FdDYLl07b6xToDGVLGjDT4%2FlE%2Ftt%2F7g1uXbLL0fR68W3UJjngeQTOf78uzVDYgx7ptPaGF%2BtBHbrwt5FD4FdNB6WVOR5R65HW%2BEslVij0DmF09abuEtAP6aAHwtMPI4%2BggweZuAPMNW4jcOwew3KBozkrXyn0Q9vonspRxwSXxeq6HUaX7uoeKh0CPNXYuZ9Qndshn7ZX1k1n0bwgYGYJWdCGk2ot3rByQaD1XAjxcf4CLbhTaq1EWOjkNCOUyshRtkFVcp9VxAy2LMgvwRHx2DJMkvyRw1M6HAz9QY%2Fv6aeIUYWaZITgBPxm%2FZozuYtowIW1UHLBWL7UpKsBr6lK9HvrvYJDUvvgOsvZtlYCPB9gW%2F1%2FbtKMA%2BXIm8vzUUommF11sIRg6KSrM9xvT%2FIj1pFKVDfvFeRk9bF1%2B4%2FBKfMDC0jcHEBjqkAXAizN5p3SqNahzeDxW47uW6CUzNX%2BqDzDKMeHFXTUUXi2i2q2qZbAeap5mT0v9sNmCNoypYF5Jwcne6aWBexs1QVy7jfO8M56jkNvK7ZMNu8Z44DaGZEKN0EG5ZcjDCkNp0amYCB%2BPQU0Xbh9rvT1PRAKCJSOegu9imoiXv9GsaLkoh2C%2BmJe6lEY88s1I7cSdyQrqCZISKNPfBsdNMAxddZ0BK&X-Amz-Signature=76f6f098dcc144fcdd194a637886ec52e6f77d6b0732621c8997ef18ab11af4d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 큐브 API서버 

- kubernetes System 컴포넌트는 오직 API서버와 통신
- 컴포넌트간 통신 x
- etcd와 통신하는 유일한 컴포넌트 API
- RESTful API를 통해서 클러스터 상태를 쿼리, 수정할 수 있는 기능 제공
- 구체적인 역할
## 큐브 컨트롤러 매니저

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/5ef47069-72a4-43fe-9427-e42fc25b70d8/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YDKHWMUE%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T070452Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJIMEYCIQD6wTV8EqPKVsvK8FNx6VkE5Nv9EnooPdsraBu%2BB7ueewIhALcfXbrAHLPHrvrtV1XyKEkfWrWB7X%2BH7%2Frg%2BrenIE0OKv8DCD8QABoMNjM3NDIzMTgzODA1IgxCuNAfJ01ZaJ%2FnGHMq3APCHes4akaQjeTpjlZzRH9srq%2Bdj8guIx67B39QCkV4GlUZmixwqdCYNmd%2B4HdbRB5APaAtmw4hPjfxMivz7FBfPMwqI5PCShUE1nuYWkAnJIb3c6LWnfHRC1qrjdAx8rDQJerZ3bCMjUHIsRMsrpq98VqDf7bT5aYEGDjeZ38%2BcogcKz2xfw3KZ86h0KtUhgAXcwYCXNiRTYuyl%2FdDYLl07b6xToDGVLGjDT4%2FlE%2Ftt%2F7g1uXbLL0fR68W3UJjngeQTOf78uzVDYgx7ptPaGF%2BtBHbrwt5FD4FdNB6WVOR5R65HW%2BEslVij0DmF09abuEtAP6aAHwtMPI4%2BggweZuAPMNW4jcOwew3KBozkrXyn0Q9vonspRxwSXxeq6HUaX7uoeKh0CPNXYuZ9Qndshn7ZX1k1n0bwgYGYJWdCGk2ot3rByQaD1XAjxcf4CLbhTaq1EWOjkNCOUyshRtkFVcp9VxAy2LMgvwRHx2DJMkvyRw1M6HAz9QY%2Fv6aeIUYWaZITgBPxm%2FZozuYtowIW1UHLBWL7UpKsBr6lK9HvrvYJDUvvgOsvZtlYCPB9gW%2F1%2FbtKMA%2BXIm8vzUUommF11sIRg6KSrM9xvT%2FIj1pFKVDfvFeRk9bF1%2B4%2FBKfMDC0jcHEBjqkAXAizN5p3SqNahzeDxW47uW6CUzNX%2BqDzDKMeHFXTUUXi2i2q2qZbAeap5mT0v9sNmCNoypYF5Jwcne6aWBexs1QVy7jfO8M56jkNvK7ZMNu8Z44DaGZEKN0EG5ZcjDCkNp0amYCB%2BPQU0Xbh9rvT1PRAKCJSOegu9imoiXv9GsaLkoh2C%2BmJe6lEY88s1I7cSdyQrqCZISKNPfBsdNMAxddZ0BK&X-Amz-Signature=020cad01b4db21212e1a140670bfd3e6d58dfa1724b903a7ddb059a49464a794&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 큐브 스케쥴러

- 일반적으로 실행 할 노드를 직접 정해주지 않음
- 요청 받은 리소스를 어느 노드에서 실행할지 결정하는 역할
- 현재 노드의 상태를 점검하고 최상의 노드를 찾아 배치
- 다수의 포드를 배치하는 경우에는 라운드로빈을 사용하여 분산
## kubernetes System컴포넌트 확인

```yaml
kubectl get pod -n kube-system
```

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/a39272d3-e754-49e8-9357-c94342b1bb23/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YDKHWMUE%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T070452Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJIMEYCIQD6wTV8EqPKVsvK8FNx6VkE5Nv9EnooPdsraBu%2BB7ueewIhALcfXbrAHLPHrvrtV1XyKEkfWrWB7X%2BH7%2Frg%2BrenIE0OKv8DCD8QABoMNjM3NDIzMTgzODA1IgxCuNAfJ01ZaJ%2FnGHMq3APCHes4akaQjeTpjlZzRH9srq%2Bdj8guIx67B39QCkV4GlUZmixwqdCYNmd%2B4HdbRB5APaAtmw4hPjfxMivz7FBfPMwqI5PCShUE1nuYWkAnJIb3c6LWnfHRC1qrjdAx8rDQJerZ3bCMjUHIsRMsrpq98VqDf7bT5aYEGDjeZ38%2BcogcKz2xfw3KZ86h0KtUhgAXcwYCXNiRTYuyl%2FdDYLl07b6xToDGVLGjDT4%2FlE%2Ftt%2F7g1uXbLL0fR68W3UJjngeQTOf78uzVDYgx7ptPaGF%2BtBHbrwt5FD4FdNB6WVOR5R65HW%2BEslVij0DmF09abuEtAP6aAHwtMPI4%2BggweZuAPMNW4jcOwew3KBozkrXyn0Q9vonspRxwSXxeq6HUaX7uoeKh0CPNXYuZ9Qndshn7ZX1k1n0bwgYGYJWdCGk2ot3rByQaD1XAjxcf4CLbhTaq1EWOjkNCOUyshRtkFVcp9VxAy2LMgvwRHx2DJMkvyRw1M6HAz9QY%2Fv6aeIUYWaZITgBPxm%2FZozuYtowIW1UHLBWL7UpKsBr6lK9HvrvYJDUvvgOsvZtlYCPB9gW%2F1%2FbtKMA%2BXIm8vzUUommF11sIRg6KSrM9xvT%2FIj1pFKVDfvFeRk9bF1%2B4%2FBKfMDC0jcHEBjqkAXAizN5p3SqNahzeDxW47uW6CUzNX%2BqDzDKMeHFXTUUXi2i2q2qZbAeap5mT0v9sNmCNoypYF5Jwcne6aWBexs1QVy7jfO8M56jkNvK7ZMNu8Z44DaGZEKN0EG5ZcjDCkNp0amYCB%2BPQU0Xbh9rvT1PRAKCJSOegu9imoiXv9GsaLkoh2C%2BmJe6lEY88s1I7cSdyQrqCZISKNPfBsdNMAxddZ0BK&X-Amz-Signature=caf4c9fddf5e97959f1a938250c7fa11de8645039ea49917bfc0506ff1fce4b3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


