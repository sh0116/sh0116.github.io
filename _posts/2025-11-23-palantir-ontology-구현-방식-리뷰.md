---
title: "Palantir Ontology 구현 방식 리뷰"
date: 2025-11-23 09:13:00 +0900
categories: [기술소개]
tags: [Architecture, 팔란티어, platform, palantir, ontology]
description: Palantir Ontology 구현 방식 리뷰
toc: true
comments: true
---

## Ontology Layer 

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/24bfc627-5108-4107-8b73-ce84dd21c2a0/image.png)

**데이터 수집/전처리/적재(일반, 대규모, 실시간)**

1. 데이터 처리 Workflow 
1. 기반 처리 기술
**온톨로지 메타모델**

온톨로지의 개념은 객체지향프로그래밍(OOP)과 매우 유사하다.

각 기업(조직)의 비즈니스 개념들을 객체지향방식으로 데이터 모델링하여 추상화한 계층이다.

| 팔란티어 개념 | 객체 지향 모델 개념 | 테이블 모델 개념 |
| --- | --- | --- |
| 객체(Object) | 클래스(Class) | 테이블 |
| 속성(Property) | 속성(Attribute) | 컬럼 |
| 연결(Link) | 관계(Association) | FK |

**온톨로지 메타모델 구현 방식**

온톨로지의 요구 사항은 특정 객체를 빠르게 조회하고, 객체 간의 복잡한 관계성을 탐색하며, 대규모 데이터셋을 검색하는 것이다.

때문에, 단일 데이터베이스를 사용하는 것이 아닌 여러 기술을 조합한 복합적인 구조가 생성된다.

- 객체 저장소 : 객체 데이터 자체는 카산드라(Cassandra)와 같은 수평적으로 확장 가능한, Key-Value 저장소에 저장될 수 있다. 각 객체는 고유 ID를 KEY형식으로 / 각 객체의 실 데이터를 Json 포맷으로 Value값으로 저장한다.
- 검색 및 그래프 인덱싱 : 빠른 검색, 집계, 그래프 탐색 기능을 위해서 엘라스틱서치(Elasticsearch)나 루씬(Lucene) 기반의 인덱스 검색이 필수적이다. Key-Value 저장소에 저장된 객체 데이터는 검색 엔진에 인덱싱되어 쿼리를 통해 제공된다
**팔란티어의 온톨로지 데이터 활용 방식**

개발자는 파이썬 OSDK (Ontology SDK)를 사용하여 온톨로지와 상호작용한다.

> # 연착 상태인 비행기들을 전부 불러오는 코드를 보다 직관적으로 작성할 수 있다.**
client.ontology.object.비행기.where(status=”연착”).all()  **

온톨로지에는 액션(Action)이라는 동적 요소도 정의할 수 있어, 액션(Action)을 호출하면 Data의 업데이트, 플랫폼의 거버넌스, 보안, 감사추적 등 모든 트랙잭션들을 수행할 수 있다.

참고자료

- https://daddynkidsmakers.blogspot.com/2025/10/blog-post_11.html

