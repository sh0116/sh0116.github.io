---
title: "Kubernetes - Replication Controller"
date: 2025-08-04 06:05:00 +0900
categories: [kubernetes]
tags: [Kubernetes]
description: Kubernetes 기초
toc: true
comments: true
---

## ReplicaSet & replication controller

- pod 가 항상 실행되도록 유지하는 쿠버네티스 리소스
- 노드가 클러스터에서 사라지는 경우 해당 pod를 감지하고 대체 pod생성
- 실행 중인 pod의 목록을 지속적으로 모니터링으로 하고 ‘유형’ 의 실제 pod수가 원하는 수와 항상 일치하는지 확인
![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/62301a90-6c63-42b4-adb7-d05287ad1abc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665P67MP5G%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T070524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIQCNbv6JTNZFC1EO1WgtT4lZWbGQf5QcHxV%2FtpWJEPLFGQIgBpDpc87rLttVRfqQmv70Xtqeot3nfLbQFtqYyUbqGe8q%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDD8QrzRmjOjdUSCquircA11wRTq2Zo%2BklyXe27x2%2Fw2Ks6sRtF8uwb7jFxPf%2BJ86Ry%2FYvGSojr6xsD%2FOgZJPaIjqG83MQo9SqVb%2BJUiuecOujT%2FVeXjLrGPHYtgID4EsPmjI9i%2F%2F74GVvY0OC4%2FXrpIoKnxL1vw6G%2BWCFWEVqmfYEy6njQp57gZ9rF1aKvbdQ%2BlntQQlm52kyoPuH1HaKYEhG%2BjQWmpcVkpY6dt6Fi%2F6RaTfnahe7hdt3nopmVeir1GrklwJatPc%2F9Un%2BhmsgbJMtrWHpjTd2p9hNEP%2BpUpryya77SMOwaOUFXD3X11rO6uCiPjRhBri1a%2B74V5sD9QiN4%2F93YrYCc%2BDyD7TzowcHmH6InLavAnoSbp8LtvP%2FMM5mWaTbMmAAGFM5ATleV9gXVhMqxaXFKb%2BTuoWdsNSpAcyLPKTf1Ap8hoxjHYdnjM2gcDGEa5mpCQha72MCg8huFHUitoUCGb5ADzAt4%2BEv2A%2FkW0v2XdPOgUZbJDqg6Me%2FBuZBDO90K2F48YgjbeNK9%2B0p3iUF5IUMvUiZ3%2FFIVc39ORtWN2SPM108117MvET1ZX2NRUu91E%2Ba8b%2B%2BAwI3f4zCbtAsG3PFAi8n9iCWPwW9VrVsSgb9z7G3Lnz5pnH6GLBs%2FEEByo%2FMOy2wcQGOqUBZ4gHGl%2BwWn9DzoG2j24e%2FdJuZLYMnL%2BjNmo4wJ98AsReLfI2oM77rvr3N7hjyzfVB5G%2BpluPcIZC73VOY1y8klIMGVPeTr6zR36uwTLDEximiLis%2F5x%2FFgEkSXDh3D6UjKfLSzGt5m09ZI5r5HYBJ7ndHpDY57z94JugtJC7%2FSyrtOgDJT7KU4Sxi47htX0TXG9lJIWb76nTfqFUNZ3ULj63E9zN&X-Amz-Signature=a0e1035fcd6f5cfb931632960e6e99da67a2a89193281a270935fc36099e2e0b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

 

## replication controller 세가지 요소

- 관리하는 pod범위를 결정하는 레이블 셀렉터
- 실행해야하는 pod의 수를 결정하는 복제본 수
- 새로운 pod의 모양을 설명하는 pod템플릿
## replication controller 장점 

- pod가 없는 경우 새 pod 항상 실행
- 노드에 장애 발생 시 다른 노드에 복제본 생성
- 수동, 자동으로 수평 스케일
## replication controller YAML 작성

```yaml
apiVersion: v1
kind: ReplicationController
metadata:
  name: nginx
spec:
  replicas: 3
  selector:
    app: nginx
  template:
    metadata:
      name: nginx
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx
        ports:
        - containerPort: 80
```

## replication controller 조회

```bash
kubectl get  rc #replicationcontrolle 줄임
```

```bash
kubectl describe rc rc이름 #상세 정보 확인 (이벤트 로그 확인 가능)
```

## replication controller 수정

```bash
kubectl scale rc rc이름 --replicas=5 # replica를 5로 늘리는 수정

kubectl edit rc rc이름 # 설정 파일 수정 가능 (vim형태)
```

## replication controller 삭제

```bash
kubectl delete rc rc이름 # rc삭제
kubectl delete rc rc이름 --cascade=false # 실행된 pod는 유지 rc는 삭제
```

## replication controller node 장애 

- 여러 노드에 분산 배치된 pod가 있을 때 만약 한 노드에서 장애가 발생하면 
![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/5734a11c-7eb9-439a-94e2-3aa375662766/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665P67MP5G%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T070524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIQCNbv6JTNZFC1EO1WgtT4lZWbGQf5QcHxV%2FtpWJEPLFGQIgBpDpc87rLttVRfqQmv70Xtqeot3nfLbQFtqYyUbqGe8q%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDD8QrzRmjOjdUSCquircA11wRTq2Zo%2BklyXe27x2%2Fw2Ks6sRtF8uwb7jFxPf%2BJ86Ry%2FYvGSojr6xsD%2FOgZJPaIjqG83MQo9SqVb%2BJUiuecOujT%2FVeXjLrGPHYtgID4EsPmjI9i%2F%2F74GVvY0OC4%2FXrpIoKnxL1vw6G%2BWCFWEVqmfYEy6njQp57gZ9rF1aKvbdQ%2BlntQQlm52kyoPuH1HaKYEhG%2BjQWmpcVkpY6dt6Fi%2F6RaTfnahe7hdt3nopmVeir1GrklwJatPc%2F9Un%2BhmsgbJMtrWHpjTd2p9hNEP%2BpUpryya77SMOwaOUFXD3X11rO6uCiPjRhBri1a%2B74V5sD9QiN4%2F93YrYCc%2BDyD7TzowcHmH6InLavAnoSbp8LtvP%2FMM5mWaTbMmAAGFM5ATleV9gXVhMqxaXFKb%2BTuoWdsNSpAcyLPKTf1Ap8hoxjHYdnjM2gcDGEa5mpCQha72MCg8huFHUitoUCGb5ADzAt4%2BEv2A%2FkW0v2XdPOgUZbJDqg6Me%2FBuZBDO90K2F48YgjbeNK9%2B0p3iUF5IUMvUiZ3%2FFIVc39ORtWN2SPM108117MvET1ZX2NRUu91E%2Ba8b%2B%2BAwI3f4zCbtAsG3PFAi8n9iCWPwW9VrVsSgb9z7G3Lnz5pnH6GLBs%2FEEByo%2FMOy2wcQGOqUBZ4gHGl%2BwWn9DzoG2j24e%2FdJuZLYMnL%2BjNmo4wJ98AsReLfI2oM77rvr3N7hjyzfVB5G%2BpluPcIZC73VOY1y8klIMGVPeTr6zR36uwTLDEximiLis%2F5x%2FFgEkSXDh3D6UjKfLSzGt5m09ZI5r5HYBJ7ndHpDY57z94JugtJC7%2FSyrtOgDJT7KU4Sxi47htX0TXG9lJIWb76nTfqFUNZ3ULj63E9zN&X-Amz-Signature=ef73d8384955261b70034de20948279801f39f0c695827198938317bad1a9dfb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


