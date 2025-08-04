---
title: "kubernetes - windows 환경설정"
date: 2025-08-04 06:05:00 +0900
categories: [kubernetes]
tags: [Kubernetes]
description: Kubernetes 기초
toc: true
comments: true
---

## Windows 로컬에서 쿠버네티스 환경 구축 방법

VMware를 사용하여 구축

## Master Node와 Worker Node 구축

vmware에 동일한 os 3개를 만든다.

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/3de07ad7-c5d7-4b15-8f38-79e4edb4ab53/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SXUCBMF6%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T072209Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIAsufRaIp83%2ByViVF8nmrO1OBgHmkP%2BZNPFMBURfY2SRAiEAyr34eSgmgBLAMzZeIObQwz7vZVzTRyubE9Iw3t4ylIwq%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDPFDOGi1J84F92hH1ircA7Vn%2B0zhWn%2FbkxHylmBZoljW%2FdeGXuwjENTMofYe4ONpq68VusJa8%2B0qEvhqxIs4uKdv775hv2gBYO4zEMzkkSWPF4NZZ61VVwiAaAX%2BbkHTbotxOzZr3hhVTZ7NMabGE02L7ti%2FEvqURbBX3F5uFhGu%2B%2FlRKbHm4Oz%2BJ6ZkgGzZ1NsGfTJzzCpm8MUGncOxkLRhz4l0A7JBbx%2BTBFlUNAYCXejEkOVcQ1vP7ZzqkJ6G%2FF6hh08SebruUFSE5mlVBlz0vr1xc7Sh4021gLRLTofwQ9FIatMWzNz17p2Q97aHgR0yT7vai22sNtx0YmXZZoP7azsYZJkbdDPJ7KqIIf7h9vnq%2FUpSbCchUTSyWnLBKtEsxFGqf%2BWHoOxR%2FiIt7Ntk2%2Bf5F6%2BtzhtV%2FWP0VGcJ8pgb36M2vxyUT3zvHLWvUZ3ZfqjsFTEDGMiVSZbD21p6eqRrA9tkPKYztFlqVw5czeM5U5KWC8CNrmquc3nWKcvjfpZJD%2BtbS3C1H66ABL%2BatY%2FDQe7QJCojWdHbFeEK%2F9cVbscKbxsAAZ62DUytA%2BcyuCddLsos5ITXABfRGfjByGGNOvop3LBwvhhcJP1yNGVHOoNGlGM%2BAwgMT6%2B2GTRETzJ6Skg4VLyEMKO3wcQGOqUBTkoJHRDEdfX95CBal1M6d8rQS%2F48yznR4KC6ndB6YophuA7yhCJH4QXT3%2FqULB1CkVc0fOBJH3u7hCgVi6MJgBOWSxULP3k9QMltFtU0s0bVMtE%2BgZntt7ISZejDfvddL7MJGKyJzYVTDTbFfJkS5yLle4skOzRzq9d4hUin09UoEZ%2BymMtwVnThjHl9Z4uzB8k2TSrriRuvJS4Mips4a2a69cde&X-Amz-Signature=524d06c8c89e1272308f476698eb58824678bfe05d8d2f59d349db23fdd9ff33&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 네트워크 설정

아래 링크처럼 네트워크 설정을 진행하면 된다.

[RAW: {"type": "mention", "mention": {"type": "page", "page": {"id": "b38afbf4-2c2a-4c35-a4b2-706089788550"}}, "annotations": {"bold": false, "italic": false, "strikethrough": false, "underline": false, "code": false, "color": "default"}, "plain_text": "Untitled", "href": "https://www.notion.so/b38afbf42c2a4c35a4b2706089788550"}] 

나의 경우는 vmware로 켜놓고 로컬 터미널(파워쉘)에서 ssh로 접속해서 사용중입니당 

(windows11의 경우 터미널 구성이 잘되어있어서 vmware보다 편함)

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/a573e309-abae-43f5-8edd-c218412f9b26/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SXUCBMF6%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T072209Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIAsufRaIp83%2ByViVF8nmrO1OBgHmkP%2BZNPFMBURfY2SRAiEAyr34eSgmgBLAMzZeIObQwz7vZVzTRyubE9Iw3t4ylIwq%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDPFDOGi1J84F92hH1ircA7Vn%2B0zhWn%2FbkxHylmBZoljW%2FdeGXuwjENTMofYe4ONpq68VusJa8%2B0qEvhqxIs4uKdv775hv2gBYO4zEMzkkSWPF4NZZ61VVwiAaAX%2BbkHTbotxOzZr3hhVTZ7NMabGE02L7ti%2FEvqURbBX3F5uFhGu%2B%2FlRKbHm4Oz%2BJ6ZkgGzZ1NsGfTJzzCpm8MUGncOxkLRhz4l0A7JBbx%2BTBFlUNAYCXejEkOVcQ1vP7ZzqkJ6G%2FF6hh08SebruUFSE5mlVBlz0vr1xc7Sh4021gLRLTofwQ9FIatMWzNz17p2Q97aHgR0yT7vai22sNtx0YmXZZoP7azsYZJkbdDPJ7KqIIf7h9vnq%2FUpSbCchUTSyWnLBKtEsxFGqf%2BWHoOxR%2FiIt7Ntk2%2Bf5F6%2BtzhtV%2FWP0VGcJ8pgb36M2vxyUT3zvHLWvUZ3ZfqjsFTEDGMiVSZbD21p6eqRrA9tkPKYztFlqVw5czeM5U5KWC8CNrmquc3nWKcvjfpZJD%2BtbS3C1H66ABL%2BatY%2FDQe7QJCojWdHbFeEK%2F9cVbscKbxsAAZ62DUytA%2BcyuCddLsos5ITXABfRGfjByGGNOvop3LBwvhhcJP1yNGVHOoNGlGM%2BAwgMT6%2B2GTRETzJ6Skg4VLyEMKO3wcQGOqUBTkoJHRDEdfX95CBal1M6d8rQS%2F48yznR4KC6ndB6YophuA7yhCJH4QXT3%2FqULB1CkVc0fOBJH3u7hCgVi6MJgBOWSxULP3k9QMltFtU0s0bVMtE%2BgZntt7ISZejDfvddL7MJGKyJzYVTDTbFfJkS5yLle4skOzRzq9d4hUin09UoEZ%2BymMtwVnThjHl9Z4uzB8k2TSrriRuvJS4Mips4a2a69cde&X-Amz-Signature=d5ded18f64bfe4cc8af0f345215263216665b887cc7047fb0605c8321d427676&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 각 OS Hostname설정

아래의 경우 master노드 mater0라는 호스트네임 설정 방법

각 워커노드도 똑같이 설

```bash
sudo hostnamectl set-hostname master0
sudo vim /etc/hosts
	# 기존 호스트 이름에서 바꾼 호스트 이름으로 적용 후 저장
```

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/cc882e15-e2c5-43e7-bcf7-b2da2c1ede50/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SXUCBMF6%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T072209Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIAsufRaIp83%2ByViVF8nmrO1OBgHmkP%2BZNPFMBURfY2SRAiEAyr34eSgmgBLAMzZeIObQwz7vZVzTRyubE9Iw3t4ylIwq%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDPFDOGi1J84F92hH1ircA7Vn%2B0zhWn%2FbkxHylmBZoljW%2FdeGXuwjENTMofYe4ONpq68VusJa8%2B0qEvhqxIs4uKdv775hv2gBYO4zEMzkkSWPF4NZZ61VVwiAaAX%2BbkHTbotxOzZr3hhVTZ7NMabGE02L7ti%2FEvqURbBX3F5uFhGu%2B%2FlRKbHm4Oz%2BJ6ZkgGzZ1NsGfTJzzCpm8MUGncOxkLRhz4l0A7JBbx%2BTBFlUNAYCXejEkOVcQ1vP7ZzqkJ6G%2FF6hh08SebruUFSE5mlVBlz0vr1xc7Sh4021gLRLTofwQ9FIatMWzNz17p2Q97aHgR0yT7vai22sNtx0YmXZZoP7azsYZJkbdDPJ7KqIIf7h9vnq%2FUpSbCchUTSyWnLBKtEsxFGqf%2BWHoOxR%2FiIt7Ntk2%2Bf5F6%2BtzhtV%2FWP0VGcJ8pgb36M2vxyUT3zvHLWvUZ3ZfqjsFTEDGMiVSZbD21p6eqRrA9tkPKYztFlqVw5czeM5U5KWC8CNrmquc3nWKcvjfpZJD%2BtbS3C1H66ABL%2BatY%2FDQe7QJCojWdHbFeEK%2F9cVbscKbxsAAZ62DUytA%2BcyuCddLsos5ITXABfRGfjByGGNOvop3LBwvhhcJP1yNGVHOoNGlGM%2BAwgMT6%2B2GTRETzJ6Skg4VLyEMKO3wcQGOqUBTkoJHRDEdfX95CBal1M6d8rQS%2F48yznR4KC6ndB6YophuA7yhCJH4QXT3%2FqULB1CkVc0fOBJH3u7hCgVi6MJgBOWSxULP3k9QMltFtU0s0bVMtE%2BgZntt7ISZejDfvddL7MJGKyJzYVTDTbFfJkS5yLle4skOzRzq9d4hUin09UoEZ%2BymMtwVnThjHl9Z4uzB8k2TSrriRuvJS4Mips4a2a69cde&X-Amz-Signature=aebd6467385c4a9b1925cd3c1b55439ce9174b29583056bbfda0804f07248a02&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


