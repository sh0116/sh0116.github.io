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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/35742fe6-0f6d-41c3-a55c-0af6e8de2e29/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TMKL572A%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T071438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJIMEYCIQD8G62SWTgmv%2FK9NTcrmDTTwdD8Cg8d6Bdu7OmXRxPHdAIhALEM%2B%2BtMmGD8Ip3f30lhwa5MqDrTay9CYGDZ%2BDjfL%2FuxKv8DCEAQABoMNjM3NDIzMTgzODA1IgwdQwslOjburjTvi9gq3AOLUFRfsmlYbzYnNQtSlLBUKdAUYu4QecbQmV4d%2FGURXg%2BP3JlpeGKA0yggctRbEtj9xfiCS7az6Xy0vsE1Cn0Evfldau%2F1FMzOSWa2C66QZCtXwG65vShmxGeakvgMcqi8RkKrlVS3KoDc8qbqviiBPskuVWvvC0ASTk%2FMrHI%2FMw8T1lQIZRKHAlkPm9oTUW%2BlfG5bJVGDdGEIEql%2BWP%2BkU%2Fhmw86jd%2FgkwG3ACGnAUdn44eW1OxUdT45atfLSzP5uAFdR9V0hyP5zh%2B3lsNW%2BlRuDBhtrsxpfQ1rzQMxmPd9eQC7yyxJlTqPgiteOjb2Q69%2BxvO2NgI7Bu6hNADGH5IqEAJTlXSuIJiLlrh599I%2BwmfWQ0DqQ%2BrnbaDBmr2Ox7whKCAiVQ3xPf43gqco2s9ILQcpzrFphGcV6mSivLMZNer8ywfWD8gtod2AM5ai%2BmKUAMKRrnd8lriGA6sH92SUNEmtbfCGnls8BUwzCtLAQNkndR015e9P%2Btn%2BmC3AYwWspu%2Bh8mdCLr7b6xGvwR5vlQOzh%2BJ1kBXvuv8YifZjLQMlrUlt2h2qSUb4M32KK%2FD%2BCKI3eiOEth%2FWOEwQj3Py4kyXXgsu6zecj9XmhyunnCNq7%2FkboL5I7ETD%2Ft8HEBjqkAdWzy%2B7usRD%2FctG79Ylcqdd0f0zcnjlpyM6aLDeXhlGyt4pOopSwJqCqohUrYpWgDtvfjTNIk8qsuR6l%2BjRlM98dnbYSIhWB6ocj3Ua6%2BeuyUrdYlC4Q4TQ20xZjjjt93yP15wc21BLKDaesGbB5Lj3usecbTIAor3AqXbaIqbSrF6Gq2xmRvscq8eucYpCw4xCsYv8G3IEyROzIhZMiNGZdO3tk&X-Amz-Signature=327cedd40a1e602ab7874f0bc7a0ff550060648ce4280ba924e215585c96476a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## ReplicaSet 생성

replication 보다 업그레이드되었고 metchExp를 추가하여 label 조건에 더 자유롭

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/e26579b4-01e4-429e-98f4-7aa4d0e3495d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TMKL572A%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T071438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJIMEYCIQD8G62SWTgmv%2FK9NTcrmDTTwdD8Cg8d6Bdu7OmXRxPHdAIhALEM%2B%2BtMmGD8Ip3f30lhwa5MqDrTay9CYGDZ%2BDjfL%2FuxKv8DCEAQABoMNjM3NDIzMTgzODA1IgwdQwslOjburjTvi9gq3AOLUFRfsmlYbzYnNQtSlLBUKdAUYu4QecbQmV4d%2FGURXg%2BP3JlpeGKA0yggctRbEtj9xfiCS7az6Xy0vsE1Cn0Evfldau%2F1FMzOSWa2C66QZCtXwG65vShmxGeakvgMcqi8RkKrlVS3KoDc8qbqviiBPskuVWvvC0ASTk%2FMrHI%2FMw8T1lQIZRKHAlkPm9oTUW%2BlfG5bJVGDdGEIEql%2BWP%2BkU%2Fhmw86jd%2FgkwG3ACGnAUdn44eW1OxUdT45atfLSzP5uAFdR9V0hyP5zh%2B3lsNW%2BlRuDBhtrsxpfQ1rzQMxmPd9eQC7yyxJlTqPgiteOjb2Q69%2BxvO2NgI7Bu6hNADGH5IqEAJTlXSuIJiLlrh599I%2BwmfWQ0DqQ%2BrnbaDBmr2Ox7whKCAiVQ3xPf43gqco2s9ILQcpzrFphGcV6mSivLMZNer8ywfWD8gtod2AM5ai%2BmKUAMKRrnd8lriGA6sH92SUNEmtbfCGnls8BUwzCtLAQNkndR015e9P%2Btn%2BmC3AYwWspu%2Bh8mdCLr7b6xGvwR5vlQOzh%2BJ1kBXvuv8YifZjLQMlrUlt2h2qSUb4M32KK%2FD%2BCKI3eiOEth%2FWOEwQj3Py4kyXXgsu6zecj9XmhyunnCNq7%2FkboL5I7ETD%2Ft8HEBjqkAdWzy%2B7usRD%2FctG79Ylcqdd0f0zcnjlpyM6aLDeXhlGyt4pOopSwJqCqohUrYpWgDtvfjTNIk8qsuR6l%2BjRlM98dnbYSIhWB6ocj3Ua6%2BeuyUrdYlC4Q4TQ20xZjjjt93yP15wc21BLKDaesGbB5Lj3usecbTIAor3AqXbaIqbSrF6Gq2xmRvscq8eucYpCw4xCsYv8G3IEyROzIhZMiNGZdO3tk&X-Amz-Signature=18c52464eed8447b1c469dcc5740a7ee28a2aafa78d8a9ad13e73a6617b08b17&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/c60f5b28-6cbb-4a8f-914e-b940a64e304d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TMKL572A%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T071438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJIMEYCIQD8G62SWTgmv%2FK9NTcrmDTTwdD8Cg8d6Bdu7OmXRxPHdAIhALEM%2B%2BtMmGD8Ip3f30lhwa5MqDrTay9CYGDZ%2BDjfL%2FuxKv8DCEAQABoMNjM3NDIzMTgzODA1IgwdQwslOjburjTvi9gq3AOLUFRfsmlYbzYnNQtSlLBUKdAUYu4QecbQmV4d%2FGURXg%2BP3JlpeGKA0yggctRbEtj9xfiCS7az6Xy0vsE1Cn0Evfldau%2F1FMzOSWa2C66QZCtXwG65vShmxGeakvgMcqi8RkKrlVS3KoDc8qbqviiBPskuVWvvC0ASTk%2FMrHI%2FMw8T1lQIZRKHAlkPm9oTUW%2BlfG5bJVGDdGEIEql%2BWP%2BkU%2Fhmw86jd%2FgkwG3ACGnAUdn44eW1OxUdT45atfLSzP5uAFdR9V0hyP5zh%2B3lsNW%2BlRuDBhtrsxpfQ1rzQMxmPd9eQC7yyxJlTqPgiteOjb2Q69%2BxvO2NgI7Bu6hNADGH5IqEAJTlXSuIJiLlrh599I%2BwmfWQ0DqQ%2BrnbaDBmr2Ox7whKCAiVQ3xPf43gqco2s9ILQcpzrFphGcV6mSivLMZNer8ywfWD8gtod2AM5ai%2BmKUAMKRrnd8lriGA6sH92SUNEmtbfCGnls8BUwzCtLAQNkndR015e9P%2Btn%2BmC3AYwWspu%2Bh8mdCLr7b6xGvwR5vlQOzh%2BJ1kBXvuv8YifZjLQMlrUlt2h2qSUb4M32KK%2FD%2BCKI3eiOEth%2FWOEwQj3Py4kyXXgsu6zecj9XmhyunnCNq7%2FkboL5I7ETD%2Ft8HEBjqkAdWzy%2B7usRD%2FctG79Ylcqdd0f0zcnjlpyM6aLDeXhlGyt4pOopSwJqCqohUrYpWgDtvfjTNIk8qsuR6l%2BjRlM98dnbYSIhWB6ocj3Ua6%2BeuyUrdYlC4Q4TQ20xZjjjt93yP15wc21BLKDaesGbB5Lj3usecbTIAor3AqXbaIqbSrF6Gq2xmRvscq8eucYpCw4xCsYv8G3IEyROzIhZMiNGZdO3tk&X-Amz-Signature=7ed6248dc6d093e6bc2ae96c95e8b3e5e58f021966a386ac71c6338e588915a0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


