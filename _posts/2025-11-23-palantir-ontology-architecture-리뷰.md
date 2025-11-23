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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/8e7b8811-c76a-48c8-a087-1597798bc64b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663D6S7ZFE%2F20251123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251123T092254Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG0aCXVzLXdlc3QtMiJGMEQCICFGzoQ%2FUGrb7eaavqOHnFS9yM1qvmi90rBa17NxNvuiAiB9FWIALQQtsciVZSSmBJXlJju3VVqwV3on61QGoyGaxSr%2FAwg2EAAaDDYzNzQyMzE4MzgwNSIMSQaGdzdXiRgQs8pgKtwDREox%2FQXrdQxfiSPZSDQcd5BbbyvDJ63QiOtzNQEKkR30%2FFyfrcBXEQF%2BkAAF%2Frn4tz%2FuzcNxXn3Tnriw7QeX7siqZwXBywNv90fS7cEq4Brqmh4wywCoWW7BIrDTfcRbvqBbTo0y9JfqIaBFFd9%2F3ZW5juhNqU7ht6rmxdYeNsrTd5YSLA9HJNQD6RL5S%2BIR6mnm5Czn4sI%2FpwO7UNl%2BB8lgKdJ0nuHpaTu6dstHm%2FMBcjVahiS31iut8o3aFrsccGCwq2ASBbRz%2FgDYtPZsirE8IDEEycFs%2Fg4xx3h327ExWHYtXEY55iVy1prppwxRriguMCX5OnAocrtv7lzXoV4tyJStIlkp%2B%2Bh73%2BRskDTs5vE%2B99XIpzvQKtibvFfABSZFGV6pP9IDWJUaTZutUcmFHejsaq5mk%2BO1VHyR%2BypqGbaQJq3sT7%2BRuVMHjwYQggmdGslYUgdaiK6PMDA7FFcbgT3JhixcVRdopPYsZWbqpjVKZVTn8K2afARS73iI3farUwh6IiQCd5yqDfQIjjI1pTBofDVGwN%2FvOA7amwryywT0IpKaNY9Owv4cs0ttrbcI4jsiG9HqoE4SFUCinxvtl2FhgzD78KWUl9QHnOr33GoP4ww3IGKkJeUw4qOKyQY6pgETLuvbZtkHrPW3CRrXNLuvM%2Bq%2BMlf05yR3D%2FpMyJNvLq%2BwSLxGCDuHLCClfNwyh3d6Af5%2FCbu9AI9zFIzKNjN3htpBQ4hw%2FbilK4lKn5qYU9ZzqytvUDkUzGTy%2BAAGO%2Bw5BV0hYGzQpaHaJlB0UeWJWwAC1fCFGODxmT%2FDa7MN7l8fu%2BA11m5vwI9dSMI2AN4mIEdLu8vzkpHe7JwrPdhqL%2FjVfY49&X-Amz-Signature=792343c0dc61eb16ca9272921eba599bf89b6211a9b78aeb32eec7b3aa1f2f92&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/d6c01b0a-3d88-4c6d-b505-b0df9e9cf21e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663D6S7ZFE%2F20251123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251123T092254Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG0aCXVzLXdlc3QtMiJGMEQCICFGzoQ%2FUGrb7eaavqOHnFS9yM1qvmi90rBa17NxNvuiAiB9FWIALQQtsciVZSSmBJXlJju3VVqwV3on61QGoyGaxSr%2FAwg2EAAaDDYzNzQyMzE4MzgwNSIMSQaGdzdXiRgQs8pgKtwDREox%2FQXrdQxfiSPZSDQcd5BbbyvDJ63QiOtzNQEKkR30%2FFyfrcBXEQF%2BkAAF%2Frn4tz%2FuzcNxXn3Tnriw7QeX7siqZwXBywNv90fS7cEq4Brqmh4wywCoWW7BIrDTfcRbvqBbTo0y9JfqIaBFFd9%2F3ZW5juhNqU7ht6rmxdYeNsrTd5YSLA9HJNQD6RL5S%2BIR6mnm5Czn4sI%2FpwO7UNl%2BB8lgKdJ0nuHpaTu6dstHm%2FMBcjVahiS31iut8o3aFrsccGCwq2ASBbRz%2FgDYtPZsirE8IDEEycFs%2Fg4xx3h327ExWHYtXEY55iVy1prppwxRriguMCX5OnAocrtv7lzXoV4tyJStIlkp%2B%2Bh73%2BRskDTs5vE%2B99XIpzvQKtibvFfABSZFGV6pP9IDWJUaTZutUcmFHejsaq5mk%2BO1VHyR%2BypqGbaQJq3sT7%2BRuVMHjwYQggmdGslYUgdaiK6PMDA7FFcbgT3JhixcVRdopPYsZWbqpjVKZVTn8K2afARS73iI3farUwh6IiQCd5yqDfQIjjI1pTBofDVGwN%2FvOA7amwryywT0IpKaNY9Owv4cs0ttrbcI4jsiG9HqoE4SFUCinxvtl2FhgzD78KWUl9QHnOr33GoP4ww3IGKkJeUw4qOKyQY6pgETLuvbZtkHrPW3CRrXNLuvM%2Bq%2BMlf05yR3D%2FpMyJNvLq%2BwSLxGCDuHLCClfNwyh3d6Af5%2FCbu9AI9zFIzKNjN3htpBQ4hw%2FbilK4lKn5qYU9ZzqytvUDkUzGTy%2BAAGO%2Bw5BV0hYGzQpaHaJlB0UeWJWwAC1fCFGODxmT%2FDa7MN7l8fu%2BA11m5vwI9dSMI2AN4mIEdLu8vzkpHe7JwrPdhqL%2FjVfY49&X-Amz-Signature=5963f78005f572efc4d010dcd99258399a0623f7ebe0bc76efb3cc0e3ba18d06&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

