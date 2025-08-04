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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/b2e43ef6-e7b5-4858-88bd-11445be5cc29/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663MQZTA5I%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T064844Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCIDo3Lokp5KSj9eXhI3irC8f2b%2BgEvE7IrauRN3Nc2nnpAiEApLZQEywTxWF3cyk2SZOZGhcF%2BZSKPz6a4we334Bh8QAq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDJUORgWlQ3va6JFnEyrcA6eiDeZRVN9r0EL5PvOYVCRvJZYNpB80ozX9Kx%2FC%2BQiU9SSiWCDcApF968mAhpRqCkckJZgcN6LJdWb7mgcxfJ0CPiwdB3%2BBVl2z9K9p1jbsQyi4NRXeHiXTtBz5N2rQWZIqDZ8cB6Z2z2uk5Ca2cEplAxasSHa1J7FD4RCzuuojwtJMjltcX%2FPtJU5Kw30uZfd2OpgCA3amKyvRjJ7srQaom2ygNlJYeR1oAPtO3d81Ir9nFJ50kj7cm0DaQSgAxsro2F9pAXeemkdmo6JEHfY8Nl8twVtayXfia%2FQ%2B0UPQSxsNVUremoPG6lWhVPQgQDpu3yW5XxaSsY2haiA3Y9XwnFiHsROEc8umXBZ9vLNbRK2KnEX1dbn4Oni4giAmYo1V79U9VuDdMN%2Bp%2F4zWJ0kp1fPhJ%2FQORuKLDoRvasFpsE5NWVopyYaVpxaL50%2F4Jv%2F1UiS%2Fp764lLnxKP8J1KNGI41bAd62hhSCEjBR5OJtLCMCma8eUWOLLKZTmivf7aZYDtaxn5xRsY%2FQ%2FZk8Z82yIH7HX3g3CNH5oYtJAV%2Fd4DDHZGg3Z4tmDisBra%2BOOWTFyoGxAAK8Z9fD3djjDKvuJZLe%2FzxdRPy2n1qt9x977IMUZBXWTg89cYjXMIKNwcQGOqUBlZj%2BbSIV4qo9uvlrhEakkf1Qf6siXCLt4KmlaMQQcqyJvrVEKeLAnB4t1n9ZvjyEYARNZqBXSF5z%2BwWhXtR6JEaiPnwbvLdn3n2XtxyJUbnEF4vzVWSwL84mwfC3%2Firbxrb5vZcmWKM9ihaHe3g9TqAQTBTg6cqvuxyhgkNpu0DHtxAW2pAqXGIX2Rk7Q5n3gSn0VFqmxqC2SJ%2Bb3dSJQ3FzzfJB&X-Amz-Signature=8b72ef75d8a1bef5ac2f5914f82a28d36f3a07036cc3e387cbc4232b1c0ac369&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Encoder 는 N개의 Encoder Block 으로 구성되어 있다.  (논문에서는 N = 6으로 사용했다. )

Encoder Block의 Input/output 형태는 동일하다. 어떤 Matrix 를 Input으로 받는다고 했을 때, output 역시 해당 Matrix와 같은 형태(Shape)를 갖고있다. → Shape이 바뀌지 않는다 (멱등하다.)

각 Encoder 모델은 연결되어 있다. N-1 EB 와 N EB가 연결되어 있다. 각 Input / Output Matrix Shape도 같기 때문에 전체 Encoder의 Shape은 항상 일정하다 (멱등하다.)

Encoder Block을 여러 겹으로 쌓는 것인가? 
Encoder Block은 Input으로 들어오는 문장을 Vector화 하여 Context로 만든다, Context로 만들어진 문장은 추상화되어 더 넓은 관점으로 높은 차원에서 고려될 수 있는 정보로 바뀌고 이 과정을 반복하면 매우 높은 차원의(추상화된 정보) Context가 생성되고 더 많은 관점에서 피처들을 뽑아낼 수 있다.

문장 → 높은 차원의 Context → 보다 더 높은 차원의 Context → …. → Output

일단 이 정도로만 하고 넘어가면 될 것 같다. 

## **Encoder Block**

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/14fc4b24-1f46-437d-80dc-f938777ef95b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663MQZTA5I%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T064844Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCIDo3Lokp5KSj9eXhI3irC8f2b%2BgEvE7IrauRN3Nc2nnpAiEApLZQEywTxWF3cyk2SZOZGhcF%2BZSKPz6a4we334Bh8QAq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDJUORgWlQ3va6JFnEyrcA6eiDeZRVN9r0EL5PvOYVCRvJZYNpB80ozX9Kx%2FC%2BQiU9SSiWCDcApF968mAhpRqCkckJZgcN6LJdWb7mgcxfJ0CPiwdB3%2BBVl2z9K9p1jbsQyi4NRXeHiXTtBz5N2rQWZIqDZ8cB6Z2z2uk5Ca2cEplAxasSHa1J7FD4RCzuuojwtJMjltcX%2FPtJU5Kw30uZfd2OpgCA3amKyvRjJ7srQaom2ygNlJYeR1oAPtO3d81Ir9nFJ50kj7cm0DaQSgAxsro2F9pAXeemkdmo6JEHfY8Nl8twVtayXfia%2FQ%2B0UPQSxsNVUremoPG6lWhVPQgQDpu3yW5XxaSsY2haiA3Y9XwnFiHsROEc8umXBZ9vLNbRK2KnEX1dbn4Oni4giAmYo1V79U9VuDdMN%2Bp%2F4zWJ0kp1fPhJ%2FQORuKLDoRvasFpsE5NWVopyYaVpxaL50%2F4Jv%2F1UiS%2Fp764lLnxKP8J1KNGI41bAd62hhSCEjBR5OJtLCMCma8eUWOLLKZTmivf7aZYDtaxn5xRsY%2FQ%2FZk8Z82yIH7HX3g3CNH5oYtJAV%2Fd4DDHZGg3Z4tmDisBra%2BOOWTFyoGxAAK8Z9fD3djjDKvuJZLe%2FzxdRPy2n1qt9x977IMUZBXWTg89cYjXMIKNwcQGOqUBlZj%2BbSIV4qo9uvlrhEakkf1Qf6siXCLt4KmlaMQQcqyJvrVEKeLAnB4t1n9ZvjyEYARNZqBXSF5z%2BwWhXtR6JEaiPnwbvLdn3n2XtxyJUbnEF4vzVWSwL84mwfC3%2Firbxrb5vZcmWKM9ihaHe3g9TqAQTBTg6cqvuxyhgkNpu0DHtxAW2pAqXGIX2Rk7Q5n3gSn0VFqmxqC2SJ%2Bb3dSJQ3FzzfJB&X-Amz-Signature=793873d26114baffa05ab0b941b39edb40442cc9a1cff5ca22612d1ad77d3c54&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Encoder Block은 크게 Multi-Head Attention Layer, Position-wise Feed-Forward Layer로 구성된다.

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/2934b9e2-c4eb-4789-b583-072f846976a0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663MQZTA5I%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T064844Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCIDo3Lokp5KSj9eXhI3irC8f2b%2BgEvE7IrauRN3Nc2nnpAiEApLZQEywTxWF3cyk2SZOZGhcF%2BZSKPz6a4we334Bh8QAq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDJUORgWlQ3va6JFnEyrcA6eiDeZRVN9r0EL5PvOYVCRvJZYNpB80ozX9Kx%2FC%2BQiU9SSiWCDcApF968mAhpRqCkckJZgcN6LJdWb7mgcxfJ0CPiwdB3%2BBVl2z9K9p1jbsQyi4NRXeHiXTtBz5N2rQWZIqDZ8cB6Z2z2uk5Ca2cEplAxasSHa1J7FD4RCzuuojwtJMjltcX%2FPtJU5Kw30uZfd2OpgCA3amKyvRjJ7srQaom2ygNlJYeR1oAPtO3d81Ir9nFJ50kj7cm0DaQSgAxsro2F9pAXeemkdmo6JEHfY8Nl8twVtayXfia%2FQ%2B0UPQSxsNVUremoPG6lWhVPQgQDpu3yW5XxaSsY2haiA3Y9XwnFiHsROEc8umXBZ9vLNbRK2KnEX1dbn4Oni4giAmYo1V79U9VuDdMN%2Bp%2F4zWJ0kp1fPhJ%2FQORuKLDoRvasFpsE5NWVopyYaVpxaL50%2F4Jv%2F1UiS%2Fp764lLnxKP8J1KNGI41bAd62hhSCEjBR5OJtLCMCma8eUWOLLKZTmivf7aZYDtaxn5xRsY%2FQ%2FZk8Z82yIH7HX3g3CNH5oYtJAV%2Fd4DDHZGg3Z4tmDisBra%2BOOWTFyoGxAAK8Z9fD3djjDKvuJZLe%2FzxdRPy2n1qt9x977IMUZBXWTg89cYjXMIKNwcQGOqUBlZj%2BbSIV4qo9uvlrhEakkf1Qf6siXCLt4KmlaMQQcqyJvrVEKeLAnB4t1n9ZvjyEYARNZqBXSF5z%2BwWhXtR6JEaiPnwbvLdn3n2XtxyJUbnEF4vzVWSwL84mwfC3%2Firbxrb5vZcmWKM9ihaHe3g9TqAQTBTg6cqvuxyhgkNpu0DHtxAW2pAqXGIX2Rk7Q5n3gSn0VFqmxqC2SJ%2Bb3dSJQ3FzzfJB&X-Amz-Signature=0f4f6106d40c61f6a602c9d84a3040a6d096c72bc022300024e09bbce7665f0e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/dac62052-f9b4-4944-8208-320b66c9da6e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663MQZTA5I%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T064844Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCIDo3Lokp5KSj9eXhI3irC8f2b%2BgEvE7IrauRN3Nc2nnpAiEApLZQEywTxWF3cyk2SZOZGhcF%2BZSKPz6a4we334Bh8QAq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDJUORgWlQ3va6JFnEyrcA6eiDeZRVN9r0EL5PvOYVCRvJZYNpB80ozX9Kx%2FC%2BQiU9SSiWCDcApF968mAhpRqCkckJZgcN6LJdWb7mgcxfJ0CPiwdB3%2BBVl2z9K9p1jbsQyi4NRXeHiXTtBz5N2rQWZIqDZ8cB6Z2z2uk5Ca2cEplAxasSHa1J7FD4RCzuuojwtJMjltcX%2FPtJU5Kw30uZfd2OpgCA3amKyvRjJ7srQaom2ygNlJYeR1oAPtO3d81Ir9nFJ50kj7cm0DaQSgAxsro2F9pAXeemkdmo6JEHfY8Nl8twVtayXfia%2FQ%2B0UPQSxsNVUremoPG6lWhVPQgQDpu3yW5XxaSsY2haiA3Y9XwnFiHsROEc8umXBZ9vLNbRK2KnEX1dbn4Oni4giAmYo1V79U9VuDdMN%2Bp%2F4zWJ0kp1fPhJ%2FQORuKLDoRvasFpsE5NWVopyYaVpxaL50%2F4Jv%2F1UiS%2Fp764lLnxKP8J1KNGI41bAd62hhSCEjBR5OJtLCMCma8eUWOLLKZTmivf7aZYDtaxn5xRsY%2FQ%2FZk8Z82yIH7HX3g3CNH5oYtJAV%2Fd4DDHZGg3Z4tmDisBra%2BOOWTFyoGxAAK8Z9fD3djjDKvuJZLe%2FzxdRPy2n1qt9x977IMUZBXWTg89cYjXMIKNwcQGOqUBlZj%2BbSIV4qo9uvlrhEakkf1Qf6siXCLt4KmlaMQQcqyJvrVEKeLAnB4t1n9ZvjyEYARNZqBXSF5z%2BwWhXtR6JEaiPnwbvLdn3n2XtxyJUbnEF4vzVWSwL84mwfC3%2Firbxrb5vZcmWKM9ihaHe3g9TqAQTBTg6cqvuxyhgkNpu0DHtxAW2pAqXGIX2Rk7Q5n3gSn0VFqmxqC2SJ%2Bb3dSJQ3FzzfJB&X-Amz-Signature=fc1f740bf0075368dc710d0c64d73f1a7c8851d67aae8abb85b8faa03bff8b11&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

1. Input에는 Position Encoding + Embeding된 데이터가 들어온다.
1. Linear에서는 1번 Input Matrix에 대해 차원 축소와 출력 Matrix의 모양과 맞춰주는 역할을 한다. 
1. MatMUL에서는 Query와 Key 행렬의 내적을 통해 Attention Score Matrix 를 만든다. 
1. 이후에 Scale과 SoftMax를 통해서 각 유사도의 값의 합(항목별)이 1이 되도록 SoftMax해준다.
![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/c25b2651-1360-4dc3-8392-b5431fd36014/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663MQZTA5I%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T064844Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCIDo3Lokp5KSj9eXhI3irC8f2b%2BgEvE7IrauRN3Nc2nnpAiEApLZQEywTxWF3cyk2SZOZGhcF%2BZSKPz6a4we334Bh8QAq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDJUORgWlQ3va6JFnEyrcA6eiDeZRVN9r0EL5PvOYVCRvJZYNpB80ozX9Kx%2FC%2BQiU9SSiWCDcApF968mAhpRqCkckJZgcN6LJdWb7mgcxfJ0CPiwdB3%2BBVl2z9K9p1jbsQyi4NRXeHiXTtBz5N2rQWZIqDZ8cB6Z2z2uk5Ca2cEplAxasSHa1J7FD4RCzuuojwtJMjltcX%2FPtJU5Kw30uZfd2OpgCA3amKyvRjJ7srQaom2ygNlJYeR1oAPtO3d81Ir9nFJ50kj7cm0DaQSgAxsro2F9pAXeemkdmo6JEHfY8Nl8twVtayXfia%2FQ%2B0UPQSxsNVUremoPG6lWhVPQgQDpu3yW5XxaSsY2haiA3Y9XwnFiHsROEc8umXBZ9vLNbRK2KnEX1dbn4Oni4giAmYo1V79U9VuDdMN%2Bp%2F4zWJ0kp1fPhJ%2FQORuKLDoRvasFpsE5NWVopyYaVpxaL50%2F4Jv%2F1UiS%2Fp764lLnxKP8J1KNGI41bAd62hhSCEjBR5OJtLCMCma8eUWOLLKZTmivf7aZYDtaxn5xRsY%2FQ%2FZk8Z82yIH7HX3g3CNH5oYtJAV%2Fd4DDHZGg3Z4tmDisBra%2BOOWTFyoGxAAK8Z9fD3djjDKvuJZLe%2FzxdRPy2n1qt9x977IMUZBXWTg89cYjXMIKNwcQGOqUBlZj%2BbSIV4qo9uvlrhEakkf1Qf6siXCLt4KmlaMQQcqyJvrVEKeLAnB4t1n9ZvjyEYARNZqBXSF5z%2BwWhXtR6JEaiPnwbvLdn3n2XtxyJUbnEF4vzVWSwL84mwfC3%2Firbxrb5vZcmWKM9ihaHe3g9TqAQTBTg6cqvuxyhgkNpu0DHtxAW2pAqXGIX2Rk7Q5n3gSn0VFqmxqC2SJ%2Bb3dSJQ3FzzfJB&X-Amz-Signature=ed5f8cecbf9d892f86acda3f1d53feba560b935adf5544131d3c79d9a3ec445e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/34305e15-6d2f-4993-a64c-9ef01a463274/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663MQZTA5I%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T064844Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCIDo3Lokp5KSj9eXhI3irC8f2b%2BgEvE7IrauRN3Nc2nnpAiEApLZQEywTxWF3cyk2SZOZGhcF%2BZSKPz6a4we334Bh8QAq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDJUORgWlQ3va6JFnEyrcA6eiDeZRVN9r0EL5PvOYVCRvJZYNpB80ozX9Kx%2FC%2BQiU9SSiWCDcApF968mAhpRqCkckJZgcN6LJdWb7mgcxfJ0CPiwdB3%2BBVl2z9K9p1jbsQyi4NRXeHiXTtBz5N2rQWZIqDZ8cB6Z2z2uk5Ca2cEplAxasSHa1J7FD4RCzuuojwtJMjltcX%2FPtJU5Kw30uZfd2OpgCA3amKyvRjJ7srQaom2ygNlJYeR1oAPtO3d81Ir9nFJ50kj7cm0DaQSgAxsro2F9pAXeemkdmo6JEHfY8Nl8twVtayXfia%2FQ%2B0UPQSxsNVUremoPG6lWhVPQgQDpu3yW5XxaSsY2haiA3Y9XwnFiHsROEc8umXBZ9vLNbRK2KnEX1dbn4Oni4giAmYo1V79U9VuDdMN%2Bp%2F4zWJ0kp1fPhJ%2FQORuKLDoRvasFpsE5NWVopyYaVpxaL50%2F4Jv%2F1UiS%2Fp764lLnxKP8J1KNGI41bAd62hhSCEjBR5OJtLCMCma8eUWOLLKZTmivf7aZYDtaxn5xRsY%2FQ%2FZk8Z82yIH7HX3g3CNH5oYtJAV%2Fd4DDHZGg3Z4tmDisBra%2BOOWTFyoGxAAK8Z9fD3djjDKvuJZLe%2FzxdRPy2n1qt9x977IMUZBXWTg89cYjXMIKNwcQGOqUBlZj%2BbSIV4qo9uvlrhEakkf1Qf6siXCLt4KmlaMQQcqyJvrVEKeLAnB4t1n9ZvjyEYARNZqBXSF5z%2BwWhXtR6JEaiPnwbvLdn3n2XtxyJUbnEF4vzVWSwL84mwfC3%2Firbxrb5vZcmWKM9ihaHe3g9TqAQTBTg6cqvuxyhgkNpu0DHtxAW2pAqXGIX2Rk7Q5n3gSn0VFqmxqC2SJ%2Bb3dSJQ3FzzfJB&X-Amz-Signature=236bc4e86c507c898c1c1a3c04074b05643499a15fc8642b74b32b7e7dac5084&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

마지막에 Value Matrix와 내적한다. 

조금 주요 부분을 리즈너블하게 설명을 하자면

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/2a36b0af-a461-4513-9bcc-7d2d30b5a238/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663MQZTA5I%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T064845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCIDo3Lokp5KSj9eXhI3irC8f2b%2BgEvE7IrauRN3Nc2nnpAiEApLZQEywTxWF3cyk2SZOZGhcF%2BZSKPz6a4we334Bh8QAq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDJUORgWlQ3va6JFnEyrcA6eiDeZRVN9r0EL5PvOYVCRvJZYNpB80ozX9Kx%2FC%2BQiU9SSiWCDcApF968mAhpRqCkckJZgcN6LJdWb7mgcxfJ0CPiwdB3%2BBVl2z9K9p1jbsQyi4NRXeHiXTtBz5N2rQWZIqDZ8cB6Z2z2uk5Ca2cEplAxasSHa1J7FD4RCzuuojwtJMjltcX%2FPtJU5Kw30uZfd2OpgCA3amKyvRjJ7srQaom2ygNlJYeR1oAPtO3d81Ir9nFJ50kj7cm0DaQSgAxsro2F9pAXeemkdmo6JEHfY8Nl8twVtayXfia%2FQ%2B0UPQSxsNVUremoPG6lWhVPQgQDpu3yW5XxaSsY2haiA3Y9XwnFiHsROEc8umXBZ9vLNbRK2KnEX1dbn4Oni4giAmYo1V79U9VuDdMN%2Bp%2F4zWJ0kp1fPhJ%2FQORuKLDoRvasFpsE5NWVopyYaVpxaL50%2F4Jv%2F1UiS%2Fp764lLnxKP8J1KNGI41bAd62hhSCEjBR5OJtLCMCma8eUWOLLKZTmivf7aZYDtaxn5xRsY%2FQ%2FZk8Z82yIH7HX3g3CNH5oYtJAV%2Fd4DDHZGg3Z4tmDisBra%2BOOWTFyoGxAAK8Z9fD3djjDKvuJZLe%2FzxdRPy2n1qt9x977IMUZBXWTg89cYjXMIKNwcQGOqUBlZj%2BbSIV4qo9uvlrhEakkf1Qf6siXCLt4KmlaMQQcqyJvrVEKeLAnB4t1n9ZvjyEYARNZqBXSF5z%2BwWhXtR6JEaiPnwbvLdn3n2XtxyJUbnEF4vzVWSwL84mwfC3%2Firbxrb5vZcmWKM9ihaHe3g9TqAQTBTg6cqvuxyhgkNpu0DHtxAW2pAqXGIX2Rk7Q5n3gSn0VFqmxqC2SJ%2Bb3dSJQ3FzzfJB&X-Amz-Signature=e7305d8f82c88357df0bbc8ded2c8c8b6b527ddc7c22a98391d1ea93cdafe8e0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

1. Matmul에서 Query와 Key 간의 유사도를 계산한다, 각 단어(토큰) 간의 유사도를 계산해서 관련 있는 부분은 더 많은 정보를, 유사도가 적은 단어(토큰)은 적은 정보를 가져간다. 
1. 마지막에 Value를 내적하여 Attention Score Matrix를 적용한다.
1. 이걸 Multi Head 방식으로 여러 겹 쌓는 이유는 위 그림처럼 다양한 관점에서 더 복잡한 관계성을 파악할 수 있는 장점이 있기 때문이다. 
참조

https://www.blossominkyung.com/deeplearning/transformer-mha

https://tech.scatterlab.co.kr/vllm-implementation-details/

https://cpm0722.github.io/pytorch-implementation/transformer


