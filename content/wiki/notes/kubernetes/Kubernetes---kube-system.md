---
source: knowledge-base
origin: notion
title: "Kubernetes - kube-system "
area: "Kubernetes"
tags: ["area/kubernetes", "tech/kubernetes"]
created: "2025-08-04T06:06:00.000Z"
last_edited: "2025-08-04T06:27:00.000Z"
status: published
public: true
notion_id: "245172a5-56d6-80bd-9eb1-e03ec580c49c"
notion_url: "https://www.notion.so/Kubernetes-kube-system-245172a556d680bd9eb1e03ec580c49c"
type: note
updated: 2026-07-07
---

# Kubernetes - kube-system 

## 요약

Kubernetes 기초

Kubernetes 큰 주제 아래에서 세부 개념과 실습 절차를 연결하기 위한 노트입니다.

## 핵심 포인트

- Kubernetes 기초
- Kube-system 컴포넌트의 이해
- 큐브 API서버
- 큐브 컨트롤러 매니저
- 큐브 스케쥴러

## 지식 그래프

- [[wiki/mocs/Knowledge Base|Knowledge Base]]
- [[wiki/mocs/Kubernetes|Kubernetes]]

## 정리 내용

## Kube-system 컴포넌트의 이해
![[_attachments/notion/Kubernetes---kube-system/245172a556d68114b90cc73ef2bf995b.png]]
### 큐브 API서버 
- kubernetes System 컴포넌트는 오직 API서버와 통신
- 컴포넌트간 통신 x
- etcd와 통신하는 유일한 컴포넌트 API
- RESTful API를 통해서 클러스터 상태를 쿼리, 수정할 수 있는 기능 제공
- 구체적인 역할
  - 인증 플러그인 - 클라이언트 인증
  - 권한 승인 플러그인 - 클라이언트 인증
  - 승인 제어 플러그인 - 요청 리소스 확인/수정
  - 리소스 검증 및 영구 저
### 큐브 컨트롤러 매니저
![[_attachments/notion/Kubernetes---kube-system/245172a556d681409e92f1f8ef740557.png]]
### 큐브 스케쥴러
- 일반적으로 실행 할 노드를 직접 정해주지 않음
- 요청 받은 리소스를 어느 노드에서 실행할지 결정하는 역할
- 현재 노드의 상태를 점검하고 최상의 노드를 찾아 배치
- 다수의 포드를 배치하는 경우에는 라운드로빈을 사용하여 분산
### kubernetes System컴포넌트 확인
```yaml
kubectl get pod -n kube-system
```
![[_attachments/notion/Kubernetes---kube-system/245172a556d681a6ab71ed28e167777e.png]]
#### yaml파일 저장 위치확
```yaml
ls /etc/kubernetes/manifests/
```
## static pod
- kubelet이 직접 실행하는 포드
- 각각의 노드에서 kubelet에 의해 실행
- pod들을 삭제할 때, apiserver를 통해서 실행되지 않은  static pod는 삭제 불가
- 즉, 노드의 필요에 의해 사용하고자 하는 포드는 static pod로 셋팅
- 다음 명령들을 사용하여 실행하고자 하는  static pod의 위치를 설정 가능
- /etc/kubernetes/manifest/ 폴더 기본 경로
## etcd 란
- etcd는 데이터베이스다!
- Key - value 데이터 셋 형식으로 구성
- 다중 Key - value 가능
![[_attachments/notion/Kubernetes---kube-system/245172a556d68110b688c394e1c0779c.png]]

![[_attachments/notion/Kubernetes---kube-system/245172a556d68146b7e1f989a33e0f59.png]]
- etcdctl 명령어가 필요 → 다운받아야함
```yaml
wget https://github.com/etcd-io/etcd/releases/download/v3.5.6/etcd-v3.5.6-linux-amd64.tar.gz
tar -xf etcd-v3.5.6-linux-amd64.tar.gz

sudo ETCDCTL_API=3 ./etcdctl --endpoints 127.0.0.1:2379 --cacert /etc/kubernetes/pki/etcd/ca.crt --cert /etc/kubernetes/pki/etcd/server.crt --key /etc/kubernetes/pki/etcd/server.key get / --prefix --keys-only
```
#### 간단한 key-value put & get
```yaml
sudo ETCDCTL_API=3 ./etcdctl --endpoints 127.0.0.1:2379 --cacert /etc/kubernetes/pki/etcd/ca.crt --cert /etc/kubernetes/pki/etcd/server.crt --key /etc/kubernetes/pki/etcd/server.key  put key1 value1
sudo ETCDCTL_API=3 ./etcdctl --endpoints 127.0.0.1:2379 --cacert /etc/kubernetes/pki/etcd/ca.crt --cert /etc/kubernetes/pki/etcd/server.crt --key /etc/kubernetes/pki/etcd/server.key get key1
```

## 출처

- 원문: https://www.notion.so/Kubernetes-kube-system-245172a556d680bd9eb1e03ec580c49c
- Vault path: wiki/notes/kubernetes/Kubernetes---kube-system.md
