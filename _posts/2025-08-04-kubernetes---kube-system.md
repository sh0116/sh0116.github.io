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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/b231983e-0ca9-463d-a773-6c60f2c51f50/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZFNOGEEN%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T063221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCIQCBeC88YDLuP5lYY8F4Wx4Y2Kbt%2F9HXu1g7VRf1bxo53gIgUd0VuSc2XehnEKdRcHrQlf3mbhT0G7mottywFPYEEmYq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDFO9gism0tZDYD3I3CrcA%2BPtYpjoP%2F3ejPnKdDt1zaefAVFUJ157v9dMIg8ZMOjXhRcxg%2FNPH%2F8aOWwFzYAcRqCLL6QoKJST0lKVH52032K7GMUUnrCBU4SYmML5xYVgkRHS6RNpKhJQ4rQ5V37jQZhEZei%2BCEHsR8%2B9VNkZ%2FwbVtvKUthT4yxSD%2BXVKCZYc%2BJTBwlGRLnByiCsjS%2FzKBLS0hfS5IgLnnVwMOXUabpuLDQuzPgDHyjarFc7rq82c1U%2BaOIWsHaQ69kLzjHWKM837MgY4QxFyHTuI9rP%2FbfZijcgtSHTVhtJgu6kGB08gZWVSAmVoAGhYWQabM25GRg0a1ky5y3lOoz1%2B0f2cEZjh7VcyPbNpgvC%2BV%2FHd5q8g2iSFikSfXEIkGZjSXNmcSQz5dy6NGTy2ZCMKhW3X550SFx8I34amBBeKVTV4IWjmbw6jQIbvri0fokbpjqib%2FT5ZfVu6Z1cWAHH8mwn%2F%2B9yUu5aJZ04HW3DsaAZvMNckGUaAGJGn9EDpmWTOic4lDwmQdZaksJ5SUGvCq7Tcw2wehD99WJfEZdakSBHvG5vfTqJcJRlMZ8yPncRs6kMIIyQ3E5Rx9Czyw0WoolRyWajcjVn4WvoZTRepWVW6oTtPy7pktO3fvYvVl2ahMICNwcQGOqUBonuExmxhWb1llWI1sLWMb1309rCAzdEC%2Bn7EdMGopgPJBVUWIkm8CPbLS9dZzyT8PR8KZzGRRzZjo7KtQAdmkKX6p%2FUvRKPmGWMldViAd%2FbYPyIJ5D8CrqKTs7QyRlDqdFkmOc31sRRzb%2BLGqnu3r0DeUbcT8ecfFQOXKnGMSZ5zgHeGACXJlpfoY53HGa9DIMddLG6F8RUcIkN8rLz3w5pmteBV&X-Amz-Signature=83a166e9307ccc1224578bdc37d12bd19a12085614b394fd392131a612eab390&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 큐브 API서버 

- kubernetes System 컴포넌트는 오직 API서버와 통신
- 컴포넌트간 통신 x
- etcd와 통신하는 유일한 컴포넌트 API
- RESTful API를 통해서 클러스터 상태를 쿼리, 수정할 수 있는 기능 제공
- 구체적인 역할
## 큐브 컨트롤러 매니저

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/5ef47069-72a4-43fe-9427-e42fc25b70d8/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZFNOGEEN%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T063221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCIQCBeC88YDLuP5lYY8F4Wx4Y2Kbt%2F9HXu1g7VRf1bxo53gIgUd0VuSc2XehnEKdRcHrQlf3mbhT0G7mottywFPYEEmYq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDFO9gism0tZDYD3I3CrcA%2BPtYpjoP%2F3ejPnKdDt1zaefAVFUJ157v9dMIg8ZMOjXhRcxg%2FNPH%2F8aOWwFzYAcRqCLL6QoKJST0lKVH52032K7GMUUnrCBU4SYmML5xYVgkRHS6RNpKhJQ4rQ5V37jQZhEZei%2BCEHsR8%2B9VNkZ%2FwbVtvKUthT4yxSD%2BXVKCZYc%2BJTBwlGRLnByiCsjS%2FzKBLS0hfS5IgLnnVwMOXUabpuLDQuzPgDHyjarFc7rq82c1U%2BaOIWsHaQ69kLzjHWKM837MgY4QxFyHTuI9rP%2FbfZijcgtSHTVhtJgu6kGB08gZWVSAmVoAGhYWQabM25GRg0a1ky5y3lOoz1%2B0f2cEZjh7VcyPbNpgvC%2BV%2FHd5q8g2iSFikSfXEIkGZjSXNmcSQz5dy6NGTy2ZCMKhW3X550SFx8I34amBBeKVTV4IWjmbw6jQIbvri0fokbpjqib%2FT5ZfVu6Z1cWAHH8mwn%2F%2B9yUu5aJZ04HW3DsaAZvMNckGUaAGJGn9EDpmWTOic4lDwmQdZaksJ5SUGvCq7Tcw2wehD99WJfEZdakSBHvG5vfTqJcJRlMZ8yPncRs6kMIIyQ3E5Rx9Czyw0WoolRyWajcjVn4WvoZTRepWVW6oTtPy7pktO3fvYvVl2ahMICNwcQGOqUBonuExmxhWb1llWI1sLWMb1309rCAzdEC%2Bn7EdMGopgPJBVUWIkm8CPbLS9dZzyT8PR8KZzGRRzZjo7KtQAdmkKX6p%2FUvRKPmGWMldViAd%2FbYPyIJ5D8CrqKTs7QyRlDqdFkmOc31sRRzb%2BLGqnu3r0DeUbcT8ecfFQOXKnGMSZ5zgHeGACXJlpfoY53HGa9DIMddLG6F8RUcIkN8rLz3w5pmteBV&X-Amz-Signature=015f4999d234e5cef44407304e1fbfe0c15f1361e395dc97e7a893ff703ad4a3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 큐브 스케쥴러

- 일반적으로 실행 할 노드를 직접 정해주지 않음
- 요청 받은 리소스를 어느 노드에서 실행할지 결정하는 역할
- 현재 노드의 상태를 점검하고 최상의 노드를 찾아 배치
- 다수의 포드를 배치하는 경우에는 라운드로빈을 사용하여 분산
## kubernetes System컴포넌트 확인

```yaml
kubectl get pod -n kube-system
```

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/a39272d3-e754-49e8-9357-c94342b1bb23/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZFNOGEEN%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T063221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCIQCBeC88YDLuP5lYY8F4Wx4Y2Kbt%2F9HXu1g7VRf1bxo53gIgUd0VuSc2XehnEKdRcHrQlf3mbhT0G7mottywFPYEEmYq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDFO9gism0tZDYD3I3CrcA%2BPtYpjoP%2F3ejPnKdDt1zaefAVFUJ157v9dMIg8ZMOjXhRcxg%2FNPH%2F8aOWwFzYAcRqCLL6QoKJST0lKVH52032K7GMUUnrCBU4SYmML5xYVgkRHS6RNpKhJQ4rQ5V37jQZhEZei%2BCEHsR8%2B9VNkZ%2FwbVtvKUthT4yxSD%2BXVKCZYc%2BJTBwlGRLnByiCsjS%2FzKBLS0hfS5IgLnnVwMOXUabpuLDQuzPgDHyjarFc7rq82c1U%2BaOIWsHaQ69kLzjHWKM837MgY4QxFyHTuI9rP%2FbfZijcgtSHTVhtJgu6kGB08gZWVSAmVoAGhYWQabM25GRg0a1ky5y3lOoz1%2B0f2cEZjh7VcyPbNpgvC%2BV%2FHd5q8g2iSFikSfXEIkGZjSXNmcSQz5dy6NGTy2ZCMKhW3X550SFx8I34amBBeKVTV4IWjmbw6jQIbvri0fokbpjqib%2FT5ZfVu6Z1cWAHH8mwn%2F%2B9yUu5aJZ04HW3DsaAZvMNckGUaAGJGn9EDpmWTOic4lDwmQdZaksJ5SUGvCq7Tcw2wehD99WJfEZdakSBHvG5vfTqJcJRlMZ8yPncRs6kMIIyQ3E5Rx9Czyw0WoolRyWajcjVn4WvoZTRepWVW6oTtPy7pktO3fvYvVl2ahMICNwcQGOqUBonuExmxhWb1llWI1sLWMb1309rCAzdEC%2Bn7EdMGopgPJBVUWIkm8CPbLS9dZzyT8PR8KZzGRRzZjo7KtQAdmkKX6p%2FUvRKPmGWMldViAd%2FbYPyIJ5D8CrqKTs7QyRlDqdFkmOc31sRRzb%2BLGqnu3r0DeUbcT8ecfFQOXKnGMSZ5zgHeGACXJlpfoY53HGa9DIMddLG6F8RUcIkN8rLz3w5pmteBV&X-Amz-Signature=c32d69b2f53ee4df0c8a4f7f02b24c10644df5cce8c98f259381d6dc147406b9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


