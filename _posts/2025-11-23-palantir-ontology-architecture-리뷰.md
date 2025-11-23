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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/8e7b8811-c76a-48c8-a087-1597798bc64b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666EYTNLQD%2F20251123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251123T232329Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJGMEQCIGBjNmh1coFRXBUwe7FXF2gPJcHQExdlImu1RKHkYOkbAiB4HlXR6m7tpQPetOQOdtVNtenbI4NwlPHYEgU5FNQwKCr%2FAwhIEAAaDDYzNzQyMzE4MzgwNSIMkTKAjWwSudao2KKeKtwDgE89BP%2BIpTI3w%2B2vgFcwSpwKnh7rKsWxbw8KZ1mzw%2Fd7Q4Z8fmXmoasVEfcsFIj8q8OZu5%2BVtk4Hl54XP3zKWYpOfmq5ZchItrjWW4p35AvZyQTKw%2FlygmvpT%2FOHceLBo8zMac8buWCeyMQMJigccS3CGCDKYeI%2BjltRbQuQwFBVpTxBxkrD20LPfQ%2BrOsNXMaY1sn2gR9JUxZkvOr1ZvE46e5Wmzg6IaQFRY8rH5saBspbPpA5KYVN0lcDBG%2FN40Es1qaBxChxDdVvauOwSZ9RglFeP954l2CUOOABaij3IX1TmWXNFuv9ic6Quqfa4zH2LvT%2BecohHCMTQvsI9DFIIi6Nq6OUInhfZrAoldN1uRwKHSCOnh1JWtBHb512vE7UArwoxigb6OYxNkDz6QhP%2B1twLuc1aNa7UbqU%2BUpFdagWJxdu61bCmoe7e6cpUV9t6ahPWCrnGwAK99Kp9CDEL1l%2B%2BUJ8lPENkiA78lX2Ic6xtih7yau9Gl5xCRDyk6b1FqEe%2FCSlo5IVUwaMtbGo1XTyAy1%2FPp%2BGojIRY4CJny1ic4l%2BSjesKKl3kbfCoJBEQ0Z8Q4wGZJUz6r%2Fw%2BFWBGs9e6LgJnVplXoIzUzVKKAAs8hzADaAyEPwEwjJqOyQY6pgHFjDqytneMKPYWeREWZ8RRfqgfwbXl4u9dhKpHeqXDGoQucNCOJ6YYzKzbyQV7oYFYGbEtdfUKhf%2BnXuhTNCeGi%2F0KUpgoi8zhigN0CRIwXR2ZBR6l5vY2h1eYDvu%2FoZ5WbGY5g8ZDAtfXtb514kXKrrwUaAPEJaGMZWLLWUlSx130oBR1m2n3lCPeqjUnU%2FAc4OyPFH16Sgni4EQDO7Onk%2BaRoH4r&X-Amz-Signature=e9855119aaf1b46983341eabc46ebfb28a6ed2a6a116db9d15676cacfbdd2a96&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/d6c01b0a-3d88-4c6d-b505-b0df9e9cf21e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666EYTNLQD%2F20251123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251123T232329Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJGMEQCIGBjNmh1coFRXBUwe7FXF2gPJcHQExdlImu1RKHkYOkbAiB4HlXR6m7tpQPetOQOdtVNtenbI4NwlPHYEgU5FNQwKCr%2FAwhIEAAaDDYzNzQyMzE4MzgwNSIMkTKAjWwSudao2KKeKtwDgE89BP%2BIpTI3w%2B2vgFcwSpwKnh7rKsWxbw8KZ1mzw%2Fd7Q4Z8fmXmoasVEfcsFIj8q8OZu5%2BVtk4Hl54XP3zKWYpOfmq5ZchItrjWW4p35AvZyQTKw%2FlygmvpT%2FOHceLBo8zMac8buWCeyMQMJigccS3CGCDKYeI%2BjltRbQuQwFBVpTxBxkrD20LPfQ%2BrOsNXMaY1sn2gR9JUxZkvOr1ZvE46e5Wmzg6IaQFRY8rH5saBspbPpA5KYVN0lcDBG%2FN40Es1qaBxChxDdVvauOwSZ9RglFeP954l2CUOOABaij3IX1TmWXNFuv9ic6Quqfa4zH2LvT%2BecohHCMTQvsI9DFIIi6Nq6OUInhfZrAoldN1uRwKHSCOnh1JWtBHb512vE7UArwoxigb6OYxNkDz6QhP%2B1twLuc1aNa7UbqU%2BUpFdagWJxdu61bCmoe7e6cpUV9t6ahPWCrnGwAK99Kp9CDEL1l%2B%2BUJ8lPENkiA78lX2Ic6xtih7yau9Gl5xCRDyk6b1FqEe%2FCSlo5IVUwaMtbGo1XTyAy1%2FPp%2BGojIRY4CJny1ic4l%2BSjesKKl3kbfCoJBEQ0Z8Q4wGZJUz6r%2Fw%2BFWBGs9e6LgJnVplXoIzUzVKKAAs8hzADaAyEPwEwjJqOyQY6pgHFjDqytneMKPYWeREWZ8RRfqgfwbXl4u9dhKpHeqXDGoQucNCOJ6YYzKzbyQV7oYFYGbEtdfUKhf%2BnXuhTNCeGi%2F0KUpgoi8zhigN0CRIwXR2ZBR6l5vY2h1eYDvu%2FoZ5WbGY5g8ZDAtfXtb514kXKrrwUaAPEJaGMZWLLWUlSx130oBR1m2n3lCPeqjUnU%2FAc4OyPFH16Sgni4EQDO7Onk%2BaRoH4r&X-Amz-Signature=899560067e27ed529234707f7e1e8cb4f76c53c7100930081fe180586b4f62c7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

