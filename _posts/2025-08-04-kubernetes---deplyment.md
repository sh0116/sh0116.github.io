---
title: "Kubernetes - Deplyment"
date: 2025-08-04 06:05:00 +0900
categories: [kubernetes]
tags: [Kubernetes]
description: Kubernetes 기초
toc: true
comments: true
---

## Deployment

- Application을 다운 타입 없이 업데이트 가능하도록 도와주는 리소스!
- ReplicaSet과 Replication Controller 상위에 배포되는 리소스
![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/9faef226-8b82-4d03-b75a-857efb7979b8/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46665PUOVFH%2F20250805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250805T061042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJHMEUCIQDyCDO23Tl3Zc6GSi4kv40wl0u%2F8b%2Fz1rDq4yaNNRTzVwIgM1EaOrQj2%2B7%2FlYn8DuT0NohzmWsGaK%2F%2F64qpvkynOZEq%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDGQvlpzn8%2BaS0YLMLCrcAyWNq6muRpPkaaTZ8qW1DM9vnYkXAdoYDNfQ%2BrAgQMIicpxbaPlYuM6iT8g7Dy0we8tglnK04EJ%2BQ%2F%2BcVRytm1LqeqIuflHeHFnnscelh%2BInVJiTY%2FfGob%2BPTSCnIcSPx80VomeLXcBzDRS6z51OhYr9YsdrfV%2Bj9BilE07mVLF4BMiCJoMI8iC%2FU%2FWw7o0fECcLdnN5WVzvVcxgKHM0UKtyFekDSayvl4MMBVXV15fOkKmpZ82ojVMGAvV0KNQ5NV%2Fktg2cBwaZA0zgc%2B%2FEBexHFyU3ZFSaqdcIUMM%2B%2Bmi9Z1%2BgUj2XqsdfPhaectPa7vFkiiCiAlvrDrGicZMIlzm4sup1OFEdO60ICCfSM%2BGA5IF8A8BlyOiW56NQfxensU4TveQyN3NSbVverYVZvcnmk5nNoW5%2FEsHwG9E67nwSbYCwUkJ100dL%2F3IBfxc6Jn8IjRpCeVd5Iq5JH7%2FGeOLMeic5lGWTNhubbTNkTfc%2FUpl9AaYtA7wNZoyDDet7Fi2N%2F2Rx6kP4vYYzy87YF%2FRGJ%2F5Yc8kTB0SrdrdcZgAbqV5KTljxMD0uykjlW6SG7j2vec5WIl7sACUs3iPhRznhv1IPb5vB2cvQcj6jexx%2B1qZ%2FXIBFl92spql1MK2zxsQGOqUBmQc6%2FrWeg0DCajAXQ6Z3Jh0XftPcJHJHZtl%2FUMT3Qt8nz9cp%2BqLGESRAhs4zNyMUMtgsx%2BmuWGB2GgRgKAZdpAASzgLvgYU1iglBclhEJHQzqblnb4GmdV2udbhrQW%2BP0tr7z2WBp%2BhlXRqetW8hRCGghniOnyMhIorKsdLHzd329FTOGETPxd3BhNSh3Kbjo0QiuyArNhtLkYrkLEj3fKXzNFdM&X-Amz-Signature=2ac114e5df0b5e3693ea01211d8de5c3b764268e6a5c51c9fd016f00997f6aee&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 업데이트 전략

- recreate 
- Rolling Update :
# Deployment 실습

- Jenkins deployment 생성 - deploy-jenkins
- jenkins deployment로 배포되는 앱을 app : jenkins-test로 레이블링
- deployment로 배포된 pod를 하나 삭제하고 이후 생성되는 포드를 관찰
- 새로 생성된 pod의 레이블을 바꿔 deployment 관리영역에서 벗어나게 하라
- scale명령으로 사용할 replica 수 를 5개로 정의
- edit 기능을 사용하여 10로 스켈일링
### Jenkins deployment 생성 - deploy-jenkins

```yaml
kubectl create -f yaml이름
```

### jenkins deployment로 배포되는 앱을 app : jenkins-test로 레이블링

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: deploy-jenkins
  labels:
    app: jenkins-test
spec:
  replicas: 3
  selector:
    matchLabels:
      app: jenkins-test
  template:
    metadata:
      labels:
        app: jenkins-test
    spec:
      containers:
      - name: jk
        image: jenkins/jenkins
        ports:
        - containerPort: 8080
```

### deployment로 배포된 pod를 하나 삭제하고 이후 생성되는 포드를관찰

```bash
kubectl delete pod pod명
kubectl get pod -w --show-labels
```

### 새로 생성된 pod의 레이블을 바꿔 deployment 관리영역에서 벗어나게 하라

```bash
k label pod deploy-jenkins-69d6b7df8c-mjc2m app-
```

### scale명령으로 사용할 replica 수 를 5개로 정의

```yaml
kubectl scale deploy deploy이름 --replicas=5
```

### edit 기능을 사용하여 10로 스켈일링

```yaml
kubectl edit deploy deploy이름
```

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/162bac64-5cd6-4c19-8588-644a8869155a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46665PUOVFH%2F20250805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250805T061042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJHMEUCIQDyCDO23Tl3Zc6GSi4kv40wl0u%2F8b%2Fz1rDq4yaNNRTzVwIgM1EaOrQj2%2B7%2FlYn8DuT0NohzmWsGaK%2F%2F64qpvkynOZEq%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDGQvlpzn8%2BaS0YLMLCrcAyWNq6muRpPkaaTZ8qW1DM9vnYkXAdoYDNfQ%2BrAgQMIicpxbaPlYuM6iT8g7Dy0we8tglnK04EJ%2BQ%2F%2BcVRytm1LqeqIuflHeHFnnscelh%2BInVJiTY%2FfGob%2BPTSCnIcSPx80VomeLXcBzDRS6z51OhYr9YsdrfV%2Bj9BilE07mVLF4BMiCJoMI8iC%2FU%2FWw7o0fECcLdnN5WVzvVcxgKHM0UKtyFekDSayvl4MMBVXV15fOkKmpZ82ojVMGAvV0KNQ5NV%2Fktg2cBwaZA0zgc%2B%2FEBexHFyU3ZFSaqdcIUMM%2B%2Bmi9Z1%2BgUj2XqsdfPhaectPa7vFkiiCiAlvrDrGicZMIlzm4sup1OFEdO60ICCfSM%2BGA5IF8A8BlyOiW56NQfxensU4TveQyN3NSbVverYVZvcnmk5nNoW5%2FEsHwG9E67nwSbYCwUkJ100dL%2F3IBfxc6Jn8IjRpCeVd5Iq5JH7%2FGeOLMeic5lGWTNhubbTNkTfc%2FUpl9AaYtA7wNZoyDDet7Fi2N%2F2Rx6kP4vYYzy87YF%2FRGJ%2F5Yc8kTB0SrdrdcZgAbqV5KTljxMD0uykjlW6SG7j2vec5WIl7sACUs3iPhRznhv1IPb5vB2cvQcj6jexx%2B1qZ%2FXIBFl92spql1MK2zxsQGOqUBmQc6%2FrWeg0DCajAXQ6Z3Jh0XftPcJHJHZtl%2FUMT3Qt8nz9cp%2BqLGESRAhs4zNyMUMtgsx%2BmuWGB2GgRgKAZdpAASzgLvgYU1iglBclhEJHQzqblnb4GmdV2udbhrQW%2BP0tr7z2WBp%2BhlXRqetW8hRCGghniOnyMhIorKsdLHzd329FTOGETPxd3BhNSh3Kbjo0QiuyArNhtLkYrkLEj3fKXzNFdM&X-Amz-Signature=6926bfe47f2471692685214e6e04bcb5f52ad7a7699b9dcb626d2fd688b02cd6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


