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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/24bfc627-5108-4107-8b73-ce84dd21c2a0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666AQV772G%2F20251123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251123T224726Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJHMEUCIQCS0craKwfaooMiFB%2F%2BfVd6CWsVBJiCZk0Rbm0wXDrPzgIgU1cUgbjL%2FtwXF7UeKzGRNnBjD57nZa%2BAuqdWh%2BcDnVMq%2FwMISBAAGgw2Mzc0MjMxODM4MDUiDNczPQspxaYXuYH60yrcAweb0wBA8ekaN6ObmUDA6iyQRwjou1am%2BqEXMvezzQD0Lk32lIKdxEflxPiiyodKKkUECbqN2f2E6USFe2Cl8xjFyGw0QZMxhdZWdgU1DvaAKHXbEIolhMELr0nhjfevXrFXszsBAuEMuuxQY%2FzJqyzJUFwtp9xiuNfIE4qMUiEZHNc1F9MSrXrRDZDLn%2B1oG0rd6eBAkdZalU%2F83Qi9ftnf9AUy76KDcMILvIk0p1VfLZkRrHsz%2FxbJ57J2y5fYuata7adQmrZRBSv7EQUKbSz%2BrhsMs6cZKvhjIvipFl61iJmobuEJ0O%2Flp116W%2B8%2Fajf3J7nUB7ZjKORcUwJxsVPWHE5liwmGXfziQTYDWjXdPuoBlTCOQ64bDgrjpFZXeNup2RUA3V7HuodsKOszJhpogch%2FkhuDrBI5bjNbFkIjeFrnBl8vyJwFqwqJ44s%2BbRotXXr6vZXS8lGENk74oDc%2FNU27BxISaYN3aHkeuqJ039qCJYfpWifLYflCEFRO1K3EEiaajoYwpGVE6YNrXCj6aWifBx2yUdZZC%2FKnZl%2Bpi1IMZFQlD1GmH8nimj9Zf53OaJkOQzuW%2FesJEnn91qbTRyfhsC7sCdaoIc1Crx3sg9xRjvWI9MUYtOyXMNyZjskGOqUBH%2BqIEbEBilCLRriqx09Pv9YlvpKApwick4DIvKczQDRmfbYNZtcpvUFokFjREqNRycz8aUCH7hVAhYyFaBFz3QmyNOzs2JSckKNkXACHc50a0dxZQWKJsUEH24MyjIsi%2BRuL506NwrbifGEhO%2Frz7Yp4n2jZ2ofIP5rTBHr7vLUyXPztyfeqUhVSzfD8ggAKmjbJdUwXAS7%2FE0j%2BIxYxY0b%2BhiBH&X-Amz-Signature=d8ac8e803574e193643a9daae04859f81ddd3591228d1bfb54824502bae09008&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

**데이터 수집/전처리/적재(일반, 대규모, 실시간)**

1. 데이터 처리 Workflow 
1. 기반 처리 기술
**온톨로지 메타모델**

온톨로지의 개념은 객체지향프로그래밍(OOP)과 매우 유사하다.

| 팔란티어 개념 | 테이블 모델 ㄱ |   |
| --- | --- | --- |
|   |   |   |
|   |   |   |


