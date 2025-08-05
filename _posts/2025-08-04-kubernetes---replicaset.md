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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/35742fe6-0f6d-41c3-a55c-0af6e8de2e29/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663VQVAQ33%2F20250805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250805T061031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJGMEQCIA8TikgeW9Ad%2FCNEtcHSYioRp28MRFwGOFKODLhJwy3BAiBRG35IPZNes4sSfeicOEhLvnlyLN3wnF5RE55l5OzUcCr%2FAwhXEAAaDDYzNzQyMzE4MzgwNSIMxHi3Ew7O6jS9f%2BgFKtwDv7o4zad2SVf3Pa%2Fqle6ROPmtRp7gRf9dLDRkGr2IX1Ik9cRHyju3RJnlLLZtBpOkbX%2Ba%2Bye7U3fIwCXKoRU25PK8njh4zWl6iFEyFQotQ5gefU0k3st9zApfqi7As2ucm6eC7vFWiuqJzzQEFGkwvXgE1nDgdu1IUe7%2BiipB0kcRx0Z7xpnTIVuoUQ1unA2MsT4bvjGXd3FxLXOvJcc7t4lFnGPNAE6YBYz4O7Iu5w%2F5hiD4V24ISz9pPKxS604mfcMM7WYllLqIxI7u5on1oOP1rrFRSuctEXSMURJPd0T5hYDrc4p7g%2BFy9I%2BsBRlllV5PrSS6iLyy7%2BE2OM%2Bl7j%2FuhT0SC3WnLI%2FZkQgXXaI7QZ28jMGz8v3V4Z0gm7hToVwdqMGpfOaxzWfMjuQ%2Bi7BRpXpHkv%2B6uNASXGSl8MKjceGlmeUokzNgIXD4ptzCgcExEuxai%2FrsGcuKT05CirSei5B9VnVtfYXWBgY%2F66jUh7orWc6lVl61GKoaD7V7h2W1YhsjptbTAT5J0KkG4r%2BRTO7oCuQUZDhgOAfXa8K%2BDQaz6nNgh3l21WnrhhMgE3PYsj7n3MLT62u2FyirEUMkVcRhSskN%2FDIy1YL1sxjy2r4jF8I6UId2eyowl7TGxAY6pgFa%2By0YlDy2%2BPjZhs%2Bo6FBdrb0vPj9LZUqDQASYvp0AruBho6ptLr3AYgq836JyI3Kfh6k2bvYAf9BQNm9lQCiIYS%2FaaTf1DqjAouAHzbLdUrsNAkbc7NQjTMYrK0CztTfBn5DJMwbfVZBOyA4n37MAGtp99IWOP6tcbvuZrf7LzUrCs0r03wnrAjpPUq4gZB6emW2lJ8qwr7ObyhrL0vk3H7SowZj8&X-Amz-Signature=0ea688173cda52a6e22f5636929beaa907a40e81b2901ec02d8fc96815d5e742&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## ReplicaSet 생성

replication 보다 업그레이드되었고 metchExp를 추가하여 label 조건에 더 자유롭

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/e26579b4-01e4-429e-98f4-7aa4d0e3495d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663VQVAQ33%2F20250805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250805T061031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJGMEQCIA8TikgeW9Ad%2FCNEtcHSYioRp28MRFwGOFKODLhJwy3BAiBRG35IPZNes4sSfeicOEhLvnlyLN3wnF5RE55l5OzUcCr%2FAwhXEAAaDDYzNzQyMzE4MzgwNSIMxHi3Ew7O6jS9f%2BgFKtwDv7o4zad2SVf3Pa%2Fqle6ROPmtRp7gRf9dLDRkGr2IX1Ik9cRHyju3RJnlLLZtBpOkbX%2Ba%2Bye7U3fIwCXKoRU25PK8njh4zWl6iFEyFQotQ5gefU0k3st9zApfqi7As2ucm6eC7vFWiuqJzzQEFGkwvXgE1nDgdu1IUe7%2BiipB0kcRx0Z7xpnTIVuoUQ1unA2MsT4bvjGXd3FxLXOvJcc7t4lFnGPNAE6YBYz4O7Iu5w%2F5hiD4V24ISz9pPKxS604mfcMM7WYllLqIxI7u5on1oOP1rrFRSuctEXSMURJPd0T5hYDrc4p7g%2BFy9I%2BsBRlllV5PrSS6iLyy7%2BE2OM%2Bl7j%2FuhT0SC3WnLI%2FZkQgXXaI7QZ28jMGz8v3V4Z0gm7hToVwdqMGpfOaxzWfMjuQ%2Bi7BRpXpHkv%2B6uNASXGSl8MKjceGlmeUokzNgIXD4ptzCgcExEuxai%2FrsGcuKT05CirSei5B9VnVtfYXWBgY%2F66jUh7orWc6lVl61GKoaD7V7h2W1YhsjptbTAT5J0KkG4r%2BRTO7oCuQUZDhgOAfXa8K%2BDQaz6nNgh3l21WnrhhMgE3PYsj7n3MLT62u2FyirEUMkVcRhSskN%2FDIy1YL1sxjy2r4jF8I6UId2eyowl7TGxAY6pgFa%2By0YlDy2%2BPjZhs%2Bo6FBdrb0vPj9LZUqDQASYvp0AruBho6ptLr3AYgq836JyI3Kfh6k2bvYAf9BQNm9lQCiIYS%2FaaTf1DqjAouAHzbLdUrsNAkbc7NQjTMYrK0CztTfBn5DJMwbfVZBOyA4n37MAGtp99IWOP6tcbvuZrf7LzUrCs0r03wnrAjpPUq4gZB6emW2lJ8qwr7ObyhrL0vk3H7SowZj8&X-Amz-Signature=9973cd83a78c7fdb35371992b836939037c30a720623c285aaa42f4c516bf3c3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/c60f5b28-6cbb-4a8f-914e-b940a64e304d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663VQVAQ33%2F20250805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250805T061031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJGMEQCIA8TikgeW9Ad%2FCNEtcHSYioRp28MRFwGOFKODLhJwy3BAiBRG35IPZNes4sSfeicOEhLvnlyLN3wnF5RE55l5OzUcCr%2FAwhXEAAaDDYzNzQyMzE4MzgwNSIMxHi3Ew7O6jS9f%2BgFKtwDv7o4zad2SVf3Pa%2Fqle6ROPmtRp7gRf9dLDRkGr2IX1Ik9cRHyju3RJnlLLZtBpOkbX%2Ba%2Bye7U3fIwCXKoRU25PK8njh4zWl6iFEyFQotQ5gefU0k3st9zApfqi7As2ucm6eC7vFWiuqJzzQEFGkwvXgE1nDgdu1IUe7%2BiipB0kcRx0Z7xpnTIVuoUQ1unA2MsT4bvjGXd3FxLXOvJcc7t4lFnGPNAE6YBYz4O7Iu5w%2F5hiD4V24ISz9pPKxS604mfcMM7WYllLqIxI7u5on1oOP1rrFRSuctEXSMURJPd0T5hYDrc4p7g%2BFy9I%2BsBRlllV5PrSS6iLyy7%2BE2OM%2Bl7j%2FuhT0SC3WnLI%2FZkQgXXaI7QZ28jMGz8v3V4Z0gm7hToVwdqMGpfOaxzWfMjuQ%2Bi7BRpXpHkv%2B6uNASXGSl8MKjceGlmeUokzNgIXD4ptzCgcExEuxai%2FrsGcuKT05CirSei5B9VnVtfYXWBgY%2F66jUh7orWc6lVl61GKoaD7V7h2W1YhsjptbTAT5J0KkG4r%2BRTO7oCuQUZDhgOAfXa8K%2BDQaz6nNgh3l21WnrhhMgE3PYsj7n3MLT62u2FyirEUMkVcRhSskN%2FDIy1YL1sxjy2r4jF8I6UId2eyowl7TGxAY6pgFa%2By0YlDy2%2BPjZhs%2Bo6FBdrb0vPj9LZUqDQASYvp0AruBho6ptLr3AYgq836JyI3Kfh6k2bvYAf9BQNm9lQCiIYS%2FaaTf1DqjAouAHzbLdUrsNAkbc7NQjTMYrK0CztTfBn5DJMwbfVZBOyA4n37MAGtp99IWOP6tcbvuZrf7LzUrCs0r03wnrAjpPUq4gZB6emW2lJ8qwr7ObyhrL0vk3H7SowZj8&X-Amz-Signature=3d6482e234ca3ea5a839c14ccbf9510c11455953696823151c5472b6960a807b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


