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
![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/62301a90-6c63-42b4-adb7-d05287ad1abc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UR7Z6IEX%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T072153Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIGkC8w1Ebo0QMpXgPMdmi%2B2kj16ZvYqu1d6sV11%2FheAMAiEA7y8Q668SqhEVaKlG1y6MukYTLkX1BT3sJbqFen5LYYIq%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDFJNxF3M%2BVhSB8meFircA%2BX4al6tQTPorCdNJHDXlmQrxU0vWm4XdwT1kiUv3lkR01G51AvCWxUS5Er6175wDhu6KQmQpZBDMAwZnQib3YT4k4Q7wCc7O73XSxA8NkyVRQo5JnpLMPpjqJAu0VoRqNc1PudpP%2BK9xatDCJUAjO5v2HVfisZUEfs%2BaCWx%2BfTu1yuYgc4b%2BsFwLpX8VL3pwwUoc%2BR%2F6cYNAHcA2GMXSreAMIMzWq6Rch1AoQmtQIlGW5b0qtS%2BRE0%2FL7Rtle4Alrtd3vGKyqYh%2FZxcsMDtcvkjeCF17UCQeQYR365dzMAxT31dJXevF2Q1xN4MQa%2B%2F10w7%2FwGE%2F9QxV4wFo86jf3ei9cRjRAv4hoPm1sAaenpuOB80GxGIauMK5V3H4%2BanaAXxZHa32HdmD%2Fw9Itc1WNKkqUahsJ4mkjpGJHAvexkwlHKSrtmYCGzi2MQDlHlATKtQO%2BcPQlK4Oh%2FppUJ7uKMkNRh4mxk3OIjk%2F61sBWTQ%2Fi%2BznfALFRlkLj%2B3VqzoBmcXNwQgkaWBw35nXd3xBABuCDgULDuLXFKdVIqfcbDGVPGBrUEepHAsQW0%2FT%2BH6cHget%2BjYkyVheHhcV0ShhMCYG4jRQZu7u0567Y4fh6BDteWfUupyxSzXKKZ1MMq2wcQGOqUBfyb14GnAmafwleg8FdNEXD179hbsfj5R0aIiMwMtG1fBRJy0kDFpT2jIWt%2FmX2Rgs04QwuD7i5aQqpLXmUsHs%2FYIbMDmn2IwByYQZOn%2BmER7AWldAsYnIvQpkRSzwotCJdQKmtoR%2B5ZKmzP2tfHuzmRBbDGDxMmrvEmEnOa5v4Ehyz0fwXov007BDiP5TMLgGwwitki5o%2BkkFiRbhD%2BHAqbnZkom&X-Amz-Signature=4517546fd5c0ca6c71757f5595710ecdb6ae24a5abfe3d12dadee72a6292270c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

 

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
![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/5734a11c-7eb9-439a-94e2-3aa375662766/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UR7Z6IEX%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T072153Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIGkC8w1Ebo0QMpXgPMdmi%2B2kj16ZvYqu1d6sV11%2FheAMAiEA7y8Q668SqhEVaKlG1y6MukYTLkX1BT3sJbqFen5LYYIq%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDFJNxF3M%2BVhSB8meFircA%2BX4al6tQTPorCdNJHDXlmQrxU0vWm4XdwT1kiUv3lkR01G51AvCWxUS5Er6175wDhu6KQmQpZBDMAwZnQib3YT4k4Q7wCc7O73XSxA8NkyVRQo5JnpLMPpjqJAu0VoRqNc1PudpP%2BK9xatDCJUAjO5v2HVfisZUEfs%2BaCWx%2BfTu1yuYgc4b%2BsFwLpX8VL3pwwUoc%2BR%2F6cYNAHcA2GMXSreAMIMzWq6Rch1AoQmtQIlGW5b0qtS%2BRE0%2FL7Rtle4Alrtd3vGKyqYh%2FZxcsMDtcvkjeCF17UCQeQYR365dzMAxT31dJXevF2Q1xN4MQa%2B%2F10w7%2FwGE%2F9QxV4wFo86jf3ei9cRjRAv4hoPm1sAaenpuOB80GxGIauMK5V3H4%2BanaAXxZHa32HdmD%2Fw9Itc1WNKkqUahsJ4mkjpGJHAvexkwlHKSrtmYCGzi2MQDlHlATKtQO%2BcPQlK4Oh%2FppUJ7uKMkNRh4mxk3OIjk%2F61sBWTQ%2Fi%2BznfALFRlkLj%2B3VqzoBmcXNwQgkaWBw35nXd3xBABuCDgULDuLXFKdVIqfcbDGVPGBrUEepHAsQW0%2FT%2BH6cHget%2BjYkyVheHhcV0ShhMCYG4jRQZu7u0567Y4fh6BDteWfUupyxSzXKKZ1MMq2wcQGOqUBfyb14GnAmafwleg8FdNEXD179hbsfj5R0aIiMwMtG1fBRJy0kDFpT2jIWt%2FmX2Rgs04QwuD7i5aQqpLXmUsHs%2FYIbMDmn2IwByYQZOn%2BmER7AWldAsYnIvQpkRSzwotCJdQKmtoR%2B5ZKmzP2tfHuzmRBbDGDxMmrvEmEnOa5v4Ehyz0fwXov007BDiP5TMLgGwwitki5o%2BkkFiRbhD%2BHAqbnZkom&X-Amz-Signature=e101c9bdb0297cd4efc3492bf8ab87c2b7b0e837217fcc675f8fb09eadaf9722&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


