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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/3de07ad7-c5d7-4b15-8f38-79e4edb4ab53/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZQICVYHL%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T071431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJIMEYCIQDT0refQoEfycWbIeb2IRQK0R4Sc0Mygt%2BVRY1S%2BnyxzAIhAOgxichv7OKcyi45AMFsmgLs%2FLbacYaeWhJrZ1Ta4ElnKv8DCEAQABoMNjM3NDIzMTgzODA1IgwWHd5Gh1OZDWvNX3Uq3AP6Q1jzYiOh%2BaySzhod9Zq3BkATZh%2FAUFQECYcqXsdhFLIwpMuzvaEVb7wjztd9a7EtjDukuHqIPQ3%2BCUltEQxNycXEkLy1EzRGcVwSRE%2BKBTIzvw7%2F3BjSjdI4QlmjnbGWImhBoGMZikbClimFrolfp72F9Luzx0hxim6m0C%2FGIKjtD7WZn1Olnp5R9r%2B%2FEtKvy4gwXbTZkNpqglYhyBF0IISKdZbLxoqRtFgYYpyJy16EkwWOSdQg5J3cF8f1bhZRrqzs%2BOq8hwZ6fJNGL3xAX%2BW4qTebfnF%2BFXG61U0mpsWZ42w7JiSC2rQqMh%2F1lRcrAqtLITbXNRe8Bpj6%2BxKSlMwlEh919kRUHTHpHXg2SJ8xQHK0yhYeNDbFqwuSZgJA0quWmLQoAf463dZNTFYDT8Sqfy2QieM9DKlNI0MLvSkI%2FN6paZX1y6SQxbhVtO0fJACia09WooHJyj6pMbYadXLE5FXQbe3WLcG5GDcQKjwI0PzHaQEaJ%2FVA0vCjhh4k5L8%2BsHBdxfi6vwuzdy6nWqTZUz4VsvdqUJB%2BP0A4nFiRphm%2F9I4XXKyypOLWO2gOWAf%2F8sV4jDpcQLph8cpW1Y0%2Ftw3imzswKvpA3EAOl3iFiyIZi5tcsd2XxTCluMHEBjqkAUUSyGAvtYShieC%2BwpV78iDBjEOZH4UFJ99hgTOLulGIa9XfTH%2BIX2F5ZQq7spDK5o0WjWAvNsCxwOeIHdZ25gx0HhfJjreuNM3FseG299cboKwJgVPjsWQm6wuFAFP9SB4VIzD4YaOPFGD0nHCkcfLlUTlx6f1kyLqofTYhlxWLkx21OIu4eBxH6PTtdTXVS7Qh%2FbwwPVcNyqyYq9hiBr%2BXPg5g&X-Amz-Signature=d83117a124837e6cf797a21aaa2467fa9f8bc1269a8ce521a5fde9587f27b378&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 네트워크 설정

아래 링크처럼 네트워크 설정을 진행하면 된다.

[RAW: {"type": "mention", "mention": {"type": "page", "page": {"id": "b38afbf4-2c2a-4c35-a4b2-706089788550"}}, "annotations": {"bold": false, "italic": false, "strikethrough": false, "underline": false, "code": false, "color": "default"}, "plain_text": "Untitled", "href": "https://www.notion.so/b38afbf42c2a4c35a4b2706089788550"}] 

나의 경우는 vmware로 켜놓고 로컬 터미널(파워쉘)에서 ssh로 접속해서 사용중입니당 

(windows11의 경우 터미널 구성이 잘되어있어서 vmware보다 편함)

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/a573e309-abae-43f5-8edd-c218412f9b26/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZQICVYHL%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T071431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJIMEYCIQDT0refQoEfycWbIeb2IRQK0R4Sc0Mygt%2BVRY1S%2BnyxzAIhAOgxichv7OKcyi45AMFsmgLs%2FLbacYaeWhJrZ1Ta4ElnKv8DCEAQABoMNjM3NDIzMTgzODA1IgwWHd5Gh1OZDWvNX3Uq3AP6Q1jzYiOh%2BaySzhod9Zq3BkATZh%2FAUFQECYcqXsdhFLIwpMuzvaEVb7wjztd9a7EtjDukuHqIPQ3%2BCUltEQxNycXEkLy1EzRGcVwSRE%2BKBTIzvw7%2F3BjSjdI4QlmjnbGWImhBoGMZikbClimFrolfp72F9Luzx0hxim6m0C%2FGIKjtD7WZn1Olnp5R9r%2B%2FEtKvy4gwXbTZkNpqglYhyBF0IISKdZbLxoqRtFgYYpyJy16EkwWOSdQg5J3cF8f1bhZRrqzs%2BOq8hwZ6fJNGL3xAX%2BW4qTebfnF%2BFXG61U0mpsWZ42w7JiSC2rQqMh%2F1lRcrAqtLITbXNRe8Bpj6%2BxKSlMwlEh919kRUHTHpHXg2SJ8xQHK0yhYeNDbFqwuSZgJA0quWmLQoAf463dZNTFYDT8Sqfy2QieM9DKlNI0MLvSkI%2FN6paZX1y6SQxbhVtO0fJACia09WooHJyj6pMbYadXLE5FXQbe3WLcG5GDcQKjwI0PzHaQEaJ%2FVA0vCjhh4k5L8%2BsHBdxfi6vwuzdy6nWqTZUz4VsvdqUJB%2BP0A4nFiRphm%2F9I4XXKyypOLWO2gOWAf%2F8sV4jDpcQLph8cpW1Y0%2Ftw3imzswKvpA3EAOl3iFiyIZi5tcsd2XxTCluMHEBjqkAUUSyGAvtYShieC%2BwpV78iDBjEOZH4UFJ99hgTOLulGIa9XfTH%2BIX2F5ZQq7spDK5o0WjWAvNsCxwOeIHdZ25gx0HhfJjreuNM3FseG299cboKwJgVPjsWQm6wuFAFP9SB4VIzD4YaOPFGD0nHCkcfLlUTlx6f1kyLqofTYhlxWLkx21OIu4eBxH6PTtdTXVS7Qh%2FbwwPVcNyqyYq9hiBr%2BXPg5g&X-Amz-Signature=95661880c376d7029441333214a1d55af70dc2fce5413647e2321d74df379666&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 각 OS Hostname설정

아래의 경우 master노드 mater0라는 호스트네임 설정 방법

각 워커노드도 똑같이 설

```bash
sudo hostnamectl set-hostname master0
sudo vim /etc/hosts
	# 기존 호스트 이름에서 바꾼 호스트 이름으로 적용 후 저장
```

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/cc882e15-e2c5-43e7-bcf7-b2da2c1ede50/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZQICVYHL%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T071431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJIMEYCIQDT0refQoEfycWbIeb2IRQK0R4Sc0Mygt%2BVRY1S%2BnyxzAIhAOgxichv7OKcyi45AMFsmgLs%2FLbacYaeWhJrZ1Ta4ElnKv8DCEAQABoMNjM3NDIzMTgzODA1IgwWHd5Gh1OZDWvNX3Uq3AP6Q1jzYiOh%2BaySzhod9Zq3BkATZh%2FAUFQECYcqXsdhFLIwpMuzvaEVb7wjztd9a7EtjDukuHqIPQ3%2BCUltEQxNycXEkLy1EzRGcVwSRE%2BKBTIzvw7%2F3BjSjdI4QlmjnbGWImhBoGMZikbClimFrolfp72F9Luzx0hxim6m0C%2FGIKjtD7WZn1Olnp5R9r%2B%2FEtKvy4gwXbTZkNpqglYhyBF0IISKdZbLxoqRtFgYYpyJy16EkwWOSdQg5J3cF8f1bhZRrqzs%2BOq8hwZ6fJNGL3xAX%2BW4qTebfnF%2BFXG61U0mpsWZ42w7JiSC2rQqMh%2F1lRcrAqtLITbXNRe8Bpj6%2BxKSlMwlEh919kRUHTHpHXg2SJ8xQHK0yhYeNDbFqwuSZgJA0quWmLQoAf463dZNTFYDT8Sqfy2QieM9DKlNI0MLvSkI%2FN6paZX1y6SQxbhVtO0fJACia09WooHJyj6pMbYadXLE5FXQbe3WLcG5GDcQKjwI0PzHaQEaJ%2FVA0vCjhh4k5L8%2BsHBdxfi6vwuzdy6nWqTZUz4VsvdqUJB%2BP0A4nFiRphm%2F9I4XXKyypOLWO2gOWAf%2F8sV4jDpcQLph8cpW1Y0%2Ftw3imzswKvpA3EAOl3iFiyIZi5tcsd2XxTCluMHEBjqkAUUSyGAvtYShieC%2BwpV78iDBjEOZH4UFJ99hgTOLulGIa9XfTH%2BIX2F5ZQq7spDK5o0WjWAvNsCxwOeIHdZ25gx0HhfJjreuNM3FseG299cboKwJgVPjsWQm6wuFAFP9SB4VIzD4YaOPFGD0nHCkcfLlUTlx6f1kyLqofTYhlxWLkx21OIu4eBxH6PTtdTXVS7Qh%2FbwwPVcNyqyYq9hiBr%2BXPg5g&X-Amz-Signature=1ce2afdb6e3451aed4c9f8a7f3bb0172ea8213b250f4776e96c3490d88f9409d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


