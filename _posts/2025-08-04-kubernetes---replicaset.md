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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/35742fe6-0f6d-41c3-a55c-0af6e8de2e29/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W7EQ7BBN%2F20250805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250805T002738Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJHMEUCIBCc59ec1v6evdwSXR%2BMyCcAIE%2Ftcbqpfu%2FRLpMyKX77AiEA9W1353WwtB6cwAuq2w8ueh20UPNhqzYg6EcOz5WLgwAq%2FwMIUBAAGgw2Mzc0MjMxODM4MDUiDNQ8q6ImYDu%2FcW9yWCrcA4F0fmBPkkn%2B4tc5KxBY7LbsFBISCQJcK2sxJg0dutWcinum9wQc%2F4TDCN827SP4UTkMHpz1ZTKl2rVUGJVDQ7xrWSI9HZL6PBzst6JFirRV2L1Ly1ifwhIkdtViqgxbjMLBe%2F%2B8agfSWH4R%2FJlcaVbN6yIx1Dic1sWtyXrtYNzHe58HtMHtVm7trOQNeO%2F1hhIDH2IepIZ4b3eu69huPkwibAb674bSJnua3M%2B6CqyirEEW5AEgt%2FpZokJaP8ZdOMplPVpD8DnJAg2G68ysUigZ4Bal8BoSZGLajQMk%2FRxZwWqlabUuiq54fDqW15qwrVFHd%2FSY9dxXbU4tjanp%2B0hTK0bTMJ33b392pVaQsbph4ZdL0wF3mK%2BOtEGUvv5P6leyevzJJu3g2ahSweX%2FkmPvIMaiWl%2BQCMrXwwAVOXdU6Il%2Br1pmPyCBUc1yTcV3F1K96EBYN03fpqbB3dzJW8X3g0%2BrKurx%2B6Oul2CzZFXFAQ%2Fk%2BnK45A9f3NsZ60aE1qKRypybuL92%2B4hQLDFN1GMhSEubFZvqhmwFXezN1anaXOK7LfH4WyR%2BtzLcxpvC6gzXV3vtsMwQIwVMNTUgXbx7V2UjNanpSERTqSnXbxAqXpU6%2BDGh0hEzNGfzMPH0xMQGOqUB9I065OGJs%2BbdlYkoEwhxSp63ktgJFNplEFYayT8LSigQWPfEhRCgq5O18%2FN65Y9TwjIAbU9AD5164MWvMkruc3iy56HH%2BGtiCyMtlJ%2BlQp9l3LN%2BqxJOn3kqRhtQoZAqqAi7mZp%2FCfVpBYUGpaJVf9g%2FVwrZBu5jWW7NZj0gQEiJjKyFK%2BqisLHftDlApCbWoNnhd%2FbtNxnmDgTqINfmEKh%2BOyyo&X-Amz-Signature=1939731cdfcb9540178badc3c6ed461351950b23ee458d3782dabbd8a0499911&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## ReplicaSet 생성

replication 보다 업그레이드되었고 metchExp를 추가하여 label 조건에 더 자유롭

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/e26579b4-01e4-429e-98f4-7aa4d0e3495d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W7EQ7BBN%2F20250805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250805T002738Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJHMEUCIBCc59ec1v6evdwSXR%2BMyCcAIE%2Ftcbqpfu%2FRLpMyKX77AiEA9W1353WwtB6cwAuq2w8ueh20UPNhqzYg6EcOz5WLgwAq%2FwMIUBAAGgw2Mzc0MjMxODM4MDUiDNQ8q6ImYDu%2FcW9yWCrcA4F0fmBPkkn%2B4tc5KxBY7LbsFBISCQJcK2sxJg0dutWcinum9wQc%2F4TDCN827SP4UTkMHpz1ZTKl2rVUGJVDQ7xrWSI9HZL6PBzst6JFirRV2L1Ly1ifwhIkdtViqgxbjMLBe%2F%2B8agfSWH4R%2FJlcaVbN6yIx1Dic1sWtyXrtYNzHe58HtMHtVm7trOQNeO%2F1hhIDH2IepIZ4b3eu69huPkwibAb674bSJnua3M%2B6CqyirEEW5AEgt%2FpZokJaP8ZdOMplPVpD8DnJAg2G68ysUigZ4Bal8BoSZGLajQMk%2FRxZwWqlabUuiq54fDqW15qwrVFHd%2FSY9dxXbU4tjanp%2B0hTK0bTMJ33b392pVaQsbph4ZdL0wF3mK%2BOtEGUvv5P6leyevzJJu3g2ahSweX%2FkmPvIMaiWl%2BQCMrXwwAVOXdU6Il%2Br1pmPyCBUc1yTcV3F1K96EBYN03fpqbB3dzJW8X3g0%2BrKurx%2B6Oul2CzZFXFAQ%2Fk%2BnK45A9f3NsZ60aE1qKRypybuL92%2B4hQLDFN1GMhSEubFZvqhmwFXezN1anaXOK7LfH4WyR%2BtzLcxpvC6gzXV3vtsMwQIwVMNTUgXbx7V2UjNanpSERTqSnXbxAqXpU6%2BDGh0hEzNGfzMPH0xMQGOqUB9I065OGJs%2BbdlYkoEwhxSp63ktgJFNplEFYayT8LSigQWPfEhRCgq5O18%2FN65Y9TwjIAbU9AD5164MWvMkruc3iy56HH%2BGtiCyMtlJ%2BlQp9l3LN%2BqxJOn3kqRhtQoZAqqAi7mZp%2FCfVpBYUGpaJVf9g%2FVwrZBu5jWW7NZj0gQEiJjKyFK%2BqisLHftDlApCbWoNnhd%2FbtNxnmDgTqINfmEKh%2BOyyo&X-Amz-Signature=0637e3ec231fec7c9e8b293355fd4d0f63cf69451897617f9b4d10edd361d9ee&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/c60f5b28-6cbb-4a8f-914e-b940a64e304d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W7EQ7BBN%2F20250805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250805T002738Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJHMEUCIBCc59ec1v6evdwSXR%2BMyCcAIE%2Ftcbqpfu%2FRLpMyKX77AiEA9W1353WwtB6cwAuq2w8ueh20UPNhqzYg6EcOz5WLgwAq%2FwMIUBAAGgw2Mzc0MjMxODM4MDUiDNQ8q6ImYDu%2FcW9yWCrcA4F0fmBPkkn%2B4tc5KxBY7LbsFBISCQJcK2sxJg0dutWcinum9wQc%2F4TDCN827SP4UTkMHpz1ZTKl2rVUGJVDQ7xrWSI9HZL6PBzst6JFirRV2L1Ly1ifwhIkdtViqgxbjMLBe%2F%2B8agfSWH4R%2FJlcaVbN6yIx1Dic1sWtyXrtYNzHe58HtMHtVm7trOQNeO%2F1hhIDH2IepIZ4b3eu69huPkwibAb674bSJnua3M%2B6CqyirEEW5AEgt%2FpZokJaP8ZdOMplPVpD8DnJAg2G68ysUigZ4Bal8BoSZGLajQMk%2FRxZwWqlabUuiq54fDqW15qwrVFHd%2FSY9dxXbU4tjanp%2B0hTK0bTMJ33b392pVaQsbph4ZdL0wF3mK%2BOtEGUvv5P6leyevzJJu3g2ahSweX%2FkmPvIMaiWl%2BQCMrXwwAVOXdU6Il%2Br1pmPyCBUc1yTcV3F1K96EBYN03fpqbB3dzJW8X3g0%2BrKurx%2B6Oul2CzZFXFAQ%2Fk%2BnK45A9f3NsZ60aE1qKRypybuL92%2B4hQLDFN1GMhSEubFZvqhmwFXezN1anaXOK7LfH4WyR%2BtzLcxpvC6gzXV3vtsMwQIwVMNTUgXbx7V2UjNanpSERTqSnXbxAqXpU6%2BDGh0hEzNGfzMPH0xMQGOqUB9I065OGJs%2BbdlYkoEwhxSp63ktgJFNplEFYayT8LSigQWPfEhRCgq5O18%2FN65Y9TwjIAbU9AD5164MWvMkruc3iy56HH%2BGtiCyMtlJ%2BlQp9l3LN%2BqxJOn3kqRhtQoZAqqAi7mZp%2FCfVpBYUGpaJVf9g%2FVwrZBu5jWW7NZj0gQEiJjKyFK%2BqisLHftDlApCbWoNnhd%2FbtNxnmDgTqINfmEKh%2BOyyo&X-Amz-Signature=1b82683391a676f957d6ca4d66eb978594ab02fc27fe32ceff750cbe15be3296&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


