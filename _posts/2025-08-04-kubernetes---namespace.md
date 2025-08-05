---
title: "Kubernetes - NameSpace"
date: 2025-08-04 06:05:00 +0900
categories: [kubernetes]
tags: [Kubernetes]
description: Kubernetes 기초
toc: true
comments: true
---

# NameSpace

- 리소스를 각각의 분리된 영역으로 나누기 좋은 방법
- 여러 네임스페이스를 사용하면 복잡한 쿠버네티스 시스템을 더 작은 그룹으로 분할
- 멀티 테넌트(multi-tenant) 환경을 분리하여 리소스를 생산, 개발, QA환경 등으로 사용
- 리소스 이름은 네임스페이스 내에서만 고유 명칭 사용
```yaml
kubectl get namespace
kubectl get ns
```

# Namespace 생성

```yaml
kubectl create ns ns이름 --dry-run -o yaml > yaml파일 이름
# yaml수정 
kubectl create -f yaml파일 이름
```

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/7c11461c-1127-4433-ab12-5e84b3fcecaf/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VLLXHVRC%2F20250805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250805T002844Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJIMEYCIQDfibpUoI1Wso0xE1Oumr20OH7T6W%2FRFTaccRzK3%2B6vHgIhAM%2FTsYMNu5ytwTT5JHTi75ju9ptdBspQ9dreGNRN0mJoKv8DCFAQABoMNjM3NDIzMTgzODA1Igzqam6Lf28DE8%2FAcEsq3AP2Bkos%2FNOhAHXvDgEhCtrJM1fkHrKdTXrguD9%2FUFekWnisTm1oKPFCeTQzPOdUzypzCjbMIGbHLaWf%2FxwgNPJMRedE%2B8lcJINmAiOsxnEGB3uY3AKhr6oF3ey4sFpVyTrdLeDbHNIx8I9NGtegSIMii3ejYYvdqNrfmNZ%2FMJMmNVk9lD02uWUa%2F6ei5%2FOupu1YWjFE%2BrvVNKVQVshC7h9PI3CThErdFSrdfhLPjFgwSYLBC%2FZewZ6e3h3z7v2FyBRSXcetSshJD4W2BoRGZjKZcj0ZVVkb2ygDAu9wqPdT3bl%2FEH3VtxaJi65%2Bv2KM%2Fw%2FRFKjJxIxtt5w4aMLE%2B5LIy2Y8CbAc6OzY%2B6fDkQwvrgBUhNr62YYeM0tS8HqYfRa27F4coXkS68O4AfE0L2lLOsduCSgFJm8%2FoIIceLcHtWtomRI5t9XVXEJfO1jU48GU80aaVydr8Ip7269tt39BeMwdN4NTTMb%2BsdQFaKhEsLG1v5ERcpR6nKoltgu8D%2BuQS4YyCI6QlotDTn4%2BSyF7IZl7j8QRJpPWKaRJ2oGK6rM0kRUlwB06WNGGNjN7HO%2Brmcw7ManRVwQvLu5iBULo6KedyukRrLbtAnR9uJ9u6SgGD5a9WO93zAYaCjCX9MTEBjqkASxW1m9xRRmBAe3lqOpIyTkJKJLH9u4yAksYuKSGO6m3xkejJ%2FC%2F8SPGUvCq327k%2BWV6lZefK9gE59Vh36oIWWY2BzGLjtASiTErpHS8q%2FMfOpSDVuzl6c27i08585reI4wZK7G1x5PnI%2FgJp8%2FGgTXEQWL5G%2FyJSX5G3B5MLfXuzR26XighbOf9Eyn0ANe8qT0UAXUZrx7IGjSBfYSIUMnINPXV&X-Amz-Signature=00cfb9f1ccd5c0a3ec53984bca7363b55f7b9b10bda16350fba2cfad5ec36726&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

# NameSpace 연습문제

- 현재 시스템에는 몇 개의 Namespace가 존재하는가?
- Kube-system에는 몇 개의 포드가 존재하는가?
- ns-jenkins 네임스페이스를 생성하고 jenkins포드를 배치하라
- coredns 는 어는 네임스페이스에 속해있는가?

