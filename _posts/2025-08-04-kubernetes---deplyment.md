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
![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/9faef226-8b82-4d03-b75a-857efb7979b8/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YUFPWGZH%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T072226Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIQCkzgHe2uKek2MOA53md5K%2F1ylAxZvFhWcYd3IL5lX1rQIgaZp%2B2CyzeWKJMIXcw5US2SrBlbY5biN4ikz%2BH3WqleAq%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDIge7ct0GZo%2BZEdrQircA8DOWwPqrbz3zKQlxtsrkz0lh6DXROJikzGkOKpv8QtIylVrQgHi2AI8B2D2uRScCkpJ3K9UwRvv5YESf0w6atM6zEw951VZbTTE%2F1Ns5vAjmBee0CcEKEoe601bZMWVKzFcZBwKqKPRAhIjvLhjedrUlUKNbvxNo0fCbTt2k6vuQREWCkG%2BoPUwP0CujOqSQaxnEZa84KJvM%2BG834SMZzaRlTDl3xarJtNy1yFzxcw39agoqehpcgY73K978sJ7yitJVxDi9VJbDm0S64FjyKH444PGETHwpr%2BeEjwryiPKloaOhQ0G9ZMetordjloQw5lifWh78cIgeVMx2j5b%2BgEa7waKojPG5XKByNuFXgCvgxddG8Bxe%2BCT5YDr%2FwZ7%2FaI%2B2bSvKHoXk0%2BdCO95pPgJLBKxtZ%2FW6%2FFk%2BirwdbGHNxGmX%2FVOYRRwp30kcJNZRfGbtam8pf5x59WJvb5dT2VqOmFpLZY9pbeeliF8N%2BYQQyMbkXxspC2YidXVqQv8lSjunzUczQQokeQJzPMKcIiEaYyEmJNU58q0slAS615M1nXt9%2FjBQ8UI%2FVh%2Fy31tle5F%2FkZqIWTzjVUgdR3pOLgeHBDrCO57SmRkBkG4JkVbeNFXRFAOKchtg1ZxMN22wcQGOqUBrHAfJ8FuDhp7cY2L%2BJunSJKSbbkbp%2FgsEMADCJRiw9WlYMl1XkOwFCUfKTVFjpYjtKoNTmozyAIpvrMfY2Cd1XBRMCepNCVu7UNLs%2B%2BFLum%2Ff6Z5bqV6vpcMMJpD1X3cQKuz7g5OF1vmTzxk9iTYnUT%2BoptF1i3nzUJD4UTTwGcI1tmoFuXi7CUKr5wRmerdzzopn3ct%2FsNckLl3RfTupqYhsZsN&X-Amz-Signature=516264137d76ace2144a0939b3b0ac6de194acc417d1d6c38dfc6d2946d1ace0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/162bac64-5cd6-4c19-8588-644a8869155a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YUFPWGZH%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T072226Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIQCkzgHe2uKek2MOA53md5K%2F1ylAxZvFhWcYd3IL5lX1rQIgaZp%2B2CyzeWKJMIXcw5US2SrBlbY5biN4ikz%2BH3WqleAq%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDIge7ct0GZo%2BZEdrQircA8DOWwPqrbz3zKQlxtsrkz0lh6DXROJikzGkOKpv8QtIylVrQgHi2AI8B2D2uRScCkpJ3K9UwRvv5YESf0w6atM6zEw951VZbTTE%2F1Ns5vAjmBee0CcEKEoe601bZMWVKzFcZBwKqKPRAhIjvLhjedrUlUKNbvxNo0fCbTt2k6vuQREWCkG%2BoPUwP0CujOqSQaxnEZa84KJvM%2BG834SMZzaRlTDl3xarJtNy1yFzxcw39agoqehpcgY73K978sJ7yitJVxDi9VJbDm0S64FjyKH444PGETHwpr%2BeEjwryiPKloaOhQ0G9ZMetordjloQw5lifWh78cIgeVMx2j5b%2BgEa7waKojPG5XKByNuFXgCvgxddG8Bxe%2BCT5YDr%2FwZ7%2FaI%2B2bSvKHoXk0%2BdCO95pPgJLBKxtZ%2FW6%2FFk%2BirwdbGHNxGmX%2FVOYRRwp30kcJNZRfGbtam8pf5x59WJvb5dT2VqOmFpLZY9pbeeliF8N%2BYQQyMbkXxspC2YidXVqQv8lSjunzUczQQokeQJzPMKcIiEaYyEmJNU58q0slAS615M1nXt9%2FjBQ8UI%2FVh%2Fy31tle5F%2FkZqIWTzjVUgdR3pOLgeHBDrCO57SmRkBkG4JkVbeNFXRFAOKchtg1ZxMN22wcQGOqUBrHAfJ8FuDhp7cY2L%2BJunSJKSbbkbp%2FgsEMADCJRiw9WlYMl1XkOwFCUfKTVFjpYjtKoNTmozyAIpvrMfY2Cd1XBRMCepNCVu7UNLs%2B%2BFLum%2Ff6Z5bqV6vpcMMJpD1X3cQKuz7g5OF1vmTzxk9iTYnUT%2BoptF1i3nzUJD4UTTwGcI1tmoFuXi7CUKr5wRmerdzzopn3ct%2FsNckLl3RfTupqYhsZsN&X-Amz-Signature=7fd990e762dea6eeb5bb78dac0460a02a9ccd8e2c95c51d55e19760ba18c1f16&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


