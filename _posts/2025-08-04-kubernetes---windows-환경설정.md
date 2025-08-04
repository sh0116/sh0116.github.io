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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/3de07ad7-c5d7-4b15-8f38-79e4edb4ab53/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SIXL2BZ2%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T072041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJIMEYCIQCWnZYI69cB5nO7njOWN%2BaQQRpCG%2FY4UjJWx8VHrgokhAIhAJdkyaNVccofF%2BqKmY3tslOqkfyiknQ2DmuDRWoc0AKAKv8DCEAQABoMNjM3NDIzMTgzODA1IgxlDXR%2BkVnPUh8AXX0q3APgH9fGxoPMbVrvGkU7VfHOluY%2Fe43Lhls%2BfzLVSdoPiuLvZs7txTTgEMHlXF8SQiNtwNgECYhOugDhDL82W5SxNH2cnC5CvHb9ljOH8kJh%2BCtGzMp6yF3TAxZ0JRJRKF2jMIuBd1jOTavB%2BaJdpi8aqpRDAG%2BEek3zrIvsSZ8wKEdxJJchSXfhLKbEICL7ZWduxbE9XMawRQQkpTUtdtLiXs0uRco14YSS%2FKX24wSg9dDLwomgQlq36NDIxkl2w9q20FH244%2FVpdioyfmjM9wB7FEwKRYVjdW6MlD2GZv086IvrH4zP3fXp0IemzunM8lI%2FnriP2rEcZYD2B3h1dZy%2FFkhu%2BPZWGdIti%2BerI6AXZbvt0LG1yeiXqUDMXCq22RVxnLjwXvpRFZQUfLY%2BxQ%2FnYUgg1tg6ZruT3K6akVuFLYYHUy0QgugUSYM5p%2FzgzJ7p%2B617Jnh31A4rlix1Jcp30u%2B9Rrko4yyLG%2B3levNqWL%2B03xy7FB9dZgX12II9Re1nyiQgXsF%2BBP1msyOCsKu0ygH2jukXvZ1J7pa2r4DEkejCmoQ2s4OiuveOOy23ODZLY0D3fbu4bfuQ6LitYSdzzi7uiNW1KH3nAMkDvyGw0y8X5c9Oc0BeD60TDDJuMHEBjqkAddFnveHo1jad6xMhV36aONR3jygJoK8bKgPQSRmrprdDlrkvhUjdaPxgIYMPHbq9JROv6poNvELzDMixf7L1I2ZbamCPpx36j3PwEwMLzU4EYdyfwrIW9gIViCwx45x1ha6cm3cV8YoGGYhqgjDH6cTWKLOs2112lJ%2FrSlCUy%2F6EoD8vEbsevHhI4fneNmbtJm2H6RSMNZMMLOfAeoU3Mu%2FLX%2F2&X-Amz-Signature=77ad1509325db0cc286bc9f46606dffcc68869b63701eff5373013499ba716bc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 네트워크 설정

아래 링크처럼 네트워크 설정을 진행하면 된다.

[RAW: {"type": "mention", "mention": {"type": "page", "page": {"id": "b38afbf4-2c2a-4c35-a4b2-706089788550"}}, "annotations": {"bold": false, "italic": false, "strikethrough": false, "underline": false, "code": false, "color": "default"}, "plain_text": "Untitled", "href": "https://www.notion.so/b38afbf42c2a4c35a4b2706089788550"}] 

나의 경우는 vmware로 켜놓고 로컬 터미널(파워쉘)에서 ssh로 접속해서 사용중입니당 

(windows11의 경우 터미널 구성이 잘되어있어서 vmware보다 편함)

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/a573e309-abae-43f5-8edd-c218412f9b26/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SIXL2BZ2%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T072041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJIMEYCIQCWnZYI69cB5nO7njOWN%2BaQQRpCG%2FY4UjJWx8VHrgokhAIhAJdkyaNVccofF%2BqKmY3tslOqkfyiknQ2DmuDRWoc0AKAKv8DCEAQABoMNjM3NDIzMTgzODA1IgxlDXR%2BkVnPUh8AXX0q3APgH9fGxoPMbVrvGkU7VfHOluY%2Fe43Lhls%2BfzLVSdoPiuLvZs7txTTgEMHlXF8SQiNtwNgECYhOugDhDL82W5SxNH2cnC5CvHb9ljOH8kJh%2BCtGzMp6yF3TAxZ0JRJRKF2jMIuBd1jOTavB%2BaJdpi8aqpRDAG%2BEek3zrIvsSZ8wKEdxJJchSXfhLKbEICL7ZWduxbE9XMawRQQkpTUtdtLiXs0uRco14YSS%2FKX24wSg9dDLwomgQlq36NDIxkl2w9q20FH244%2FVpdioyfmjM9wB7FEwKRYVjdW6MlD2GZv086IvrH4zP3fXp0IemzunM8lI%2FnriP2rEcZYD2B3h1dZy%2FFkhu%2BPZWGdIti%2BerI6AXZbvt0LG1yeiXqUDMXCq22RVxnLjwXvpRFZQUfLY%2BxQ%2FnYUgg1tg6ZruT3K6akVuFLYYHUy0QgugUSYM5p%2FzgzJ7p%2B617Jnh31A4rlix1Jcp30u%2B9Rrko4yyLG%2B3levNqWL%2B03xy7FB9dZgX12II9Re1nyiQgXsF%2BBP1msyOCsKu0ygH2jukXvZ1J7pa2r4DEkejCmoQ2s4OiuveOOy23ODZLY0D3fbu4bfuQ6LitYSdzzi7uiNW1KH3nAMkDvyGw0y8X5c9Oc0BeD60TDDJuMHEBjqkAddFnveHo1jad6xMhV36aONR3jygJoK8bKgPQSRmrprdDlrkvhUjdaPxgIYMPHbq9JROv6poNvELzDMixf7L1I2ZbamCPpx36j3PwEwMLzU4EYdyfwrIW9gIViCwx45x1ha6cm3cV8YoGGYhqgjDH6cTWKLOs2112lJ%2FrSlCUy%2F6EoD8vEbsevHhI4fneNmbtJm2H6RSMNZMMLOfAeoU3Mu%2FLX%2F2&X-Amz-Signature=dfcf59e198f20a98351b28f9a80d4bce55eefdeaa8bf51ac378ad54fcbc9c0f7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 각 OS Hostname설정

아래의 경우 master노드 mater0라는 호스트네임 설정 방법

각 워커노드도 똑같이 설

```bash
sudo hostnamectl set-hostname master0
sudo vim /etc/hosts
	# 기존 호스트 이름에서 바꾼 호스트 이름으로 적용 후 저장
```

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/cc882e15-e2c5-43e7-bcf7-b2da2c1ede50/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SIXL2BZ2%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T072041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJIMEYCIQCWnZYI69cB5nO7njOWN%2BaQQRpCG%2FY4UjJWx8VHrgokhAIhAJdkyaNVccofF%2BqKmY3tslOqkfyiknQ2DmuDRWoc0AKAKv8DCEAQABoMNjM3NDIzMTgzODA1IgxlDXR%2BkVnPUh8AXX0q3APgH9fGxoPMbVrvGkU7VfHOluY%2Fe43Lhls%2BfzLVSdoPiuLvZs7txTTgEMHlXF8SQiNtwNgECYhOugDhDL82W5SxNH2cnC5CvHb9ljOH8kJh%2BCtGzMp6yF3TAxZ0JRJRKF2jMIuBd1jOTavB%2BaJdpi8aqpRDAG%2BEek3zrIvsSZ8wKEdxJJchSXfhLKbEICL7ZWduxbE9XMawRQQkpTUtdtLiXs0uRco14YSS%2FKX24wSg9dDLwomgQlq36NDIxkl2w9q20FH244%2FVpdioyfmjM9wB7FEwKRYVjdW6MlD2GZv086IvrH4zP3fXp0IemzunM8lI%2FnriP2rEcZYD2B3h1dZy%2FFkhu%2BPZWGdIti%2BerI6AXZbvt0LG1yeiXqUDMXCq22RVxnLjwXvpRFZQUfLY%2BxQ%2FnYUgg1tg6ZruT3K6akVuFLYYHUy0QgugUSYM5p%2FzgzJ7p%2B617Jnh31A4rlix1Jcp30u%2B9Rrko4yyLG%2B3levNqWL%2B03xy7FB9dZgX12II9Re1nyiQgXsF%2BBP1msyOCsKu0ygH2jukXvZ1J7pa2r4DEkejCmoQ2s4OiuveOOy23ODZLY0D3fbu4bfuQ6LitYSdzzi7uiNW1KH3nAMkDvyGw0y8X5c9Oc0BeD60TDDJuMHEBjqkAddFnveHo1jad6xMhV36aONR3jygJoK8bKgPQSRmrprdDlrkvhUjdaPxgIYMPHbq9JROv6poNvELzDMixf7L1I2ZbamCPpx36j3PwEwMLzU4EYdyfwrIW9gIViCwx45x1ha6cm3cV8YoGGYhqgjDH6cTWKLOs2112lJ%2FrSlCUy%2F6EoD8vEbsevHhI4fneNmbtJm2H6RSMNZMMLOfAeoU3Mu%2FLX%2F2&X-Amz-Signature=516b548863d09e0162c0ba9f575439b0d3691d73671539cb32b3a0ac33ae60f4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


