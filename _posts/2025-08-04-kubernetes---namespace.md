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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/7c11461c-1127-4433-ab12-5e84b3fcecaf/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665GHYNYTF%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T072311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIC1OVYKearvSTkiIanade%2Fp0qd5cmaTvwte7iGVtm94sAiEAkwAIAWJx48bkieOTQOKPSuHdVicZlvTXx9TKGqynZk0q%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDDnIfZP6rO%2FueYyX6SrcA6ciVZTeElv0w6EFuxNkmCLneUTqbT1eWTH6mMb2gXa2SNxOhmfqpE4yOixj23X5tiJqCrBhc43rlz1ubp1w4LB7TQLU3n5dQq0FZk1VEec2PZozFWd6mu2c8Qy8N3oSLjylfqQoUu%2FAnlb5MIVMd1L6qJ0SjiN1P66UZ6ZKbzTaW%2Fkc3uDwwrrum2cZn8L1rskRFyPOUICrgHhFs0XQ2wh0Crd6BILBs5T7IVNKd3RQV%2BC%2BNM6KbV%2BUD1r6eMAzPL4QLuvYKJdqHQN9Xl7%2FVhFjx7m4PJ%2F8e1OJWEEVeCyLgFYePedqMPVtHvS0StPbBf4ssdmyoekReFcgnXBU23I%2FizZsS42NjBLTSPtYqR3JJcegAFlvYd%2FyY%2F%2BP6nb65qG4TTh16xbq%2F4H9TzbQbsVdTTFO10p9lZpNr5HXhArXUQb5gcYrKgLfY9J3t3YJFRFSNcmVZswxLC7yjJL%2F3PKHIDMQId5upn3tZoRL4bpNkbeX8idmqQZvv7hy8OR%2F%2Fuekdt%2BevKWod0LhngpHu9wuci0%2BLplgmuxL2Hv7PYooFKwGAczNsRxx7z%2BVyD3YIqRjt6%2B5Jwfqv1dcZ8cb8gZp3QJ5%2BMYInTCBBwjnDujTTHQ9Y1BRhPhj3sCLMMe2wcQGOqUBQzSjtjJ8U5twyVwaWL7TYa0nk5wC21H7nhFI6bXdgcd8NCVSGxcLejtD8QuqBGTc3z56rpbQ16AB76Doq0Bs40afTmHUWFBGWgEYnMZ%2BE1TeE22iOEkHQE7HvR3lfeTGV1Ore4ZkRulcr%2FAAlubNWNmgBHUaJ8kRZcjzKhx72H%2FtdRsASthmKXcaqsWYiQCnl1%2FSSMWmaLdyzIaexQ0p24K4x5XY&X-Amz-Signature=0d665550ce51305c2e662079c1c48023fec3cce78e90bae5d4126580d08b7d25&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

# NameSpace 연습문제

- 현재 시스템에는 몇 개의 Namespace가 존재하는가?
- Kube-system에는 몇 개의 포드가 존재하는가?
- ns-jenkins 네임스페이스를 생성하고 jenkins포드를 배치하라
- coredns 는 어는 네임스페이스에 속해있는가?

