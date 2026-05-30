---
title: "AWS VPC PrivateLink를 이용한 네트워크 구성 전략 (Network Architecture using AWS PrivateLink) - 당근 SRE 밋업 1회"
date: 2025-08-04 06:05:00 +0900
categories: [세미나]
tags: [notion, automation]
description: 당근마켓 세미나 리뷰
toc: true
comments: true
---

발표자 : 박병진님
GITHUB : posquit0

## AWS VPC 상의 망 연계 문제점

- 목적에 따라 분리 된 여러 VPC를 어떻게 연결할 수 있을까?
- 개발자가 VPC의 Private 영역에 접근할 수 있도록 제공하려면?
- AWS VPC에서 인터넷을 통하지 않고 S3, ECR, KMS등의 서비스를 호출할 수 없을까?
- 사무실 네트워크와 AWS VPC를 안전하게 연결하려면?
- 대외 기관과의 시스템 연계는?
![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/1c016ec7-a2eb-49d9-aaab-5e468a12e5c6/Untitled.png)

(저작권은 박병진님에게 있습니다.)

## AWS PrivateLink

AWS VPC와 대상 서비스 간 안전한 연결을 위한 기술

고가영성과 확장성을 제공

- AWS 서비스 (S3, EC2, ECR …)
- 다른 AWS 계정 상에서 제공되는 서비스 VPC 엔드포인트 서비스
- AWS 마켓플레이스 상의 파트너 서비스
![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/d223edf1-1406-420b-a488-381b177483d9/Untitled.png)

### 게이트 웨이 엔드 포인트 (Gateway Endpoint)

라우팅 규칙을 통한 AWS 서비스에 사설 접근

- Managed Prefix List를 사용하여 라우팅 규칙 관리
### 인터페이스 엔드 포인트 (Interface Endpoint)

- 네트워크 인터페이스를 통해 사설 IP 부여
- 다양한 AWS 서비스에 대해 이용 가
### 엔드 포인트 서비스 (Endpoint Service)

- 다른 AWS 계정에게 서비스 제공 모적
- 사설 도메인 제공 가능
## 세 줄 요약

- AWS PrivateLink를 사용하면 망 연계에 있어 안전하고 확장성 있는 네트워크 구성을 가져 갈 수 있어요.
- AWS PrivateLink서비스 제공자의 AZ구성과 NLB Cross-zone Load Balancing 옵션을 주의해야 한다.
- PrivateLink를 여러 VPC와 온프레미스에 통합 적용하고 싶다면 Route53 기능을 활용할 수 있어요.

