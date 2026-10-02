---
source: knowledge-base
origin: notion
title: "EKS 핸즈온 "
area: "세미나"
tags: ["area/seminars", "cloud/aws", "type/seminar"]
created: "2025-08-04T06:05:00.000Z"
last_edited: "2025-08-04T06:28:00.000Z"
status: published
public: true
notion_id: "245172a5-56d6-801b-bb23-c963dbb4b0f8"
notion_url: "https://www.notion.so/EKS-245172a556d6801bbb23c963dbb4b0f8"
type: note
updated: 2026-07-07
---

# EKS 핸즈온 

## 요약

AWS 세미나 리뷰

세미나에서 얻은 아이디어와 후속 조사거리를 분리하기 위한 기록입니다.

## 핵심 포인트

- AWS 세미나 리뷰
- k8s 위협 모델
- IAM 인증 & 인가
- NO IRSA
- IRSA

## 지식 그래프

- [[wiki/mocs/Knowledge Base|Knowledge Base]]
- [[wiki/mocs/세미나|세미나]]

## 정리 내용

### k8s 위협 모델
- DDos,
-  SSRF 
- 권한 상승
- 악성코드삽입
- 취약점공격
- Public Access 
- 취약한 이미지 
### IAM 인증 & 인가
AWS EKS를 사용하면 쿠버네티스에서 직접 다른 AWS 서비스를 활용가능
사용자와 서비스 어카운트
실제 사용자를 위한 어카운트와 APP를 위한 어카운트가 존재
### NO IRSA 
모든 룰이 모든 Pod를 담당
### IRSA 
각자 다른 역할을 가진 Role을 pod마다 적용가능
### 참고해라 eks aws-auth configmap
실습
- 하위 페이지: 실습
  참고 자료
  [https://www.eksworkshop.com/](https://www.eksworkshop.com/020_prerequisites/k8stools/)
  ```python
aws s3 cp s3://ee-assets-prod-us-east-1/modules/bd7b369f613f452dacbcea2a5d058d5b/v6/eksinit.sh . && chmod +x eksinit.sh && ./eksinit.sh ; source ~/.bash_profile ; source ~/.bashrc
  ```
## USING IAM GROUPS TO MANAGE KUBERNETES CLUSTER ACCESS
### CREATE IAM ROLES
  - a k8sAdmin role which will have admin rights in our EKS cluster
  - a k8sDev role which will give access to the developers namespace in our EKS cluster
  - a k8sInteg role which will give access to the integration namespace in our EKS cluster
### CREATE IAM GROUPS
  - k8sAdmin - users from this group will have admin rights on the kubernetes cluster
  - k8sDev - users from this group will have full access only in the development namespace of the cluster
  - k8sInteg - users from this group will have access to integration namespace.
### CREATE IAM USERS
  - PaulAdmin is in the k8sAdmin group and will be able to assume the k8sAdmin role.
  - JeanDev is in k8sDev Group and will be able to assume IAM role k8sDev
  - PierreInteg is in k8sInteg group and will be able to assume IAM role k8sInteg
### CONFIGURE KUBERNETES RBAC
  - development namespace will be accessible for IAM users from k8sDev group
  - integration namespace will be accessible for IAM users from k8sInteg group
### CONFIGURE KUBERNETES ROLE ACCESS
  DEV ROLE 과 AWS ROLE을 1대1 매칭시켜서 내부적으로 
  DEV ROLE 1 == AWS ROLE 1 은 같은 권한을 갖게하는 기
#### Update the aws-auth ConfigMap to allow our IAM roles
  The aws-auth ConfigMap from the kube-system namespace must be edited in order to allow or delete arn Groups.
  This file makes the mapping between IAM role and k8S RBAC rights.
  We can edit it using [eksctl](https://github.com/weaveworks/eksctl) :
## 결과
  ![[_attachments/notion/EKS-핸즈온/245172a556d68182bbffe1d0dc05d0a0.png]]
## 삭제
  ![[_attachments/notion/EKS-핸즈온/245172a556d681e5a7a4c9c1187a7907.png]]
- 하위 페이지: 실습2
### GitOps
  인프라가 코드(IaC)로 정의되고 Git 리포짙토리에서 버전이 관리되며
  애플리케이션 소프트웨어 코드와 동일한 Pull Request프로세스에 따라
  프로비저닝 되는 접근 방식입니다.
#### IaC & GIT & CI/CD
### GitOps 배포
  클러스터 내에서 소프트웨어를 구동하려면 필요
  Flux 
  ArgoCF
### Helm이란
  k8s 매니페스트 파일들을 패키징하고 관라하는 패키지 매니저
  패키징된 Chart를 통해 애플리케이션을 실행하는데 필요한 종속성 관리
  환경별로 서로 다른 설정 값들을 변수화
  등등등
  주요 명령어
  ```bash
helm create
helm search
helm install
helm list
helm repo
helm uninsatall
helm upgrade
helm rollback
...

  ```
  ![[_attachments/notion/EKS-핸즈온/245172a556d681949620f3c9eecb43ff.png]]
- 하위 페이지: 실습 3
## EKS 네트워크
  EKS 클러스터 EndPoint는 퍼블릭, 퍼블릭/프라이빗, 프라이빗 3가지 종류가 있다.
### Amazon VPC CNI (Container Network Interface)
  VPC가 주는 장점들(flow log, 로깅, 보안문제) 등등을 같이 사용 가능

## 출처

- 원문: https://www.notion.so/EKS-245172a556d6801bbb23c963dbb4b0f8
- Vault path: wiki/notes/seminars/EKS-핸즈온.md
