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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/24bfc627-5108-4107-8b73-ce84dd21c2a0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WCS7ZGLC%2F20251123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251123T225656Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJIMEYCIQDj9CHIct2MjPQHDkw3afsbs6Xom89s%2B0UHGM5AO4qVaAIhAOgmx6M%2F1XhfOQKSgvlJQGafVjJ1%2BbQbtXP4XrLgY8W2Kv8DCEgQABoMNjM3NDIzMTgzODA1Igws8TpVHN4%2Fm8krbdoq3AMj7txPnNF3pd03eRmPX%2F9yPP8xwwAlXuVh3UpYC3GgtlEa9J%2FcgpJmuGkEFTcx2QJ8%2B60EGnAOhx65ZqVMfx5uybFJr7DLicNXjiBzCoupIgsaWYTQOsQAvYEQYc9zYdDIgaGvwsbewJsjNxCjtYmJ2RtACwOX0S2w%2FNjXzdh%2B9BQA2cpvCH5T77ohHdGy1ipZEw8nmcCbH%2FfMffAh4H%2FqORxhG%2FmS35I8QOmTicYko9zjZw7tgqTo4U9CZE3QP1jo46kpkXNhO14y9aHln2BiXmgMVrnKRZJ1o5OuHaM5VLkkUvMnbhEHRCqrdsv4OPc0r4diLZd0X0tpuyZlDuv40fNG2mcDF5rPwS3GeqLfYyY%2FeWOLMFurmnvscMeHrYAUAwvHCPWOpNCEYZ7Xl60O6YDw3kcbazTPbPhF6%2FvriXwWu3SnL8nn8r1dsLf%2FXmJ6QfqbYl49gnuleFRbrsIXXa3FcGYdHOCxZ0CO3jqACPgAGu81lpIgXJCF%2Bj6P%2F88wrT3Dn2I3bgs2MLgKh0iP5qaTpG2TTNqtpPmIrGsno8FCTYWJ53H%2BdxLJlAJ1Pe2Bg5nGwO6%2BcF3l0NSuTI0EA4w79rOuehJg3gfe3L75svbHXqr4fgcyp2%2FV3TDTmo7JBjqkAXiWpgNPYU8znj4xXfl8%2F%2BQWakxAFqwgzczy6YBrFelBj0GobhkIaryuZ7YQ1QW%2Fy2JodUJNiWqYxbO1IzqGrlnZJ9qO3dsxySHFh6QtECMq5Asf9BNbSpjqq2iY31RcPXGS3vvat69lLIrZ%2BlxEKL3W%2B4XBp5ef4KkRxxS5XwNP8SAZd5Pg6M81F%2FlReMsBhHNdh%2BcZ%2BswOhU5RPYLysdW%2BcY9i&X-Amz-Signature=66cdf20c6c80bb12d1457bdcee756600b3e5fe2de2f8ef704fa7cdee8583ab8c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

