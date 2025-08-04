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
![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/9faef226-8b82-4d03-b75a-857efb7979b8/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VRY7QIVQ%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T072059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJGMEQCIHg2%2BCzk69XSAPxKkL%2FkAfRCOpZ568AEttaGxdlFKv2ZAiAyrpLQRVrJ8FadqIa4XdSTUJ7zFgcHET00bc%2FNFavySir%2FAwhAEAAaDDYzNzQyMzE4MzgwNSIMgE64G7BtqmJL%2ByGaKtwDkbNvmG7HCSAlJqPuyMjLRwssLMAa06sa0D3dg9SMWJQ8JzKeGXDImaor9vym17%2BBfwH%2Bt4VIH8XyrPT%2FQ%2FdB9aLN0owFOeauXR05vnz9%2B8tncCnBvsyqwP66hkZC5wmOXsUZHjiAwF47AaLCoLkB3lNc4AHqjtLMzgUT5yU6YOGXoM5GkSrz7Kr7oyrGgnsdlO5kQ4lHi8xUhGTkG0eSfH8U4M6b2%2Fd9w7UJG%2BIMysmf%2FVhEhPwA%2FhHJckg888SYZ91hvUo67TRVk1g6Pl8Mr84vIu8cFfqeo1hx%2BCUhTrfBSyaZCsQmaetsnay3nhScieaITS2TFaXW6G8ZO1CzT70RDq4jf9b94hX4E5NFbB4dV6clEdu02gXYS%2BUKjEkI2aLJMBdDNEm3i5lW%2BK4mscriNhMsOzcFRq1ShRc66FOwbm4a2iTgOOWdhMELqwDr5w07AFt7mODKHPQqKzfI77uV7r1xPdWBlR1pWSMVMdhBTns6ovjZASm0fpulaJs6i9hHQhcu1W0QLtY0ZXOd0xFxGi8p38B94NJyXB%2FGIhQ4UlwG6SeirUa4thh9zd0xKyni%2FCfO7QpdMykiVUSsGJ18QGyB1hzA%2FYDXCzmBQp5vVdOS25HqindZYMcw7LbBxAY6pgE8v1bPcU%2BZlx0jFo40hZfyIKTB%2FSLa8RFzt7EdbWidJIJUlppNnWL4RlKrzCup6ifbOLFU3UK3aJETGU932KGMgfbFEaUf1XEhunZqFvFFGfovuXeMLC9sGi5lLXLS6L0dOjF0wuiaKZrVxoSg2UUHOIwYLEbHGcsnkjrHFTxeR87DQiPX2nRY%2F4k1gu4BpuR1b3SWmpAOCVWxyCDBe0plAPf%2FVGYp&X-Amz-Signature=0706fcff4d8514a539398d2564872789589a43014ccf0de35a112a1732675ee9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/162bac64-5cd6-4c19-8588-644a8869155a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VRY7QIVQ%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T072059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJGMEQCIHg2%2BCzk69XSAPxKkL%2FkAfRCOpZ568AEttaGxdlFKv2ZAiAyrpLQRVrJ8FadqIa4XdSTUJ7zFgcHET00bc%2FNFavySir%2FAwhAEAAaDDYzNzQyMzE4MzgwNSIMgE64G7BtqmJL%2ByGaKtwDkbNvmG7HCSAlJqPuyMjLRwssLMAa06sa0D3dg9SMWJQ8JzKeGXDImaor9vym17%2BBfwH%2Bt4VIH8XyrPT%2FQ%2FdB9aLN0owFOeauXR05vnz9%2B8tncCnBvsyqwP66hkZC5wmOXsUZHjiAwF47AaLCoLkB3lNc4AHqjtLMzgUT5yU6YOGXoM5GkSrz7Kr7oyrGgnsdlO5kQ4lHi8xUhGTkG0eSfH8U4M6b2%2Fd9w7UJG%2BIMysmf%2FVhEhPwA%2FhHJckg888SYZ91hvUo67TRVk1g6Pl8Mr84vIu8cFfqeo1hx%2BCUhTrfBSyaZCsQmaetsnay3nhScieaITS2TFaXW6G8ZO1CzT70RDq4jf9b94hX4E5NFbB4dV6clEdu02gXYS%2BUKjEkI2aLJMBdDNEm3i5lW%2BK4mscriNhMsOzcFRq1ShRc66FOwbm4a2iTgOOWdhMELqwDr5w07AFt7mODKHPQqKzfI77uV7r1xPdWBlR1pWSMVMdhBTns6ovjZASm0fpulaJs6i9hHQhcu1W0QLtY0ZXOd0xFxGi8p38B94NJyXB%2FGIhQ4UlwG6SeirUa4thh9zd0xKyni%2FCfO7QpdMykiVUSsGJ18QGyB1hzA%2FYDXCzmBQp5vVdOS25HqindZYMcw7LbBxAY6pgE8v1bPcU%2BZlx0jFo40hZfyIKTB%2FSLa8RFzt7EdbWidJIJUlppNnWL4RlKrzCup6ifbOLFU3UK3aJETGU932KGMgfbFEaUf1XEhunZqFvFFGfovuXeMLC9sGi5lLXLS6L0dOjF0wuiaKZrVxoSg2UUHOIwYLEbHGcsnkjrHFTxeR87DQiPX2nRY%2F4k1gu4BpuR1b3SWmpAOCVWxyCDBe0plAPf%2FVGYp&X-Amz-Signature=5758abad72f45e1147246b5728a0a21222eac51dcdf8b9131e170a1b103a825c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


