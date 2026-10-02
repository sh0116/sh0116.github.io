---
source: knowledge-base
origin: notion
title: "Palantir Ontology Architecture 리뷰"
area: "아키텍처와 기술 소개"
tags: ["area/architecture", "concept/architecture", "concept/ontology", "vendor/palantir"]
created: "2025-11-23T07:09:00.000Z"
last_edited: "2025-11-23T23:16:00.000Z"
status: published
public: true
notion_id: "2b4172a5-56d6-8038-987b-e5c30450a112"
notion_url: "https://www.notion.so/Palantir-Ontology-Architecture-2b4172a556d68038987be5c30450a112"
type: note
updated: 2026-07-07
---

# Palantir Ontology Architecture 리뷰

## 요약

팔란티어 온톨로지 아키텍처 리뷰

아키텍처 개념을 실제 설계 판단에 연결하기 위한 참고 노트입니다.

## 핵심 포인트

- 팔란티어 온톨로지 아키텍처 리뷰
- Palantir Ontology Architecture 리뷰
- Ontology 온톨로지 핵심 개념
- 팔란티어의 온톨로지
- 기능적 구성 요소 및 아키텍처

## 지식 그래프

- [[wiki/mocs/Knowledge Base|Knowledge Base]]
- [[wiki/mocs/아키텍처와-기술-소개|아키텍처와 기술 소개]]

## 정리 내용

### Palantir Ontology Architecture 리뷰
온톨로지란 조직의 디지털 트윈 역할을 합니다.
기업 내/외 방대한 양의 데이터를 기반으로 의미를 부여하고, 관계성을 부여하여 모든 유형의 의미적요소(객체, 속성, 링크)와 동적 요소(작업, 함수)을 모두 포함합니다.
#### Ontology 온톨로지 핵심 개념
조직(기업)의 현실세계(Real-World)를 디지털로 가상화하여, 조직의 문제점을 디지털에서 최적화된 알고리즘을 통해 해결해 나아갈 수 있는 기반을 마련하는 것이 Ontology Architeture의 개념이다.
#### 팔란티어의 온톨로지 
- Palantir의 온톨로지는 실체(entity) + 속성(property) + 관계(link) + 행위(action)의 모델링을 통해 조직의 데이터를 의미론적으로 재구성하는 구조입니다.
- 기존의 “테이블 + 컬럼” 모델을 객체지향적 모델로 바꾸어, 조직 전반의 데이터를 객체 그래프(object-graph) 형태로 표현할 수 있게 합니다.
- 또한 단순히 데이터 분석을 위한 모델이 아니라, 액션(행위) 스키마까지 포함하고 있어 분석 결과 → 실행 흐름을 설계하는 데 적합합니다.
- 조직 내 여러 팀/도메인이 객체 타입을 정의하고 공유속성/shared properties, 인터페이스/interfaces 등을 활용해 일관된 데이터 모델을 유지할 수 있도록 설계되어 있습니다.
- 권한(Role) 및 함수(Function) 등도 온톨로지 내부에 포함되어 있습니다.
주요 구성 요소
![[_attachments/notion/Palantir-Ontology-Architecture-리뷰/2b4172a556d680079bf7fdc4b1478940.png]]
![[_attachments/notion/Palantir-Ontology-Architecture-리뷰/2b4172a556d6808fa27bea0043b69f84.png]]
- Object Type(객체 타입) 
  - 조직 내 Entity 또는 Event를 나타내는 스키마의 정의
  - 고객, 주문, 자산취득 등이 될 수 있음.
  - 테이블 기반의 모델링을 벗어나, 객체 지향적인 모델링 관점에서 바라봐야함, 테이블 명이 객체 타입, 컬럼을 속성(property)로 전환하여 생각하면 적당할 것 같다.
- Property (속성)
  - 객체 타입(Object Type)에 대한 특징을 정의하는 스키마 단위
  - 이름, 고객번호, 등록일
  - 동일하거나 유사한 속성을 여러 도메인에 걸쳐 재사용할 수 있음, 데이터의 일관선이 올라감.
- Shared property (공유 속성)
  - 여러 ObjectType이 공유하는 동일한 Property 이다.
- Link type (링크 타입)
  - 두 객체(Property) 간의 관계를 정의하는 스키마이다.
  - FK로 조인하는 테이블 모델 대신, 객체-관계 모델을 명시적으로 설계함으로써 조직 전반의 연결성을 더 명확히 표현할 수 있다.
- Action Type (액션 타입)
  - 객체나 링크에 대해 편집 또는 변경을 정의한 스키마이다.
  - 고객 상태 변경, 주문 승인, 자산 소각
  - 액션을 통해 부수효과(Side-effect)도 본 스키마에 포함된다.
  - 데이터 기반의 행위를 설계할 수 있는 동적 요소를 위해 중요한 파트이다.
- Roles (역할)
  - 리소스(객체, 속성, 링크, 액션 등)에 접근할 수 있는 권한 제어
  - 보안 및 거버넌스 측면에서 객체 혹은 액션에 대해 어떤 권한을 갖는지 명시 및 관리할 수 있다.
- Functions (함수)
  - 코드 기반의 로직으로 객체 및 객체 집합(Object Set)을 입력으로 받아 처리하고, 결과를 반환
  - 동적요소로써 액션, Application등에 활용함.
- Interfaces (인터페이스)
  - 객체 타입이 구현해야하는 형태(shape) 및 기능(Capabilities)를 정해주는 스키마(타입)
  - 여러 객체 타입을 동일한 인터페이스로 구현함으로써, 다형성을 지원합니다.
  - 객체 타입 간 공통된 행위나 속성을 묶을 수 있어, 모델의 확장성 및 재사용성을 지원함.
- Object Views (객체뷰)
  - 객체 인스턴스와 관련된 정보를 한데 모은 중앙 허브 역할.
  - 객체의 속성, 연결된 객체, 연관 매트릭, 분석 대시보드/어플리케이션 등이 포함됨
  - 객체 기반 분석, 워크 플로우를 빠르게 수행할 수 있고, 객체 지향적 객체 중심적인 UX설계가 가능함.
#### 기능적 구성 요소 및 아키텍처 
아래는 Palantir의 Ontology 백엔드 구조의 주요 컴포넌트입니다. [Palantir](https://palantir.com/docs/foundry/object-backend/overview/?utm_source=chatgpt.com)
- Ontology Metadata Service (OMS): Ontology  내 객체 타입(object types), 링크 타입(link types), 액션 타입(action types) 등을 정의하는 메타데이터 서비스. 
- Object Databases: 실제 객체 데이터(instance)들을 저장하고 인덱싱하는 저장소.
- Object Set Service (OSS): 객체 집합(object sets)을 조회하고 필터링·공유하는 서비스.
- Object Data Funnel: 여러 데이터 소스(dataset, streaming, views 등)에서 객체 인덱싱(write) 과정으로 데이터를 받아들이고 Ontology 저장소로 쓰기(write)하는 파이프라인 서비스.
- Actions / Functions: 객체에 대한 행위(action)나 함수(function)를 정의하고 실행 가능하도록 하는 부분. 즉 “데이터가 바뀌면 어떤 행동이 발생할 수 있는가”를 모델링합니다.
참고자료
- [https://www.palantir.com/docs/foundry/ontology/overview/](https://www.palantir.com/docs/foundry/ontology/overview/)
- [https://www.palantir.com/docs/foundry/ontology/core-concepts](https://www.palantir.com/docs/foundry/ontology/core-concepts)
- [https://www.palantir.com/docs/foundry/object-backend/overview/](https://www.palantir.com/docs/foundry/object-backend/overview/?utm_source=chatgpt.com)
- [https://www.palantir.com/docs/foundry/object-backend/overview/?utm_source=chatgpt.com](https://www.palantir.com/docs/foundry/object-backend/overview/?utm_source=chatgpt.com)

## 출처

- 원문: https://www.notion.so/Palantir-Ontology-Architecture-2b4172a556d68038987be5c30450a112
- Vault path: wiki/notes/architecture/Palantir-Ontology-Architecture-리뷰.md
