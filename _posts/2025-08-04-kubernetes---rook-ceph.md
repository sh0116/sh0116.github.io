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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/cbb8b20f-f959-4b43-b1d7-dffd346657f5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V4NRAES7%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T072042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIHhazDtNEAbImvYbZNTVkLFV%2FvWDAzuR6AOMPCPEE%2FobAiEA1cWq78DLBiJv7LQqB9QpMHSk1gWo2BCA4FwDN2aLPGcq%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDOWyLZaX5FyIzjPSUircA5GcfMHgT67bZaf4KRtsg7ka%2BJbm7LPEb4UyvWnHmiFZu51s0XohJX3SKfjwW1c7REHAXmE8ywzUEk3kRs1RvjFOy%2FKglUMC1vm5aucSHFuAgTL%2FLl3wCcEIf%2B8vIERMmiZ1O86IdOYzCxCHBRNR%2BK3fJPV%2BFQ%2BizL%2F9Pt7JSj%2FE9fBxiMaMzwY4uhMsyRamIVFpc%2FyEsdNLYxNvQodrSkfc6H3mSCjY1p3ygQLBnpWC3rF3eZrhROCGw6p7D0Soueogqj8eWEqtdH%2B29jWBDwlmonN8lKALDuZ9be70H3TS6eVOwpMlq2UwYmToLrqhYJCMmk1F6SOLuoeIDV32ea%2BjKiPbTesBT1%2BjYfhXWV5PUo4hJewy50j4kdGdXPeQopYOfyusfsDg8YA0etcXd9IE%2FXDZrF%2FKeDZardmF50m%2B7LloX1gnmrpIWO0ufzTvwg7DONpdup2sRbtXI8YHB5f0c5WF70fJFGBCQMottxFXmcaDKltGcuFGXfkKBTuyMFukJyFd85CPKBf9kzd2gNEWp3%2B1%2Bd3wJyijTJ%2B30hqHQfXqcdqspz7kBK0vpjxjkGUn6MCzSj46PebQBsP%2FZKE%2BzzHcS9qBxoiS8VT6aI5sxEAbOIaimKPSwTi7MKa4wcQGOqUBXo0gaRqDJwFd4ULxRSAiJt4Dpwln0fy2pFLpr01tbj5QPzMVNYx73fWdXQtpVct8oL6zWsGcLn404jfyJo%2F4KszN7vTb4q5Tnggghbb6fwC7DI781yTbIhBxQt59wTGJI4XMQluwrJ9KrDJvikzYpzMkWTp3weL99O%2FZmMZbeeJyXFpXPzVsbH%2FEMTpHfu3Okh6rkgUGWpwdWVVPrCO0kxMlcGkt&X-Amz-Signature=5f1b34cf890f11f2f8a66ecf5f42306d2184f63e9355337ee2d45c9d6709873a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 로컬 실습

### 요구 사항 

- Worker노드 3대 필요
- 각 Worker노드에 빈디스크가 필요

