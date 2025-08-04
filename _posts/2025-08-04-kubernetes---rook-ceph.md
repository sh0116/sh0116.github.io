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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/cbb8b20f-f959-4b43-b1d7-dffd346657f5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667IEKOGCW%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T072210Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJIMEYCIQCGTfZ5KglHsg%2BdPE40A2wsZFEl09a6I7Sn3P%2BPS7yDdgIhANy1P4mIqSmiJq4TP1ObhVogrkWniy7zFWF1QCAIy%2BLpKv8DCEAQABoMNjM3NDIzMTgzODA1IgxWx7FzRYhrkD8ZoaUq3AMuIO1fqbtWcNCmTxAgScMcnKi9En0PZldM1naJi44aXP9zfTlZCM7KPl6%2FT4oHjA2zyBuPDv%2BX8OEUrDaBrPAy74rwEgrgurgAOOxCiNz0N7mzTSfisBXQ1YmxNfa%2FM%2BZ6hqA8qnLKK1YowsCRnw2ffgk8K%2BZoAfb3SFoQZ87tlHfg%2BcKI2F5RO1U7gwpfQWxTGb3ZWcOt7%2BtQ6IF%2BgELkLnsyXTssruK1iiED8BMLL1oYG%2FmYpWY1wLRu7uspyTPBoIDDJ9%2BQJ%2B3h0H5KOzYOqH7H7zokmLtwmpEtWyvJ3gdvLnQ0wvhD8m5GVFJy8W0U46FfPMcHvgqG5jxtbyhyHyxA2gxs4wSPFELIvT5PQF8daDJ9mECi0aCsVNXMt16PEyI%2FB8%2BVZp8yqKtVQ8YFbc1bEhwkhDtygxq1Z2r%2FOeXaBlTWMmRLLpRxKBqtqntF3VBgQG4aIg1TzZbe4SEM6qjXL4RyQS5zHCdBA6OS%2Fd2beKGtO1RHzvNszuVQyeAsoakxRj3j9CynC9Ru2XuR0cRhCHXlPXUE8HzTmCAyq6%2Ff8oAdFzIk1347QXlfMOMV4Kv56SeBtfZS0rOzCz9yDH3gTSK0Av4ETLgo%2B%2Fwi6S7asDO4pMNQ8MeGizDTtsHEBjqkAdfbofI12Qwjv60sIdAFxe%2FhZc5ufcGegBG9POIXSpCfhv1ofukLiLWhYF4IVMNHxEhB%2FTp%2BXFVqCA1OwciCr4WGLdqNoRcCWfU%2BKnUKCp%2B2s3xOKdLPok1f74lODyj18zRHeMh%2Balt8R%2BA9qPzwZJXZhphINRDVOU1XWouzb81new33bfo43gbfAFPP1DhyiBybhip2h4hTwQzDwDQSjYwoaUwP&X-Amz-Signature=ecc3fbb137df5b91af11d58844770b91e1661e5b147e30e2ba7dba6275ebbb5e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 로컬 실습

### 요구 사항 

- Worker노드 3대 필요
- 각 Worker노드에 빈디스크가 필요

