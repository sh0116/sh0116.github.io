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
![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/62301a90-6c63-42b4-adb7-d05287ad1abc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YJ3LZTFA%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T071417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIGQbSePoQTCjEpXvAUJsqEXI6Ui3q%2FfO9bqdoZ5Du5iQAiEA9753o9grIm%2FH4d5pG44dGXdZGBXNdnSrqMJqwXv732wq%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDKFL2k2vSZ3ws5TYfCrcA0yQ7e2Ts%2Ffo6tjxoPwHMFHZp9g6FgmvLYJnVGTycIvzNCU%2BxsfwknXe3rt7XtOR%2BWlecmcq0a%2Fn3%2BmDXliA3IZ3tJnFIlMF4HDos%2B0rIW59pZW7n6Oe1zidQRGY4Oc293LY91rZOHAJDy6MqEbZ2gAt8HfjDw71I5HxxWQDT%2B6MrCvVY5YZpVPOtz06CPuP4kWt8a7T8OFrt6xTd60RvgPh8swIEg3D2j%2BdF4M05MwOdK9UyK2WYlc%2FxFaNIVvyNP4EPgzGT4XDf9ePcGPKJobMQNNwhqDJslR3Ic%2Fx8hl%2BjfIu5gX3RjGsjW9n3IvQfnhAxENKicaAiAvtS3dzUF9VWt2PtOIuN5yE4YNjeKYa8xTLSNR%2FE%2F4l00A4gQuONAPT5BSLRu%2FQaq7KfsA%2BWk5USeDjCUgZT2rbJfT2Q%2F%2FYHdA%2FOgbHVDdU4s1uiwk7qeJGGmuJGB6FnuoR9n0LGvzc7Wm%2B01lZDBKEy7UposRu1Voii8sph0FHaYcM7zmcQ7kL1Civ1wHciVRr9ZwQ%2B6ahXyxa1n6Sg%2BQPyxCjepYxeZ0VM%2BXG1QFezuWN2WShtTJCjU1u%2BWQNj2PVR6OMbV441ww7%2BrnJJ%2BARWfp8RwAAJj5IDoWaMm3%2Fq%2FWZMMi2wcQGOqUBBFe72iw5Y6KULTUkbJS7PFuXpOnyFOegL3HH1XlY%2FS87KksMNpTsqnf4qoTVTUA%2F1hq4jNH6pFqAlD3sd842bPSRD5ixn4PSzHOltT3zziuIvoKKbeMZ%2BWEo4pUfhC0aGbF7lBucpMZb1RV0jigEiU%2BtAtz9MnYNXIVFHhXvzP9YO767SpXfz34QgIomKVrl%2B%2FdiiLOoh%2FHB1d0tosiXZ2SzyBjR&X-Amz-Signature=3cdb7b811ec3cd1b2cfdbf897c8fad1d8bd49f88556c786efb3d97545fa77a37&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

 

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
![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/5734a11c-7eb9-439a-94e2-3aa375662766/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YJ3LZTFA%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T071417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIGQbSePoQTCjEpXvAUJsqEXI6Ui3q%2FfO9bqdoZ5Du5iQAiEA9753o9grIm%2FH4d5pG44dGXdZGBXNdnSrqMJqwXv732wq%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDKFL2k2vSZ3ws5TYfCrcA0yQ7e2Ts%2Ffo6tjxoPwHMFHZp9g6FgmvLYJnVGTycIvzNCU%2BxsfwknXe3rt7XtOR%2BWlecmcq0a%2Fn3%2BmDXliA3IZ3tJnFIlMF4HDos%2B0rIW59pZW7n6Oe1zidQRGY4Oc293LY91rZOHAJDy6MqEbZ2gAt8HfjDw71I5HxxWQDT%2B6MrCvVY5YZpVPOtz06CPuP4kWt8a7T8OFrt6xTd60RvgPh8swIEg3D2j%2BdF4M05MwOdK9UyK2WYlc%2FxFaNIVvyNP4EPgzGT4XDf9ePcGPKJobMQNNwhqDJslR3Ic%2Fx8hl%2BjfIu5gX3RjGsjW9n3IvQfnhAxENKicaAiAvtS3dzUF9VWt2PtOIuN5yE4YNjeKYa8xTLSNR%2FE%2F4l00A4gQuONAPT5BSLRu%2FQaq7KfsA%2BWk5USeDjCUgZT2rbJfT2Q%2F%2FYHdA%2FOgbHVDdU4s1uiwk7qeJGGmuJGB6FnuoR9n0LGvzc7Wm%2B01lZDBKEy7UposRu1Voii8sph0FHaYcM7zmcQ7kL1Civ1wHciVRr9ZwQ%2B6ahXyxa1n6Sg%2BQPyxCjepYxeZ0VM%2BXG1QFezuWN2WShtTJCjU1u%2BWQNj2PVR6OMbV441ww7%2BrnJJ%2BARWfp8RwAAJj5IDoWaMm3%2Fq%2FWZMMi2wcQGOqUBBFe72iw5Y6KULTUkbJS7PFuXpOnyFOegL3HH1XlY%2FS87KksMNpTsqnf4qoTVTUA%2F1hq4jNH6pFqAlD3sd842bPSRD5ixn4PSzHOltT3zziuIvoKKbeMZ%2BWEo4pUfhC0aGbF7lBucpMZb1RV0jigEiU%2BtAtz9MnYNXIVFHhXvzP9YO767SpXfz34QgIomKVrl%2B%2FdiiLOoh%2FHB1d0tosiXZ2SzyBjR&X-Amz-Signature=56f177efa2bb62247b4e4ddb6763e53c738fc56bd73723d1db3c70d95280a55b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


