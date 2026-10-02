---
source: knowledge-base
origin: notion
title: "AWS Demogo Prime "
area: "세미나"
tags: ["area/seminars", "cloud/aws", "type/seminar"]
created: "2025-08-04T06:07:00.000Z"
last_edited: "2025-08-04T06:28:00.000Z"
status: published
public: true
notion_id: "245172a5-56d6-8061-9033-dd70e3aedfd4"
notion_url: "https://www.notion.so/AWS-Demogo-Prime-245172a556d680619033dd70e3aedfd4"
type: note
updated: 2026-07-07
---

# AWS Demogo Prime 

## 요약

AWS 세미나 리뷰

세미나에서 얻은 아이디어와 후속 조사거리를 분리하기 위한 기록입니다.

## 핵심 포인트

- AWS 세미나 리뷰
- Demogo Prime
- Demo Content
- 데이터 수집부터 분석까지, 데이터 파이프 라인 구축 함께 해요!
- 데이터 수집, 분석, 파이프라인

## 지식 그래프

- [[wiki/mocs/Knowledge Base|Knowledge Base]]
- [[wiki/mocs/세미나|세미나]]

## 정리 내용

### Demogo Prime
데이터 수집부터 분석까지, 데이터 파이프라인 구축 함께 시작해요! - 
10월12일(수) 1:00 PM – 5:00 PM

![[_attachments/notion/AWS-Demogo-Prime/245172a556d681898288f6a37df0829f.png]]
![[_attachments/notion/AWS-Demogo-Prime/245172a556d681b883b6d74719a0af81.png]]
### Demo Content
![[_attachments/notion/AWS-Demogo-Prime/245172a556d6814781f9c7a8a46c15f4.png]]
상품
  ![[_attachments/notion/AWS-Demogo-Prime/245172a556d681d49d43f8163b57044f.png]]
### 데이터 수집부터 분석까지, 데이터 파이프 라인 구축 함께 해요!
Amazon Web Service, Solutions Architect 성재우
- 목표 : 우리가 가지고있는 데이터를 AWS에서 분석하려면 어떻게 파이프라인을 구성해야 하는지
#### 데이터 수집, 분석, 파이프라인
![[_attachments/notion/AWS-Demogo-Prime/245172a556d681b8b90ff305e3d1f9e8.png]]
#### 과거에 했던 일들, 어려웠던 점들
데이터 분석 플랫폼 발전 과정
- 1990’s 
  - ERP, CRM, SCM, PLM등 기업의 정보화
- 2000’s
  - Silo 데이터 통합, Data Warehouse
- 2010’s
  - 3V, BigData, Data Pond, Data Scientist
- 2020’s
  - Data Lake, Citizen, Self-Service
기존의 방법으로 어려웠던 점
- 폭발적으로 증가하는 데이터
- 새로운 데이터 소스
- 다양해지는 데이터 유형
- 많은 곳에서 데이터를 사용
- 다양한 애플리케이션에서 데이터를 사용
데이터 Silo 문제
- 모든 데이터 소스를 한번에 볼 수 있는 단일 뷰가 없는 상황ㅁ
![[_attachments/notion/AWS-Demogo-Prime/245172a556d68175a425cf3205b73f01.png]]
#### AWS Modern Data Analytics & Pipeline
Data Trends  그리고 AWS
![[_attachments/notion/AWS-Demogo-Prime/245172a556d681f6a65ff1e93d3b40d2.png]]
AWS Analytics
![[_attachments/notion/AWS-Demogo-Prime/245172a556d68180a350e451d03eba2f.png]]
- 직접 서버를 설치해서 운영하지 않아도 되는 완전 관리형 분석 서비스
  - 변경 요청
  - 모니터링
  - 패치관리
  - 보안
  - 백업 서비스
![[_attachments/notion/AWS-Demogo-Prime/245172a556d68101a91fed4075015d2d.png]]
![[_attachments/notion/AWS-Demogo-Prime/245172a556d681a5bc09ed8ef26d7785.png]]
### AWS 데이터 수집 제공 서비스
- Kinesis
- DataSync
- DB Migration Service
#### DB Migration Service
![[_attachments/notion/AWS-Demogo-Prime/245172a556d68119b9f8ffb3e3612cd5.png]]
![[_attachments/notion/AWS-Demogo-Prime/245172a556d681a48d14f53abd315cb3.png]]
#### DataSync 온라인 데이터 전송 및 마이그레이션
![[_attachments/notion/AWS-Demogo-Prime/245172a556d681788aa9e797bc8ddc73.png]]
#### Kinesis 실시간 데이터 수집, 프로세싱 분석
사례
  - 이상 및 사기 탐지
  - 실시간 고객 경험 조정
  - 실시간 개인화 (추천 시스템) 
  - 의료 및 응급 서비스 지원
![[_attachments/notion/AWS-Demogo-Prime/245172a556d681c28809fdfcd75ed1a3.png]]
![[_attachments/notion/AWS-Demogo-Prime/245172a556d6819f89e1ebcd1722b163.png]]
![[_attachments/notion/AWS-Demogo-Prime/245172a556d681c08827f5c4b2657c11.png]]
![[_attachments/notion/AWS-Demogo-Prime/245172a556d681e68a12eb3c6f7b86db.png]]
### AWS 데이터 저장
#### S3 Amazon Simple Storage Service
![[_attachments/notion/AWS-Demogo-Prime/245172a556d6817fb03dc1cfdf1289a0.png]]
![[_attachments/notion/AWS-Demogo-Prime/245172a556d68119b10bc16c4edecb22.png]]
### AWS 데이터 처리
- AWS Glue 데이터 카탈로그
  - 데이터 Schema확인을 데이터를 읽는 시점에 하는 것 Schema On Read
  - Insert할 때 스키마 체크를 하지 않음으로 빈번하게 데이터가 바뀔 수 있는 벡데이터 환경에 최적화된 방법
  - 반대 Schema On Write
#### AWS Glue 데이터 카탈로그
- 간편하고 확장 가능한 서버리스 ETL 서비스
![[_attachments/notion/AWS-Demogo-Prime/245172a556d6814abc69c799d49da5ca.png]]
#### Amazon Athena 표준 SQL을 통한 s3데이터 분석
- 서버 리스 환경
- s3에서 직접 쿼리 실행
### AWS 데이터 활용
#### Amazon QuickSight 인사이트 도출을 위한 클라우드 기반 시각화 도구
![[_attachments/notion/AWS-Demogo-Prime/245172a556d6815bba99c91a84b4cb3e.png]]
### AWS 데이터 파이프라인
#### Amazon MWAA - Managed Workflow of Apache Airflow
![[_attachments/notion/AWS-Demogo-Prime/245172a556d6812a86cffb5946a2c63b.png]]
## 큰 그림
![[_attachments/notion/AWS-Demogo-Prime/245172a556d681f1bd0afabb595fa7d7.png]]
## Demogo Prime Lab 아키텍쳐
MySQL 예시
![[_attachments/notion/AWS-Demogo-Prime/245172a556d681a3a639cedfff3bd923.png]]
몽고 디비 예시
![[_attachments/notion/AWS-Demogo-Prime/245172a556d681ac922ddb3633c4d9eb.png]]
Windows File 서버 예시
![[_attachments/notion/AWS-Demogo-Prime/245172a556d681c59939de3c8a5a1938.png]]
스트리밍 이벤트 예시
![[_attachments/notion/AWS-Demogo-Prime/245172a556d6816fbf40e5a529c54b99.png]]
외부 데이터 Naver API 에시
![[_attachments/notion/AWS-Demogo-Prime/245172a556d681fb8aacfdcc16bdeb38.png]]
오케스트레이션 예시
![[_attachments/notion/AWS-Demogo-Prime/245172a556d681b6b5f3c5ca19af50ad.png]]
## 실습 진행
- 하위 페이지: 실습 진행
## Workshop Architecture
  ![[_attachments/notion/AWS-Demogo-Prime/245172a556d681ef9a77e9bd4ae05220.png]]
### [AWS Database Migration Service란?](https://catalog.us-east-1.prod.workshops.aws/workshops/7f59c02a-e96d-414f-b513-f0da08844108/ko-KR/module3#aws-database-migration-service)
  AWS Database Migration Service는 데이터베이스를 AWS로 빠르고 안전하게 마이그레이션할 수 있도록 지원합니다. 마이그레이션하는 동안 소스 데이터베이스가 변함없이 운영되어 해당 데이터베이스를 사용하는 애플리케이션의 가동 중지 시간을 최소화할 수 있습니다. AWS Database Migration Service를 통해 짧은 대기 시간으로 지원되는 모든 소스에서 지원되는 모든 대상으로 데이터를 지속적으로 복제할 수 있습니다. 예를 들어 여러 소스에서 Amazon Simple Storage Service(Amazon S3)로 복제하여 뛰어난 가용성 및 확장성을 갖춘 데이터 레이크 솔루션을 구축할 수 있습니다.
### [실습 단계 소개](https://catalog.us-east-1.prod.workshops.aws/workshops/7f59c02a-e96d-414f-b513-f0da08844108/ko-KR/module3#)
  1.  이번 실습의 소스 데이터는 가상의 E-commerce 데이터를 MySQL 데이터베이스에 생성하였으며, EC2 인스턴스 위에 CloudFormation으로 자동 생성됩니다.
  1. DMS Replication instance는 생성에 시간이 소요되기 때문에 '실습 아키텍처 및 환경 구성 단계'에서 진행하였고 생성되는 동안 다른 파이프라인 구성을 진행하도록 워크샵이 구성되어 있습니다.
  1.  DMS 구성에 필요한 Source, Target endpoint를 순차적으로 생성하고 이를 task로 정의 하고 실행하면 MySQL에 저장된 데이터를 S3 버킷의 지정된 폴더로 전송하게 됩니다.
  1. 이렇게 수집한 최초의 데이터를 AWS 데이터 분석 서비스에서 활용할 수 있도록 AWS Glue Crawler에서 데이터 카탈로그 작업을 구성합니다.
  1. 이어 AWS Glue의 Spark Job을 이용해 Parquet 변환, 데이터 타입 변환, 데이터 암호화의 데이터 처리 작업을 수행해 봅니다.
  1. 가공된 데이터는 Athena를 통해 QuickSight에서 활용할 수 있는 데이터로 추가 가공하여 Data Mart로 구성하게 됩니다.
## 실습 자료 및 가이드 라인
## Module 0. MySQL 파이프라인
####  [Data Preparation](https://catalog.us-east-1.prod.workshops.aws/workshops/7f59c02a-e96d-414f-b513-f0da08844108/ko-KR/module3/3-1)
## Data Preparation
      테스트 데이터를 확인하기 위해 CloudFormation으로 생성된 [MySQL EC2 Instance ](https://ap-northeast-2.console.aws.amazon.com/ec2/home?region=ap-northeast-2#Instances:)에 접속하여 데이터베이스 상태를 확인합니다.
      1. 해당 인스턴스 선택 후 Connect 버튼을 클릭합니다.
      1. Session Manager를 선택하고 Connect 버튼을 클릭합니다.
      1. 인스턴스 콘솔 창에서 MySQL에 접속 한 후 demogo DB의 customers Table이 존재 하는지 확인합니다. DB 접속 계정과 패스워드는 admin, Demogo+2022 입니다.
      위와 같이 select * from demogo.customers limit 10; 명령어로 확인해봅니다.
      - MySQL이 설치된 EC2는 Source endpoint로 raw data 저장을 위해 생성한 S3 버킷은 Target endpoint로 구성합니다.
- 구성전에 두 가지 정보를 확인합니다. 이후 작업에서 값을 복사 붙여넣기 할 수 있도록 별도의 탭을 열어 확인합니다.
      1. 먼저 데이터 소스인 MySQL이 설치된 인스턴스 (demogo-workshop-MySQL)의 프라이빗 네트워크 주소를 확인합니다. (퍼블릭 네트워크 주소도 가능)
      1. DMS 를 위해 CloudFormation으로 생성한 IAM Role (Demogo-workshop-DMS-role)의 ARN을 확인합니다.
      이어서 다음 과정인 DMS 구성을 진행합니다
#### [Data Ingestion](https://catalog.us-east-1.prod.workshops.aws/workshops/7f59c02a-e96d-414f-b513-f0da08844108/ko-KR/module3/3-2)
## Data Ingestion
      [Endpoint 구성](https://catalog.us-east-1.prod.workshops.aws/workshops/7f59c02a-e96d-414f-b513-f0da08844108/ko-KR/module3/3-2#endpoint)
      1. 먼저 Source endpoint를 생성합니다. AWS DMS 콘솔의 Endpoints에서 Create endpoint 버튼을 클릭하여 생성을 시작합니다.
      1. Endpoint 생성 화면에서 아래 설정을 완료합니다.
      - Source endpoint가 선택된 상태에서 Endpoint identifier에 source endpoint를 구분할 수 있도록 demogo-dms-endpoint-mysql로 명명합니다.
      - Source engine은 MySQL을 선택 합니다.
      - Access to endpoint database 는 Provide access information manually를 선택합니다.
      - Server name에 앞서 확인한 네트워크 주소를 입력하고 Port는 MySQL의 기본 Port인 3306을 입력합니다.
      - 마지막으로 User name은 admin, Password는 Demogo+2022를 입력합니다.
      1. 이어서 하단의 Test endpoint connection (optional)을 확장하여 아래 과정을 수행합니다.
      - VPC를 눌러서 demogo-workshop-vpc를 클릭합니다.
      - 앞서 생성한 Replication instance가 선택 되었는지 확인 한 후 Run test 버튼을 클릭합니다.
      - 약 3분 후 Status 값이 successful로 바뀌는 것을 확인합니다. Failed 메세지가 발생할 경우 Replication instance에서 MySQL EC2 인스턴스로 접속이 안되는 경우입니다.
      - 앞서 입력한 Server name, Port, User name, Password 그리고 MySQL EC2 인스턴스의 Security Group의 inbound 정책을 다시 확인해봅니다.
      - Run test를 수행한 경우 endpoint가 생성되기 때문에 Create endpoint 버튼을 클릭하여 생성을 완료하고 Endpoint 메인 창에서 다시 Test connection을 시도합니다.
      1. 이어서 Target endpoint 생성을 진행하겠습니다. 생성 과정은 유사하지만 타겟 유형에 따라 입력 값이 달라집니다. 동일하게 Create endpoint 버튼을 클릭하여 생성을 시작합니다.
      1. Endpoint 생성 화면에서 아래 설정을 완료합니다.
      - Endpoint type으로 Target endpoint를 선택합니다.
      - Endpoint identifier에 Target endpoint를 구분할 수 있도록 demogo-dms-endpoint-s3로 명명합니다.
      - Target engine으로 Amazon S3를 찾아 선택합니다.
      - Service access role ARN은 앞서 확인을 위해 별도의 탭에 열어 둔 IAM Role (Demogo-workshop-DMS-role)의 ARN 값을 복사하여 붙여넣습니다.
      - Bucket name은 개인별로 생성한 버킷명을 입력하고 Bucket folder는 stage/mysql/을 입력합니다.
      1. Endpoint settings 를 펼친 후 Add new setting 버튼을 클릭하여 Setting 값에 AddColumnName, Value 값에 true 를 입력합니다.
      1. Source endpoint 생성시 수행한 테스트와 동일하게 Run test 버튼을 클릭하여 결과를 확인 한 후 Create endpoint 버튼을 클릭하여 생성을 완료합니다.
      만약 테스트가 Failed인 경우 앞서 생성한 IAM Role의 Policy 확인이 필요합니다. 워크샵의 환경과 동일하게 진행하셨다면 IAM Role의 Policy를 확인하시기 바랍니다.
      [Task 구성](https://catalog.us-east-1.prod.workshops.aws/workshops/7f59c02a-e96d-414f-b513-f0da08844108/ko-KR/module3/3-2#task)
      앞서 생성한 Replication instance가 Source endpoint 에서 데이터를 수집하여 Target endpoint인 S3로 저장하는 일련의 과정을 Task로 생성하겠습니다.
      1. [AWS DMS ](https://ap-northeast-2.console.aws.amazon.com/dms/v2/home?region=ap-northeast-2) 콘솔의 Database migration tasks에서 Create task 버튼을 클릭합니다.
      1. Create database migration task에서 아래 테이블을 참조하여 설정을 완료합니다.
      - Task identifier에 task 명을 입력합니다.
      - Replication instance에 앞서 생성한 인스턴스를 선택합니다.
      - Source database endpoint 와 Target database endpoint 에 앞서 생성한 endpoint를 입력합니다.
      1. Task settings에서 Task logs의 Enable CloudWatch logs를 체크합니다.
      1. Table mappings의 Add new selection rule 버튼을 클릭한 후 Schema는 Enter a schema를 선택하고 Source name은 demogo를 입력합니다.
      1. 그 외 나머지는 기본값으로 유지한 후 Create task 버튼을 클릭하여 task생성을 완료합니다.
2. Task 생성 후 자동으로 migration이 진행되도록 기본 옵션을 선택했습니다. 최종 상태가 Load complete으로 변경되면 S3 목적지 폴더로 이동하여 데이터를 확인합니다. 수동으로 task를 실행하고 싶은 경우 Actions 버튼을 클릭한 후 Restart/Resume을 선택하면 됩니다.
      1. 이후 MWAA를 구성하면 DMS는 정기적으로 MySQL 소스 데이터를 stage 폴더에 저장하게 되고 MWAA의 task를 통해 stage 내의 데이터는 raw 폴더에 실행날짜 별로 저장됩니다. 이를 통해 과거의 원천 데이터를 raw 폴더에 모두 저장 할 수 있게 됩니다. MWAA의 task 수행을 위해 stage의 데이터를 raw로 옮기는 작업을 진행합니다. 아래 표의 source 경로에서 파일을 선택한 후 해당되는 target 경로를 붙여 넣어 수행합니다.
      아래 3개 항목은 Optional입니다. 추후 QuickSight 대시보드를 완성할때 진행하시면 됩니다.
      1. Stage 폴더에 저장된 customers 테이블의 데이터 파일을 선택한 후 Actions 버튼을 클릭하여 Copy를 수행합니다.
      1. 팝업창의 Destination 항목에 Raw 폴더 경로를 복사해서 붙여 넣습니다. 버킷명은 실습자의 환경마다 다르기 때문에 Browse S3 버튼을 클릭하여 버킷을 선택한 후 하위 경로만 붙여 넣습니다. 목적지 전체 경로는 검색되지 않기 때문에 하위 경로는 아래 표를 참조하여 붙여넣습니다. 경로 입력 후 하단의 Copy 버튼을 클릭하여 완료합니다.
      1. 이어서 sessions 테이블의 데이터도 동일하게 Stage 폴더 경로에서 Raw 폴더 경로로 복사를 수행합니다.
      1. 데이터 복사가 잘 되었는지 raw 폴더에서 확인합니다
#### [Data Cataloging](https://catalog.us-east-1.prod.workshops.aws/workshops/7f59c02a-e96d-414f-b513-f0da08844108/ko-KR/module3/3-4)
## Data Cataloging
      저장된 raw 데이터에 대해 Glue Crawler를 이용하여 Catalog data를 생성합니다.
      1. [AWS Glue ](https://ap-northeast-2.console.aws.amazon.com/glue/home?region=ap-northeast-2) 콘솔의 Crawlers 에서 Create crawler 버튼을 클릭하여 생성을 시작합니다.
      1. MySQL 데이터 전용 crawler를 demogo-mysql-raw로 명명합니다.
      1. MySQL 데이터의 저장 위치를 지정합니다. Add a data source 버튼을 클릭하면 Add data source 팝업창이 나옵니다.
      1. Data source는 S3로 지정하고 S3 path에 저장 위치를 입력 또는 Browse 버튼을 클릭하여 선택합니다. (s3://demogo-AccountID-base/raw/mysql/demogo/)
      그리고
      Add an S3 data source
      버튼을 클릭 한 후,
      Next
      버튼을 클릭하여 다음 단계를 진행합니다.
      1. Crawler가 사용할 IAM role을 생성합니다. Create new IAM role 버튼을 클릭 한 후 팝업창에 나머지 이름을 입력합니다. 이후 Next버튼을 클릭하여 다음 단계를 진행합니다.
      만약 AWSGlueServiceRole-dp22로 생성된 Role이 이미 있다면, Update chosen IAM Role을 눌러서 업데이트를 진행해야 합니다
      1. Target database를 선택합니다. 사전에 CloudFormation으로 생성한 데이터베이스 (demogo_raw_db)를 선택합니다. Add database 버튼을 클릭하여 간단하게 생성할 수 있지만 워크샵의 전체 데이터 구조에 맞게 사전에 생성한 데이터베이스 선택을 권고드립니다. 테이블 구분을 위해 Table name prefix에 mysql-를 입력합니다.
      1. Create crawler 버튼을 클릭하여 생성을 완료합니다. 생성한 Crawler가 Ready 상태가 되면 Run 버튼을 클릭하여 실행합니다.
      1. Crawler 통해 생성된 카탈로그 데이터를 확인합니다. 먼저 Crawlers 창에서 5개의 테이블이 생성 된 것을 확인 할 수 있으며 View log를 클릭하여 세부 내용도 확인할 수 있습니다.
      다음으로
      [AWS Glue](https://ap-northeast-2.console.aws.amazon.com/glue/home?region=ap-northeast-2)
      콘솔의 Tables에서 새로 생성된 카탈로그 데이터 테이블을 확인 할 수 있습니다.
#### [Data Processing](https://catalog.us-east-1.prod.workshops.aws/workshops/7f59c02a-e96d-414f-b513-f0da08844108/ko-KR/module3/3-5)
## Data Processing
      MySQL 데이터의 ETL 작업은 스크립트를 이용하여 진행합니다. 이후 MongoDB에서는 GUI를 이용한 방법을 소개해 드립니다.
      1. 먼저 아래 URL을 클릭 또는 브라우저 주소창에 입력하여 스크립트 5개를 실습자의 로컬 디스크에 다운로드 받습니다.
      - [https://demogo-shared-artifacts.s3.ap-northeast-2.amazonaws.com/mysql_glue_script/demogo_mysql_raw_customers.py](https://demogo-shared-artifacts.s3.ap-northeast-2.amazonaws.com/mysql_glue_script/demogo_mysql_raw_customers.py)
      - [https://demogo-shared-artifacts.s3.ap-northeast-2.amazonaws.com/mysql_glue_script/demogo_mysql_raw_sessions.py](https://demogo-shared-artifacts.s3.ap-northeast-2.amazonaws.com/mysql_glue_script/demogo_mysql_raw_sessions.py)
      아래 3개는 Optional 입니다. QuickSight 대시보드를 완성하고 싶을 때 진행합니다
      https://demogo-shared-artifacts.s3.ap-northeast-2.amazonaws.com/mysql_glue_script/demogo_mysql_raw_orders.py
https://demogo-shared-artifacts.s3.ap-northeast-2.amazonaws.com/mysql_glue_script/demogo_mysql_raw_order_detailed.py
https://demogo-shared-artifacts.s3.ap-northeast-2.amazonaws.com/mysql_glue_script/demogo_mysql_raw_products.py
      1. 다음으로 [AWS Glue Studio ](https://ap-northeast-2.console.aws.amazon.com/gluestudio/home?region=ap-northeast-2) 콘솔로 이동합니다.
      - 좌측 메뉴의 Jobs를 클릭합니다.
      - Create job 창에서 Spark script editor를 선택한 후 Options에서 Upload and edit an existing script를 선택합니다.
      - Choose file 버튼을 클릭하여 다운로드 받은 스크립트를 선택합니다.
      - 먼저 demogo_mysql_raw_customers.py 를 선택합니다.
      - 파일은 한번에 한 개씩만 업로드 됩니다. 업로드 후 Create 버튼을 클릭합니다.
      1. 업로드된 스크립트의 S3 버킷 경로를 수정합니다. demogo_mysql_raw_customers.py 파일의 경우 50번째 행에 수정해야할 S3 경로가 있습니다. 실습자의 어카운트에서 생성된 S3 버킷명을 확인하여 수정합니다.
      1. 업로드 된 script 첫 행에 job 명이 주석 처리 되어있습니다. Job 명을 복사합니다. (# 제외)
      1. Job details에서 아래 설정을 완료합니다.
      - Name에 복사한 Job 명을 붙여넣습니다.
      - IAM Role은 CloudFormation으로 생성한 Demogo-workshop-Glue-role을 선택합니다.
      - 신속한 상태 확인을 위해 Number of retries는 0, Job timeout은 10으로 변경합니다.
      - 하단의 Advanced properties 를 클릭하여 확장시킨 후 Job parameters를 2개 입력합니다.
      Key : --class, Value : GlueApp
Key : --EXECUTION_DATE, Value : 221009
      1. 우측 상단의 Save 버튼을 클릭합니다.
      1. 두번째 스크립트 demogo_mysql_raw_sessions.py를 업로드 후 create 하겠습니다. 수정해야할 스크립트는 27번 행에 있습니다.
      Job details탭의 내용을 업데이트 한 후 Save 버튼을 클릭합니다.
      아래 8, 9, 10번은 Optional 입니다. QuickSight 대시보드를 완성하고 싶을 때 진행합니다
      1. (Optional) 세번째 스크립트 demogo_mysql_raw_orders.py 를 업로드 후 create 하겠습니다. 앞의 과정과 동일하게 job을 생성합니다. 수정해야할 스크립트는 27번 행에 있습니다.
      Job details 탭의 내용을 업데이트 한 후 Save 버튼을 클릭합니다.
      1. (Optional) 네 번째 스크립트 demogo_mysql_raw_order_detailed.py를 업로드 후 create 하겠습니다. 수정해야할 스크립트는 27번 행에 있습니다.
      Job details탭의 내용을 업데이트 한 후 Save 버튼을 클릭합니다.
      1. (Optional) 다섯 번째 스크립트 demogo_mysql_raw_products.py를 업로드 후 create 하겠습니다. 수정해야할 스크립트는 27번 행에 있습니다.
      Job details탭의 내용을 업데이트 한 후 Save 버튼을 클릭합니다.
      1. [AWS Glue Studio ](https://ap-northeast-2.console.aws.amazon.com/gluestudio/home?region=ap-northeast-2) 콘솔 좌측 메뉴의 Jobs를 선택하여 생성된 2개의 job을 확인합니다. 그리고 한 개씩 선택 후 Run job 버튼을 클릭하여 job을 실행합니다.
      1. Job이 정상적으로 수행되면 Runs 탭에서 Run status Succeeded을 확인할 수 있습니다.
      그리고 AWS Glue 콘솔의 Tables 창을 확인하면 parquet로 변경된 demogo_created_db의 테이블들을 확인할 수 있습니다.
      마지막으로 Amazon S3의 curated 폴더를 확인해 보면 ETL의 결과 파일을 확인할 수 있습니다.
      지금까지 MySQL의 데이터를 S3에 넣고 분석에 필요한 형태로 정제하는 과정까지 진행해 봤습니다. 다음으로 이러한 데이터를 활용해 볼 수 있어야 하는데요, AWS에서는 크게 Athena와 Redshift라는 서비스를 제공하고 있습니다. Athena는 간단하고 저렴하게 데이터 분석에 사용해 볼 수 있는 서비스이고, Redshift는 DW 서비스로써 본격적으로 분석에 활용하고자 하면 도입을 고려해 볼 수 있습니다.
      이번 실습에서는 Athena를 이용하여 가져온 데이터를 분석하고, 데이터 시각화를 위해 Data Mart를 생성해 보도록 하겠습니다.
      [Amazon Athena란?](https://catalog.us-east-1.prod.workshops.aws/workshops/7f59c02a-e96d-414f-b513-f0da08844108/ko-KR/module3/3-5#amazon-athena)
      Amazon Athena는 표준 SQL을 사용하여 Amazon S3에 있는 데이터를 직접 간편하게 분석할 수 있는 대화형 쿼리 서비스입니다. Athena는 서버리스 서비스로 관리할 인프라가 없으며 비용 또한 사용한 만큼만 지불하여 간단한 워크로드에서 사용하기 좋습니다. 또한, 자동으로 확장되어 쿼리를 병렬로 실행하기 때문에 대규모 질의에서도 빠르게 결과를 얻을 수 있습니다.
      > Amazon Athena, Amazon EMR, Amazon Redshift 등 여러 비슷한 서비스를 어느 상황에서 사용해야 할 지 고민이 될 때가 많습니다. 다음 링크를 통해 현재 상황에 맞는 서비스를 선택하는 것도 좋은 방법입니다. https://docs.aws.amazon.com/ko_kr/athena/latest/ug/when-should-i-use-ate.html
      [Athena 세팅](https://catalog.us-east-1.prod.workshops.aws/workshops/7f59c02a-e96d-414f-b513-f0da08844108/ko-KR/module3/3-5#athena)
      1. [Athena ](https://ap-northeast-2.console.aws.amazon.com/athena/home?region=ap-northeast-2)를 선택하여 이동합니다.
      1. Explore the query editor 버튼을 누릅니다.
      1. Edit settings를 클릭합니다.
      1. Query result location에 아래 값을 입력합니다. Assign bucket owner full control over query results 항목을 체크합니다. 그리고 save 버튼을 누릅니다.
      s3 location :
      ```plain text
aws-athena-query-results-ap-northeast-2-${ACCOUNT-ID}
      ```
      Assign bucket owner :
      ```plain text
check
      ```
      1. Editor 버튼을 눌러서 편집 화면으로 이동합니다.
      1. Database를 아래 그림과 같이 세팅하고, mysql-customers테이블 우측 탭을 눌러서 Preview Table 버튼을 클릭합니다.
      1. 화면에 데이터가 나오는 것을 확인합니다.
      [Data Mart 구성](https://catalog.us-east-1.prod.workshops.aws/workshops/7f59c02a-e96d-414f-b513-f0da08844108/ko-KR/module3/3-5#data-mart)
      Athena의 기본 세팅이 끝났으니, 이제 시각화에 사용할 Data Mart를 구성해 보겠습니다.
      1. MAU(Monthly Active Users) 월간 활성 사용자에 대한 테이블을 아래와 같이 구성합니다.
      다음 쿼리문을 복사하여 Query editor 창에 붙여넣고, 4번 행의 external_location 에서 'demogo-어카운트ID-base'를 실습자의 S3 버킷명으로 변경합니다. 입력 및 수정이 완료되면 Run again 버튼을 클릭하여 쿼리문을 실행합니다. 쿼리문을 통해 생성된 테이블은 이후 QuickSight에서 사용됩니다.
      1
2
3
4
5
6
7
8
9
10
11
12
CREATE TABLE demogo_app_db.monthly_active_users
WITH (
    format = 'PARQUET',
    external_location = 's3://demogo-어카운트ID-base/app/mart/demogo_app_db/monthly_active_users/',   /* Change Bucket name */
    write_compression = 'SNAPPY'
)
AS
SELECT
       CAST(count(DISTINCT customer_id) * random() * 1000000 as INT) AS user_count,
       SUBSTR(created_at, 1, 7) AS month
FROM demogo_curated_db."mysql-sessions"
GROUP BY SUBSTR(created_at, 1, 7)
      아래 2,3번은 Optional 입니다. QuickSight 대시보드를 완성하고 싶을 때 진행합니다
      1. (Optional) 연간 매출 데이터를 아래와 같이 구성합니다. (Optional, glue 작업을 5개 테이블에 대해 모두 수행한 경우에 진행 가능)
      다음 쿼리문을 복사하여 Query editor 창에 붙여넣고, 4번 행의 external_location 에서 'demogo-어카운트ID-base'를 실습자의 S3 버킷명으로 변경합니다. 입력 및 수정이 완료되면 Run again 버튼을 클릭하여 쿼리문을 실행합니다. 쿼리문을 통해 생성된 테이블은 이후 QuickSight에서 사용됩니다.
      1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
CREATE TABLE demogo_app_db.total_sales_yoy
WITH (
    format = 'PARQUET',
    external_location = 's3://demogo-어카운트ID-base/app/mart/demogo_app_db/total_sales_yoy/',  /* Change Bucket name */
    write_compression = 'SNAPPY'
)
AS
WITH CALCULATED_PRICE AS (
    SELECT
    t1.order_id,
    CAST(t1.quantity * CAST(t2.price as DECIMAL(10,3)) as INT) / 1000 * 1000 as calculated_price
    FROM demogo_curated_db."mysql-order_detailed" AS t1
    LEFT OUTER JOIN demogo_curated_db."mysql-products" AS t2
    ON t1.product_id = t2.product_id
)
SELECT
    SUBSTR(t1.order_date, 1, 4) as year,
    sum(t2.calculated_price) as price
FROM demogo_curated_db."mysql-orders" AS t1
LEFT OUTER JOIN CALCULATED_PRICE AS t2
ON t1.order_id = t2.order_id
WHERE t1.status = 'Completed'
GROUP BY SUBSTR(t1.order_date, 1, 4)
ORDER BY year DESC;
      1. (Optional) 카테고리별 매출 데이터를 구성합니다. (Optional, glue 작업을 5개 테이블에 대해 모두 수행한 경우에 진행 가능)
      다음 쿼리문을 복사하여 Query editor 창에 붙여넣고, 4번 행의 external_location 에서 'demogo-어카운트ID-base'를 실습자의 S3 버킷명으로 변경합니다. 입력 및 수정이 완료되면 Run again 버튼을 클릭하여 쿼리문을 실행합니다. 쿼리문을 통해 생성된 테이블은 이후 QuickSight에서 사용됩니다.
      1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
CREATE TABLE demogo_app_db.total_sales_by_category_yoy
WITH (
    format = 'PARQUET',
    external_location = 's3://demogo-어카운트ID-base/app/mart/demogo_app_db/total_sales_by_category_yoy/',  /* Change Bucket name */
    write_compression = 'SNAPPY'
)
AS
WITH CALCULATED_PRICE_BY_CATEGORY AS (
    SELECT
    t1.order_id,
    t2.category,
    t2.sub_category,
    CAST(t1.quantity * CAST(t2.price as DECIMAL(10,3)) as INT) / 1000 * 1000 as calculated_price
    FROM demogo_curated_db."mysql-order_detailed" AS t1
    LEFT OUTER JOIN demogo_curated_db."mysql-products" AS t2
    ON t1.product_id = t2.product_id
)
SELECT
    t2.category,
    t2.sub_category,
    t2.calculated_price,
    t1.order_date
FROM demogo_curated_db."mysql-orders" AS t1
LEFT OUTER JOIN CALCULATED_PRICE_BY_CATEGORY AS t2
ON t1.order_id = t2.order_id
WHERE t1.status = 'Completed';
      여기까지 간단하게 Data Mart를 Amazon Athena를 사용하여 구성해 봤습니다. 이 테이블들은 시각화 도구에서 사용하기 편한 상태로 구성한 것이며 비즈니스 요건에 맞춰서 생성되는 최종 테이블 형태라고 생각하시면 되겠습니다. 다음으로는, Amazon Quicksight를 이용하여 해당 데이터를 시각화 해보도록 하겠습니다.
#### [Data Consumption](https://catalog.us-east-1.prod.workshops.aws/workshops/7f59c02a-e96d-414f-b513-f0da08844108/ko-KR/module3/3-7)
## Data Consumption
      이전 모듈에서 데이터 시각화를 위한 Mart 구성을 진행하였습니다. 이러한 데이터를 바탕으로 Amazon QuickSight 서비스를 활용하여 손쉽게 시각화를 할 수 있습니다.
      [Amazon QuickSight란?](https://catalog.us-east-1.prod.workshops.aws/workshops/7f59c02a-e96d-414f-b513-f0da08844108/ko-KR/module3/3-7#amazon-quicksight)
      Amazon QuickSight는 클라우드 비즈니스 인텔리전스(BI) 서비스입니다. 다양한 데이터 소스로부터 데이터를 가져와서 손쉽게 시각화 할 수 있는 방법을 제공합니다. 단일 대시보드에서 AWS 데이터, 타사 데이터, B2B 데이터 등을 포함할 수 있습니다. 완전관리형 서비스로써 인프라 관리를 사용자가 하지 않아도 괜찮습니다.
      [QuickSight 세팅](https://catalog.us-east-1.prod.workshops.aws/workshops/7f59c02a-e96d-414f-b513-f0da08844108/ko-KR/module3/3-7#quicksight)
      1. [Amazon QuickSight ](https://quicksight.aws.amazon.com/)로 이동합니다.
      1. Sign up for QuickSight를 누릅니다.
      1. Standard 버튼을 클릭합니다.
      1. Seoul region을 선택하고, account와 email을 입력합니다. (account는 유일한 값이어야 하므로 이름등을 넣으시는걸 추천합니다)
      1. QuickSight access to AWS Services에서 아래와 같이 설정하고, S3를 체크합니다.
      1. Select all 버튼을 누르고 Finish 버튼을 누릅니다.
      1. Finish 버튼을 누릅니다.
      1. QuickSight 환경이 구성되는데 약 1분가량 소요됩니다. 완료되면 아래 버튼을 클릭합니다.
      1. 좌측 탭의 Datasets를 클릭합니다.
      1. 우측 New dataset을 클릭합니다.
      1. Athena를 클릭합니다.
      1. Data source name을 입력하고 Create data source 버튼을 누릅니다.
      1. database를 선택하고 table을 선택합니다. 그리고 select 버튼을 누릅니다.
      1. Email은 체크 해제하고 Visualize를 클릭합니다.
      1. 좌측 탭 user_count 항목을 클릭합니다. 그러면 기본적인 Sum of User_count가 Sheet에 표기됩니다. 우리는 월별 평균 접속자를 보고 싶으므로, sum에서 average로 바꿔줄 필요가 있습니다. 상단 #user_count(sum)을 클릭합니다.
      1. Value를 누르고, Aggregate를 누른다음 Average를 클릭합니다.
      1. 화면과 같이 숫자가 평균값으로 바뀐 것을 볼 수 있습니다. 연필 모양 아이콘을 클릭합니다.
      1. 좌측 Title, Edit title 버튼을 클릭합니다.
      1. Average MAU를 입력하고 가운데 정렬 후 Save를 누릅니다.
      1. 숫자가 너무 크므로 단위를 조정해보겠습니다. 다시 상단 user_count Value를 클릭하고 Format, More formatting options를 눌러서 좌측 Units에서 Thousands로 바꿔보겠습니다.
      1. 이어서 MAU 그래프도 구성해 보겠습니다. 좌측 상단 +ADD 버튼을 누르고 Add visual을 누릅니다.
      1. 좌측 하단에서 꺾은선 그래프 모양을 클릭합니다.
      1. 현재 month가 text값이라 정렬이 제대로 되지 않습니다. month를 date type으로 바꿔보도록 하겠습니다. 좌측 상단 연필을 클릭해주세요.
      1. Edit 버튼을 클릭해 줍니다.
      1. month 컬럼 밑 String을 눌러서 Date로 바꿉니다.
      1. yyyy-MM 을 타이핑하고 Update 버튼을 누릅니다.
      1. 우측 상단 Publish & Visualize 버튼을 누릅니다.
      1. month와 user_count를 순서대로 눌러서 X axis에 month가, Y axis에 user_count가 들어가도록 합니다. 이후 user_count의 Aggregate를 Max로 바꿉니다.
      1. MAU Mart 데이터로부터 아래와 같은 components를 구성하였습니다.
      1. (Optional) 이외에도 Athena Data Mart 파트에서 추가로 구성한 다른 테이블을 위와 같은 과정을 거쳐서 최종적으로 아래와 같은 대시보드를 구성할 수 있습니다.
      아래 대시보드를 구성하기 위해서는 Module 0. MySQL 파이프라인에서 5개 테이블에 대해 모두 처리 작업을 해야 가능합니다
      여기까지 시각화 단계를 마무리합니다. 이로써 데이터 수집부터 처리, 활용까지 기나긴 내용을 같이 살펴보았습니다. 다음으로는 이러한 복잡한 과정을 매번 반복하지 않기 위해 Orchestration 서비스를 이용하여 자동화 하는 부분을 진행해 보도록 하겠습니다.
## Module 1. External Data 파이프라인
#### [Data Crawling](https://catalog.us-east-1.prod.workshops.aws/workshops/7f59c02a-e96d-414f-b513-f0da08844108/ko-KR/module4/4-1)
## Data Crawling
      이번 단계에서는Naver API를 호출하여 JSON 형식의 응답을 받아와, CSV 형태로 바꿔 S3에 저장하는 함수를 AWS Lambda로 구현 할 것입니다.
      Naver API 사용을 위해 [https://developers.naver.com/ ](https://developers.naver.com/) 에서 회원가입, 어플리케이션 등록을 하셔야 합니다. 어플리케이션 등록 시 사용 할 API에 데이터랩(검색어트랜드)를 추가 해 주세요. 등록이 마친 후, 좌측 애플리케이션 목록에서 등록한 애플리케이션을 클릭합니다. API 호출을 위해서는 우측에 보이는 Client ID와 Client Secret가 필요하기 때문에 복사 해 두시길 바랍니다.
      1. AWS Console에서 [AWS Lambda ](https://ap-northeast-2.console.aws.amazon.com/lambda/home?region=ap-northeast-2)로 이동합니다.
      1. 우측 상단의 Create function을 클릭합니다.
      1. Function name을 demogo-external-crawler로, Runtime을 Python 3.8, Execution Role에 Create a new role with basic Lambda permission을 선택 한 후 Create function을 클릭합니다.
      1. 아래 코드를 복사합니다.
      ```python
import csv
import json
import boto3
import datetime
import urllib.request

BUCKET = 'demogo-account-base' 

class naverKeywordAPI():
    def __init__(self, clientId, clientSecret):
        self.url = 'https://openapi.naver.com/v1/datalab/search'
        self.clientId = clientId
        self.clientSecret = clientSecret
        self.keywordGroups = []
        self.payload = {
            'startDate': '',
            'endDate': '',
            'timeUnit': '',
            'keywordGroups': []
        }

    def add_keyword_group(self, group_name, *keywords):
        keywordGroup = {
            'groupName': group_name,
            'keywords': keywords
        }
        self.keywordGroups.append(keywordGroup)

    def get_data(self, start_date, end_date, time_unit, **kwargs):
        self.payload['startDate'] = start_date
        self.payload['endDate'] = end_date
        self.payload['timeUnit'] = time_unit
        self.payload['keywordGroups'] = self.keywordGroups
        
        paramKeys= ['device', 'gender', 'ages']
        for key, value in kwargs.items():
            if key in paramKeys:
                self.payload[key] = value

        requestBody = json.dumps(self.payload, ensure_ascii=False)

        request = urllib.request.Request(self.url)
        request.add_header("X-Naver-Client-Id",self.clientId)
        request.add_header("X-Naver-Client-Secret",self.clientSecret)
        request.add_header("Content-Type","application/json")
        response = urllib.request.urlopen(request, data=requestBody.encode("utf-8"))
        rescode = response.getcode()
        if(rescode==200):
            response_body = response.read()
            # print(response_body.decode('utf-8'))
            return response_body
        else:
            print("Error Code:" + rescode)

def transform_json_to_csv(json_data, gender, age):
    target_data = []
    end_date = json_data['endDate']
    for i in json_data['results']:
        for j in i['data']:
            target_data.append({
                'gender':gender,
                'age':age,
                'title':i['title'],
                'period':j['period'],
                'ratio':j['ratio']
            })
    output_file = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    output_path = '/tmp/{}.csv'.format(output_file)
    with open(output_path, 'w', newline='', encoding='utf-8') as csv_file:
        new_val = ['gender','age','title','period','ratio'] 
        j = csv.DictWriter(csv_file, fieldnames=new_val)
        j.writeheader()
        j.writerows(target_data)

    prefix = 'raw/external'
    s3_resource = boto3.resource('s3')
    bucket = s3_resource.Bucket(BUCKET)
    bucket.upload_file(output_path, f'{prefix}/end_date={end_date}/{output_file}.csv')
    print(f'{prefix}/end_date={end_date}/{output_file}.csv is upload')

def lambda_handler(event, context):
    naver_api = naverKeywordAPI(event['client_id'], event['client_secret'])
    naver_api.add_keyword_group('나이키', '나이키', 'NIKE')
    naver_api.add_keyword_group('뉴발란스', '뉴발란스', '뉴발', 'New Balance')
    naver_api.add_keyword_group('휠라', '휠라', 'FILA')
    naver_api.add_keyword_group('룰루레몬', '룰루레몬', 'Lulu lemon')
    naver_api.add_keyword_group('아디다스', '아다스', 'ADIDAS')
    start_date = '2020-01-01'
    end_date = str(datetime.datetime.now())[:10]
    time_unit = 'date'

    for gender in ('f', 'm'):
        for age in range(1,12):
            response = naver_api.get_data(start_date, end_date, time_unit, ages=[str(age)], gender='m')
            original_json = json.loads(response)
            transform_json_to_csv(original_json, gender, age)

    return {
        'statusCode': 200,
        'body': json.dumps('crawling done')
    }
      ```
      1. 복사 한 코드를 lambda_function 칸에 붙여넣습니다. 7번째 줄 BUCKET 변수 값을 앞서 생성한 S3 버킷명으로 바꿔줍니다.
2. Deploy 버튼을 눌러 코드를 배포 합니다.
      1. 화면 상단에 초록색으로 함수가 업데이트 된 것을 확인한 다음, Configuration 탭으로 이동합니다.
      1. 화면 상단에 초록색으로 함수가 업데이트 된 것을 확인한 다음, Configuration 탭으로 이동 해 람다 함수의 설정들을 바꿔 보겠습니다.
2. 이번에 만든 외부 API 크롤링을 위한 람다 함수는 실행시간이 오래 걸리기 때문에, 람다함수의 실행 제한시간을 3초에서 10분으로 바꿔 줄 예정입니다. General configuration 우측에 Edit를 클릭 하세요
      1. Timeout 항목을 10 min으로 바꾼 후 화면 하단의 Save를 클릭하세요.
      1. 이제 람다 함수가 S3 버켓에 접근할 수 있도록 권한을 줘 보도록 하겠습니다. 람다함수의 Configuration 탭에서 왼쪽 메뉴의 Permissions를 클릭하세요. 그리고 Execution role에 Role name으로 나온 항목을 클릭 해 새 탭으로 링크를 열겠습니다.
      1. 새 탭에서 열린 IAM Role 화면입니다. 람다함수를 실행할 때 사용되는 Role에 대한 관리 화면입니다. 우리는 이 Role에 S3 접근 권한을 추가해야 하기 때문에, Add Permission > Attach policies를 클릭 합니다.
      1. 정책을 추가하는 화면입니다. Filter 란에 S3를 입력하고 엔터를 치시면, S3 관련한 정책들이 나오게 됩니다. 이번 워크샵에서는 AmazonS3FullAccess를 선택하고 Attach Policies 버튼을 클릭 해 정책을 추가하도록 하겠습니다.
      1. 다시 람다 함수 탭으로 돌아가보겠습니다. Test 탭을 클릭 해, 람다함수를 테스트 하기 위한 Json 요청서식을 만들어 보겠습니다. Event name을 원하는 이름으로 작성 합니다. 아래 코드를 복사해 Event JSON 필드에 붙여넣으시고, 앞서 복사해 둔 client id와 client secret 값으로 바꾸세요. 그리고 Save 버튼을 클릭 해 요청서식을 저장합니다.
      {
  "client_id": "<your client id>",
  "client_secret": "<your client secret>"
}
      1. Code 탭으로 이동한 후, Test를 클릭 해 실제 람다 함수가 작동하는지 확인합니다.
      1. 크롤링은 약 3-5분 정도 기다리면 완료됩니다. 정상적으로 완료 되었다면 StatusCode가 200으로 나오며, Execution result 탭에서 다음과 같이 S3에 저장된다는 로그파일을 확인 할 수 있습니다.
      지금까지 AWS Lambda 함수를 통해 진행 한 부분은 Naver API를 통해 Json 형태의 데이터를 받아서, 오른쪽의 형식을 가진 CSV 파일로 S3에 저장하는 내용이었습니다. Next 페이지로 넘어가서 Data cataloging을 진행 해 보세요.
#### [Data Cataloging](https://catalog.us-east-1.prod.workshops.aws/workshops/7f59c02a-e96d-414f-b513-f0da08844108/ko-KR/module4/4-2)
## Data Cataloging
      Data Catalog - AWS Glue Crawlers 저장된 raw 데이터에 대해 Glue Crawler를 이용하여 Catalog data를 생성합니다.
      1. [AWS Glue ](https://ap-northeast-2.console.aws.amazon.com/glue/home?region=ap-northeast-2) 콘솔의 [Crawlers ](https://ap-northeast-2.console.aws.amazon.com/glue/home?region=ap-northeast-2#/v2/data-catalog/crawlers) 에서 Create crawler 버튼을 클릭하여 생성을 시작합니다.
      1. 외부데이터 전용 crawler를 명명합니다 (demogo-external-raw)
      1. 데이터의 저장 위치를 지정합니다. Add a data source 버튼을 클릭하면 Add data source 팝업창이 나옵니다.
      1. Data source는 S3로 지정하고 S3 Path에 저장위치를 입력 또는 Browse 버튼을 클릭하여 선택합니다 (s3://Bucket-name/raw/external/). 그 다음 Add an S3 data source 버튼을 클릭한 후 Next 버튼을 클릭합니다.
      1. Crawler가 사용할 IAM role을 생성합니다. Create new IAM role 버튼을 클릭한 후 팝업창에 나머지 이름을 입력합니다. Next 버튼을 클릭하여 다음 스텝으로 진행합니다.
      만약 AWSGlueServiceRole-dp22로 생성된 Role이 이미 있다면, Update chosen IAM Role을 눌러서 업데이트를 진행해야 합니다
      1. Target database는 demogo_raw_db 데이터베이스를 선택하고 Next 버튼을 클릭합니다.
      1. Create crawler 버튼을 클릭하여 생성을 완료 합니다. 생성한 Crawler가 Ready 상태가 되면 Run 버튼을 클릭하여 실행합니다.
#### [Data Processing](https://catalog.us-east-1.prod.workshops.aws/workshops/7f59c02a-e96d-414f-b513-f0da08844108/ko-KR/module4/4-3)
## Data Processing
      현재 S3로 수집된 데이터는 CSV 형태의 File Format을 가지고 있습니다. Big Data 환경에서 분석을 용이하게 하기 위해 Parquet File Format으로 변경하고, 데이터 저장 공간 효율 향상과 비용 절감을 위해 압축 등을 수행해야 합니다. 이외에도 서비스에서 필요한 데이터로 가공하거나 데이터를 암호화 하는 등 여러가지 처리를 이 단계에서 진행하는데, AWS Glue의 Spark Job을 통해 작업을 구성합니다.
      1. [AWS Glue ](https://ap-northeast-2.console.aws.amazon.com/glue/home?region=ap-northeast-2)의 좌측 메뉴에서 AWS Glue Studio > [Jobs ](https://ap-northeast-2.console.aws.amazon.com/gluestudio/home?region=ap-northeast-2#/jobs)를 클릭합니다.
      1. Visual with a soource and target을 누르고 Create 버튼을 클릭합니다.
      1. Job Name을 demogo_external_curated로 변경하고, Data-source를 클릭하여 database와 table을 demogo_raw_db, external로 선택합니다.
      1. Data target을 클릭하여 Format과 Compression Type, S3 Target Location을 변경합니다. S3 Target Location은 s3://버킷명/curated/external/로 지정합니다. Database는 demogo_curated로 선택하시고, Table은 external로 지정합니다. 끝으로 Add a Partition Key를 클릭 후 end_date를 선택합니다.
      1. Job details를 클릭하여 IAM Role, Role, bookmark, number of retries, job timeout을 아래와 같이 설정합니다.
      - IAM Role: Demogo-workshop-Glue-role
      - Job bookmark: Disable
      - Number of retries: 1
      - Job timeout: 5
      1. 우측 상단의 Save 버튼을 클릭합니다. 성공적으로 Job이 업데이트 되었다면, 이어서 Run을 클릭합니다.
      1. Runs 탭을 확인 하여 현재 Job의 실행 상태를 확인합니다.
      1. Run status가 Succeeded로 바뀌었다면 S3로 들어가서 데이터를 확인 해 봅니다.
      1. 데이터가 있다면, Glue의 Data Catalog도 Parquet으로 만들어졌는지 확인합니다. 데이터가 정상적으로 들어왔는지 확인하기 위해 Table Data를 클릭합니다. Amazon Athena로 연결되도록 Proceed를 클릭 합니다.
      1. Data에서 demogo-external-curated Job의 data target으로 지정 했던demogo_curated_db의 external 테이블을 선택 해 Preview Table을 실행합니다.
      1. 쿼리 결과가 잘 나오는지 확인 합니다.
      [Athena 사전 설정 ](https://catalog.us-east-1.prod.workshops.aws/workshops/7f59c02a-e96d-414f-b513-f0da08844108/ko-KR/module3/3-5#athena)을 하지 않았다면 Query가 무한 pending 상태가 될 수 있습니다.
      지금까지 S3에 CSV 형태로 저장 된 외부 데이터를 Glue Data Catalog로 담고, Parquet형태로 변환, 데이터 저장 공간 효율 향상과 비용 절감을 위해 압축 등을 수행 했습니다. 이를 Amazon Athena를 통해 조회하는 것 까지 해 보았습니다. Amazon Quicksight를 시각화는 MySQL의 시각화와 동일하게 진행이 가능하므로 본 워크샵에서는 다루지 않습니다.
## Module 2. MongoDB 파이프라인 (Optional)
#### Data Ingestion
      이번 단계에서는 AWS Data Migration Service를 이용하여 MongoDB에서 S3로 데이터를 이동시킬 것입니다.
      1. [AWS 콘솔 ](https://ap-northeast-2.console.aws.amazon.com/console/home?region=ap-northeast-2)에 로그인합니다.
2. 다음 단계로 진입하기 전에, 사전 세팅에서 설치해둔 MongoDB의 DNS 정보를 얻어와야 합니다.
3. MongoDB가 설치된 [EC2 ](https://ap-northeast-2.console.aws.amazon.com/ec2/home?region=ap-northeast-2)로 이동합니다. EC2는 준비 단계에서 수행한 Cloudformation stack을 통해 자동 생성된 자원입니다.
      1. 검색 창에 demogo 를 입력합니다.
      1. demogo-mongo Instance ID를 클릭합니다.
      1. Public IPv4 DNS 정보를 저장하여 Notepad등에 저장해 둡니다. (추후 사용합니다)
      1. 다시 AWS DMS 콘솔 화면으로 돌아가서, 좌측 Endpoints를 눌러 화면을 이동합니다.
      1. Create endpoint 버튼을 클릭합니다.
      > endpoint란 AWS DMS가 데이터를 가져올 source와 target에 대한 정보를 구성하는 것을 말합니다.
      1. endpoint type은 source endpoint 그대로 두고 넘어갑니다.
      1. Endpoint identifier, Source engine, Access to endpoint database를 아래와 같이 입력합니다.
      - Endpoint identifier: demogo-mongo
      - Source engine: MongoDB
      - Access to endpoint database: Provide access information manually
      > Access to endpoint database는 AWS Secrets Manager를 활용하면 더 안전하게 접속 정보를 관리할 수 있지만, 이번 Lab에서는 편의성을 위해 manual로 입력합니다.
      1. 6번에서 미리 복사해 둔 MongoDB EC2의 Public IPv4 DNS을 Server Name에 입력합니다.
      - Server name: 미리 복사해 둔 Public IPv4 DNS 붙여넣기
      - Port: 27017
      - Authentication mode: Password
      - User name: demogo
      - Password: demogo
      - Authentication source: admin
      - Database name: demogo
      - Metadata mode: table
      - Number of documents to scan: 1000
      1. Create endpoint 버튼을 눌러 endpoint를 생성합니다.
      1. endpoint가 정상적으로 생성되었는지 확인하고, Name을 클릭합니다.
      1. Connections - Test connections 버튼을 누릅니다.
      1. Run Test 버튼을 클릭하여 MongoDB와 DMS instance 사이 연결성을 확인합니다. (이 작업에는 1-2분 가량 시간이 소요됩니다)
      1. Status 성공을 확인합니다.
      1. 다음으로 S3 target endpoint를 생성하기 전에, service에 접근하기 위해 IAM Role의 ARN을 가져와야 합니다. [IAM ](https://console.aws.amazon.com/iam/home?region=ap-northeast-2) 으로 이동합니다.
      1. 좌측의 Roles를 클릭하고 검색 창에서 dms를 검색합니다. 이후 Demogo-workshop-DMS-role을 클릭합니다.
      1. Role의 ARN을 복사하여 notepad 등에 저장해 둡니다. (추후 활용됩니다)
      1. [AWS DMS ](https://ap-northeast-2.console.aws.amazon.com/dms/v2/home?region=ap-northeast-2)로 이동합니다.
      1. 다시 좌측 Endpoints를 눌러 화면을 이동합니다.
      1. Create endpoint 버튼을 클릭합니다.
      1. Endpoint Type을 Target endpoint로 변경합니다.
      1. Endpoint Identifier, Target engine, Service access role ARN을 아래와 같이 입력합니다.
      - Endpoint Identifier: demogo-s3-mongo
      - Target engine: Amazon S3
      - Service access role ARN: 27번 항목에서 복사한 ARN 붙여넣기
      1. Bucket name, Bucket folder, Endpoint settings를 아래와 같이 설정합니다.
      - Bucket name: demogo-${account-id}-base
      - Bucket folder: raw/mongo/
      - AddColumnName: true
      - *${account-id}**는 개인별로 모두 다릅니다. 아래 내용 참고해서 개인 환경에 맞는 값을 넣으시길 바랍니다
      > s3 bucket name은 실습 아키텍처 및 환경구성 -> S3 Folder 구조에서 생성한 버킷입니다.
      1. Create endpoint 버튼을 눌러 endpoint를 생성합니다.
      1. demogo-s3-mongo endpoint가 정상적으로 생성되었는지 확인하고 클릭합니다.
      1. Connections - Test connections을 클릭합니다.
      1. Run test 버튼을 눌러 DMS와 S3간 연결성을 테스트합니다. 상태가 successful이 되는 것을 확인합니다. (이 작업에는 1-2분 가량 시간이 소요됩니다)
      1. 여기까지 DMS의 instance를 만들고, Source(Mongo)와 Target(S3)의 Endpoint(연결점)을 생성하였습니다. 이제, 이를 활용하여 데이터를 옮기는 Task를 생성해 보겠습니다. 좌측 탭의 Database migration tasks를 클릭해 주세요
      1. 이어서 Create task 버튼을 눌러줍니다.
      1. Task Configuration을 아래와 같이 작성합니다.
      - Task identifier: demogo-mongo-s3-task
      - Replication instance: demogo-dms-vpc-..
      - Source database endpoint: demogo-mongo
      - Target databse endpoint: demogo-s3-mongo
      - Migration type: Migrate existing data
      1. Task settings에서 Task logs 옵션에 체크합니다.
      1. Table mappings에서, DMS가 demogo db만 가져오도록 설정해 줍니다.
      1. Task 생성 후 Manual 하게 실행하도록 설정해 줍니다.
      1. Create task 버튼을 클릭합니다.
      1. 생성한 Task의 상태가 Ready가 되었는지 확인합니다. (이 작업에는 1-2분 가량 시간이 소요됩니다)
      1. task를 클릭하여 restart/resume 메뉴를 클릭합니다.
      1. Task 상태가 Running에서 ~로 바뀌는 것을 확인합니다.
      1. 데이터가 정상적으로 옮겨졌는지 확인하기 위해 [Amazon S3 ](https://s3.console.aws.amazon.com/s3/home?region=ap-northeast-2)로 이동합니다.
      1. 사전 생성한 버킷을 클릭하여 데이터를 확인합니다.
      1. Run SQL query 버튼을 클릭하여 데이터가 정상적으로 들어왔는지 확인합니다.
      1. 여기까지 AWS DMS를 통해 MongoDB에서 S3로 데이터를 가져오는 작업을 진행하였습니다. Query with S3 Select 기능을 통해 데이터도 확인해 봤지만, 본격적으로 분석을 진행하고 데이터를 활용하기 위해서는 추가적인 작업이 필요합니다. 이어서 Data Cataloging을 통해 가져온 데이터의 필요한 정보를 저장하는 실습을 진행해 보겠습니다.
#### Data Cataloging
## Data Cataloging
      1. S3에 있는 데이터의 Catalog를 저장하기 위해 AWS Glue Crawler를 사용합니다. 우리가 수동으로 catalog를 저장할 수도 있지만, crawler를 사용하면 보다 편하게 catalog를 저장할 수 있습니다.
2. [AWS Glue ](https://ap-northeast-2.console.aws.amazon.com/glue/home?region=ap-northeast-2)로 이동합니다.
      1. 좌측 메뉴에서 Crawlers를 클릭합니다.
      1. Create crawler 버튼을 클릭합니다.
      1. Name을 아래와 같이 적고 next 버튼을 누릅니다.
      Name: demogo-mongo-raw
      1. Add a data source를 누릅니다.
      1. 다른 값은 기본 상태로 두고, S3 Path에서 Browse 버튼을 누릅니다.
      1. 이전에 생성한 demogo-${account-id}-base 버킷을 선택한 후 Choose 버튼을 누릅니다.
      1. 이후에 자동으로 입력된 s3 path 끝에 추가 경로를 직접 추가해 줍니다.
      ```plain text
S3 path = s3://demogo-${account-id}-base/raw/mongo/demogo/
      ```
      1. Add an S3 data source를 클릭합니다.
      1. Next 버튼을 누릅니다.
      1. Create new IAM role을 선택합니다.
      1. 아래와 같이 이름을 입력하고 Create 버튼을 누릅니다.
      Name:
      ```plain text
AWSGlueServiceRole-demogo
      ```
      1. 생성한 Role이 제대로 들어갔는지 확인 후 Next 버튼을 누릅니다.
      1. Target Database와 Table name prefirx를 아래와 같이 설정합니다.
      - Target Database: demogo_raw_db
      - Table name prefirx: mongo-
      1. Advanced options을 눌러서 Table level을 5로 설정해 줍니다.
      > Table level을 설정하는 이유는, glue crawler에서는 설정한 data source의 s3 path 기준으로 table명을 설정하는 것에 그 이유가 있습니다.
        우리가 위 9번에서 Glue crawelr data source를 추가 할 때, S3 path를 s3://demogo-${account-id}/raw/mongo/demogo/ 로 설정했습니다. 이는 db 기준으로 table의 catalog를 자동으로 가져오기 위해 db까지 path를 지정한 건데, 만약 table level을 따로 설정하지 않으면 data source의 가장 마지막 부분인 db명을 table명으로 인식하고 catalog가 생성되게 됩니다.
      > 따라서, table이 5번째 위치가 되므로 Table level 5를 지정해야 catalog table명이 올바르게 생성되게 됩니다.
        하지만 Glue Crawler에는 테이블 추론 기능이 있는데, 이를 통해 table level을 지정하지 않아도 자동으로 처리되는 경우도 있습니다. 더 자세한 내용은 [https://docs.aws.amazon.com/glue/latest/dg/crawler-s3-folder-table-partition.html ](https://docs.aws.amazon.com/glue/latest/dg/crawler-s3-folder-table-partition.html) 를 참고 바랍니다.
      1. Next 버튼을 클릭합니다.
      1. Review를 한번 확인하고, Create crawler 버튼을 클릭합니다.
      1. Crawler 상태가 Ready인 것을 확인하고, Run 버튼을 누릅니다.
      1. Crawler의 Last run이 Succeeded인 것을 확인합니다. (이 작업에는 1-2분 가량 시간이 소요됩니다)
      1. 좌측 메뉴에서 Tables를 클릭하고 아래와 같이 필터링하여 catalog가 제대로 생성되었는지 확인합니다.
      - Database: demogo_raw_db
      - Name: mongo-cart
      1. mongo-cart를 클릭하여 Schema를 보고, Flattening이 잘 처리되었는지 확인합니다.
      1. 여기까지 Glue Crawler를 이용하여 catalog 생성을 완료하였습니다. 현재 데이터는 csv 형태인데, 데이터 분석에 용이하도록 parquet 형태로 변환하고 비용절감을 위해 압축하는 작업을 진행해 보겠습니다.
#### Data Processing
## Data Processing
      1. [AWS Glue Studio ](https://ap-northeast-2.console.aws.amazon.com/gluestudio/home?region=ap-northeast-2)로 이동합니다.
      1. Visual with a soource and target을 누르고 Create 버튼을 클릭합니다.
      1. Job Name을 변경하고, Data source를 클릭하여 database와 table을 아래와 같이 작성합니다.
      - Job Name: demogo-mongo-raw-to-curated
      - Database: demogo_raw_db
      - Table: mongo-cart
      1. Transform을 선택하여 array_items key를 drop합니다.
      1. Data Target을 클릭하여 Format과 Compression Type, S3 Target Location 등을 변경합니다.
      - Format: Parquet
      - Compression Typ: Snappy
      - S3 Target Location: s3://demogo-${account-id}-base/curated/mongo/demogo/cart/ (curated 이하는 직접 타이핑)
      - Database: demogo_curated_db
      - Table name: mongo-cart
      1. Job details를 클릭하여 IAM Role, bookmark, number of retries, job timeout을 아래와 같이 설정합니다.
      - IAM Role: Demogo-workshop-Glue-role
      - Job bookmark: Disable
      - Number of retries: 1
      - Job timeout: 5
      1. Save 버튼을 클릭합니다.
      1. 좌측 탭 Jobs를 눌러 저장한 Job이 있는지 확인하고, Run Job을 눌러서 실행시킵니다.
      1. Job을 눌러서 Runs 탭을 확인하여 현재 Job의 실행 상태를 확인합니다.
      1. Run Status가 Succeeded로 바뀌었다면, [S3 ](https://s3.console.aws.amazon.com/s3/home?region=ap-northeast-2)로 들어가서 데이터를 확인해 봅니다.
      1. 데이터가 있다면, Parquet 타입의 Catalog도 정상 생성되었는지 확인합니다.
      > 이전에는 Glue Crawler를 만들어서 Raw에 대한 catalog를 생성하였지만 curated에서는 그 작업이 따로 없었습니다. 왜 그럴까요?
        정답은 Glue Job을 구성했던 5번 작업에서 Data Catalog Update option을 주었기 때문입니다. 이로써 더 간단하게 catalog를 구성할 수 있게 되었습니다.
      1. Catalog를 클릭하여 Schema에서 우리가 제외한 array_items가 없는지 확인합니다.
      1. 여기까지 Glue Job을 통해 데이터를 분석에 용이한 형태로 변경하는 처리 작업을 구성해 보았습니다. 다음으로는 이렇게 구성한 데이터를 AWS Athena 서비스를 이용하여 사용해보는 과정일 진행해 보도록 하겠습니다.
#### Data Consumption
## Data Consumption
      사전에 MySQL 실습 모듈에서 Athena 초기 세팅을 진행해야 합니다.
      1. [Amazon Athena ](https://ap-northeast-2.console.aws.amazon.com/athena/home?region=ap-northeast-2)로 이동합니다.
      1. 좌측 탭에서 database, table을 선택하고 Preview Table을 선택합니다.
      1. 화면에서 간단한 Select Query가 자동으로 생성되고 실행되어 결과가 출력되는 것을 보실 수 있습니다.
      - 활용 측면에서는 간단하게 Adhoc Query가 가능한 Athena를 이용하여 Query를 하는 것 까지 보았습니다. 데이터 시각화는 MySQL 파이프라인 모듈에서 실습을 제공하니 참고 부탁 드립니다.
      - 이렇게 MongoDB에서 데이터를 S3로 가져와서 Catalog를 생성, 전처리, 활용하는 측면까지 파이프라인을 구성해 보았습니다.
      - 지금까지는 Web Console에서 직접 클릭하여 구성하였지만 AWS에서는 거의 대부분의 작업을 API로 제공하여 이런 구성 작업을 Workflow tool을 통해 자동화 및 배치 작업 구성을 할 수 있는 유연성이 있습니다.
      - 이러한 Orchestration 과정은 mysql 섹션에서 다루고 있으니 참고 부탁 드립니다.
## Module 3. File Data 파이프라인 (Optional)
    이번 실습은 DataSync를 이용하여 Server Message Blcok (SMB) 공유 저장소에서 Amazon S3로 데이터를 수집하는 방법을 실습합니다. 원활한 실습 환경을 위해 SMB 파일 공유가 설정된 윈도우 서버는 CloudFormation으로 생성하여 제공합니다. DataSync 구성은 agent 전용 EC2설치 및 agent 설정, source 및 destination location 설정, 그리고 task 설정 작업 순으로 진행됩니다.
#### Data Preparation
## Data Preparation
      테스트 데이터 확인
      1. CloudFormation으로 생성된 [SMB EC2 Instance ](https://ap-northeast-2.console.aws.amazon.com/ec2/home?region=ap-northeast-2#Instances:)에 접속하여 파일 공유 상태를 확인합니다. 해당 인스턴스 선택 후 Connect 버튼을 클릭합니다.
      1. Session Manager를 선택하고 Connect 버튼을 클릭합니다. RDP Client 접속을 원하시는 경우 Security Group inbound에서 tcp 3389 허용이 필요합니다. 인스턴스 접속 계정은 demogo, 패스워드는 P@ssw0rd 입니다.
      1. PowerShell 창에서 net share demogo 를 입력하여 네트워크 드라이브 공유 상태를 확인합니다.
#### Data Ingestion
## Data Ingestion
      [DataSync agent 구성](https://catalog.us-east-1.prod.workshops.aws/workshops/7f59c02a-e96d-414f-b513-f0da08844108/ko-KR/module6/6-2#datasync-agent)
      본격적으로 DataSync를 이용한 파일 전송 환경을 구성해보겠습니다. 먼저DataSync agent가 실행 될 EC2 인스턴스를 생성하겠습니다. DataSync agent는 온프레미스와 클라우드 모두 설치 가능하며 이번 워크샵에서는 EC2 인스턴스에 설치하게 됩니다.
      EC2 인스턴스 설치를 위한 AMI 확인 방법은 링크 (
      [https://docs.aws.amazon.com/datasync/latest/userguide/deploy-agents.html)에서](https://docs.aws.amazon.com/datasync/latest/userguide/deploy-agents.html)%EC%97%90%EC%84%9C)
      확인 가능합니다. 워크샵을 작성한 시점을 기준으로 가장 최신 AMI는 ‘aws-datasync-2.0.1664216628.1-x86_64-gp2’이며 해당 버전을 이용하여 DataSync agent를 생성하겠습니다.
      [EC2 생성](https://catalog.us-east-1.prod.workshops.aws/workshops/7f59c02a-e96d-414f-b513-f0da08844108/ko-KR/module6/6-2#ec2)
      1. DataSync agent가 설치되는 EC2 인스턴스의 Security Group을 먼저 생성하겠습니다.
      [EC2](https://ap-northeast-2.console.aws.amazon.com/ec2/home?region=ap-northeast-2)
      콘솔창에서 Network & Security > Security Groups를 선택 후,
      Create security group
      을 클릭합니다.
      1. Security group name, Description을 입력하고 워크샵을 위해 생성한 VPC를 선택합니다.
      DataSync agent 인증을 위해서 HTTP (TCP 80) inbound 허용 정책이 필요합니다.
      Add rules
      버튼을 클릭한 후 Anywhere IPv4로부터의 HTTP inbound 허용 정책을 생성합니다. 소스 데이터 저장소와 통신하기 위해Outbound 정책은 기본 정책 그대로 (0.0.0.0/0, All traffic) 유지합니다.
      Create security group
      을 클릭하여 생성합니다.
      1. 이제 DataSync agent가 구동할 EC2 인스턴스를 생성합니다. [EC2 ](https://ap-northeast-2.console.aws.amazon.com/ec2/home?region=ap-northeast-2#Instances:) 콘솔에서 Launch Instance를 클릭하여 실행합니다.
      1. 인스턴스 이름을 입력합니다.
      1. AMI 검색 창에 aws-datasync-2.0.1664216628.1-x86_64-gp2 입력하고 검색합니다
      1. Community AMIs에서 검색된 이미지의 Select 버튼을 클릭합니다
      1. DataSync agent를 구동하기 위한 최소 메모리는 4GB 입니다. 메모리가4GB 이상인 인스턴스를 선택합니다. Key pair는 Proceed without a key pair를 선택합니다.
      1. Network settings의 Edit 버튼을 클릭합니다. 워크샵을 위해 생서한 VPC를 선택한 후, 앞서 생성한 Security Group을 선택합니다.
      1. Advanced details 에서 IAM Instance profile을 변경합니다. SSMInstanceProfile은 Session Manager를 이용해 인스턴스 접속 시 필요하며 CloudFormation으로 사전에 생성 되었습니다. DataSync를 통한 데이터 전송을 위해 필요한 단계는 아니며 DataSync agent가 설치된 인스턴스 접속을 위해 설정하는 사항입니다.
      1. Launch instance를 클릭하여 인스턴스 생성을 완료합니다.
      [DataSync Agents 설정](https://catalog.us-east-1.prod.workshops.aws/workshops/7f59c02a-e96d-414f-b513-f0da08844108/ko-KR/module6/6-2#datasync-agents)
      1. [DataSync ](https://ap-northeast-2.console.aws.amazon.com/datasync/home?region=ap-northeast-2) 콘솔 화면으로 이동하여 Agents의 Create agent를 클릭합니다.
      1. Deploy agent는 Amazon EC2를 선택합니다. Agent address에는 앞서 생성한 EC2 인스턴스의 public ip를 입력합니다. EC 콘솔창을 새로운 탭에서 열고 생성된 DataSync agent의 IP를 확인합니다.
      1. 인증 완료 후 Agent name을 입력하고 Create agent를 클릭하여 생성을 완료합니다.
      생성 후 Agent status online을 확인합니다.
      [Location 설정](https://catalog.us-east-1.prod.workshops.aws/workshops/7f59c02a-e96d-414f-b513-f0da08844108/ko-KR/module6/6-2#location)
      1. Agent가 데이터를 이동할 Location을 생성합니다. 이번 워크샵의 Source Location은 파일 공유가 설정된 EC2 인스턴스이고 Destinaton Location은 S3 입니다. 먼저 Source Location을 생성하겠습니다. DataSync 좌측 패널메뉴에서 [Locations ](https://ap-northeast-2.console.aws.amazon.com/datasync/home?region=ap-northeast-2#/locations)를 선택한 후 Create location 버튼을 클릭합니다.
      1. Configuration에서 Location type은 Server Message Block (SMB)를 선택합니다. Agents는 앞서 생성한 DataSync agent를 선택합니다. SMB Server IP는 CloudFormation으로 사전 생성 된 EC2 인스턴스의 IP를 입력합니다. Private/Public IP 모두 가능합니다. Share name은 demogo를 입력합니다.
      1. User settings에서 네트워크 드라이브 접속을 위한 계정, 패스워드 정보를 입력합니다. User에 demogo, Password에 P@ssw0rd를 입력합니다.
      1. 우측 하단의 Create location 버튼을 클릭하여 Source location 생성을 완료합니다.
2. 이어서 Destinaton location을 생성합니다. 동일하게 Create location 버튼을 클릭하여 생성을 시작합니다.
      1. Configuration에서Location type은 Amazon S3를 선택합니다. S3 bucket은 데이터 저장을 위해 앞서 생성한 실습자의 bucket 을 선택합니다. Folder또한 사전에 정의한 경로를 입력합니다. S3 bucket에 접근하기 위해 IAM role을 선택합니다. Autogenerate 버튼 클릭 후 refresh 버튼을 클릭하면 새로 생성된 IAM role을 선택할 수 있습니다. 우측 하단의 Create location 버튼을 클릭하여 Destinaton location 생성을 완료합니다.
      [Tasks 설정](https://catalog.us-east-1.prod.workshops.aws/workshops/7f59c02a-e96d-414f-b513-f0da08844108/ko-KR/module6/6-2#tasks)
      DataSync agent와 Location을 이용하여 데이터를 Source에서 Destinaton으로 복제하는 Task를 생성해보겠습니다.
      1. DataSync 좌측 패널 메뉴에서 [Tasks ](https://ap-northeast-2.console.aws.amazon.com/datasync/home?region=ap-northeast-2#/tasks) 선택 후 Create task 버튼을 클릭합니다.
      1. Source location을 지정합니다. Choose an existing location 선택 후, 서울 리전과 앞서 생성한 source location(SMB)을 선택합니다.
      1. Destinaton location을 지정합니다. Choose an existing location 선택 후, 앞서 생성한 destination location(S3)를 선택합니다.
      1. Task Name을 입력합니다. Schedule frequency에서 희망하는 반복 주기를 선택 합니다. 워크샵에서는 매00시에 동작하도록 하였습니다. Task logging 에서 Autogenerate 버튼을 클릭하여 CloudWatch를 통한 log 확인이 가능하도록 설정합니다.
      1. 설정한 내용을 Review한 후 Create task 버튼을 클릭하여 생성을 완료합니다.
      [데이터 전송 확인](https://catalog.us-east-1.prod.workshops.aws/workshops/7f59c02a-e96d-414f-b513-f0da08844108/ko-KR/module6/6-2#)
      1. Task 생성이 완료되면 Start > Start with defaults 를 클릭하여 실행합니다.
      1. Task 실행 결과는 DataSync > History 메뉴를 통해 확인 할 수 있으며, 복제된 데이터는 목적지인 S3의 경로에서 확인 할 수 있습니다.
      이것으로 DataSync를 이용한 File 데이터 복제 작업 실습이 완료되었습니다.
## Module 4. Streaming Data 파이프라인 (Optional)
    [Amazon Kinesis란?](https://catalog.us-east-1.prod.workshops.aws/workshops/7f59c02a-e96d-414f-b513-f0da08844108/ko-KR/module7#amazon-kinesis)
    Amazon Kinesis
    를 사용하면 실시간 스트리밍 데이터를 손쉽게 수집, 처리 및 분석할 수 있으므로 적시에 통찰력을 확보하고 새로운 정보에 신속하게 대응할 수 있습니다. Amazon Kinesis는 모든 규모의 스트리밍 데이터를 비용 효율적으로 처리할 수 있는 핵심 기능과 더불어 애플리케이션 요구 사항에 가장 적합한 도구를 선택할 수 있는 유연성을 제공합니다.
    이번 실습에서는 AWS Lambda를 이용해 가상의 클릭 스트림 데이터를 발생시키고 이 데이터를 Kinesis Data Streams 와 Kinesis Data Firehose를 거쳐 S3에 저장합니다. 이후 수집된 데이터에 대해 Crawler를 통해 카탈로그 데이터를 생성하여 Athena, QuickSight를 통한 데이터 분석이 가능한 파이프라인을 구성합니다.
#### Data Ingestion
## Data Ingestion
      [Kinesis Data Stream 생성](https://catalog.us-east-1.prod.workshops.aws/workshops/7f59c02a-e96d-414f-b513-f0da08844108/ko-KR/module7/7-1#kinesis-data-stream)
      스트리밍 데이터를 S3에 저장하기 위해 워크샵에서는 Kinesis를 이용합니다. 먼저 Kinesis Data stream을 생성합니다.
      1. Amazon Kinesis 콘솔의 좌측 메뉴에서 [Data streams ](https://ap-northeast-2.console.aws.amazon.com/firehose/home?region=ap-northeast-2#/dashboard/list) 선택 후 Create data stream 버튼을 클릭합니다.
      1. Data stream name에 dp22-datastream을 입력한 후 기본 상태에서 Create data stream 버튼을 클릭합니다.
      [Data Catalog Table 생성](https://catalog.us-east-1.prod.workshops.aws/workshops/7f59c02a-e96d-414f-b513-f0da08844108/ko-KR/module7/7-1#data-catalog-table)
      이번에는 Kinesis Firehose (Delivery streams)를 이용하여 데이터 파일을 Parquet 타입으로 S3에 저장하게 합니다. 이를 위해 Kinesis Firehose에서 참조할 table 정보를 먼저 생성하겠습니다.
      1. AWS Glue 콘솔에서 [Tables ](https://ap-northeast-2.console.aws.amazon.com/glue/home?region=ap-northeast-2#/v2/data-catalog/tables)를 선택한 후 Add table을 클릭합니다
      1. 테이블 속성 정보를 입력합니다. 입력 내용은 하기 표를 참고하시기 바랍니다. 데이터 저장소는 S3를 선택하고, 데이터가 저장되는 경로를 입력합니다. 아직 폴더를 생성하지 않은 경우 직접 입력합니다. 경로의 마지막은 ‘/’로 끝나야 합니다. 데이터 포맷은 JSON을 선택합니다.
      1. 워크샵에서 사용할 스트리밍 데이터의 스키마를 정의합니다. 테스트 데이터의 스키마는 다음과 같습니다. Add 버튼을 클릭하여 모두 입력 후 Next 버튼을 클릭합니다.
      1. 정보 확인 후 Create 버튼을 클릭하여 테이블 생성을 완료합니다.
      [Kinesis Firehose Stream 생성](https://catalog.us-east-1.prod.workshops.aws/workshops/7f59c02a-e96d-414f-b513-f0da08844108/ko-KR/module7/7-1#kinesis-firehose-stream)
      스트리밍 데이터는 Kinesis Data Stream에서 Kinesis Firehose를 거쳐 S3에 저장되게 됩니다.
      1. Amazon Kinesis 콘솔의 Delivery streams 선택 후 Create delivery stream을 클릭하여 생성을 시작합니다.
      1. Source는 Amazon Kinesis Data Streams, Destination은 Amazon S3를 선택합니다.
      소스 Kinesis data stream은 Browse 버튼을 클릭한 후 앞서 생성한 것을 선택합니다. Delivery stream name은 자동 생성되는 것을 그대로 사용하겠습니다.
      1. 수집되는 스트리밍 데이터를 Apache Parquet 형식으로 S3에 저장하도록 Transform and convert records를 설정합니다.
      Record format conversion에서
      ```plain text
Enabled
      ```
      , Output format 은
      ```plain text
Apache Parquet
      ```
      를 선택합니다. AWS Glue region은
      ```plain text
Asia Pacific (Seoul)
      ```
      을 선택하고 Database는
      ```plain text
demogo_raw_db
      ```
      를 선택합니다.
      Browse
      버튼을 클릭한 후 앞서 생성한 stream 테이블을 팝업창에서 선택합니다.
      1. Destination settings에서 S3 정보를 입력합니다.
      S3 bucket은 CloudFormation에서 생성된
      ```plain text
demogo-AccountID-base
      ```
      를 선택합니다.
      Browse
      버튼을 클릭한 후 팝업창에서 선택합니다. S3 bucket prefix 와 S3 bucket error output prefix는 아래 표의 값을 입력합니다. 스트리밍 데이터 저장의 빠른 확인을 위해 Buffer interval은
      ```plain text
60
      ```
      초로 변경합니다.
      1. 나머지 설정은 기본 값으로 유지한 후 Create delivery stream을 클릭하여 생성을 완료합니다.
#### Data Preparation
## Data Preparation
      스트리밍 데이터가 Kinesis data stream, Kinesis Firehose를 거쳐 S3에 저장되는 구조를 완성하였습니다. 이제 가상의 클릭 스트림 데이터를 발생시켜 이 데이터 파이프라인이 동작 하는지 확인해 보겠습니다.
      1. AWS Lambda 콘솔 [Functions ](https://ap-northeast-2.console.aws.amazon.com/lambda/home?region=ap-northeast-2#/functions) 메뉴를 선택 후 Create function 버튼을 클릭합니다.
      1. Function name에 dp22-datastream을 입력하고 Runtime은 Python 3.7을 선택합니다. Create function 버튼을 클릭합니다.
      1. 생성된 Lambda function에 코드를 입력합니다. Lambda_funtion.py의 예제 코드를 삭제하고 아래 코드를 입력합니다. 34번 라인의 StreamName은 앞서 생성한 Kinesis Data Stream의 이름을 입력해야 합니다. 소스코드를 입력 한 후 Depoly 버튼을 클릭합니다.
      1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
import json
import boto3
import random
import datetime
import logging
import os
LOGGER = logging.getLogger()
LOGGER.setLevel(os.getenv("LOG_LEVEL", logging.INFO))
kinesis = boto3.client('kinesis')
def getClickStream():
    timestamp = datetime.datetime.now()
    timestamp_ser= timestamp.isoformat()
    clickstream={}
    clickstream['UserId']=random.randint(1,999)
    clickstream['Device']=random.choice(['web','mobile','tablet'])
    clickstream['Event']=random.choice(['P101','P201','P301','P401','P501'])
    clickstream['EventType']='Promotion'
    clickstream['Timestamp']=timestamp_ser
    return clickstream
def lambda_handler(event, context):
  LOGGER.info(f'Event received: {event}')
  begining = datetime.datetime.now()
  newtime = begining
  try:
    while (newtime - begining).total_seconds()<55:
        data = json.dumps(getClickStream())
        payload = str(data)+'\n'
        print (payload)
        response=kinesis.put_record(
                StreamName='dp22-datastream',
                Data=payload,
                PartitionKey='partitionkey')
        LOGGER.info('Added record to stream')
        LOGGER.info(f'{response}')
        newtime = datetime.datetime.now()
    LOGGER.info('Execution completed.')
  except Exception as e:
      LOGGER.error(f'Error ingesting clickstream data: {e}')
      raise
      1. 다음은 생성한 Lambda function이 Kinesis data stream으로 데이터를 전송 할 수 있도록 IAM Role의 policy를 추가합니다.
      생성한 Lambda function의 Configuration 탭에서
      ```plain text
Permissions
      ```
      를 선택합니다. 자동으로 생성된
      [IAM Role](https://console.aws.amazon.com/iam/home?region=ap-northeast-2)
      클릭하여 IAM 콘솔 화면으로 이동합니다.
      1. 새로 열린 IAM Role 화면에서 Add permissions의 Attach policies를 클릭합니다.
      검색창에
      ```plain text
amazonkinesisfullaccess
      ```
      를 입력하여 검색 된 Polciy를 선택한 후
      Attach policies
      버튼을 클릭하여 추가합니다.
      이것으로 Lambda function에서 Kinesis data stream으로 데이터 전송이 가능한 상태가 되었습니다. 이제 마지막 작업으로 이 Lambda function으 주기적으로 동작 할 수 있도록 EventBridge를 트리거로 설정하겠습니다.
      1. 생성한 Lambda function의 overview 화면에서 Add trigger 버튼을 클릭합니다.
      1. 첫 화면의 Select a source박스에서 EventBrdige (CloudWatch Events)를 찾아 선택합니다.
      Create a new rule을 선택 한 후 Rule name에
      ```plain text
dp22-datastream-minute
      ```
      을 입력합니다. Schedule expression은 매 분마다 실행 되도록
      ```plain text
rate(1 minute)
      ```
      을 입력합니다.
      Add
      버튼을 클릭하여 트리거를 완성합니다.
      1. Lambda function의 동작 상태는 Monitor 탭의 Logs를 선택하여 확인 할 수 있습니다.
      스트리밍 데이터가 목적지 저장소 S3로 잘 전송 되었는지 확인합니다. (S3://demogo-AccountID-base/raw/kinesis/stream/)
#### Data Cataloging
## Data Cataloging
      Kinesis를 통해 S3에 저장된 가상의 스트리밍 데이터에 대해 Catalog data를 생성합니다. Glue Crawlers를 이용하여 메타데이터 캡처를 쉽게 할 수 있습니다. Catalog data가 생성되면 Amazon Athena에서 raw 포맷의 데이터에 대해 쿼리를 시작할 수 있습니다.
      1. AWS Glue 콘솔창의 좌측 패널에서 Crawlers를 선택 한 후 Create crawler 버튼을 클릭합니다.
      1. Crawler의 이름을 입력 한 후 Next 버튼을 클릭합니다.
      1. Add a data source 버튼을 클릭하여 저장된 데이터의 위치 정보를 입력합니다.
      1. Add a data source를 클릭하면 아래 그림과 같은 팝업창이 뜹니다.
      - Data source는 S3를 선택 합니다.
      - S3 path는 Browse 버튼을 클릭하여 스트리밍 데이터를 저장한 경로를 지정합니다. (s3://demogo-AccountID-base/raw/kinesis/stream/)
      - 경로를 선택하면 경고 메세지가 뜨는데 S3 path 끝에 ‘/’를 입력하면 사라집니다.
      - Exclude Files matching pattern을 선택 한 후 Add new exclusion pattern 버튼을 클릭 합니다.
      - Exclude pattern입력박스에 error/** 을 입력하여 Kinesis Firehose 전송간 발생한 오류 로그는 Crawler 작업에서 제외 되도록 합니다.
      - Add an S3 data source 버튼을 클릭합니다.
      - Next 버튼을 클릭한 후 다음 단계를 진행합니다.
      1. IAM role을 설정합니다. 직전에 생성한 Glue 서비스용 role이 없다면 Create new IAM role 버튼을 클릭하여 생성합니다. 버튼을 클릭하면 이름을 입력하는 팝업창이 뜨며 정책은 자동으로 생성됩니다. 만약 기존에 생성한 Glue 서비스용 role이 있다면, 해당 role 선택 후 Update chosen IAM role 버튼을 클릭한 후, 팝업창에서 Confirm 버튼을 클릭합니다. 작업이 완료되었으면 Next 버튼을 클릭합니다.
      1. Catalog data를 저장 할 데이터베이스를 선택합니다. 앞서 생성한 demogo_raw_db를 사용합니다. 데이터베이스 선택 후 Next 버튼을 클릭합니다.
      1. 입력한 정보를 리뷰 후 Create crawler 버튼을 클릭하여 생성을 완료합니다.
      1. Crawler 생성이 완료되어 State가 Ready가 되면 해당 Crawler 선택 후 Run 버튼을 클릭하여 실행합니다.
      1. Crawler 작업이 완료되면 테이블이 생성됩니다. Crawler가 생성한 테이블은 앞서 Kinesis Firehose 생성 단계에서 만들었던 테이블을 덮어 쓰게 되며 이 때 데이터 포맷은 JSON에서 Parquet로 변경됩니다. 또한 파티션 컬럼이 테이블에 추가 됩니다.
      1. Crawler 작업이 정상 완료되었다면 Amazon Athena에서 데이터를 쿼리 할 수 있습니다. Database에서 demogo_raw_db를 선택하고 Tables 에서 stream의 Preview Table을 클릭합니다. 생성된 쿼리 탭을 확인 한 후 Run again 버튼을 클릭합니다
## Module 5. MWAA를 활용한 데이터 파이프라인 오케스트레이션
    [Amazon MWAA란?](https://catalog.us-east-1.prod.workshops.aws/workshops/7f59c02a-e96d-414f-b513-f0da08844108/ko-KR/module8#amazon-mwaa)
    Amazon Managed Workflows for Apache Airflow(MWAA)는 Apache Airflow를 위한 관리형 오케스트레이션 서비스로, 클라우드에서 엔드 투 엔드 데이터 파이프라인을 대규모로 보다 쉽게 설정하고 운영할 수 있게 해줍니다. Apache Airflow는 ‘워크플로’라고 하는 프로세스와 작업의 시퀀스를 프로그래밍 방식으로 작성, 예약 및 모니터링하는 데 사용되는 오픈 소스 도구입니다.   Amazon MWAA에서는 Airflow와 Python을 사용하여 워크플로를 생성할 수 있으며, 확장성, 가용성, 보안을 위해 기본 인프라를 관리할 필요가 없습니다. Managed Workflows는 해당 워크플로 실행 용량을 자동으로 확장하여 사용자의 요구 사항을 충족하고, AWS 보안 서비스와 통합되어 데이터에 빠르고 안전하게 액세스할 수 있게 해줍니다.
#### [Airflow 개념](https://catalog.us-east-1.prod.workshops.aws/workshops/7f59c02a-e96d-414f-b513-f0da08844108/ko-KR/module8/8-1)
## Airflow 개념
      Airflow는 워크플로를 구축하고 실행할 수 있는 플랫폼입니다. 워크플로는 DAG(Directed Acyclic Graph)로 표시되며, 종속성과 데이터 흐름을 고려하여 정렬된 Task라는 개별 작업을 포함합니다.
      DAG는 작업 간의 종속성과 Task를 실행하고 재시도를 실행하는 순서를 지정합니다. Airflow는 일반적으로 다음 구성 요소를 포함합니다.
      - Scheduler: 예약된 워크플로를 트리거하고 Task를 실행하도록 함
      - Executor: 실행중인 task를 처리. 기본적으로 executor는 scheduler 내에 포함된 task를 관리하지만 운영 환경에 적합한 executor는 worker에 task를 푸시
      - Webserver: DAG 및 task의 동작을 검사, 트리거 및 디버그할 수 있는 사용자 인터페이스를 제공
      - Metadata Database: Scheduler, executor 및 webserver에서 상태를 저장하는 데 사용하는 메타데이터 데이터베이스
      Workloads DAG는 일련의 task를 통해 실행되며 다음과 같은 세 가지 일반적인 task 유형이 있습니다.
      - Operators: 개념적으로 DAG 내에서 미리 정의된 task에 대한 템플릿
      - Sensors: 한 가지 task를 수행하도록 설계된 특수한 유형의 operator
      - TaskFlow: Python 코드를 사용하여 DAG를 작성하는 경우, TaskFlow API를 사용하면 추가 상용구 없이 DAG를 쉽게 작성 가능
      Control Flow
      DAG는 여러 번 실행되도록 설계되었으며 동시에 여러 번 실행할 수 있습니다. Task는 서로에 대해 종속성이 있습니다. >> 및 << 연산자를 사용하여 DAG를 구성할 수 있습니다.
      - first_task >> [second_task, third_task]
      - fourth_task << third_task
#### [S3 설정](https://catalog.us-east-1.prod.workshops.aws/workshops/7f59c02a-e96d-414f-b513-f0da08844108/ko-KR/module8/8-2)
## S3 설정
      MWAA에서 DAG, Requirement 등 설정을 위해 [Amazon S3 ](https://s3.console.aws.amazon.com/s3/home?region=ap-northeast-2) 콘솔로 이동합니다.
      1. Create bucket 버튼을 누른 후 bucket 이름을 설정합니다. Bucket 이름은 유일해야 합니다. 예시. airflow-yourname-bucket
      1. Region은 서울 (ap-northeast-2)을 선택합니다.
2. 기타 설정은 하지 않고 아래 Create bucket 버튼을 클릭해 bucket을 생성합니다.
3. S3 버킷리스트에서 새로 생성된 버킷을 클릭하여 Properties 탭에 있는 S3 Amazon Resource Name (ARN) 을 기록해 둡니다.
4. Objects 탭에서 Create folder를 클릭합니다.
5. 폴더이름에 Dags 를 입력하고 Create folder 를 클릭합니다.
      1. Objects 탭에서 Create folder 를 한번 더 선택합니다.
2. 폴더이름에 plugins 을 입력하고 Create folder 를 클릭합니다.
      1. Objects 탭에서 Create folder를 한번 더 선택합니다.
2. 폴더이름에 requirements를 입력하고 Create folder를 클릭합니다.
      1. 완료된 이후 bucket 내 폴더 형태는 아래와 같을 것입니다.
      완료되면 다음 단계에서 Managed Workflows for Apache Airflow (MWAA) 환경을 구성합니다.
#### [MWAA 설정](https://catalog.us-east-1.prod.workshops.aws/workshops/7f59c02a-e96d-414f-b513-f0da08844108/ko-KR/module8/8-3)
## MWAA 설정
      이번 과정에서는 MWAA 인스턴스 환경과 DAGs 및 환경 구성을 위한 S3 bucket 설정 등을 진행합니다. Console에서 [MWAA ](https://ap-northeast-2.console.aws.amazon.com/mwaa/home?region=ap-northeast-2)를 입력해서 이동합니다.
      1. 메인 화면에서 Create environment를 클릭합니다.
      1. Name에는 Airflow-Yourname 형태로 자유롭게 입력합니다.
      1. Airflow Version은 최신 버젼인 2.2.2를 선택합니다.
2. 아래 그림과 같이 전 단계에서 설정한 bucket 구조를 선택해서 구성합니다. S3 Bucket에는 Browse S3 버튼을 클릭해서 최상위 bucket인 “airflow-yourname-bucket”를 선택합니다.
      1. 선택하면 DAGs 폴더와 Plugin, Requirements 파일을 선택하는 창이 새로 뜹니다.
      1. DAGs 폴더는 직접 만든 airflow-yourname-bucket 하위의 Dags 폴더를 선택합니다.
2. 현재 Plugin은 없으니 Requirements만 설정을 진행합니다. [requirements.txt ](https://demogo-shared-artifacts.s3.ap-northeast-2.amazonaws.com/mwaa/requirements.txt)를 클릭하셔서 다운로드 (우클릭 후 다른 이름으로 저장) 받으시고 requirements 폴더에 파일을 업로드 합니다.
      아래와 같이 S3의 requirements 폴더에서 Upload 버튼을 클릭합니다.
      그리고 Add files 버튼을 클릭하고 저장한 requirements.txt 파일을 더블 클릭합니다.
      마지막으로 Upload 버튼을 클릭합니다.
      1. 그리고 Requirements files에서 Browse S3 버튼을 클릭하고 requirements 폴더 아래에 있는 txt 파일을 지정합니다.
2. 이후 Next 버튼을 클릭합니다.
3. 이번 단계에서는 네트워크, 인스턴스, 모니터링과 같은 환경 구성을 진행합니다.
4. VPC는 기존에 구성되어 있는 것을 선택해서 사용해도 되지만 IP 제한 등 변수를 방지하기 위해 새로 구성합니다. Create MWAA VPC 버튼을 클릭하면 새로운 탭에 Stack을 구성하는 화면이 뜨게 됩니다.
      1. Stack name을 별도로 설정하고 나머지 값은 기본값을 그대로 사용합니다.
2. Create Stack 버튼을 클릭해서 환경을 구성합니다.
      1. 약 3~4분 뒤에 CloudFormation이 완료된 것을 확인할 수 있습니다.
      1. 다시 MWAA로 돌아와서 VPC에서 방금 만들어진 VPC를 선택합니다.
      1. 그리고 Subnet 1과 Subnet 2는 각각 Private을 선택합니다.
      17. Web server access 설정에서는
      Public network
      를 선택하고 Security group은 새로 만들도록 하겠습니다.
      1. 이번에는 MWAA를 설정하는 단계입니다. 실습에서는 가장 작은 인스턴스를 선택하고 worker count도 기본값으로 두고 진행합니다.
      1. Monitoring 설정 단계에서는 다양한 선택을 할 수 있습니다. 기본적으로 CloudWatch로 로그를 보낼 수 있고 Airflow task logs를 수집합니다. 그 외 web server, scheduler, worker, DAG processing log는 필요하다면 활성화 시킵니다.
      1. Airflow에서 새로운 dag가 올라왔는지 확인하는 주기를 설정합니다. 이번 워크샵에서는 시간을 줄이기 위해 5초로 설정합니다.
      scheduler.dag_dir_list_interval : 5
scheduler.min_file_process_interval : 5
      1. 마지막으로 MWAA의 role을 생성합니다. Create a new role을 선택하고 Role name은 적절히 변경합니다. 다음 단계에서 이 role에 다른 권한을 부여하는 작업을 진행합니다.
      1. Step 3에서는 그동안 설정한 내용을 review하고 확인이 되면 Create environment 버튼을 눌러서 MWAA를 구성합니다. 만약 Unable to check PublicAccessBlock configuration.. 이라는 에러가 나면 아래와 같이 S3 bucket 설정에서 Permissions 탭으로 이동한 후 public access를 모두 block 하시기 바랍니다. 이 작업은 약 20-30분 정도 소요됩니다.
      MWAA Environment가 완료되면 Airflow UI에 접근할 수 있습니다. 아래와 같이 가장 상단에 있는 Airflow UI 링크를 클릭합니다.
      클릭하면 아래와 같이 Apache Airflow UI가 보입니다. 아직 DAG을 구성하지 않았기 때문에 별도로 작업 내용이 보이진 않습니다.
#### IAM 설정
## IAM 설정
      1. 이 전 MWAA 생성 단계에서 새로 만든 role에 S3 접근 권한을 부여하기 위해 방금 생성한 [Environment ](https://ap-northeast-2.console.aws.amazon.com/mwaa/home?region=ap-northeast-2#/environments)를 클릭해서 들어갑니다. 이 링크를 통해서 들어갈 수 있습니다. 가장 아래쪽에 Permissions가 보이고 해당 role을 클릭해서 IAM 메뉴로 이동합니다.
      1. IAM에서 확인하면 MWAA-Execution-Policy만 확인됩니다. 여기에 AWSGlueConsoleFullAccess, AWSGlueServiceRole, AWSLambda_FullAccess, AmazonS3FullAccess 총 4개의 policy를 추가합니다.
      1. 아래와 같이 5개의 policy를 각각 입력해서 체크한 후 추가합니다.
      3-1. AmazonS3FullAccess
      3-2. AWSGlueConsoleFullAccess
      3-3. AWSGlueServiceRole
      3-4. AWSLambda_FullAccess
      3-5. Demogo-DMS-Policy는 직접 json 형태로 policy를 만들어서 추가합니다.
      3-6. Create policy 버튼을 클릭합니다.
      3-7. JSON 탭을 클릭 후 아래 내용을 복사해서 붙여넣습니다.
      {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "dms:*",
            "Resource": "*"
        }
    ]
}
      3-8. Next 클릭 후 Review policy에서 Name 부분을 Demogo-DMS-Policy로 설정 후 create policy 버튼을 클릭합니다.
      3-9. 그리고 다시 Role에서 policy 추가하는 화면으로 돌아가 Demogo로 검색하셔서 방금 만든 policy를 체크하고 추가합니다.
      1. 최종적으로는 아래와 같이 새로 추가한 5개의 policy를 확인할 수 있습니다.
#### [DAG 구성 개요](https://catalog.us-east-1.prod.workshops.aws/workshops/7f59c02a-e96d-414f-b513-f0da08844108/ko-KR/module8/8-5)
## DAG 구성 개요
      이제 MWAA에서 Airflow 인스턴스 설정을 완료했으므로 실제 데이터 파이프라인을 구축하는 방법을 알아봅니다. 위에서 실습한 내용 중 External Data 수집과 RDB 수집에 대한 파이프라인을 구축할 예정입니다.
      1. External Data
      - AWS Lambda를 이용해 Naver에서 제공하는 데이터 수집
      - Amazon S3에 저장
      - AWS Glue Crawler를 이용해 메타데이터 추출
      - AWS Glue Data Catalog 생성
      - Amazon Athena를 이용해 Query 수행
      - Amazon QuickSight로 시각화
      1. RDB
      - Amazon RDS MySQL에서 AWS DMS로 마이그레이션
      - Amazon S3에 저장된 DB를 AWS Glue Crawer로 Catalog 생성
      - Amazon Athena에서 Query한 내용을 별도 Amazon S3에 저장
      - Amazon QuickSight로 시각화
#### DAG 구성 (External Data)
## DAG 구성 (External Data)
      1. AWS 콘솔에서 [Amazon MWAA ](https://ap-northeast-2.console.aws.amazon.com/mwaa/home?region=ap-northeast-2) 서비스로 이동합니다
      1. Airflow environments에서 Open Airflow UI를 클릭하여 Airflow 웹 콘솔로 이동합니다.
      1. 환경 변수에 Naver API Key를 등록하기 위해 Admin > Variables 메뉴로 이동합니다.
      1. 
    ◦ 버튼을 클릭하여 Add Variable 화면으로 이동합니다.
      1. Key에는 naver_apikey, Value에는 Naver에서 발급 해 준 API 인증정보를 아래 서식에 맞춰 넣어 줍니다.
      {
"client_id": "<your secret id>",
"client_secret": "<your secret key>"
}
      1. 이제 DAG 파일을 작성하겠습니다. 아래 코드를 복사하여 Visual Studio Code 또는 텍스트 에디터에서 열어 주세요.
      ```python
`from __future__ import annotations

import logging
import sys
import tempfile
import time

import pendulum
from airflow import DAG
from airflow.decorators import task
from airflow.models import Variable
from botocore.exceptions import ClientError

BASE_DIR = tempfile.gettempdir()
lambda_function_name = "demogo-external-crawler"
glue_crawler_name = "demogo-external-raw"
glue_job_name = "demogo_external_curated"

with DAG(
        dag_id='external_pipeline',
        schedule_interval="@daily",
        start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
        catchup=False,
        tags=['demogo'],
) as dag:
    @task(task_id='lambda_crawler_run')
    def lambda_crawler_run(function_name):
        import boto3
        session = boto3.session.Session()
        lambda_client = session.client('lambda')
        payload = Variable.get("naver_apikey")
        logging.info("Invoke Lambda Crawler: {}, Payload: {}".format(function_name, payload))
        response = lambda_client.invoke(
            FunctionName=function_name,
            LogType='Tail',
            Payload=payload
        )
        logging.info("Lambda Crawler Done: {}".format(function_name))
        logging.info(response)

    @task(task_id='glue_crawler_start')
    def glue_crawler_start(crawler_name):
        import boto3
        session = boto3.session.Session()
        glue_client = session.client('glue')
        try:
            logging.info("Initializing AWS Glue Crawler: {}".format(crawler_name))
            response = glue_client.start_crawler(Name=crawler_name)
            return response
        except ClientError as e:
            raise Exception('boto3 client error in start_a_crawler: ' + e.__str__())
        except Exception as e:
            raise Exception('Unexpected error in start_a_crawler: ' + e.__str__())

    @task(task_id='glue_crawler_wait_completion')
    def glue_crawler_wait_completion(crawler_name):
        run_state = 'RUNNING'
        while True:
            if run_state in ['READY', 'STOPPING']:
                return {'CrawlerRunState': run_state}
            else:
                run_state = get_crawler_status(crawler_name)
                time.sleep(10)

    @task(task_id=f'glue_job_run')
    def glue_job_run(job_name):
        import boto3
        session = boto3.session.Session()
        glue_client = session.client('glue')
        job_run = glue_client.start_job_run(JobName=job_name)
        return wait_glue_job(job_name, job_run['JobRunId'])

    lambda_crawler_run_task = lambda_crawler_run(lambda_function_name)
    glue_crawler_raw_start_task = glue_crawler_start(glue_crawler_name)
    glue_crawler_raw_wait_completion_task = glue_crawler_wait_completion(glue_crawler_name)
    glue_job_run_task = glue_job_run(glue_job_name)

    lambda_crawler_run_task >> glue_crawler_raw_start_task >> glue_crawler_raw_wait_completion_task >> glue_job_run_task

def get_crawler_status(crawler_name):
    import boto3
    session = boto3.session.Session()
    glue_client = session.client('glue')
    logging.info(f"Polling for AWS Glue Crawler {crawler_name} current run state")
    crawler_status = glue_client.get_crawler(
        Name=crawler_name
    )
    crawler_run_state = crawler_run_state = (crawler_status['Crawler']['State']).upper()
    logging.info("Crawler Run state is {}".format(crawler_run_state))
    return crawler_run_state

def wait_glue_job(job_name, run_id):
    import boto3
    session = boto3.session.Session()
    glue_client = session.client('glue')
    run_state = 'RUNNING'
    while True:
        if run_state in ['FAILED', 'STOPPED', 'SUCCEEDED']:
            return {'JobRunState': run_state, 'JobRunId': run_id}
        else:
            logging.info(f"Polling for AWS Glue Job {run_id} current run state")
            job_run_status = glue_client.get_job_run(
                JobName=job_name,
                RunId=run_id,
                PredecessorsIncluded=True
            )
            run_state = (job_run_status['JobRun']['JobRunState']).upper()
            logging.info("Crawler Run state is {}".format(run_state))
            time.sleep(10)`
      ```
      1. 파일의 라인 15~17을 앞서 만든 Lambda, Glue crawler, Glue job 이름이 들어가도록 확인 한 다음 external_pipeline.py로 저장 합니다.
      1. 작성 한 external_pipeline.py를 MWAA에서 바라보는 S3의 Dag폴더에 업로드 해 줍니다.
      1. 이제 다시 MWAA 웹 UI로 돌아가 보겠습니다. 30초 정도 이내에 external_pipeline이 들어온 것을 확인하실 수 있습니다. 기본적으로 새로 등록 된 DAG는 일시정지 상태이기 때문에, 왼쪽 버튼을 클릭해서 워크플로우를 시작합니다. Schedule항목에는 해당 워크플로우가 어떤 주기로 수행되는지 확인 하실 수 있습니다. 그리고 수동으로 실행하고 싶을 때에는 오른쪽에 시작버튼을 눌러 수동으로 시작 할 수 있습니다.
      1. External_pipeline을 시작 하셨다면 DAG 이름을 클릭 해 세부 내용을 확인하실 수 있습니다.
      1. DAG의 상세페이지로 들어오면 각 Task 별로 실행 내역을 보실 수 있습니다. Task 별 상태가 표시 된 상자로 마우스를 가져가면 간단한 요약내용을 보실 수 있고, 클릭하면 해당 Task의 상세한 실행내역 및 로그를 확인 할 수 있습니다. 그리고 Graph를 클릭 하면
      지금까지 External Data 파이프라인을 Airflow를 통해 자동화된 워크플로우로 구성 해 보았습니다. 처음으로는 앞서 만들었던 외부 데이터 크롤링을 위한 Lambda함수, Data Catalog를 만드는 Glue Crawler, 데이터를 Parquet으로 변환/압축하는 Glue Job 을 각각의 Task에서 일 단위 주기로 호출하는DAG를 파이썬 코드로 작성 했습니다. 해당 파이썬 코드를 MWAA의 DAG 폴더에 업로드 하여 웹 UI에서 확인하는 것 까지 해 보았습니다.
#### [DAG 구성 (MySQL)](https://catalog.us-east-1.prod.workshops.aws/workshops/7f59c02a-e96d-414f-b513-f0da08844108/ko-KR/module8/8-7)
## DAG 구성 (MySQL)
      앞서 구성 한 MySQL 파이프라인을 MWAA의 DAG로 만들어 매일 자동 실행되도록 구성해 보겠습니다.
      1. 아래 코드를 복사해서 Visual Studio Code 또는 텍스트 에디터에서 새 파일에 붙여넣습니다.
      ```python
from __future__ import annotations

import logging
import time
from datetime import timedelta
from pprint import pprint

import pendulum
from airflow import DAG
from airflow.decorators import task
from airflow.utils.task_group import TaskGroup
from botocore.exceptions import ClientError

bucket_name = "<your bucket>"
mysql_raw_crawler = "demogo-mysql-raw"
tables = ['customers', 'order_detailed', 'orders', 'products', 'sessions']
dms_task_arn = '<dms task arn>'

with DAG(
        dag_id='mysql_pipeline',
        schedule_interval="@daily",
        start_date=pendulum.datetime(2022, 9, 21, tz="UTC"),
        catchup=False,
        default_args={
            'owner': 'demogo',
            'email_on_failure': False,
            'retries': 1,
            'retry_delay': timedelta(minutes=1)
        },
        template_searchpath='/airflow/dags/mart',
        tags=['demogo'],
) as dag:
    @task(task_id='start_dms_mysql_full_refresh_task')
    def start_dms(task_arn):
        import boto3
        session = boto3.session.Session()
        dms_client = session.client('dms')
        response = dms_client.start_replication_task(
            ReplicationTaskArn=task_arn,
            StartReplicationTaskType='reload-target'
        )
        pprint(response)

    @task(task_id='await_dms_replicatoin_task')
    def await_dms(task_arn):
        import boto3
        session = boto3.session.Session()
        dms_client = session.client('dms')

        FINISHED_SIGNAL = "FULL_LOAD_ONLY_FINISHED"
        logging.info(f"Polling for DMS task current run state")
        while True:
            response = dms_client.describe_replication_tasks(
                Filters=[{'Name': 'replication-task-arn',
                          'Values': [task_arn]}],
                WithoutSettings=True
            )
            task_status = response['ReplicationTasks'][0]['Status'].upper()
            if task_status == "STOPPED":
                task_stop_reason = response['ReplicationTasks'][0]['StopReason'].upper()
                if FINISHED_SIGNAL in task_stop_reason:
                    break
            if task_status not in ['RUNNING', 'STARTING']:
                raise DMSError("DMS TASK 비정상 종료")
            logging.info(f'DMS task status: {task_status}')
            time.sleep(5)

    @task(task_id='add_raw_partition_task')
    def add_raw_partition(ds=None):
        execution_date = ds.replace('-', '')[2:]
        # context = get_current_context()
        # execution_date = str(context["execution_date"])[:10].replace('-', '')[2:]
        print(f"execution_date : {execution_date}")
        for table in tables:
            move_stage_to_raw(table, execution_date)

    @task(task_id='glue_crawler_start')
    def glue_crawler_start(crawler_name):
        import boto3
        session = boto3.session.Session()
        glue_client = session.client('glue')
        try:
            logging.info("Initializing AWS Glue Crawler: {}".format(crawler_name))
            response = glue_client.start_crawler(Name=crawler_name)
            return response
        except ClientError as e:
            raise Exception('boto3 client error in start_a_crawler: ' + e.__str__())
        except Exception as e:
            raise Exception('Unexpected error in start_a_crawler: ' + e.__str__())

    @task(task_id='glue_crawler_wait_completion')
    def glue_crawler_wait_completion(crawler_name):
        run_state = 'RUNNING'
        while True:
            if run_state in ['READY', 'STOPPING']:
                return {'CrawlerRunState': run_state}
            else:
                run_state = get_crawler_status(crawler_name)
                time.sleep(10)

    with TaskGroup(group_id='glue_etl_jobs') as tg_1:
        import boto3

        session = boto3.session.Session()
        glue_client = session.client('glue')
        for i, table in enumerate(tables):
            job_name = f'demogo_mysql_raw_{table}'

            @task(task_id=f"glue_job_{table}")
            def glue_job_run(job_name, ds=None):
                execution_date = ds.replace('-', '')[2:]
                job_run = glue_client.start_job_run(
                    JobName=job_name,
                    Arguments={
                        '--EXECUTION_DATE': execution_date
                    }
                )
                return wait_glue_job(job_name, job_run['JobRunId'])

            t = glue_job_run(job_name)
    with TaskGroup(group_id='run_mart_jobs') as tg_2:
        """
            TODO : drop existing table -> delete s3 path -> create table 
        """

        @task(task_id=f'total_net_sales')
        def mart_1():
            return "total_net_sales"

        @task(task_id=f'total_sales')
        def mart_2():
            return "total_sales"

        @task(task_id=f'monthly_active_users')
        def mart_3():
            return "monthly_active_users"

        @task(task_id=f'total_sales_by_categories')
        def mart_4():
            return "total_sales_by_categories"

        @task(task_id=f'total_sales_by_channel')
        def mart_5():
            return "total_sales_by_channel"

        mart_1()
        mart_2()
        mart_3()
        mart_4()
        mart_5()

    @task(task_id='refresh_quicksight')
    def refresh_spice_quicksight():
        """
        TODO : automation
        references :
            - https://stackoverflow.com/questions/59574662/how-to-schedule-or-automate-dataset-refresh-in-aws-quicksight
            - https://gist.github.com/ShafiqaIqbal/a2ccd637786b007a0173c3fba4b1b5f0
        :return:
        """
        return "refresh"

    @task(task_id='waiting_task')
    def waiting_task():
        return 'waiting_task'

    @task(task_id='start_task')
    def start_task():
        return 'start'

    @task(task_id='end_task')
    def end_task():
        return 'end'

    start_task = start_task()
    end_task = end_task()
    start_dms_task = start_dms(dms_task_arn)
    await_dms_task = await_dms(dms_task_arn)
    add_raw_partition_task = add_raw_partition()
    glue_crawler_raw_start_task = glue_crawler_start(mysql_raw_crawler)
    glue_crawler_raw_wait_completion_task = glue_crawler_wait_completion(mysql_raw_crawler)
    refresh_spice_quicksight = refresh_spice_quicksight()
    waiting_task = waiting_task()

    start_task >> start_dms_task >> await_dms_task >> add_raw_partition_task \
    >> glue_crawler_raw_start_task >> glue_crawler_raw_wait_completion_task \
    >> tg_1 >> waiting_task >> tg_2 >> refresh_spice_quicksight >> end_task

def wait_glue_job(job_name, run_id):
    run_state = 'RUNNING'
    while True:
        if run_state in ['FAILED', 'STOPPED', 'SUCCEEDED']:
            return {'JobRunState': run_state, 'JobRunId': run_id}
        else:
            logging.info(f"Polling for AWS Glue Job {run_id} current run state")
            job_run_status = glue_client.get_job_run(
                JobName=job_name,
                RunId=run_id,
                PredecessorsIncluded=True
            )
            run_state = (job_run_status['JobRun']['JobRunState']).upper()
            logging.info("Glue Job Run state is {}".format(run_state))
            time.sleep(5)

def get_crawler_status(crawler_name):
    import boto3
    session = boto3.session.Session()
    glue_client = session.client('glue')
    logging.info(f"Polling for AWS Glue Crawler {crawler_name} current run state")
    crawler_status = glue_client.get_crawler(
        Name=crawler_name
    )
    crawler_run_state = (crawler_status['Crawler']['State']).upper()
    logging.info(f"Crawler Run state is {crawler_run_state}")
    return crawler_run_state

def move_stage_to_raw(table_name, execution_date):
    import boto3
    session = boto3.session.Session()
    s3 = session.resource('s3')
    s3_bucket = s3.Bucket(bucket_name)
    src_info = f'mysql/stage/demogo_raw/{table_name}'
    dst_info = f"mysql/demogo_raw/{table_name}/dt={execution_date}"

    for obj in s3_bucket.objects.filter(Prefix=src_info):
        old_source = {'Bucket': 'demogo', 'Key': obj.key}
        print(obj.key)
        if 'csv' in obj.key:
            new_key = obj.key.replace(src_info, dst_info, 1)
            print(f"Copy {obj.key} -> {new_key}")
            new_obj = s3_bucket.Object(new_key)
            new_obj.copy(old_source)
            s3.Object('demogo', obj.key).delete()

class DMSError(Exception):
    """Raised when the DMS Task failed with any reasons"""
    pass
      ```
      1. 14, 17 라인의 bucket_name, dms_task_arn을 앞서 구성한 설정으로 업데이트 합니다.
      - dms_task_arn 확인 ([https://ap-northeast-2.console.aws.amazon.com/dms/v2/home?region=ap-northeast-2#tasks ](https://ap-northeast-2.console.aws.amazon.com/dms/v2/home?region=ap-northeast-2#tasks))
      1. 파일을 mysql_pipeline.py로 저장한 후 S3에 Airflow용 버킷의 Dag 폴더에 업로드 합니다.
      1. 이제 MWAA 서비스([https://ap-northeast-2.console.aws.amazon.com/mwaa/home?region=ap-northeast-2#environments)로 ](https://ap-northeast-2.console.aws.amazon.com/mwaa/home?region=ap-northeast-2#environments)%EB%A1%9C) 이동하여 웹 UI를 오픈합니다.
      1. S3에 올리신 다음 3분~5분이 지나면 Airflow에 Dag가 등록된 것을 확인하실 수 있습니다. Mysql_pipeline의 왼쪽 아이콘을 클릭해서 Activate 하시고, 파이프라인 이름을 클릭 해 세부 내용을 확인 합니다.
      1. 모든 Task가 정상적으로 수행 된다면 축하 드립니다. Airflow에서 Mysql 파이프라인이 성공적으로 오케스트레이션 된 것을 확인 하셨습니다.
#### 입력값 자료
    | 열 1 | 열 2 |
    | --- | --- |
    | 입력 항목 | 입력 값 |
    | Endpoint identifier | demogo-dms-endpoint-s3 |
    | Bucket name | demogo-AccountID-base |
    | Bucket folder | stage/mysql/ |
    |   |   |
    | 열 1 | 열 2 |
    | --- | --- |
    | 입력 항목 | 입력 값 |
    | Task identifier | demogo-mysql-s3-task |
    | Replication instance | demogo-dms |
    | Source database endpoint | demogo-dms-endpoint-mysql |
    | Target database endpoint | demogo-dms-endpoint-s3 |
    |   |   |
    | 열 1 | 열 2 |
    | --- | --- |
    | Stage Folder | Raw Folder |
    | 개인 버킷/stage/mysql/demogo/customers/모든 csv 파일 선택 | s3://demogo-어카운트ID -base/raw/mysql/demogo/customers/dt=221009/ |
    | 개인 버킷/stage/mysql/demogo/sessions/모든 csv 파일 선택 | s3://demogo-어카운트ID -base/raw/mysql/demogo/sessions/dt=221009/ |
    | 열 1 | 열 2 |
    | --- | --- |
    | Stage Folder | Raw Folder |
    | 개인 버킷/stage/mysql/demogo/order_detailed/모든 csv 파일 선택 | s3://demogo-어카운트ID -base/raw/mysql/demogo/order_detailed/dt=221009/ |
    | 개인 버킷/stage/mysql/demogo/orders/모든 csv 파일 선택 | s3://demogo-어카운트ID -base/raw/mysql/demogo/orders/dt=221009/ |
    | 개인 버킷/stage/mysql/demogo/products/모든 csv 파일 선택 | s3://demogo-어카운트ID -base/raw/mysql/demogo/products/dt=221009/ |
    | 열 1 | 열 2 |
    | --- | --- |
    | Stage Folder | Raw Folder |
    | 개인 버킷/stage/mysql/demogo/customers/모든 csv 파일 선택 | s3://demogo-어카운트ID -base/raw/mysql/demogo/customers/dt=221009/ |
    | 개인 버킷/stage/mysql/demogo/sessions/모든 csv 파일 선택 | s3://demogo-어카운트ID -base/raw/mysql/demogo/sessions/dt=221009/ |
    | 열 1 | 열 2 |
    | --- | --- |
    | 입력 항목 | 입력 값 |
    | Target databse | demogo_raw_db |
    | Target name prefix | mysql- |
    | 열 1 | 열 2 |
    | --- | --- |
    | 입력 항목 | 입력 값 |
    | Name | demogo_mysql_raw_sessions |
    | IAM Role | Demogo-workshop-Glue-role |
    | Number of retries | 0 |
    | Job timeout (minutes) | 10 |
    | Job parameters (Key, Value) | --class, GlueApp |
    | Job parameters (Key, Value) | --EXECUTION_DATE, 221009 |
    | 열 1 | 열 2 |
    | --- | --- |
    | 입력 항목 | 입력 값 |
    | Name | demogo_mysql_raw_orders |
    | IAM Role | Demogo-workshop-Glue-role |
    | Number of retries | 0 |
    | Job timeout (minutes) | 10 |
    | Job parameters (Key, Value) | --class, GlueApp |
    | Job parameters (Key, Value) | --EXECUTION_DATE, 221009 |
    | 열 1 | 열 2 |
    | --- | --- |
    | 입력 항목 | 입력 값 |
    | Name | demogo_mysql_raw_order_detailed |
    | IAM Role | Demogo-workshop-Glue-role |
    | Number of retries | 0 |
    | Job timeout (minutes) | 10 |
    | Job parameters (Key, Value) | --class, GlueApp |
    | Job parameters (Key, Value) | --EXECUTION_DATE, 221009 |
    | 열 1 | 열 2 |
    | --- | --- |
    | 입력 항목 | 입력 값 |
    | Name | demogo_mysql_raw_products |
    | IAM Role | Demogo-workshop-Glue-role |
    | Number of retries | 0 |
    | Job timeout (minutes) | 10 |
    | Job parameters (Key, Value) | --class, GlueApp |
    | Job parameters (Key, Value) | --EXECUTION_DATE, 221009 |
    | 열 1 | 열 2 |
    | --- | --- |
    | Name | stream |
    | Database | demogo_raw_db |
    | Include path | s3://demogo-AccountID-base/raw/kinesis/stream/ |
    | 열 1 | 열 2 |
    | --- | --- |
    | Column name | Data type |
    | userid | Int |
    | device | string |
    | event | string |
    | eventtype | string |
    | timestamp | string |
    | 열 1 | 열 2 |
    | --- | --- |
    | S3 bucket | s3://demogo-AccountID-base/raw/kinesis/stream/ |
    | S3 bucket prefix | raw/kinesis/stream/dt=!{timestampUnknown directive<br><br>Line 87: Unknown text directive “yyyy”}-!{timestampUnknown directive<br><br>Line 87: Unknown text directive “MM”}-!{timestampUnknown directive<br><br>Line 87: Unknown text directive “dd”}/ |
    | S3 bucket error output prefix | raw/kinesis/stream/error/ |
  Q
#### 가이드 라인
  - https://catalog.us-east-1.prod.workshops.aws/workshops/7f59c02a-e96d-414f-b513-f0da08844108/ko-KR
#### 온라인 콘테스트 제출은 QuickSight 차트 2개, MWAA External DAG 1개 입니다
  실습 결과
### 후기
너무 재미있고 유익했다. 
나는 그냥 대학생이였지만 스타트업이나 AWS 클라우드 환경으로 전환하고 싶은 기업의 엔지니어들이 많이 참가한거 같았다.
 40~50명 정도의 사람이 참가하여 1시간 이론 , 3시간 실습을 진행했다.
너무 유익했다. 데이터 파이프라인의 전체적인 구조를 잡고 직접 실습을 하면서  Mysql내부 데이터를 QuickSight와 AirFlow로 가시화했다. 
정형, 비정형, 실시간,외부 데이터(Naver API) 등 여러 데이터의 종류별 처리 방법과 아키텍처를 설명해줬다.
AWS내부 여러 서비스를 직접 사용하면서 데이터 파이프라인의 전체를 구성하는 경험은 처음이였다.
기업을 다니는 분들에게도 좋지만 학생들이 교육용으로 들어도 좋을꺼같다.
AWS를 조금만 알고있다면 따라가기는 어렵지 않다.
워낙 세세하게 자세히 설명해 줬기 때문에 전체적인 Flow만 이해하고 나중에 복습하면 도움이 많이 될꺼같다.
앞으로 이런 강의가 많이 나왔으면 좋겠다, 마지막으로 AWS에게 이런 강의를 만들어줘서 감사하다고 전하고싶다.

## 출처

- 원문: https://www.notion.so/AWS-Demogo-Prime-245172a556d680619033dd70e3aedfd4
- Vault path: wiki/notes/seminars/AWS-Demogo-Prime.md
