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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/3de07ad7-c5d7-4b15-8f38-79e4edb4ab53/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6XWYRIZ%2F20250805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250805T002731Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJGMEQCIEqMlAwWgQJjJatZZYIYWbFcRzHJ%2FzmN8X7CmO8bC2YmAiB7mKQS8MpMeCO0u8VVeTD0rc8%2FrKVTvtmjvnLqEqIrzir%2FAwhQEAAaDDYzNzQyMzE4MzgwNSIMNNhLkwG4z9b5%2BGiKKtwDuxHKKJQOugo4gcuFc2Lg0PQYeNWQFQiGrZ%2FVNljjfaP0fOVU2D37VLGBldiHnBhbckz1lJvgO1n6%2BRs1XZO55%2F5%2B5j64YLTdqOxwS8%2Fw2eZBfXHi6xJK%2BT3Ap7KG2gj83SID%2BJEzz3S1hTKvCrSH9QxnvP1dYT9hBQEALOFHuwi0DOVQCwKfKdXe%2FkhE201qiPqs1CR7h1PdLOkVz7oO%2Fvd3tPMYdwbdDquj6BcRtWUbMOPjxCi1HDueN5YtZjnpnQOKhlZPETG%2B5Elwk4qyxiLaPIimFGcp3iILovPdqrM6w0DFIC4LljKfJL09171MMGQrfFe6pmZr%2Fp%2BZ0P1Dk58T6isLeTuCw0syRUXoLgDSCuTWKhNytlPIQG3MrY3ilHaa3f00IONX9RgmIDbNNPcoGQM4qfiKARZcHgEXXNm6HS3XMBv9IrP1sAYPov%2B5N1rfmYk7RsXv7ebmhke31cpcake76XsVasnl%2BTWooMlp1nIgrnTib4l1fJ%2FaazAYEyDYMqzU9%2BLFZibLOqGUClz3rpHkHTHGsPhjTahTn9nr9eovx8cIZBYQHMLir2%2Fg2knZr8r2KBpNrBcLtV94EdiVKx62f19Cg4K1ZtZO9SCP0dBejJkKL%2BiwnU0woPTExAY6pgH4ISSoAIUhrIeAJ40sCCfTabMx5v%2FDWNEJ%2BYtp%2FibRdSBfTfd8OJQRVfOdGcI0yyabRzfWQR9nVkj8%2FjjIa6QdvP6Nfca%2Ft0yUf8uMGWUaWA%2FjtHX1CLtLV14QiFZBAmDWp9S%2Bi4yficuKTpIIQCECVfrHH0O4C%2B31nDgsUBItUPyu0wkcKCKIkQCENatvYGfSAWUuawA9RU0oKg%2BOBL9SwLs9S8MQ&X-Amz-Signature=a713761850e471875bbc23c178c5252dbd7dc54dc8e3a737e1388e138006648e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 네트워크 설정

아래 링크처럼 네트워크 설정을 진행하면 된다.

[RAW: {"type": "mention", "mention": {"type": "page", "page": {"id": "b38afbf4-2c2a-4c35-a4b2-706089788550"}}, "annotations": {"bold": false, "italic": false, "strikethrough": false, "underline": false, "code": false, "color": "default"}, "plain_text": "Untitled", "href": "https://www.notion.so/b38afbf42c2a4c35a4b2706089788550"}] 

나의 경우는 vmware로 켜놓고 로컬 터미널(파워쉘)에서 ssh로 접속해서 사용중입니당 

(windows11의 경우 터미널 구성이 잘되어있어서 vmware보다 편함)

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/a573e309-abae-43f5-8edd-c218412f9b26/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6XWYRIZ%2F20250805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250805T002731Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJGMEQCIEqMlAwWgQJjJatZZYIYWbFcRzHJ%2FzmN8X7CmO8bC2YmAiB7mKQS8MpMeCO0u8VVeTD0rc8%2FrKVTvtmjvnLqEqIrzir%2FAwhQEAAaDDYzNzQyMzE4MzgwNSIMNNhLkwG4z9b5%2BGiKKtwDuxHKKJQOugo4gcuFc2Lg0PQYeNWQFQiGrZ%2FVNljjfaP0fOVU2D37VLGBldiHnBhbckz1lJvgO1n6%2BRs1XZO55%2F5%2B5j64YLTdqOxwS8%2Fw2eZBfXHi6xJK%2BT3Ap7KG2gj83SID%2BJEzz3S1hTKvCrSH9QxnvP1dYT9hBQEALOFHuwi0DOVQCwKfKdXe%2FkhE201qiPqs1CR7h1PdLOkVz7oO%2Fvd3tPMYdwbdDquj6BcRtWUbMOPjxCi1HDueN5YtZjnpnQOKhlZPETG%2B5Elwk4qyxiLaPIimFGcp3iILovPdqrM6w0DFIC4LljKfJL09171MMGQrfFe6pmZr%2Fp%2BZ0P1Dk58T6isLeTuCw0syRUXoLgDSCuTWKhNytlPIQG3MrY3ilHaa3f00IONX9RgmIDbNNPcoGQM4qfiKARZcHgEXXNm6HS3XMBv9IrP1sAYPov%2B5N1rfmYk7RsXv7ebmhke31cpcake76XsVasnl%2BTWooMlp1nIgrnTib4l1fJ%2FaazAYEyDYMqzU9%2BLFZibLOqGUClz3rpHkHTHGsPhjTahTn9nr9eovx8cIZBYQHMLir2%2Fg2knZr8r2KBpNrBcLtV94EdiVKx62f19Cg4K1ZtZO9SCP0dBejJkKL%2BiwnU0woPTExAY6pgH4ISSoAIUhrIeAJ40sCCfTabMx5v%2FDWNEJ%2BYtp%2FibRdSBfTfd8OJQRVfOdGcI0yyabRzfWQR9nVkj8%2FjjIa6QdvP6Nfca%2Ft0yUf8uMGWUaWA%2FjtHX1CLtLV14QiFZBAmDWp9S%2Bi4yficuKTpIIQCECVfrHH0O4C%2B31nDgsUBItUPyu0wkcKCKIkQCENatvYGfSAWUuawA9RU0oKg%2BOBL9SwLs9S8MQ&X-Amz-Signature=dd9b34e8c41e16027ed3f0a64c5284cac48c9b8d900c8efe4b729f6b2fd5406a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 각 OS Hostname설정

아래의 경우 master노드 mater0라는 호스트네임 설정 방법

각 워커노드도 똑같이 설

```bash
sudo hostnamectl set-hostname master0
sudo vim /etc/hosts
	# 기존 호스트 이름에서 바꾼 호스트 이름으로 적용 후 저장
```

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/cc882e15-e2c5-43e7-bcf7-b2da2c1ede50/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6XWYRIZ%2F20250805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250805T002732Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJGMEQCIEqMlAwWgQJjJatZZYIYWbFcRzHJ%2FzmN8X7CmO8bC2YmAiB7mKQS8MpMeCO0u8VVeTD0rc8%2FrKVTvtmjvnLqEqIrzir%2FAwhQEAAaDDYzNzQyMzE4MzgwNSIMNNhLkwG4z9b5%2BGiKKtwDuxHKKJQOugo4gcuFc2Lg0PQYeNWQFQiGrZ%2FVNljjfaP0fOVU2D37VLGBldiHnBhbckz1lJvgO1n6%2BRs1XZO55%2F5%2B5j64YLTdqOxwS8%2Fw2eZBfXHi6xJK%2BT3Ap7KG2gj83SID%2BJEzz3S1hTKvCrSH9QxnvP1dYT9hBQEALOFHuwi0DOVQCwKfKdXe%2FkhE201qiPqs1CR7h1PdLOkVz7oO%2Fvd3tPMYdwbdDquj6BcRtWUbMOPjxCi1HDueN5YtZjnpnQOKhlZPETG%2B5Elwk4qyxiLaPIimFGcp3iILovPdqrM6w0DFIC4LljKfJL09171MMGQrfFe6pmZr%2Fp%2BZ0P1Dk58T6isLeTuCw0syRUXoLgDSCuTWKhNytlPIQG3MrY3ilHaa3f00IONX9RgmIDbNNPcoGQM4qfiKARZcHgEXXNm6HS3XMBv9IrP1sAYPov%2B5N1rfmYk7RsXv7ebmhke31cpcake76XsVasnl%2BTWooMlp1nIgrnTib4l1fJ%2FaazAYEyDYMqzU9%2BLFZibLOqGUClz3rpHkHTHGsPhjTahTn9nr9eovx8cIZBYQHMLir2%2Fg2knZr8r2KBpNrBcLtV94EdiVKx62f19Cg4K1ZtZO9SCP0dBejJkKL%2BiwnU0woPTExAY6pgH4ISSoAIUhrIeAJ40sCCfTabMx5v%2FDWNEJ%2BYtp%2FibRdSBfTfd8OJQRVfOdGcI0yyabRzfWQR9nVkj8%2FjjIa6QdvP6Nfca%2Ft0yUf8uMGWUaWA%2FjtHX1CLtLV14QiFZBAmDWp9S%2Bi4yficuKTpIIQCECVfrHH0O4C%2B31nDgsUBItUPyu0wkcKCKIkQCENatvYGfSAWUuawA9RU0oKg%2BOBL9SwLs9S8MQ&X-Amz-Signature=de3a56b72f8a95fd705940ff3be8d05b44024cd8572c230392c52ab932eb0687&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


