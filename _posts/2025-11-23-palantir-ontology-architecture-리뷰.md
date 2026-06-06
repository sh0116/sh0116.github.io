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

조직(기업)의 현실세계(Real-World)를 디지털로 가상화하여, 조직의 문제점을 디지털에서 최적화된 알고리즘을 통해 해결해 나아갈 수 있는 기반을 마련하는 것이 Ontology Architeture의 개념이다.

### 기능적 구성 요소 및 아키텍처 

아래는 Palantir의 Ontology 백엔드 구조의 주요 컴포넌트입니다. Palantir

- **Ontology Metadata Service (OMS)**: Ontology  내 객체 타입(object types), 링크 타입(link types), 액션 타입(action types) 등을 정의하는 메타데이터 서비스. 
- **Object Databases**: 실제 객체 데이터(instance)들을 저장하고 인덱싱하는 저장소.
- **Object Set Service (OSS)**: 객체 집합(object sets)을 조회하고 필터링·공유하는 서비스.
- **Object Data Funnel**: 여러 데이터 소스(dataset, streaming, views 등)에서 객체 인덱싱(write) 과정으로 데이터를 받아들이고 Ontology 저장소로 쓰기(write)하는 파이프라인 서비스.
- **Actions / Functions**: 객체에 대한 행위(action)나 함수(function)를 정의하고 실행 가능하도록 하는 부분. 즉 “데이터가 바뀌면 어떤 행동이 발생할 수 있는가”를 모델링합니다.

