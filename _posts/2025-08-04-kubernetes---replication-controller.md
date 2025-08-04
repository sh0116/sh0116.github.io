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
![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/62301a90-6c63-42b4-adb7-d05287ad1abc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665QUM22SC%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T063257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJIMEYCIQDjFPiTZpm0TtnOvpnWzGbKXY2cmE7oyTeyCmfSi4BH5wIhAItjTE6lRWT%2Fsggy%2BNDwqinWH9dXatJ4A26Gw6Z2BuylKv8DCD8QABoMNjM3NDIzMTgzODA1IgwMltavet44MZ15X1Eq3APBpBo4VI3O0SMfcFS7ddAGfDKVx8RMgz2dAu8PU62YAX68FwXLYUhhbxUt7eplZ30DlwQjutdr3PmW%2F62JIyQ%2F0pGBZpmgMzuci%2FmUyaxvZYUcEoYVr%2BAosbWzSBEtmO11yJkiLNuCEHNw9oAU3XCjAReu%2F6dBFDymTpgdfdA%2BEgUfAVJ%2BhHG458Jr0F4tD%2FnAz9RvmANq6406%2FiAWh7VfkwCn2AMXdJPY8Cg7vZOJYK6monQ%2FQcqneLl72%2B2z6n41BZAelOtZOQc974TmKGeXsMr%2F5wASlD0tkZJf4UABAfgMrKftzK5yYDLe%2BLBjHHVBX%2BwW4f3BUJuX34uzdXnpR2Z%2BFm7Db9LwvmNsZIxUs658tSSR7%2FcO9%2BmAWNHD9aWWZhqUSUHpqedqbdwR0yuQcb9%2FTmJ6z51CGEnHxVvMCTpuKdeTSb7TY3K%2Fe2dwLyC2xzHfPsyvEB54TkMEA3ltIO4JIPmc%2F9ehKtzoR8nXx8vLXJ5QRam7Oam3iRa8j8SrGL3oASqaN5DZ6mEuQFxaZGREeiT8nbWcIw7nV%2BuOS%2BPNN37hTIPYmEBR5GRIoJVUFd7LC1B7x84LPo7iMk7%2Fqvc%2FbDWcMgomLtkfTiFPhWkboKVm%2FYbrgHT%2FiDCtjcHEBjqkAak2MHJNSXU%2BWGDkt8aWpmcT%2FxTWib2Jjh1EoT7ipKZs%2F0wrTitRzqhzOC6JcqeDmLECEA2IOYjbGGaj01gMUJ4unpbMazwbIfH4SAJp1x8VwSI4ImggambV3olxKOVunzVkpVV15uCBd7hGlFYOPss3xE6%2FlKxXI0U6k3IOxnabMIK6kV1ZSrQIznBlwGdvJlV3%2FTwg1lec3GS4oc6ogv6oy2hi&X-Amz-Signature=3856b3a51c98919e0ade64ca8ed24f1f70df52d4cefed4398311dfcd8151167f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

 

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
![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/5734a11c-7eb9-439a-94e2-3aa375662766/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665QUM22SC%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T063257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJIMEYCIQDjFPiTZpm0TtnOvpnWzGbKXY2cmE7oyTeyCmfSi4BH5wIhAItjTE6lRWT%2Fsggy%2BNDwqinWH9dXatJ4A26Gw6Z2BuylKv8DCD8QABoMNjM3NDIzMTgzODA1IgwMltavet44MZ15X1Eq3APBpBo4VI3O0SMfcFS7ddAGfDKVx8RMgz2dAu8PU62YAX68FwXLYUhhbxUt7eplZ30DlwQjutdr3PmW%2F62JIyQ%2F0pGBZpmgMzuci%2FmUyaxvZYUcEoYVr%2BAosbWzSBEtmO11yJkiLNuCEHNw9oAU3XCjAReu%2F6dBFDymTpgdfdA%2BEgUfAVJ%2BhHG458Jr0F4tD%2FnAz9RvmANq6406%2FiAWh7VfkwCn2AMXdJPY8Cg7vZOJYK6monQ%2FQcqneLl72%2B2z6n41BZAelOtZOQc974TmKGeXsMr%2F5wASlD0tkZJf4UABAfgMrKftzK5yYDLe%2BLBjHHVBX%2BwW4f3BUJuX34uzdXnpR2Z%2BFm7Db9LwvmNsZIxUs658tSSR7%2FcO9%2BmAWNHD9aWWZhqUSUHpqedqbdwR0yuQcb9%2FTmJ6z51CGEnHxVvMCTpuKdeTSb7TY3K%2Fe2dwLyC2xzHfPsyvEB54TkMEA3ltIO4JIPmc%2F9ehKtzoR8nXx8vLXJ5QRam7Oam3iRa8j8SrGL3oASqaN5DZ6mEuQFxaZGREeiT8nbWcIw7nV%2BuOS%2BPNN37hTIPYmEBR5GRIoJVUFd7LC1B7x84LPo7iMk7%2Fqvc%2FbDWcMgomLtkfTiFPhWkboKVm%2FYbrgHT%2FiDCtjcHEBjqkAak2MHJNSXU%2BWGDkt8aWpmcT%2FxTWib2Jjh1EoT7ipKZs%2F0wrTitRzqhzOC6JcqeDmLECEA2IOYjbGGaj01gMUJ4unpbMazwbIfH4SAJp1x8VwSI4ImggambV3olxKOVunzVkpVV15uCBd7hGlFYOPss3xE6%2FlKxXI0U6k3IOxnabMIK6kV1ZSrQIznBlwGdvJlV3%2FTwg1lec3GS4oc6ogv6oy2hi&X-Amz-Signature=9375d2a773f3b6269e94d8f9a52dce6065e7feb654a0e342d76453485bd8bf60&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


