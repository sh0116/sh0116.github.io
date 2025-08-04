---
title: "Kubernetes - ReplicaSet"
date: 2025-08-04 06:05:00 +0900
categories: [kubernetes]
tags: [Kubernetes]
description: Kubernetes 기초
toc: true
comments: true
---

# ReplicaSet

- ReplicaSet은 차세대 Replication Controller로 완전히 대체 가능함
- 초기 쿠버네티스에서 제공했기 때문에 현장에서는 여전히 계속 사용중인 경우 존재
- 일반적으로 ReplicaSet을 직접 생성하지 않고 상위 수준의 Deployment 리소스를 만들 때 자동으로 생성
## ReplicatSet & Replication Controller 차이점

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/35742fe6-0f6d-41c3-a55c-0af6e8de2e29/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UCV6VEAM%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T072047Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJGMEQCIFEFuQbjFT8xZsPxgdAK3mscGahb3DQ5uE1LhnqytHxHAiAhcDOEXy4ik2LjnzytLcg7fDwIQC4EYl9fvBN6R0tIqSr%2FAwhAEAAaDDYzNzQyMzE4MzgwNSIM1D9tDeiAuG%2BqbMsMKtwD31YH6eVmXAPx51U53H6nAoKUhrszwuFh%2FxZMQM8YlYFQxwOiykwQY7iF0towOd0SGT1QXWqpq%2FmCOdaWTXda4LtacXU8fFg1JebIHb2TLMzuJuuYJE%2FGIHCBpBYbcummnrRApY4fF%2Br0VEwFHu8R3yvDsnkO7CP%2BmQu4iI5cG6fjisZaAYQ7yjat4xhrGv12jxQ7FW8QiFEVq8kuB4uA6R6%2B34EljO9eUWtwuZZX7C%2BL1Miz230KbY38akAr3sEtBNh1vwxlOIDn9rCVuhuzYcJOfRfOWMeQbs%2BP2cXpmBCY98KMov7qJLm51tXT9IkinWQ2vrP5UL6gGqT3x7D7%2BmCsQzIVaKIr8dEoqwe3hrzB9IQQOAWgBWNTGxJhhJthJbqde0saABxApThkfYtRJVRWEjL56K3L%2FtAqt5RzqAstp3pA83qo6EjFgQVWD4jzgjwSQPx9SY%2BUcP069sgRHaBeyJSBkApU%2FJOR6hle%2BCWbnUBJHWSL%2BRpG0%2BXUdNu6frKTsKohoDLnASb7Lvedz28ix5RzdThtZuUFLAekoGxyW%2FtH6gvPwUuNCroK%2BQy6E0gPKu0FGiHeUzN8Esh8Ztf9%2Bhh7WtkDogZPURqTwxa7CN%2B8J%2FyLjnJ1Re4wl7fBxAY6pgGZggfLvaMg0lJ8%2BkH4eyZ%2BBJ94BNUs1A9YRJ%2BgSQA49TBm%2B%2F7c5ttPcUYczGj3kwP46Y67iCutQDLzJwvaU%2F%2FH8Oz1FwJfiYrHMc3uRO8j2OpeHSx0hFVuTf3WfmtVVdB1CSWMENS2bfkOjRLAQ6CIKNHFnKf2Bg3oxsffQYAti%2BODkOcsTHwOnJCcaA6EyfOSnS3%2B0Gszor3byT6YthggkpxiadOP&X-Amz-Signature=72a743300f6b898d25696baac65c7d5ba0d1cfb84287e6489b443edbacb4f10a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## ReplicaSet 생성

replication 보다 업그레이드되었고 metchExp를 추가하여 label 조건에 더 자유롭

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/e26579b4-01e4-429e-98f4-7aa4d0e3495d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UCV6VEAM%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T072047Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJGMEQCIFEFuQbjFT8xZsPxgdAK3mscGahb3DQ5uE1LhnqytHxHAiAhcDOEXy4ik2LjnzytLcg7fDwIQC4EYl9fvBN6R0tIqSr%2FAwhAEAAaDDYzNzQyMzE4MzgwNSIM1D9tDeiAuG%2BqbMsMKtwD31YH6eVmXAPx51U53H6nAoKUhrszwuFh%2FxZMQM8YlYFQxwOiykwQY7iF0towOd0SGT1QXWqpq%2FmCOdaWTXda4LtacXU8fFg1JebIHb2TLMzuJuuYJE%2FGIHCBpBYbcummnrRApY4fF%2Br0VEwFHu8R3yvDsnkO7CP%2BmQu4iI5cG6fjisZaAYQ7yjat4xhrGv12jxQ7FW8QiFEVq8kuB4uA6R6%2B34EljO9eUWtwuZZX7C%2BL1Miz230KbY38akAr3sEtBNh1vwxlOIDn9rCVuhuzYcJOfRfOWMeQbs%2BP2cXpmBCY98KMov7qJLm51tXT9IkinWQ2vrP5UL6gGqT3x7D7%2BmCsQzIVaKIr8dEoqwe3hrzB9IQQOAWgBWNTGxJhhJthJbqde0saABxApThkfYtRJVRWEjL56K3L%2FtAqt5RzqAstp3pA83qo6EjFgQVWD4jzgjwSQPx9SY%2BUcP069sgRHaBeyJSBkApU%2FJOR6hle%2BCWbnUBJHWSL%2BRpG0%2BXUdNu6frKTsKohoDLnASb7Lvedz28ix5RzdThtZuUFLAekoGxyW%2FtH6gvPwUuNCroK%2BQy6E0gPKu0FGiHeUzN8Esh8Ztf9%2Bhh7WtkDogZPURqTwxa7CN%2B8J%2FyLjnJ1Re4wl7fBxAY6pgGZggfLvaMg0lJ8%2BkH4eyZ%2BBJ94BNUs1A9YRJ%2BgSQA49TBm%2B%2F7c5ttPcUYczGj3kwP46Y67iCutQDLzJwvaU%2F%2FH8Oz1FwJfiYrHMc3uRO8j2OpeHSx0hFVuTf3WfmtVVdB1CSWMENS2bfkOjRLAQ6CIKNHFnKf2Bg3oxsffQYAti%2BODkOcsTHwOnJCcaA6EyfOSnS3%2B0Gszor3byT6YthggkpxiadOP&X-Amz-Signature=4cd37bc32809a007fd5de36e1dfce1cf464789a413be02a8ef8fa5e8530d8c10&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

# ReplicaSet 실습

- nginx 3개를 생성하는 rs-nginx 생성하라
- rs-nginx pod의 개수를 10개로 스케일링하라
### nginx 3개를 생성하는 rs-nginx 생성하라

```yaml
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: rs-nginx
spec:
  # modify replicas according to your case
  replicas: 3
  selector:
    matchLabels:
      app: replica
  template:
    metadata:
      labels:
        app: replica
    spec:
      containers:
      - name: rs-nginx
        image: nginx
```

```yaml
kubectl creat -f yaml이름
```

### rs-nginx pod의 개수를 10개로 스케일링하라

```yaml
kubectl edit rs rs이름
```

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/c60f5b28-6cbb-4a8f-914e-b940a64e304d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UCV6VEAM%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T072047Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJGMEQCIFEFuQbjFT8xZsPxgdAK3mscGahb3DQ5uE1LhnqytHxHAiAhcDOEXy4ik2LjnzytLcg7fDwIQC4EYl9fvBN6R0tIqSr%2FAwhAEAAaDDYzNzQyMzE4MzgwNSIM1D9tDeiAuG%2BqbMsMKtwD31YH6eVmXAPx51U53H6nAoKUhrszwuFh%2FxZMQM8YlYFQxwOiykwQY7iF0towOd0SGT1QXWqpq%2FmCOdaWTXda4LtacXU8fFg1JebIHb2TLMzuJuuYJE%2FGIHCBpBYbcummnrRApY4fF%2Br0VEwFHu8R3yvDsnkO7CP%2BmQu4iI5cG6fjisZaAYQ7yjat4xhrGv12jxQ7FW8QiFEVq8kuB4uA6R6%2B34EljO9eUWtwuZZX7C%2BL1Miz230KbY38akAr3sEtBNh1vwxlOIDn9rCVuhuzYcJOfRfOWMeQbs%2BP2cXpmBCY98KMov7qJLm51tXT9IkinWQ2vrP5UL6gGqT3x7D7%2BmCsQzIVaKIr8dEoqwe3hrzB9IQQOAWgBWNTGxJhhJthJbqde0saABxApThkfYtRJVRWEjL56K3L%2FtAqt5RzqAstp3pA83qo6EjFgQVWD4jzgjwSQPx9SY%2BUcP069sgRHaBeyJSBkApU%2FJOR6hle%2BCWbnUBJHWSL%2BRpG0%2BXUdNu6frKTsKohoDLnASb7Lvedz28ix5RzdThtZuUFLAekoGxyW%2FtH6gvPwUuNCroK%2BQy6E0gPKu0FGiHeUzN8Esh8Ztf9%2Bhh7WtkDogZPURqTwxa7CN%2B8J%2FyLjnJ1Re4wl7fBxAY6pgGZggfLvaMg0lJ8%2BkH4eyZ%2BBJ94BNUs1A9YRJ%2BgSQA49TBm%2B%2F7c5ttPcUYczGj3kwP46Y67iCutQDLzJwvaU%2F%2FH8Oz1FwJfiYrHMc3uRO8j2OpeHSx0hFVuTf3WfmtVVdB1CSWMENS2bfkOjRLAQ6CIKNHFnKf2Bg3oxsffQYAti%2BODkOcsTHwOnJCcaA6EyfOSnS3%2B0Gszor3byT6YthggkpxiadOP&X-Amz-Signature=245900836d927ead0bc3c0e5e1007acc3f760ee31070397c92bdd1b7576e2ef0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


