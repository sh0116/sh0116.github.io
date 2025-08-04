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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/9c8c0403-7165-46bc-a529-864686459827/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZD7UBJPM%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T072310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJFMEMCH2R8ABwGWzqYx7T1aX8QqzBL4r4a7FxmsjnVSUd%2FwO0CIFHU%2BpnzlFoWvojkQeQJ9LviO%2FmUkCPr5FuD4Kal0sqIKv8DCEAQABoMNjM3NDIzMTgzODA1IgxBBiF7K87BPoRzBV4q3ANMyLwRyI%2Baf1oFcQ%2FsfkSV76MEB3OGXmfZqeaiRCjqLzuOoGEplyGf6ojZbmbHPsrRyirEAxv14toOLVVafxJY%2BBJ5j%2FQ7OMc2JvK1WgFHpGE1sXPqEOHe5kniVn4%2BWjQzm8XZxRQTN2tY%2FUTrT9HUKsSclgZ2s2mYi1Wm%2BIUiS1vaCUKQtrzHuHCrmJPf2H6o43RudinZfQy4Z1dcZgf7%2BvlxaK98tT2fDk1Vfa%2F3tUlB0%2FmmBHjJ4R9LXsjHnHpO8%2FjbId70x9iGbWTYmmEGzTDeXiZTUI2raHx1BqZCqLt%2BJ4PXZPLEehKg7whxWBzYt2vLN9%2FjgbEp4ZD1YKS9vaVca25vbmGADSvGUn%2BmKDjUPbG29i3ty%2FBG%2Bsgw2dINwRFSLUz4uykXSD%2BlmY9CwTnQE3tV44qYE%2Fc4JYFfxL3wGWIpxlKf6fQMQtANaPNEeHWgGHkweTZujdsQhdzDOYRGD%2FlVhITfasZIq6PIozHHoM3oP8w7Zs0DEZ56WHXU7NoonSZe4wuDBdDuEu5bgLVajM1vd%2F5IBZgJ0ufbIupMH5mE0yrhuc%2BpwBcoNRMr1DltLVDWU0AbivQWgZiM8vmUnNUGM48XUl4huUUHzLLui6g5GpESfMQtPzClt8HEBjqnAQwTHUR37fwQADPjFvbXTWNBckWptpMs6VE9IS6cd06DydWd2XvBIY%2FuGyMSZKeS2rPoySOH%2Bi16YIniDX2zxdkWrvAhF%2F3USopozNDUL%2FoMIm%2B%2F4v%2Bb3ovbqzM0Jpf%2FBFvK%2Bvsu3ym5h5ky%2BAlI4p0t8jAha6dunmFtfn8wBVso7nDL0e6BvE%2BPjy5rFPGCgdnc1b7awWNEm2t52RdIUrLRcadM3Tif&X-Amz-Signature=f09fa2e26fe5d414ac0058d47fef64138529499dc41a3a9ab9cb87ed33468e4b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

# 업데이트 결과

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/78a6b4e1-236a-46aa-a2ba-e29ce42f16e9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZD7UBJPM%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T072310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJFMEMCH2R8ABwGWzqYx7T1aX8QqzBL4r4a7FxmsjnVSUd%2FwO0CIFHU%2BpnzlFoWvojkQeQJ9LviO%2FmUkCPr5FuD4Kal0sqIKv8DCEAQABoMNjM3NDIzMTgzODA1IgxBBiF7K87BPoRzBV4q3ANMyLwRyI%2Baf1oFcQ%2FsfkSV76MEB3OGXmfZqeaiRCjqLzuOoGEplyGf6ojZbmbHPsrRyirEAxv14toOLVVafxJY%2BBJ5j%2FQ7OMc2JvK1WgFHpGE1sXPqEOHe5kniVn4%2BWjQzm8XZxRQTN2tY%2FUTrT9HUKsSclgZ2s2mYi1Wm%2BIUiS1vaCUKQtrzHuHCrmJPf2H6o43RudinZfQy4Z1dcZgf7%2BvlxaK98tT2fDk1Vfa%2F3tUlB0%2FmmBHjJ4R9LXsjHnHpO8%2FjbId70x9iGbWTYmmEGzTDeXiZTUI2raHx1BqZCqLt%2BJ4PXZPLEehKg7whxWBzYt2vLN9%2FjgbEp4ZD1YKS9vaVca25vbmGADSvGUn%2BmKDjUPbG29i3ty%2FBG%2Bsgw2dINwRFSLUz4uykXSD%2BlmY9CwTnQE3tV44qYE%2Fc4JYFfxL3wGWIpxlKf6fQMQtANaPNEeHWgGHkweTZujdsQhdzDOYRGD%2FlVhITfasZIq6PIozHHoM3oP8w7Zs0DEZ56WHXU7NoonSZe4wuDBdDuEu5bgLVajM1vd%2F5IBZgJ0ufbIupMH5mE0yrhuc%2BpwBcoNRMr1DltLVDWU0AbivQWgZiM8vmUnNUGM48XUl4huUUHzLLui6g5GpESfMQtPzClt8HEBjqnAQwTHUR37fwQADPjFvbXTWNBckWptpMs6VE9IS6cd06DydWd2XvBIY%2FuGyMSZKeS2rPoySOH%2Bi16YIniDX2zxdkWrvAhF%2F3USopozNDUL%2FoMIm%2B%2F4v%2Bb3ovbqzM0Jpf%2FBFvK%2Bvsu3ym5h5ky%2BAlI4p0t8jAha6dunmFtfn8wBVso7nDL0e6BvE%2BPjy5rFPGCgdnc1b7awWNEm2t52RdIUrLRcadM3Tif&X-Amz-Signature=52d1192f3ab6f35c741b41a4ed6ec77578f6413b7d86604c1bfa3ab58ef5c5e1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


