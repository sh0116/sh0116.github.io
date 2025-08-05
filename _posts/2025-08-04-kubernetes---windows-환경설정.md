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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/3de07ad7-c5d7-4b15-8f38-79e4edb4ab53/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VYFSVMXB%2F20250805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250805T061025Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJGMEQCIH6iRW3wj67FDYWURkS7FNkDHyQnmHX%2BgUtPDhWa70ERAiAC3ixE60nNRC8Eo9iJ1RupOMre%2BMpKR%2FMYJAAgvjXhQSr%2FAwhXEAAaDDYzNzQyMzE4MzgwNSIMb4FgGslzD%2BLrQ2GQKtwDtRwM%2Bnczv3ZbWrER80joe2J79vEyW9bwq11H0px4QEa9sC0V6HERiO4UFDBSKtXxzteyZ1mDnl5OLKdjKFX%2FgbuBS8LL0lKRi1GH%2FFXnELDziJvHuoH6%2B%2FQVyP1SBwL64c%2FKIwpaOw72gLgCcmoOH6FK0X9xsu1lhTUvwAt8wQycx4VyQRJBec7naSXymbW3WB4p15zSD83lJDqzqUOddKGj3cIfymDpZQPBPnTw%2BUH8aepi%2Fx3hYSOxLotGYs8E87zvrDgXzRfFTQlE1E8bOOseAfIj37VYo9vJlzpZsFWsswghClM4KpBI2gqTiOj96NDz%2FXSu7YXl%2FzveqPKJq94nssta16rc4xgpDzVJk7H%2FyZJVWapHqsI1EOawtc4Oh19e1%2BL3ly1I5fJVkwmDsHp1ChBtZjGrb2lQ8iO0oiLOIjpD4DVOCDMg0o%2FtkHoAhHzjWfxt56UFU3yxOgN1IwEJGD9LpOJ4k1N35LW7cnJthVbKF99TD2K7E%2BxQjzGCOomqPtVEszjoRVFkutQh2i8eU2xmhTVwPR97kVZ2Vxxkmcszy%2ByJvzT%2FowVriMBMI%2FtRbs8PhWUEGKeLTiWX6TOk9XBrwr2dAcqa6%2FkKyYuxr80VEQymGN7D8Q8w6bPGxAY6pgHcW%2FxMPzFnZ%2FspQBuYMcvMFEPQ9egUV2lGGNDkRDySdKjzE2Q5zFAC4ms9a3wjE09tlFitP%2BK33nekaXSFevWkPIddz%2BUEz1PfMHim3LHFLlbLidaHmyAex1FrPX5%2Bbtr%2FRF%2FQlYafGVam8OQsTurfiWKTSLFDvBoj%2FEnCqzUjyje5URSSR9KnyOfg%2B%2FYGhYIeDmprgtMAAgywvex9JsSrWG6QVwXX&X-Amz-Signature=78d76e869896ae43e37818e77ee3fc15e2c874c63dd85cf0402b44ed88021a2c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 네트워크 설정

아래 링크처럼 네트워크 설정을 진행하면 된다.

[RAW: {"type": "mention", "mention": {"type": "page", "page": {"id": "b38afbf4-2c2a-4c35-a4b2-706089788550"}}, "annotations": {"bold": false, "italic": false, "strikethrough": false, "underline": false, "code": false, "color": "default"}, "plain_text": "Untitled", "href": "https://www.notion.so/b38afbf42c2a4c35a4b2706089788550"}] 

나의 경우는 vmware로 켜놓고 로컬 터미널(파워쉘)에서 ssh로 접속해서 사용중입니당 

(windows11의 경우 터미널 구성이 잘되어있어서 vmware보다 편함)

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/a573e309-abae-43f5-8edd-c218412f9b26/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VYFSVMXB%2F20250805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250805T061025Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJGMEQCIH6iRW3wj67FDYWURkS7FNkDHyQnmHX%2BgUtPDhWa70ERAiAC3ixE60nNRC8Eo9iJ1RupOMre%2BMpKR%2FMYJAAgvjXhQSr%2FAwhXEAAaDDYzNzQyMzE4MzgwNSIMb4FgGslzD%2BLrQ2GQKtwDtRwM%2Bnczv3ZbWrER80joe2J79vEyW9bwq11H0px4QEa9sC0V6HERiO4UFDBSKtXxzteyZ1mDnl5OLKdjKFX%2FgbuBS8LL0lKRi1GH%2FFXnELDziJvHuoH6%2B%2FQVyP1SBwL64c%2FKIwpaOw72gLgCcmoOH6FK0X9xsu1lhTUvwAt8wQycx4VyQRJBec7naSXymbW3WB4p15zSD83lJDqzqUOddKGj3cIfymDpZQPBPnTw%2BUH8aepi%2Fx3hYSOxLotGYs8E87zvrDgXzRfFTQlE1E8bOOseAfIj37VYo9vJlzpZsFWsswghClM4KpBI2gqTiOj96NDz%2FXSu7YXl%2FzveqPKJq94nssta16rc4xgpDzVJk7H%2FyZJVWapHqsI1EOawtc4Oh19e1%2BL3ly1I5fJVkwmDsHp1ChBtZjGrb2lQ8iO0oiLOIjpD4DVOCDMg0o%2FtkHoAhHzjWfxt56UFU3yxOgN1IwEJGD9LpOJ4k1N35LW7cnJthVbKF99TD2K7E%2BxQjzGCOomqPtVEszjoRVFkutQh2i8eU2xmhTVwPR97kVZ2Vxxkmcszy%2ByJvzT%2FowVriMBMI%2FtRbs8PhWUEGKeLTiWX6TOk9XBrwr2dAcqa6%2FkKyYuxr80VEQymGN7D8Q8w6bPGxAY6pgHcW%2FxMPzFnZ%2FspQBuYMcvMFEPQ9egUV2lGGNDkRDySdKjzE2Q5zFAC4ms9a3wjE09tlFitP%2BK33nekaXSFevWkPIddz%2BUEz1PfMHim3LHFLlbLidaHmyAex1FrPX5%2Bbtr%2FRF%2FQlYafGVam8OQsTurfiWKTSLFDvBoj%2FEnCqzUjyje5URSSR9KnyOfg%2B%2FYGhYIeDmprgtMAAgywvex9JsSrWG6QVwXX&X-Amz-Signature=6b959c0b521add8ead6c7bebcd6490dd1368a2909a5fae4d13a5c276e2984e99&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 각 OS Hostname설정

아래의 경우 master노드 mater0라는 호스트네임 설정 방법

각 워커노드도 똑같이 설

```bash
sudo hostnamectl set-hostname master0
sudo vim /etc/hosts
	# 기존 호스트 이름에서 바꾼 호스트 이름으로 적용 후 저장
```

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/cc882e15-e2c5-43e7-bcf7-b2da2c1ede50/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VYFSVMXB%2F20250805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250805T061025Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJGMEQCIH6iRW3wj67FDYWURkS7FNkDHyQnmHX%2BgUtPDhWa70ERAiAC3ixE60nNRC8Eo9iJ1RupOMre%2BMpKR%2FMYJAAgvjXhQSr%2FAwhXEAAaDDYzNzQyMzE4MzgwNSIMb4FgGslzD%2BLrQ2GQKtwDtRwM%2Bnczv3ZbWrER80joe2J79vEyW9bwq11H0px4QEa9sC0V6HERiO4UFDBSKtXxzteyZ1mDnl5OLKdjKFX%2FgbuBS8LL0lKRi1GH%2FFXnELDziJvHuoH6%2B%2FQVyP1SBwL64c%2FKIwpaOw72gLgCcmoOH6FK0X9xsu1lhTUvwAt8wQycx4VyQRJBec7naSXymbW3WB4p15zSD83lJDqzqUOddKGj3cIfymDpZQPBPnTw%2BUH8aepi%2Fx3hYSOxLotGYs8E87zvrDgXzRfFTQlE1E8bOOseAfIj37VYo9vJlzpZsFWsswghClM4KpBI2gqTiOj96NDz%2FXSu7YXl%2FzveqPKJq94nssta16rc4xgpDzVJk7H%2FyZJVWapHqsI1EOawtc4Oh19e1%2BL3ly1I5fJVkwmDsHp1ChBtZjGrb2lQ8iO0oiLOIjpD4DVOCDMg0o%2FtkHoAhHzjWfxt56UFU3yxOgN1IwEJGD9LpOJ4k1N35LW7cnJthVbKF99TD2K7E%2BxQjzGCOomqPtVEszjoRVFkutQh2i8eU2xmhTVwPR97kVZ2Vxxkmcszy%2ByJvzT%2FowVriMBMI%2FtRbs8PhWUEGKeLTiWX6TOk9XBrwr2dAcqa6%2FkKyYuxr80VEQymGN7D8Q8w6bPGxAY6pgHcW%2FxMPzFnZ%2FspQBuYMcvMFEPQ9egUV2lGGNDkRDySdKjzE2Q5zFAC4ms9a3wjE09tlFitP%2BK33nekaXSFevWkPIddz%2BUEz1PfMHim3LHFLlbLidaHmyAex1FrPX5%2Bbtr%2FRF%2FQlYafGVam8OQsTurfiWKTSLFDvBoj%2FEnCqzUjyje5URSSR9KnyOfg%2B%2FYGhYIeDmprgtMAAgywvex9JsSrWG6QVwXX&X-Amz-Signature=231f593c2f837e60183f5bc95e507e260bf375b7cf44f0a779bf2de1261ceade&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


