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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/7c11461c-1127-4433-ab12-5e84b3fcecaf/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZIF2TMPF%2F20250805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250805T061132Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQC4f2vWYLDgcUzecJzkNGztq1F1HEimJ6S2rZlKkXublAIhAP1MWFW%2FF5kRkfoqD0ZTCp%2Ftt7z4CYuZ6tvKJRoQvTiBKv8DCFcQABoMNjM3NDIzMTgzODA1IgzidlL%2BzNFyJB8Y3Jkq3AMPHHRbNhJ928r5eIjGLsjerb%2BLO63lTGSjcyVaC%2BGGT5YIXZ6Kdok%2FPwO0nP4IWJv0nuGdY0BGfiCJvTzJ%2BuiN4%2FHDTgoO%2BLhu%2Bnz%2F%2BQEQ4Uu6Ed%2B2CibgZ0IgEfAt7ERsnOzp9Jy202tbDFX%2BaX3qGydq%2BDQnMr78xNBGBn7hbu%2B5oR5oxjMkXA%2FMqSCbYdkar25M0%2FHbCzHPVUg6YF%2BRltXvb4LgLGOCFc5%2FAjnEuR9Q8Rz2zGN%2Bnhk6m0BgphzOZcrdDrO7nL7O2eVLiKhbln1vkBnAm5hduaMSMs7Yns7G%2BWTIrexoRAtHjcneIl9E9BA%2FetdUQSp1qRELZCrabVUEq2pEkzBbY4sINiNwx8i7Ge1Ajb%2Bbh0HpZOm0VxE%2BPWh64VJAJ6obMdyM9QC16wS9J7Ms%2BOzPYdRgy8Izuu2QV7hu7LoNVffi2ed62PWQWjmBqQam%2FtZCW%2BcJD%2FnFb0LAkwt3eg84Hldv9rV01WIwy4NtCAxSAbo5G9Fo5aeFhFPOC854sK0YPtkbxvnfKUvRvu7QCQyWB3jww7M46CfRptWJLIBpCJQBmCT29Rz5gAAeTcbRtT26E2Q5gaBsoKIzQLRoAtEpv%2F3ndTQDJhDI39G9772M%2FWVQSDCWs8bEBjqkAUdRG8oGFfwETeKpDhMxTNWD5iHymsY%2Fw%2FC8yCZAhxre8PGTV6MBLH5b0YK9WFbLVQ8ZUED%2BTmAKp0iTMEFqbDaO4YiygXYUxEdCEjJy%2BqisZQDfiiMlokTfYLBGtJzTQYyTbcYgzFMvj1RMOq%2FglZyBwJalwlZ4hTUri0ofFYRaBMp7bIIkGb2zq1RvL1JijdnaK14xqceZGagz5m6g%2BNyd6tdc&X-Amz-Signature=552d4c4a1241a265af3e330918eca9c1a86886ba8e41162f6864fcdea5bcec59&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

# NameSpace 연습문제

- 현재 시스템에는 몇 개의 Namespace가 존재하는가?
- Kube-system에는 몇 개의 포드가 존재하는가?
- ns-jenkins 네임스페이스를 생성하고 jenkins포드를 배치하라
- coredns 는 어는 네임스페이스에 속해있는가?

