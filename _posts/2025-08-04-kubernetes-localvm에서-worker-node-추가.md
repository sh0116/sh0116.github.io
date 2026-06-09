---
title: "Kubernetes - Local(VM)에서 Worker Node 추가"
date: 2025-08-04 06:05:00 +0900
categories: [kubernetes]
tags: [Kubernetes]
description: Kubernetes 기초
toc: true
comments: true
redirect_from:
  - /posts/kubernetes---local(vm)에서-worker-node-추가/
---

### Master Node와 기존에 이미 Worker Node가 있는 경우입니다

VMWare Pro환경

1. 기존 WorkNode의 스냅샵을 복사해서 열어준다
![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/21b55de0-e97e-4c3e-8482-c14068e3facf/Untitled.png)

1. Workstation에서 스냅샷을 열어준다
![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/f970e8c2-39e0-470f-823e-d9c5606d3fd1/Untitled.png)

1. 기존 Node들을 종료하고 새로운 Node를 실행한다.
1. 네트워크 설정이 있었다면 바꿔준다.
1. kubeadm 초기화
```yaml
kubeadm reset
```

1. Master Node로 돌아가서 token을 생성한다.
```yaml
kubeadm token create -h #도움말
kubeadm token create --print-join-command #토큰 명령어
--> 결과값을 새로 생성한 Node에 복붙해주면 된다
```

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/f3aff170-0497-48fa-9f87-e4431356d68c/Untitled.png)


