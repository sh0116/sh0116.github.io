---
source: knowledge-base
origin: notion
title: "Palantir Ontology 구현 방식 리뷰"
area: "아키텍처와 기술 소개"
tags: ["area/architecture", "concept/architecture", "concept/ontology", "concept/platform", "vendor/palantir"]
created: "2025-11-23T09:13:00.000Z"
last_edited: "2025-11-23T23:04:00.000Z"
status: published
public: true
notion_id: "2b4172a5-56d6-80f5-9088-ecbd6b8310a9"
notion_url: "https://www.notion.so/Palantir-Ontology-2b4172a556d680f59088ecbd6b8310a9"
type: note
updated: 2026-07-07
---

# Palantir Ontology 구현 방식 리뷰

## 요약

Palantir Ontology 구현 방식 리뷰

아키텍처 개념을 실제 설계 판단에 연결하기 위한 참고 노트입니다.

## 핵심 포인트

- Palantir Ontology 구현 방식 리뷰
- Ontology Layer

## 지식 그래프

- [[wiki/mocs/Knowledge Base|Knowledge Base]]
- [[wiki/mocs/아키텍처와-기술-소개|아키텍처와 기술 소개]]

## 정리 내용

### Ontology Layer 
![[_attachments/notion/Palantir-Ontology-구현-방식-리뷰/2b4172a556d68021a39dc60bb4fd6407.png]]
데이터 수집/전처리/적재(일반, 대규모, 실시간)
1. 데이터 처리 Workflow 
  - PDF, 문서, 이미지와 같은 비정형 데이터(Media Sets이라고 불림)을 수집하고, 데이터를 파싱하는 과정은 블랙박스의 형태가 아닌 Python/Java등 로직을 통해 변환한다.
  - 테스트 가능한 파이프라인 형태로 구성이 가능하여, 신뢰성과 거버넌스를 확보하는 엔지니어링이다.
1. 기반 처리 기술
  - 데이터 변환 및 통합 로직은 독점 엔진에 종속되지 않는다. 모든 데이터는 아파치 파케이(Apache Parquet), 아브로(Avro)와 같은 표준 형식으로 저장되며, 대규모 배치 처리를 위해 아파치 스파크, 실시간 스트림 처리를 위한 아파치 플링크와 같은 오픈소스 런타임을 사용한다.
온톨로지 메타모델
온톨로지의 개념은 객체지향프로그래밍(OOP)과 매우 유사하다.
각 기업(조직)의 비즈니스 개념들을 객체지향방식으로 데이터 모델링하여 추상화한 계층이다.
| 팔란티어 개념 | 객체 지향 모델 개념 | 테이블 모델 개념 |
| --- | --- | --- |
| 객체(Object) | 클래스(Class) | 테이블 |
| 속성(Property) | 속성(Attribute) | 컬럼 |
| 연결(Link) | 관계(Association) | FK |
온톨로지 메타모델 구현 방식
온톨로지의 요구 사항은 특정 객체를 빠르게 조회하고, 객체 간의 복잡한 관계성을 탐색하며, 대규모 데이터셋을 검색하는 것이다.
때문에, 단일 데이터베이스를 사용하는 것이 아닌 여러 기술을 조합한 복합적인 구조가 생성된다.
- 객체 저장소 : 객체 데이터 자체는 카산드라(Cassandra)와 같은 수평적으로 확장 가능한, Key-Value 저장소에 저장될 수 있다. 각 객체는 고유 ID를 KEY형식으로 / 각 객체의 실 데이터를 Json 포맷으로 Value값으로 저장한다.
- 검색 및 그래프 인덱싱 : 빠른 검색, 집계, 그래프 탐색 기능을 위해서 엘라스틱서치(Elasticsearch)나 루씬(Lucene) 기반의 인덱스 검색이 필수적이다. Key-Value 저장소에 저장된 객체 데이터는 검색 엔진에 인덱싱되어 쿼리를 통해 제공된다
> [!note] 레이블이 있는 속성 그래프 ( Labeled Property Graph, LPG)
  객체는 노드(Node) Link는 간선(Edge)로 표현되어 확장성이 뛰어난 Key-Value 저장소와 인덱싱 검색을 조합하여 효율적으로 구축한다.
팔란티어의 온톨로지 데이터 활용 방식
개발자는 파이썬 OSDK (Ontology SDK)를 사용하여 온톨로지와 상호작용한다.
> # 연착 상태인 비행기들을 전부 불러오는 코드를 보다 직관적으로 작성할 수 있다.
> client.ontology.object.비행기.where(status=”연착”).all()  
예시 코드
  ```scss
import os
from <YOUR_PACKAGE_NAME> import FoundryClient
from <YOUR_PACKAGE_NAME>.core.api import UserTokenAuth

# 1. Foundry 클라이언트 초기화
try:
    auth = UserTokenAuth(
        hostname=os.environ,
        token=os.environ
    )
    client = FoundryClient(auth=auth, hostname=os.environ)
except KeyError:
    print("오류: FOUNDRY_HOSTNAME 및 FOUNDRY_TOKEN 환경 변수를 설정.")
    exit()

# 2. 온톨로지 객체 쿼리: 지연된 화물 검색
#    OSDK는 온톨로지의 각 객체 유형(예: Shipment)에 대한 접근자를 제공
#    'where' 절을 사용하여 특정 속성 값(status == "Delayed")을 기준으로 객체를 필터링
print("\n'지연' 상태인 화물을 검색...")
delayed_shipments = client.ontology.objects.Shipment.where(status="Delayed").all()

if not delayed_shipments:
    print("지연된 화물이 없음.")
else:
    print(f"총 {len(delayed_shipments)}개의 지연된 화물을 찾음")

    # 3. 객체 속성 접근 및 연결된 객체 탐색
    #    검색된 각 화물 객체에 대해 속성(shipmentId, destination 등)에 직접 접근
    #    온톨로지 연결을 통해 'assignedVehicle'과 같은 연결된 객체를 로드
    for shipment in delayed_shipments:
        print(f"\n- 화물 ID: {shipment.shipmentId}")
        print(f"  목적지: {shipment.destination}")
        print(f"  현재 상태: {shipment.status}")

        # 연결된 운송 차량 정보 로드
        try:
            vehicle = shipment.assignedVehicle.get()
            print(f"  할당된 차량 ID: {vehicle.vehicleId}")
            print(f"  차량 현재 위치: {vehicle.currentLocation}")
        except Exception as e:
            print(f"  할당된 차량 정보를 가져오는 데 실패: {e}")

    # 4. 온톨로지 액션(Action) 실행
    #    온톨로지의 동역학적 계층은 'update_shipment_status'와 같은 액션을 정의
    target_shipment = delayed_shipments
    print(f"\n화물 {target_shipment.shipmentId}의 상태를 '조사 중'으로 업데이트...")

    try:
        # 'update_shipment_status'는 온톨로지에 미리 정의된 액션의 API 이름이라고 가정
        target_shipment.update_shipment_status(new_status="Investigation")
        print("상태 업데이트 액션이 성공적으로 실행.")

        # 변경 사항 확인
        updated_shipment = client.ontology.objects.Shipment.get(target_shipment.shipmentId)
        print(f"화물 {updated_shipment.shipmentId}의 새로운 상태: {updated_shipment.status}")

    except Exception as e:
        print(f"액션 실행 중 오류가 발생: {e}")
  ```
온톨로지에는 액션(Action)이라는 동적 요소도 정의할 수 있어, 액션(Action)을 호출하면 Data의 업데이트, 플랫폼의 거버넌스, 보안, 감사추적 등 모든 트랙잭션들을 수행할 수 있다.
참고자료
- [https://daddynkidsmakers.blogspot.com/2025/10/blog-post_11.html](https://daddynkidsmakers.blogspot.com/2025/10/blog-post_11.html)

## 출처

- 원문: https://www.notion.so/Palantir-Ontology-2b4172a556d680f59088ecbd6b8310a9
- Vault path: wiki/notes/architecture/Palantir-Ontology-구현-방식-리뷰.md
