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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/b231983e-0ca9-463d-a773-6c60f2c51f50/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WNQUGL5Y%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T071951Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCICQ%2Bxw36U8ySzaUOqKoGnmPwbCZM06X8b4LL2o9BkK%2BMAiEA3DoBnq8ZeiR1aIO1bNa%2FCONp%2F%2BWzWUNDHJZZlqtvJWMq%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDA5Yp7ch9hGHHRqM5yrcA5nyzD1ppUWfjH9OxtpO2xJArRG0yfgcVEFIvbBVZPlu%2FnJvA21c0WmWpomRmwdED0zcipXFqG7d78Wf73ZsduK2ct58IlS%2FsHmYIqXN3tXEOPFpK0VBX84u%2BVmvqg%2Brt8ha5ZwCYTAKISDjtAJzgJcrWuLgvhcEipywOcEwc7cFVIYNghwSSqWuYCtPMokZgAzPtuaV9SFpZU0dNetpFrF4E6kWjhzCF%2FuxSVU82h0ZfxoIJaab3iYAywMlu6rqaUx8dGiXujtQair%2BJjGOsO36xOACeZrF297nq5WC685npfIjbSqAXzcelC7VrF5LWTMfEMFQS9J3ep2sZOGa0jjNrxQ290kvfcwRG8qCrybAkwk2y5kD2J%2F05cPNllEreNV0wRnwIEVXkPhLaP%2BYKJ70En4DMfzIXWaqkGiDAqJtnnvuvqcMZ3dQd55UWUwrGZSr6YPqjNse8PgEzWQF%2FmiU2y4xrKzVZxc0ZjX6t5yQ3uAQ7Xm14uH6JOD7MJHme4dLGXTOJ0f5lEYGIfL22FvF8DkF30rytO6GS88wUb0p7BEepDBAsV458lXlxTs2XVJwf1bMA4NPg7YmhtLHjHbNBTzZIZD%2Fvv3if%2Bd6Y9UTXvFLmH9dGbXGObSQMLi4wcQGOqUBiWzDXotaGOhkWTlKPIUCiMUIYJwZPClhShGxSqkAEq9TtTR4Xr7I%2BZyVwfmtyO75TKmriLbStNTXu1hpvAmHt%2BXsFOygSD4p3VrofEGhXWOXTR5qg3zNXvG5X0w1WbEyVBTCxbwB1CDPzOCSr5MJahx07l8dOVA3rp8kt38Mp5fy8uyux56rnZL6wDPZ4HeUxrJ9T7TA4C2Nct6h59glxxUg7157&X-Amz-Signature=cf25cae32fd639119d815cac5cae2cc085b0aebc3fb525a3cd949ff87b7256ed&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 큐브 API서버 

- kubernetes System 컴포넌트는 오직 API서버와 통신
- 컴포넌트간 통신 x
- etcd와 통신하는 유일한 컴포넌트 API
- RESTful API를 통해서 클러스터 상태를 쿼리, 수정할 수 있는 기능 제공
- 구체적인 역할
## 큐브 컨트롤러 매니저

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/5ef47069-72a4-43fe-9427-e42fc25b70d8/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WNQUGL5Y%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T071951Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCICQ%2Bxw36U8ySzaUOqKoGnmPwbCZM06X8b4LL2o9BkK%2BMAiEA3DoBnq8ZeiR1aIO1bNa%2FCONp%2F%2BWzWUNDHJZZlqtvJWMq%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDA5Yp7ch9hGHHRqM5yrcA5nyzD1ppUWfjH9OxtpO2xJArRG0yfgcVEFIvbBVZPlu%2FnJvA21c0WmWpomRmwdED0zcipXFqG7d78Wf73ZsduK2ct58IlS%2FsHmYIqXN3tXEOPFpK0VBX84u%2BVmvqg%2Brt8ha5ZwCYTAKISDjtAJzgJcrWuLgvhcEipywOcEwc7cFVIYNghwSSqWuYCtPMokZgAzPtuaV9SFpZU0dNetpFrF4E6kWjhzCF%2FuxSVU82h0ZfxoIJaab3iYAywMlu6rqaUx8dGiXujtQair%2BJjGOsO36xOACeZrF297nq5WC685npfIjbSqAXzcelC7VrF5LWTMfEMFQS9J3ep2sZOGa0jjNrxQ290kvfcwRG8qCrybAkwk2y5kD2J%2F05cPNllEreNV0wRnwIEVXkPhLaP%2BYKJ70En4DMfzIXWaqkGiDAqJtnnvuvqcMZ3dQd55UWUwrGZSr6YPqjNse8PgEzWQF%2FmiU2y4xrKzVZxc0ZjX6t5yQ3uAQ7Xm14uH6JOD7MJHme4dLGXTOJ0f5lEYGIfL22FvF8DkF30rytO6GS88wUb0p7BEepDBAsV458lXlxTs2XVJwf1bMA4NPg7YmhtLHjHbNBTzZIZD%2Fvv3if%2Bd6Y9UTXvFLmH9dGbXGObSQMLi4wcQGOqUBiWzDXotaGOhkWTlKPIUCiMUIYJwZPClhShGxSqkAEq9TtTR4Xr7I%2BZyVwfmtyO75TKmriLbStNTXu1hpvAmHt%2BXsFOygSD4p3VrofEGhXWOXTR5qg3zNXvG5X0w1WbEyVBTCxbwB1CDPzOCSr5MJahx07l8dOVA3rp8kt38Mp5fy8uyux56rnZL6wDPZ4HeUxrJ9T7TA4C2Nct6h59glxxUg7157&X-Amz-Signature=4266cc2c245d9016b40c3f3e6fb78aeea3dd1e41ea716ddc914bb8e6a84c036c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 큐브 스케쥴러

- 일반적으로 실행 할 노드를 직접 정해주지 않음
- 요청 받은 리소스를 어느 노드에서 실행할지 결정하는 역할
- 현재 노드의 상태를 점검하고 최상의 노드를 찾아 배치
- 다수의 포드를 배치하는 경우에는 라운드로빈을 사용하여 분산
## kubernetes System컴포넌트 확인

```yaml
kubectl get pod -n kube-system
```

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/a39272d3-e754-49e8-9357-c94342b1bb23/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WNQUGL5Y%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T071951Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCICQ%2Bxw36U8ySzaUOqKoGnmPwbCZM06X8b4LL2o9BkK%2BMAiEA3DoBnq8ZeiR1aIO1bNa%2FCONp%2F%2BWzWUNDHJZZlqtvJWMq%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDA5Yp7ch9hGHHRqM5yrcA5nyzD1ppUWfjH9OxtpO2xJArRG0yfgcVEFIvbBVZPlu%2FnJvA21c0WmWpomRmwdED0zcipXFqG7d78Wf73ZsduK2ct58IlS%2FsHmYIqXN3tXEOPFpK0VBX84u%2BVmvqg%2Brt8ha5ZwCYTAKISDjtAJzgJcrWuLgvhcEipywOcEwc7cFVIYNghwSSqWuYCtPMokZgAzPtuaV9SFpZU0dNetpFrF4E6kWjhzCF%2FuxSVU82h0ZfxoIJaab3iYAywMlu6rqaUx8dGiXujtQair%2BJjGOsO36xOACeZrF297nq5WC685npfIjbSqAXzcelC7VrF5LWTMfEMFQS9J3ep2sZOGa0jjNrxQ290kvfcwRG8qCrybAkwk2y5kD2J%2F05cPNllEreNV0wRnwIEVXkPhLaP%2BYKJ70En4DMfzIXWaqkGiDAqJtnnvuvqcMZ3dQd55UWUwrGZSr6YPqjNse8PgEzWQF%2FmiU2y4xrKzVZxc0ZjX6t5yQ3uAQ7Xm14uH6JOD7MJHme4dLGXTOJ0f5lEYGIfL22FvF8DkF30rytO6GS88wUb0p7BEepDBAsV458lXlxTs2XVJwf1bMA4NPg7YmhtLHjHbNBTzZIZD%2Fvv3if%2Bd6Y9UTXvFLmH9dGbXGObSQMLi4wcQGOqUBiWzDXotaGOhkWTlKPIUCiMUIYJwZPClhShGxSqkAEq9TtTR4Xr7I%2BZyVwfmtyO75TKmriLbStNTXu1hpvAmHt%2BXsFOygSD4p3VrofEGhXWOXTR5qg3zNXvG5X0w1WbEyVBTCxbwB1CDPzOCSr5MJahx07l8dOVA3rp8kt38Mp5fy8uyux56rnZL6wDPZ4HeUxrJ9T7TA4C2Nct6h59glxxUg7157&X-Amz-Signature=8550b61628be8d648a2367580e47e4018c833807badfa605bad4c311d621fe8f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


