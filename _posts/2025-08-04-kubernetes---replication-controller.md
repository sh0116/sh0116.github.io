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
![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/62301a90-6c63-42b4-adb7-d05287ad1abc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VYKDCIER%2F20250805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250805T002707Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJHMEUCIHse6XppuydVfORsAN1sRkqtUvYdZrO5hdmppb8HxCVyAiEAnpaYh3JnZa295LletPxondqFtY7Y2ab7u%2BXLhkxG%2Fp8q%2FwMIUBAAGgw2Mzc0MjMxODM4MDUiDLlcbCVyZezjjgJf0ircA8Jk48H3uVXEUOohxDrKENDFqdN0V0B2lhpO3mljCNp5RHqpeFpSu%2BnYs53xrcLkJHZhpdVJ63QnyHoZSnBG9hSvRwraQB4MRV%2BSzj%2BMTj7YsyoM9jtErwUqX7HhlF1J%2Fyp6we%2B%2FUG%2FzNH3BFOFA7c4aq2dvafNj7ImNOX6rHElryjOFGfW8itLtxOBI2rYyHrJnRdKN67MMiO2qbz7PQx9PxCpt6ZpNTSnBAGb0MsGOwzenXfqr1ne9Q6%2BeRfFSgVVEVLsdMeGy4%2BJ7irvB7c%2FJssREmIKajPHSO3NVvpphPYxuklMmG9uVcMi1hboLvWOPhuw%2Fks1Q%2B5lXUUVlHC%2BZfO1MapAc7y8CL2GqBFT2lvtQeo9kGNjHwMBTe3zUwvW5ZFil3jnyvuMq%2FcF1NFeQPlM9mOJV3Suo5C8944b9NZ5V71MDJVmdVapO%2FqzmPYPuQO283HMwYmEGqTkrw2UWFFRFoKZ3LVhTQ6Ky4JE39IzN3lm8uugUvvY17UJmf7vjcQhEWtwAG%2FbEPTFpTdTGYuJWEdy3prqtXs3OURc3WJ%2FcbX4KDrozA4%2FwYEcQPp0u0c5UyyCs1I3IDPCl5FovwsC%2BkSI%2FNzbq9lbjyjUCtFUvLUhEaXKiF0SgMJf0xMQGOqUBKKu7H7fjzKXi4UoFi7GHhprm8Cp%2BdhVHLaDTQfqOsfajFxVhVNrdGGTNpb1C3c1NRq0nrGFaAPT1qCLBFdG9B0l2a4WRWTsjjMaoPPHdsN9lnjo04oZHQtwTxfmbFJ8XROAOSK4zS9WAUehYb8Yk2bZWYMEypP9dy4dT3lpCTleRVB6WcR7nH%2BbYtQTYsAll%2FAO%2BhY1tGmPuuv%2FVPWahb6U%2Fg7i2&X-Amz-Signature=f47040681395feb617e598e37af0594c99b24177a45e4bc74c3a6294d093dddb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

 

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
![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/5734a11c-7eb9-439a-94e2-3aa375662766/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VYKDCIER%2F20250805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250805T002708Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJHMEUCIHse6XppuydVfORsAN1sRkqtUvYdZrO5hdmppb8HxCVyAiEAnpaYh3JnZa295LletPxondqFtY7Y2ab7u%2BXLhkxG%2Fp8q%2FwMIUBAAGgw2Mzc0MjMxODM4MDUiDLlcbCVyZezjjgJf0ircA8Jk48H3uVXEUOohxDrKENDFqdN0V0B2lhpO3mljCNp5RHqpeFpSu%2BnYs53xrcLkJHZhpdVJ63QnyHoZSnBG9hSvRwraQB4MRV%2BSzj%2BMTj7YsyoM9jtErwUqX7HhlF1J%2Fyp6we%2B%2FUG%2FzNH3BFOFA7c4aq2dvafNj7ImNOX6rHElryjOFGfW8itLtxOBI2rYyHrJnRdKN67MMiO2qbz7PQx9PxCpt6ZpNTSnBAGb0MsGOwzenXfqr1ne9Q6%2BeRfFSgVVEVLsdMeGy4%2BJ7irvB7c%2FJssREmIKajPHSO3NVvpphPYxuklMmG9uVcMi1hboLvWOPhuw%2Fks1Q%2B5lXUUVlHC%2BZfO1MapAc7y8CL2GqBFT2lvtQeo9kGNjHwMBTe3zUwvW5ZFil3jnyvuMq%2FcF1NFeQPlM9mOJV3Suo5C8944b9NZ5V71MDJVmdVapO%2FqzmPYPuQO283HMwYmEGqTkrw2UWFFRFoKZ3LVhTQ6Ky4JE39IzN3lm8uugUvvY17UJmf7vjcQhEWtwAG%2FbEPTFpTdTGYuJWEdy3prqtXs3OURc3WJ%2FcbX4KDrozA4%2FwYEcQPp0u0c5UyyCs1I3IDPCl5FovwsC%2BkSI%2FNzbq9lbjyjUCtFUvLUhEaXKiF0SgMJf0xMQGOqUBKKu7H7fjzKXi4UoFi7GHhprm8Cp%2BdhVHLaDTQfqOsfajFxVhVNrdGGTNpb1C3c1NRq0nrGFaAPT1qCLBFdG9B0l2a4WRWTsjjMaoPPHdsN9lnjo04oZHQtwTxfmbFJ8XROAOSK4zS9WAUehYb8Yk2bZWYMEypP9dy4dT3lpCTleRVB6WcR7nH%2BbYtQTYsAll%2FAO%2BhY1tGmPuuv%2FVPWahb6U%2Fg7i2&X-Amz-Signature=d2656b90ca58382ec7ab91e9215e6e0c5e6a58dbe63844078631f02a7bfa4ac9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


