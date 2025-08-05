---
title: "Kubernete - Update, Rollback"
date: 2025-08-04 06:05:00 +0900
categories: [kubernetes]
tags: [Kubernetes]
description: Kubernetes 기초
toc: true
comments: true
---

## Application Rolling Update & RollBack

# Update 실습

http-go:v1 → v2 → v3 넘어가며 상태 살펴보기

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: http-go-deployment
  labels:
    app: http-go
spec:
  strategy:
    type: RollingUpdate
  replicas: 3
  selector:
    matchLabels:
      app: http-go
  template:
    metadata:
      labels:
        app: http-go
    spec:
      containers:
      - name: http-go
        image: seokhyeon116/http-go:v1
        ports:
        - containerPort: 8080
```

```yaml
kubectl create -f deploy-go.yaml --record=true #record 옵션을 넣어야 히스토리 확인가
```

### 업데이트 

```yaml
kubectl set image deploy http-go-deployment http-go=seokhyeon116/http-go:v2
# set image를 통해서 업데이트
kubectil edit deploy http-go-deployment # image에서 버전 변경
```

업데이트 방식이 RollingUpdate이다

- maxSurge : 최대로 생성할 수 있는 POD의 수를 정한다 (예를 들어 설정값이 30%이면 전체 POD에서 130%까지 만들 수 있다.) 
- maxUnavailable : 사용할 수 없는 최대 POD수를 정한다 (예를 들어 설정값이 30%이면 전체 POD의 70% 이상으로 항상 유지한다.)
```yaml
kubectl get pod -o wide #명령어 실행 시 아래 화면을 볼 수 있다.
# 노드를 하나씩 업데이하고 생성과 제거를 병행한다.
```

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/9c8c0403-7165-46bc-a529-864686459827/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QE5WGRPV%2F20250805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250805T061130Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQDLHMQwO%2F0MGna6w%2F4K4yNws4cRGUoAjGd3V3c8NRzFEwIhAPHvixQFRYYrPAEXiETFe9A%2FngpFDK5kpaa5XwfUG3OYKv8DCFcQABoMNjM3NDIzMTgzODA1Igw0LBNmpRRGv78%2FLzkq3AOveUI0sbflOnPj%2BZtt0IWgX4sXFXs3mrRnP6l2DDNeDSZJemDam9owwC0GW5mTLMvFqCXR9E7FU6EMyOrdlP36skqDUkd6zil2TjEuKzodh4fO2OiM1wAinFjyFYYMRRaGK6aBwkHIGUzPD2WtGpUcCTStzeA04kozxd8TJ2%2FJmBWvZY0fXdCQA7irh0f67Gi4F7uNK7x7uIliQRaPrdCg0XsHwWHLKyTr5YfpHrKtspuxb7f3zc75cIbnauCWK34Owc65p2dcpiFJocGSF3sMv8aez77YsQzs3MVXy1uFJLjCriPI4JhlieQ2AaN2%2BxbZI97rNNNN0k%2BQkUHULERtagnmgfxUeSsaNEcBu78FvSlAvD0bhqs%2BqAaq2uyKdrYaPAWycctgGzPR85Z%2BhCJJy7yMhDAUxtbdGvjHU2G4sNoxBlBhvVJv25ZtrtLcj1ZzTuhwAyuK9s6ZJUfvSJoXaiPoUoyJvNjBq11RfOtROREW4G04C%2FuSs5da8bUb65FXCQ5kzZLZwC0XARoAPhDcmNDIEzwoqvCt18ckAuAAE%2FDHjLcB8b4exOc5CXjHLSf9rf2puo1q3Xg1KyvQuQf703IztH77uRPlycJzY0XiWRc6Rk0S0V%2FDBH7vTTCPtMbEBjqkAQypglA%2FUxaPbI0xBi%2BSspbEy5XHzM7MEj9604UZrmsZIYpSX9c1rvu8yU6eM5rlTfHKeNqVZyFsNbC3F4X2thz2Fn7JffIzzRBCROZZQe84a3ilQJxLIfB1BTasZImthtvczeu5kzsKVyScKlmiDEaq0Ljg50vlV01ZwgaVjIfmCv%2Bmq%2FH1qBVsuvmlxtVwPZzFJZQhuB8TqD1gN2%2BhIWt0mSt2&X-Amz-Signature=06add1c64993ef7fedb70aff3689973e180ed96721d2065a2a31ed6ed114e6b4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

# 업데이트 결과

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/78a6b4e1-236a-46aa-a2ba-e29ce42f16e9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QE5WGRPV%2F20250805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250805T061130Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQDLHMQwO%2F0MGna6w%2F4K4yNws4cRGUoAjGd3V3c8NRzFEwIhAPHvixQFRYYrPAEXiETFe9A%2FngpFDK5kpaa5XwfUG3OYKv8DCFcQABoMNjM3NDIzMTgzODA1Igw0LBNmpRRGv78%2FLzkq3AOveUI0sbflOnPj%2BZtt0IWgX4sXFXs3mrRnP6l2DDNeDSZJemDam9owwC0GW5mTLMvFqCXR9E7FU6EMyOrdlP36skqDUkd6zil2TjEuKzodh4fO2OiM1wAinFjyFYYMRRaGK6aBwkHIGUzPD2WtGpUcCTStzeA04kozxd8TJ2%2FJmBWvZY0fXdCQA7irh0f67Gi4F7uNK7x7uIliQRaPrdCg0XsHwWHLKyTr5YfpHrKtspuxb7f3zc75cIbnauCWK34Owc65p2dcpiFJocGSF3sMv8aez77YsQzs3MVXy1uFJLjCriPI4JhlieQ2AaN2%2BxbZI97rNNNN0k%2BQkUHULERtagnmgfxUeSsaNEcBu78FvSlAvD0bhqs%2BqAaq2uyKdrYaPAWycctgGzPR85Z%2BhCJJy7yMhDAUxtbdGvjHU2G4sNoxBlBhvVJv25ZtrtLcj1ZzTuhwAyuK9s6ZJUfvSJoXaiPoUoyJvNjBq11RfOtROREW4G04C%2FuSs5da8bUb65FXCQ5kzZLZwC0XARoAPhDcmNDIEzwoqvCt18ckAuAAE%2FDHjLcB8b4exOc5CXjHLSf9rf2puo1q3Xg1KyvQuQf703IztH77uRPlycJzY0XiWRc6Rk0S0V%2FDBH7vTTCPtMbEBjqkAQypglA%2FUxaPbI0xBi%2BSspbEy5XHzM7MEj9604UZrmsZIYpSX9c1rvu8yU6eM5rlTfHKeNqVZyFsNbC3F4X2thz2Fn7JffIzzRBCROZZQe84a3ilQJxLIfB1BTasZImthtvczeu5kzsKVyScKlmiDEaq0Ljg50vlV01ZwgaVjIfmCv%2Bmq%2FH1qBVsuvmlxtVwPZzFJZQhuB8TqD1gN2%2BhIWt0mSt2&X-Amz-Signature=7d74fa7c787df44bf261731c87a009042da461eab31467b3277303e2be09d608&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## RollBack하기

```yaml
kubectl rollout undo deploy http-go-deployment #한단계전으로 undeo
kubectl rollout undo deploy http-go-deployment --to-revision=1 #history 1번으로 돌아감

kubectl rollout history deploy http-go-deployment #해당 delpoy history 출력
# create할 때 --record=true를 해야 명령줄까지 출력됨
```

ㅏ

# 연습 문제

- alpine이미지 사용하여 업데이트와 롤백을 실행하라, 모든 revision내용은 기록되어야 한다.
- 3.5로 롤링 업데이트 수행
- 3.4로 롤백 수행
```yaml
kubectl create deploy alpine-deploy --image=deploy:3.4 --dry-run -o yaml
```

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  creationTimestamp: null
  labels:
    app: alpine-deploy
  name: alpine-deploy
spec:
  replicas: 1
  selector:
    matchLabels:
      app: alpine-deploy
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 50%
      maxUnavailable: 50%
  template:
    metadata:
      creationTimestamp: null
      labels:
        app: alpine-deploy
    spec:
      containers:
      - image: deploy:3.4
        name: deploy
        resources: {}
status: {}
```

```yaml
kubectl set image deploy alpine-deploy alpine-deploy=alpine:3.5
kubectl rollout undo deploy alpine-deploy
```


