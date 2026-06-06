---
title: "Palantir Ontology Architecture 리뷰"
date: 2025-11-23 07:09:00 +0900
categories: [기술소개]
tags: [palantir, ontology, Architecture]
description: 팔란티어 온톨로지 아키텍처 리뷰
toc: true
comments: true
---

## Palantir Ontology Architecture 리뷰

온톨로지란 조직의 디지털 트윈 역할을 합니다.

기업 내/외 방대한 양의 데이터를 기반으로 의미를 부여하고, 관계성을 부여하여 모든 유형의 의미적요소(객체, 속성, 링크)와 동적 요소(작업, 함수)을 모두 포함합니다.

### Ontology 온톨로지 핵심 개념

조직(기업)의 현실세계(Real-World)를 디지털로 가상화하여, 조직의 문제점을 디지털에서 최적화된 알고리즘을 통해 해결해 나아갈 수 있는 기반을 마련하는 것이 Ontology Architeture의 개념이다.

### 팔란티어의 온톨로지 

- Palantir의 온톨로지는 **실체(entity) + 속성(property) + 관계(link) + 행위(action)**의 모델링을 통해 조직의 데이터를 의미론적으로 재구성하는 구조입니다.
- 기존의 “테이블 + 컬럼” 모델을 객체지향적 모델로 바꾸어, 조직 전반의 데이터를 **객체 그래프(object-graph)** 형태로 표현할 수 있게 합니다.
- 또한 단순히 데이터 분석을 위한 모델이 아니라, **액션(행위)** 스키마까지 포함하고 있어 분석 결과 → 실행 흐름을 설계하는 데 적합합니다.
- 조직 내 여러 팀/도메인이 객체 타입을 정의하고 공유속성/shared properties, 인터페이스/interfaces 등을 활용해 일관된 데이터 모델을 유지할 수 있도록 설계되어 있습니다.
- 권한(Role) 및 함수(Function) 등도 온톨로지 내부에 포함되어 있습니다.
**주요 구성 요소**

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/8e7b8811-c76a-48c8-a087-1597798bc64b/image.png)

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/d6c01b0a-3d88-4c6d-b505-b0df9e9cf21e/image.png)

- Object Type(객체 타입) 
- Property (속성)
- Shared property (공유 속성)
- Link type (링크 타입)
- Action Type (액션 타입)
- Roles (역할)
- Functions (함수)
- Interfaces (인터페이스)
- Object Views (객체뷰)
### 기능적 구성 요소 및 아키텍처 

아래는 Palantir의 Ontology 백엔드 구조의 주요 컴포넌트입니다. Palantir

- **Ontology Metadata Service (OMS)**: Ontology  내 객체 타입(object types), 링크 타입(link types), 액션 타입(action types) 등을 정의하는 메타데이터 서비스. 
- **Object Databases**: 실제 객체 데이터(instance)들을 저장하고 인덱싱하는 저장소.
- **Object Set Service (OSS)**: 객체 집합(object sets)을 조회하고 필터링·공유하는 서비스.
- **Object Data Funnel**: 여러 데이터 소스(dataset, streaming, views 등)에서 객체 인덱싱(write) 과정으로 데이터를 받아들이고 Ontology 저장소로 쓰기(write)하는 파이프라인 서비스.
- **Actions / Functions**: 객체에 대한 행위(action)나 함수(function)를 정의하고 실행 가능하도록 하는 부분. 즉 “데이터가 바뀌면 어떤 행동이 발생할 수 있는가”를 모델링합니다.
참고자료

- https://www.palantir.com/docs/foundry/ontology/overview/
- https://www.palantir.com/docs/foundry/ontology/core-concepts
- https://www.palantir.com/docs/foundry/object-backend/overview/
- https://www.palantir.com/docs/foundry/object-backend/overview/?utm_source=chatgpt.com

