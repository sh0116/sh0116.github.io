---
title: "Kubernetes - rook-ceph"
date: 2025-08-04 06:05:00 +0900
categories: [kubernetes]
tags: [Kubernetes]
description: Kubernetes 기초
toc: true
comments: true
---

# rook-ceph이란

온프레미스 환경에서  storage-class를 구성하는 도구

ceph은 파일 스토리지를 가상화시키는 클러스터를 구성할 수 있는 소프트웨어

직접 설치하는 방법도 있지만 rook패키지를 활용하면 쿠버네티스에서 보다 편히하게 ceph을 설치하고 관리할 수 있다.

## Rook-ceph Architecture

아래 회색의 Application이 Ceph Application이고 Rook을 통해서 pod화 하고 연결하는 과정

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/cbb8b20f-f959-4b43-b1d7-dffd346657f5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642FKTI5T%2F20250805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250805T002733Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJHMEUCIG6EF1%2FSOzjtePEf1eBC2TX30ldtWMpzqYiBPBLF6FWxAiEA1%2BwN6lVk3s5BeLjjCeMR7JBmieADANaEvDXfZshoAhUq%2FwMIUBAAGgw2Mzc0MjMxODM4MDUiDOCplGO%2FLiJAnu1oDircA5fv5zpr01KVidQbP9LiAbNo%2BBJGP%2BmTBdFFxAKnBywywDSzO%2BXt7eNp1qnMZzRTLD59WQR%2F%2B8PRppfCO6hFlHOTG2WmA4%2BRop6hUVaTj8n%2FHtVFnsy4oEF4rZp5rA3vjPF9gCVJYYHhoEZR%2Fj2bl1lBJspBhTsXCujmN6t3kZBCS90q4I7DeFf1FbKbsyXxtsvk6%2FLzAOnv2t1kx4r6MYj%2BDbORt9fV0J%2FfVUdrqoqrxMz7XqACg1pvvhsvNW6x8YbjXzdDxQyYlcP0oAbjjaM5w5WYk%2BYZOaa5XV9OduFzw49Ggq2m3XvU5emMfTGX0gG3PC30XlpdlKMN8OT6iGuAVsDVyG0v6rJTRW3z8thlDujW3n6qyvWukD50FHnkJZmm%2BNCZIr0lj6dfsjrGEk52pNygQafb9zWsANNJIk8Lyr92RBATpqrvlbwinbdHn3pFfZoj78vRvMDL99szyxywZFmbTv1UckE8GHXyY8c4ZwPx3qhNcEMk7rzVWVVw%2Fv9cqX7BodbiCIlA%2BipHpfpU2gwdq8cgPM1pIB7aAZPqCRlvDrKPMvZ1a0kUh6NUMewtx4%2BlrhpT8YBXjbTO2hAg6irzDjU8DPpFO6ohDYAg1Z5YlbmZyIEl4WThMNz0xMQGOqUBWF5RqH3NjKyrvxkeAKMHuJc85xKmlezh8XLC2mBLjZHAlbxmwXTZBJwVhYTTrUM%2Fw0N6kWmFntzv3PjZ06Pu1dnWkEYs3JQr%2Bz06F8uCnhbtMyAxaCtODdtd%2FUtX%2F8Q2abMV1kz1wAQkV9GZL5rHMNwhigqtvPp0wEJxdSDUX5EQZPUN4yptW0LwliabT1%2B3k32fSpoK2z3PzLN%2BOW8SIXjL6jJG&X-Amz-Signature=2385d3f084bcf53f449ad0854502895bd3b4451269a5b8116043c7144b82dc83&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 로컬 실습

### 요구 사항 

- Worker노드 3대 필요
- 각 Worker노드에 빈디스크가 필요

