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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/3de07ad7-c5d7-4b15-8f38-79e4edb4ab53/Untitled.png)

## 네트워크 설정

아래 링크처럼 네트워크 설정을 진행하면 된다.

[RAW: {"type": "mention", "mention": {"type": "page", "page": {"id": "b38afbf4-2c2a-4c35-a4b2-706089788550"}}, "annotations": {"bold": false, "italic": false, "strikethrough": false, "underline": false, "code": false, "color": "default"}, "plain_text": "Untitled", "href": "https://www.notion.so/b38afbf42c2a4c35a4b2706089788550"}] 

나의 경우는 vmware로 켜놓고 로컬 터미널(파워쉘)에서 ssh로 접속해서 사용중입니당 

(windows11의 경우 터미널 구성이 잘되어있어서 vmware보다 편함)

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/a573e309-abae-43f5-8edd-c218412f9b26/Untitled.png)

## 각 OS Hostname설정

아래의 경우 master노드 mater0라는 호스트네임 설정 방법

각 워커노드도 똑같이 설

```bash
sudo hostnamectl set-hostname master0
sudo vim /etc/hosts
	# 기존 호스트 이름에서 바꾼 호스트 이름으로 적용 후 저장
```

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/cc882e15-e2c5-43e7-bcf7-b2da2c1ede50/Untitled.png)


