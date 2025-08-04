---
title: "**Transformer (Attention is All You Need) 분석**"
date: 2025-08-04 06:05:00 +0900
categories: [논문리뷰]
tags: [AI, Transfomer, LLM]
description: Attention is All You Need 리뷰
toc: true
comments: true
---

# **Transformer (Attention is All You Need)**

## **Transformer Encoder / Decoder**

### Encoder 방식

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/b2e43ef6-e7b5-4858-88bd-11445be5cc29/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DH3JTJS%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T072132Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIQDRM3XT6V3E%2Bw%2BfiKYsHgQSwacOGJucHnX3oNMqSnmBVQIgSPyxCJy95DZMjmKpa81OISAFDex8ruUGM5FLqgs%2B5Ykq%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDAvPCC2cKq5TysY7vSrcA3rJSRl44CfV8ZaGR%2BMwISWTFM5ObzqsVhtlnCgttt%2F5cLScWWtC1VvsRdNbgE6sUrXryvExPULxzDhmgoSsp%2BlNOykz8BEb6HIDCQZBUXu2COFEGpOCatg9zxT7PhR9bxc0%2BYJ2RAKA3iDgYevgDG%2BjpZ7eEWK2QGY0fg8vKlN5XHlMHU0WkgPp5Pa%2Fkbtoxt8dVGPVzAneKLpmek3riaZU6t77VkwdUSSm52s05X8WCEL6fuSe87r%2BVPMrRCqXNw5HF%2BNNlxZ0kITeqHVTW4yZZJ6lDJPKfFoVh44xQL1I6wgQ3ZwA86oGdlnHR9kJtRE0maLsAAjXHAbcO%2B8hrNxXgTklW3fcKMZzIGsH7rt3mZxyXPRuv4Tvv0cb1XSC6hafhfXCY6OgBxmjYFH7xrEchSAPwXoQQ8hrcYyYmoxstJztW9FaIA7D5pGdotIE%2FuP86kKvw7MQcoZ66ZIZ7jRU8EWQZDV%2FGxYJJPlVRI1ZwGTw43v%2F3oEtsI96XnBUj9s0YcsVGX0X2fqKWTu176yrgSeZ9uFRWXFYoW%2BzXefJmhsHqPFZ%2Fv0L0LZApXZfnkbbJWcXOki7E6ARNY9qMPXaHxIFie8NRdj1jibtfNlG6xx18YvweHN%2BVzj4MKy4wcQGOqUBeMtmHonMWPV9wylwlkj7QeDt1WlPaSgK3rmTsIPxyO6p%2FU1RzwCnGKxCC9sbwtUBB61%2FJlxJEiiP9YemV0NsMQJYdEbj9MJdZHHCpMM%2F4%2FQYpgoSxRJbg304H6cVS4v7FSzYzPFYp8Q5LrSX1dMZAPN28arGTbe1XWkU5M2WqbAj0rcbBaMxwMjMUmk9hv9yMreT13gePmpjpJjvtm9ym6lsDbvj&X-Amz-Signature=45a48943adaed831a3a650e9490c296f366a1c58a92478939aac18eac1ca386d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Encoder 는 N개의 Encoder Block 으로 구성되어 있다.  (논문에서는 N = 6으로 사용했다. )

Encoder Block의 Input/output 형태는 동일하다. 어떤 Matrix 를 Input으로 받는다고 했을 때, output 역시 해당 Matrix와 같은 형태(Shape)를 갖고있다. → Shape이 바뀌지 않는다 (멱등하다.)

각 Encoder 모델은 연결되어 있다. N-1 EB 와 N EB가 연결되어 있다. 각 Input / Output Matrix Shape도 같기 때문에 전체 Encoder의 Shape은 항상 일정하다 (멱등하다.)

Encoder Block을 여러 겹으로 쌓는 것인가? 
Encoder Block은 Input으로 들어오는 문장을 Vector화 하여 Context로 만든다, Context로 만들어진 문장은 추상화되어 더 넓은 관점으로 높은 차원에서 고려될 수 있는 정보로 바뀌고 이 과정을 반복하면 매우 높은 차원의(추상화된 정보) Context가 생성되고 더 많은 관점에서 피처들을 뽑아낼 수 있다.

문장 → 높은 차원의 Context → 보다 더 높은 차원의 Context → …. → Output

일단 이 정도로만 하고 넘어가면 될 것 같다. 

## **Encoder Block**

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/14fc4b24-1f46-437d-80dc-f938777ef95b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DH3JTJS%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T072132Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIQDRM3XT6V3E%2Bw%2BfiKYsHgQSwacOGJucHnX3oNMqSnmBVQIgSPyxCJy95DZMjmKpa81OISAFDex8ruUGM5FLqgs%2B5Ykq%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDAvPCC2cKq5TysY7vSrcA3rJSRl44CfV8ZaGR%2BMwISWTFM5ObzqsVhtlnCgttt%2F5cLScWWtC1VvsRdNbgE6sUrXryvExPULxzDhmgoSsp%2BlNOykz8BEb6HIDCQZBUXu2COFEGpOCatg9zxT7PhR9bxc0%2BYJ2RAKA3iDgYevgDG%2BjpZ7eEWK2QGY0fg8vKlN5XHlMHU0WkgPp5Pa%2Fkbtoxt8dVGPVzAneKLpmek3riaZU6t77VkwdUSSm52s05X8WCEL6fuSe87r%2BVPMrRCqXNw5HF%2BNNlxZ0kITeqHVTW4yZZJ6lDJPKfFoVh44xQL1I6wgQ3ZwA86oGdlnHR9kJtRE0maLsAAjXHAbcO%2B8hrNxXgTklW3fcKMZzIGsH7rt3mZxyXPRuv4Tvv0cb1XSC6hafhfXCY6OgBxmjYFH7xrEchSAPwXoQQ8hrcYyYmoxstJztW9FaIA7D5pGdotIE%2FuP86kKvw7MQcoZ66ZIZ7jRU8EWQZDV%2FGxYJJPlVRI1ZwGTw43v%2F3oEtsI96XnBUj9s0YcsVGX0X2fqKWTu176yrgSeZ9uFRWXFYoW%2BzXefJmhsHqPFZ%2Fv0L0LZApXZfnkbbJWcXOki7E6ARNY9qMPXaHxIFie8NRdj1jibtfNlG6xx18YvweHN%2BVzj4MKy4wcQGOqUBeMtmHonMWPV9wylwlkj7QeDt1WlPaSgK3rmTsIPxyO6p%2FU1RzwCnGKxCC9sbwtUBB61%2FJlxJEiiP9YemV0NsMQJYdEbj9MJdZHHCpMM%2F4%2FQYpgoSxRJbg304H6cVS4v7FSzYzPFYp8Q5LrSX1dMZAPN28arGTbe1XWkU5M2WqbAj0rcbBaMxwMjMUmk9hv9yMreT13gePmpjpJjvtm9ym6lsDbvj&X-Amz-Signature=1c3608bebff497f3e4acafb9044581a32bc185cd89e3bcfadfea088c3b915dc1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Encoder Block은 크게 Multi-Head Attention Layer, Position-wise Feed-Forward Layer로 구성된다.

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/2934b9e2-c4eb-4789-b583-072f846976a0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DH3JTJS%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T072132Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIQDRM3XT6V3E%2Bw%2BfiKYsHgQSwacOGJucHnX3oNMqSnmBVQIgSPyxCJy95DZMjmKpa81OISAFDex8ruUGM5FLqgs%2B5Ykq%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDAvPCC2cKq5TysY7vSrcA3rJSRl44CfV8ZaGR%2BMwISWTFM5ObzqsVhtlnCgttt%2F5cLScWWtC1VvsRdNbgE6sUrXryvExPULxzDhmgoSsp%2BlNOykz8BEb6HIDCQZBUXu2COFEGpOCatg9zxT7PhR9bxc0%2BYJ2RAKA3iDgYevgDG%2BjpZ7eEWK2QGY0fg8vKlN5XHlMHU0WkgPp5Pa%2Fkbtoxt8dVGPVzAneKLpmek3riaZU6t77VkwdUSSm52s05X8WCEL6fuSe87r%2BVPMrRCqXNw5HF%2BNNlxZ0kITeqHVTW4yZZJ6lDJPKfFoVh44xQL1I6wgQ3ZwA86oGdlnHR9kJtRE0maLsAAjXHAbcO%2B8hrNxXgTklW3fcKMZzIGsH7rt3mZxyXPRuv4Tvv0cb1XSC6hafhfXCY6OgBxmjYFH7xrEchSAPwXoQQ8hrcYyYmoxstJztW9FaIA7D5pGdotIE%2FuP86kKvw7MQcoZ66ZIZ7jRU8EWQZDV%2FGxYJJPlVRI1ZwGTw43v%2F3oEtsI96XnBUj9s0YcsVGX0X2fqKWTu176yrgSeZ9uFRWXFYoW%2BzXefJmhsHqPFZ%2Fv0L0LZApXZfnkbbJWcXOki7E6ARNY9qMPXaHxIFie8NRdj1jibtfNlG6xx18YvweHN%2BVzj4MKy4wcQGOqUBeMtmHonMWPV9wylwlkj7QeDt1WlPaSgK3rmTsIPxyO6p%2FU1RzwCnGKxCC9sbwtUBB61%2FJlxJEiiP9YemV0NsMQJYdEbj9MJdZHHCpMM%2F4%2FQYpgoSxRJbg304H6cVS4v7FSzYzPFYp8Q5LrSX1dMZAPN28arGTbe1XWkU5M2WqbAj0rcbBaMxwMjMUmk9hv9yMreT13gePmpjpJjvtm9ym6lsDbvj&X-Amz-Signature=166b42a45ea0f54ddb1d3fcb68198d628bf85abcbd1537a71a851716a8919742&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Multi-Head Attention은 Attention을 여러 개 수행하는 layer이다. 

Multi-Head Attention을 이해하기 위해서는 Scaled Dot-Product Attention에 대해 먼저 알아야만 한다. Attention이라는 것은 넓은 범위의 전체 data에서 특정한 부분에 집중한다는 의미이다. 

Scaled Dot-Product Attention 자체를 줄여서 Attention 이라고 한다.

> *The animal didn’t cross the street, because it was too tired.*

위 문장에서 *‘it’*은 무엇을 지칭하는 것일까? 

사람이라면 직관적으로 *‘animal’*과 연결지을 수 있지만, 컴퓨터는 *‘it’*이 *‘animal’*을 가리키는지, *‘street’*를 가리키는지 알지 못한다.

Attention은 이러한 문제를 해결하기 위해 두 token 사이의 연관 정도를 계산해내는 방법론이다. 

위의 경우에는 **같은 문장 내**의 두 token 사이의 Attention을 계산하는 것이므로, **Self-Attention**이라고 부른다. 반면, 

**서로 다른 두 문장**에 각각 존재하는 두 token 사이의 Attention을 계산하는 것을 **Cross-Attention**이라고 부른다.


### Attention 모델의 기본 구조

**Q, K, V**

Attention 계산에는 Query, Key, Value라는 3가지 vector가 사용된다. 각 vector의 역할을 정리하면 다음과 같다.

1. Query: 입력 시퀸스에서 관련 부분을 찾으려고하는 현재의 상태 벡터 (소스)
1. Key: 관계의 연관도를 찾기 위해 Query와 비교하는데 사용되는 벡터 (타겟)
1. Value: 특정 Key에 해당하는 입력 시퀸스의 가중치를 구하는데 사용되는 벡터 (벨류)
### Scaled Dot-Product Attention 상세

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/dac62052-f9b4-4944-8208-320b66c9da6e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DH3JTJS%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T072132Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIQDRM3XT6V3E%2Bw%2BfiKYsHgQSwacOGJucHnX3oNMqSnmBVQIgSPyxCJy95DZMjmKpa81OISAFDex8ruUGM5FLqgs%2B5Ykq%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDAvPCC2cKq5TysY7vSrcA3rJSRl44CfV8ZaGR%2BMwISWTFM5ObzqsVhtlnCgttt%2F5cLScWWtC1VvsRdNbgE6sUrXryvExPULxzDhmgoSsp%2BlNOykz8BEb6HIDCQZBUXu2COFEGpOCatg9zxT7PhR9bxc0%2BYJ2RAKA3iDgYevgDG%2BjpZ7eEWK2QGY0fg8vKlN5XHlMHU0WkgPp5Pa%2Fkbtoxt8dVGPVzAneKLpmek3riaZU6t77VkwdUSSm52s05X8WCEL6fuSe87r%2BVPMrRCqXNw5HF%2BNNlxZ0kITeqHVTW4yZZJ6lDJPKfFoVh44xQL1I6wgQ3ZwA86oGdlnHR9kJtRE0maLsAAjXHAbcO%2B8hrNxXgTklW3fcKMZzIGsH7rt3mZxyXPRuv4Tvv0cb1XSC6hafhfXCY6OgBxmjYFH7xrEchSAPwXoQQ8hrcYyYmoxstJztW9FaIA7D5pGdotIE%2FuP86kKvw7MQcoZ66ZIZ7jRU8EWQZDV%2FGxYJJPlVRI1ZwGTw43v%2F3oEtsI96XnBUj9s0YcsVGX0X2fqKWTu176yrgSeZ9uFRWXFYoW%2BzXefJmhsHqPFZ%2Fv0L0LZApXZfnkbbJWcXOki7E6ARNY9qMPXaHxIFie8NRdj1jibtfNlG6xx18YvweHN%2BVzj4MKy4wcQGOqUBeMtmHonMWPV9wylwlkj7QeDt1WlPaSgK3rmTsIPxyO6p%2FU1RzwCnGKxCC9sbwtUBB61%2FJlxJEiiP9YemV0NsMQJYdEbj9MJdZHHCpMM%2F4%2FQYpgoSxRJbg304H6cVS4v7FSzYzPFYp8Q5LrSX1dMZAPN28arGTbe1XWkU5M2WqbAj0rcbBaMxwMjMUmk9hv9yMreT13gePmpjpJjvtm9ym6lsDbvj&X-Amz-Signature=ed6f3358f6ad9c75155718807bfe667328e0a3c4908b6fb17c0e8cc191bad8ef&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

1. Input에는 Position Encoding + Embeding된 데이터가 들어온다.
1. Linear에서는 1번 Input Matrix에 대해 차원 축소와 출력 Matrix의 모양과 맞춰주는 역할을 한다. 
1. MatMUL에서는 Query와 Key 행렬의 내적을 통해 Attention Score Matrix 를 만든다. 
1. 이후에 Scale과 SoftMax를 통해서 각 유사도의 값의 합(항목별)이 1이 되도록 SoftMax해준다.
![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/c25b2651-1360-4dc3-8392-b5431fd36014/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DH3JTJS%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T072132Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIQDRM3XT6V3E%2Bw%2BfiKYsHgQSwacOGJucHnX3oNMqSnmBVQIgSPyxCJy95DZMjmKpa81OISAFDex8ruUGM5FLqgs%2B5Ykq%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDAvPCC2cKq5TysY7vSrcA3rJSRl44CfV8ZaGR%2BMwISWTFM5ObzqsVhtlnCgttt%2F5cLScWWtC1VvsRdNbgE6sUrXryvExPULxzDhmgoSsp%2BlNOykz8BEb6HIDCQZBUXu2COFEGpOCatg9zxT7PhR9bxc0%2BYJ2RAKA3iDgYevgDG%2BjpZ7eEWK2QGY0fg8vKlN5XHlMHU0WkgPp5Pa%2Fkbtoxt8dVGPVzAneKLpmek3riaZU6t77VkwdUSSm52s05X8WCEL6fuSe87r%2BVPMrRCqXNw5HF%2BNNlxZ0kITeqHVTW4yZZJ6lDJPKfFoVh44xQL1I6wgQ3ZwA86oGdlnHR9kJtRE0maLsAAjXHAbcO%2B8hrNxXgTklW3fcKMZzIGsH7rt3mZxyXPRuv4Tvv0cb1XSC6hafhfXCY6OgBxmjYFH7xrEchSAPwXoQQ8hrcYyYmoxstJztW9FaIA7D5pGdotIE%2FuP86kKvw7MQcoZ66ZIZ7jRU8EWQZDV%2FGxYJJPlVRI1ZwGTw43v%2F3oEtsI96XnBUj9s0YcsVGX0X2fqKWTu176yrgSeZ9uFRWXFYoW%2BzXefJmhsHqPFZ%2Fv0L0LZApXZfnkbbJWcXOki7E6ARNY9qMPXaHxIFie8NRdj1jibtfNlG6xx18YvweHN%2BVzj4MKy4wcQGOqUBeMtmHonMWPV9wylwlkj7QeDt1WlPaSgK3rmTsIPxyO6p%2FU1RzwCnGKxCC9sbwtUBB61%2FJlxJEiiP9YemV0NsMQJYdEbj9MJdZHHCpMM%2F4%2FQYpgoSxRJbg304H6cVS4v7FSzYzPFYp8Q5LrSX1dMZAPN28arGTbe1XWkU5M2WqbAj0rcbBaMxwMjMUmk9hv9yMreT13gePmpjpJjvtm9ym6lsDbvj&X-Amz-Signature=70a9bae4f9d3ac5871d8053a4f8b9d30e290148f2df7023799be3b4d7281e95d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/34305e15-6d2f-4993-a64c-9ef01a463274/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DH3JTJS%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T072132Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIQDRM3XT6V3E%2Bw%2BfiKYsHgQSwacOGJucHnX3oNMqSnmBVQIgSPyxCJy95DZMjmKpa81OISAFDex8ruUGM5FLqgs%2B5Ykq%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDAvPCC2cKq5TysY7vSrcA3rJSRl44CfV8ZaGR%2BMwISWTFM5ObzqsVhtlnCgttt%2F5cLScWWtC1VvsRdNbgE6sUrXryvExPULxzDhmgoSsp%2BlNOykz8BEb6HIDCQZBUXu2COFEGpOCatg9zxT7PhR9bxc0%2BYJ2RAKA3iDgYevgDG%2BjpZ7eEWK2QGY0fg8vKlN5XHlMHU0WkgPp5Pa%2Fkbtoxt8dVGPVzAneKLpmek3riaZU6t77VkwdUSSm52s05X8WCEL6fuSe87r%2BVPMrRCqXNw5HF%2BNNlxZ0kITeqHVTW4yZZJ6lDJPKfFoVh44xQL1I6wgQ3ZwA86oGdlnHR9kJtRE0maLsAAjXHAbcO%2B8hrNxXgTklW3fcKMZzIGsH7rt3mZxyXPRuv4Tvv0cb1XSC6hafhfXCY6OgBxmjYFH7xrEchSAPwXoQQ8hrcYyYmoxstJztW9FaIA7D5pGdotIE%2FuP86kKvw7MQcoZ66ZIZ7jRU8EWQZDV%2FGxYJJPlVRI1ZwGTw43v%2F3oEtsI96XnBUj9s0YcsVGX0X2fqKWTu176yrgSeZ9uFRWXFYoW%2BzXefJmhsHqPFZ%2Fv0L0LZApXZfnkbbJWcXOki7E6ARNY9qMPXaHxIFie8NRdj1jibtfNlG6xx18YvweHN%2BVzj4MKy4wcQGOqUBeMtmHonMWPV9wylwlkj7QeDt1WlPaSgK3rmTsIPxyO6p%2FU1RzwCnGKxCC9sbwtUBB61%2FJlxJEiiP9YemV0NsMQJYdEbj9MJdZHHCpMM%2F4%2FQYpgoSxRJbg304H6cVS4v7FSzYzPFYp8Q5LrSX1dMZAPN28arGTbe1XWkU5M2WqbAj0rcbBaMxwMjMUmk9hv9yMreT13gePmpjpJjvtm9ym6lsDbvj&X-Amz-Signature=49efcf6e3eb5760068b56c96e1ff209a64a5777d1275850d1eeb0b9668f2c0df&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

마지막에 Value Matrix와 내적한다. 

조금 주요 부분을 리즈너블하게 설명을 하자면

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/2a36b0af-a461-4513-9bcc-7d2d30b5a238/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DH3JTJS%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T072132Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIQDRM3XT6V3E%2Bw%2BfiKYsHgQSwacOGJucHnX3oNMqSnmBVQIgSPyxCJy95DZMjmKpa81OISAFDex8ruUGM5FLqgs%2B5Ykq%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDAvPCC2cKq5TysY7vSrcA3rJSRl44CfV8ZaGR%2BMwISWTFM5ObzqsVhtlnCgttt%2F5cLScWWtC1VvsRdNbgE6sUrXryvExPULxzDhmgoSsp%2BlNOykz8BEb6HIDCQZBUXu2COFEGpOCatg9zxT7PhR9bxc0%2BYJ2RAKA3iDgYevgDG%2BjpZ7eEWK2QGY0fg8vKlN5XHlMHU0WkgPp5Pa%2Fkbtoxt8dVGPVzAneKLpmek3riaZU6t77VkwdUSSm52s05X8WCEL6fuSe87r%2BVPMrRCqXNw5HF%2BNNlxZ0kITeqHVTW4yZZJ6lDJPKfFoVh44xQL1I6wgQ3ZwA86oGdlnHR9kJtRE0maLsAAjXHAbcO%2B8hrNxXgTklW3fcKMZzIGsH7rt3mZxyXPRuv4Tvv0cb1XSC6hafhfXCY6OgBxmjYFH7xrEchSAPwXoQQ8hrcYyYmoxstJztW9FaIA7D5pGdotIE%2FuP86kKvw7MQcoZ66ZIZ7jRU8EWQZDV%2FGxYJJPlVRI1ZwGTw43v%2F3oEtsI96XnBUj9s0YcsVGX0X2fqKWTu176yrgSeZ9uFRWXFYoW%2BzXefJmhsHqPFZ%2Fv0L0LZApXZfnkbbJWcXOki7E6ARNY9qMPXaHxIFie8NRdj1jibtfNlG6xx18YvweHN%2BVzj4MKy4wcQGOqUBeMtmHonMWPV9wylwlkj7QeDt1WlPaSgK3rmTsIPxyO6p%2FU1RzwCnGKxCC9sbwtUBB61%2FJlxJEiiP9YemV0NsMQJYdEbj9MJdZHHCpMM%2F4%2FQYpgoSxRJbg304H6cVS4v7FSzYzPFYp8Q5LrSX1dMZAPN28arGTbe1XWkU5M2WqbAj0rcbBaMxwMjMUmk9hv9yMreT13gePmpjpJjvtm9ym6lsDbvj&X-Amz-Signature=7403b3bb469318faa001c9cf1bd006e4822b2f7aa8af940cca1088bc1124330b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

1. Matmul에서 Query와 Key 간의 유사도를 계산한다, 각 단어(토큰) 간의 유사도를 계산해서 관련 있는 부분은 더 많은 정보를, 유사도가 적은 단어(토큰)은 적은 정보를 가져간다. 
1. 마지막에 Value를 내적하여 Attention Score Matrix를 적용한다.
1. 이걸 Multi Head 방식으로 여러 겹 쌓는 이유는 위 그림처럼 다양한 관점에서 더 복잡한 관계성을 파악할 수 있는 장점이 있기 때문이다. 
참조

https://www.blossominkyung.com/deeplearning/transformer-mha

https://tech.scatterlab.co.kr/vllm-implementation-details/

https://cpm0722.github.io/pytorch-implementation/transformer


