---
title: "Transformer (Attention is All You Need) 분석"
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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/b2e43ef6-e7b5-4858-88bd-11445be5cc29/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46634J5UKV4%2F20250805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250805T060951Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJGMEQCIDNy%2Bm2lbT5BaTB8NQpKemYwPJZaqX4TG5mWC4tWS9MCAiBKkFkn7Ebw77QkKfzJsMFbJ8bWVMFbuoEBCBLDMueYiCr%2FAwhXEAAaDDYzNzQyMzE4MzgwNSIMRj9rhRfftAvh2osrKtwDchSWgPR7WnUUcaFJ5Mp1YPn62lLF0j4vqjnkKBMO20OB2VlVfvhiwT4ssqhp4Zw9pHtGKJjmYPDYtZ%2BIscF4QGCCnvnrnUBt%2Fr%2BdQTpoxajjQn%2BypDVDVzMNsy20xRvJm1sqvamlFlednGfP3vaL92ypHj%2Byo5zjKzZNLLgAJF6AujV1VhZfBo%2FXXmrPhtHOaP%2BSd7U9Tx7H8r%2FhZqvM%2BzklXG7ytztDnYd17X8vqS0RxcEzmXaJrV8JxGjFQsHf%2F31xcZYcXGgnKav8lv7XAm6gPwOJa1cCAdvTpmdWbqYWychCEU3RtG5%2BjMIYL3%2FEpkwV3Cg6pymNCqcBC2GGoSqjDuq5qBmAM0Av2fRL0fB4DZk6YDZyENyZAaV7ixKGzdQ5eFBrwk90iHokewU7GlDtg4iMs66fOh%2BMLpKJ2xHQRlEpxYmKNdPHP5xECdFPpoDu3bIkqGb8fnXig0PSkGPCsh9EL3jsH0aWRXVAhVLxQnEo4TIizcVN%2BWmzn1bM37SuFP2ZelnwO4BvZRocZyBKeT46%2BzuIAq96z3ciZpEqqXS%2Bwc5HKXnnYlkRjtwqp%2ByvdK5e%2BcTC3Gh69B%2B0BayXp5MrPjMo%2BHsfQS5YkjE7KIlRu4mV82%2BzEKwwmLPGxAY6pgF3c%2BEP4QvLjc5etM3iupTsHQ8n384iidvdIIdtMKCJpUfwff8Fm522Fgo6UhikHmBJyutIvR1zTt2uBoB3%2B%2FOXigGAXUuzEBR8rWKsuwEXcLCRVgGdJ7gJwbef6DJLHtJ%2B4mnIUrITI0Zl%2FbLTdcJiHmK6aRXX86oTht1DmVAZIrMVd2Qdm4DqAqk%2FKxHhIfimSejDxppI%2F490b%2Bb6WO1JJcJ09Pmk&X-Amz-Signature=ff1747ce727dd8543142137b5b1bf1bf9a8b4851748d61141293c2061fe15bb3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Encoder 는 N개의 Encoder Block 으로 구성되어 있다.  (논문에서는 N = 6으로 사용했다. )

Encoder Block의 Input/output 형태는 동일하다. 어떤 Matrix 를 Input으로 받는다고 했을 때, output 역시 해당 Matrix와 같은 형태(Shape)를 갖고있다. → Shape이 바뀌지 않는다 (멱등하다.)

각 Encoder 모델은 연결되어 있다. N-1 EB 와 N EB가 연결되어 있다. 각 Input / Output Matrix Shape도 같기 때문에 전체 Encoder의 Shape은 항상 일정하다 (멱등하다.)

Encoder Block을 여러 겹으로 쌓는 것인가? 
Encoder Block은 Input으로 들어오는 문장을 Vector화 하여 Context로 만든다, Context로 만들어진 문장은 추상화되어 더 넓은 관점으로 높은 차원에서 고려될 수 있는 정보로 바뀌고 이 과정을 반복하면 매우 높은 차원의(추상화된 정보) Context가 생성되고 더 많은 관점에서 피처들을 뽑아낼 수 있다.

문장 → 높은 차원의 Context → 보다 더 높은 차원의 Context → …. → Output

일단 이 정도로만 하고 넘어가면 될 것 같다. 

## **Encoder Block**

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/14fc4b24-1f46-437d-80dc-f938777ef95b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46634J5UKV4%2F20250805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250805T060951Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJGMEQCIDNy%2Bm2lbT5BaTB8NQpKemYwPJZaqX4TG5mWC4tWS9MCAiBKkFkn7Ebw77QkKfzJsMFbJ8bWVMFbuoEBCBLDMueYiCr%2FAwhXEAAaDDYzNzQyMzE4MzgwNSIMRj9rhRfftAvh2osrKtwDchSWgPR7WnUUcaFJ5Mp1YPn62lLF0j4vqjnkKBMO20OB2VlVfvhiwT4ssqhp4Zw9pHtGKJjmYPDYtZ%2BIscF4QGCCnvnrnUBt%2Fr%2BdQTpoxajjQn%2BypDVDVzMNsy20xRvJm1sqvamlFlednGfP3vaL92ypHj%2Byo5zjKzZNLLgAJF6AujV1VhZfBo%2FXXmrPhtHOaP%2BSd7U9Tx7H8r%2FhZqvM%2BzklXG7ytztDnYd17X8vqS0RxcEzmXaJrV8JxGjFQsHf%2F31xcZYcXGgnKav8lv7XAm6gPwOJa1cCAdvTpmdWbqYWychCEU3RtG5%2BjMIYL3%2FEpkwV3Cg6pymNCqcBC2GGoSqjDuq5qBmAM0Av2fRL0fB4DZk6YDZyENyZAaV7ixKGzdQ5eFBrwk90iHokewU7GlDtg4iMs66fOh%2BMLpKJ2xHQRlEpxYmKNdPHP5xECdFPpoDu3bIkqGb8fnXig0PSkGPCsh9EL3jsH0aWRXVAhVLxQnEo4TIizcVN%2BWmzn1bM37SuFP2ZelnwO4BvZRocZyBKeT46%2BzuIAq96z3ciZpEqqXS%2Bwc5HKXnnYlkRjtwqp%2ByvdK5e%2BcTC3Gh69B%2B0BayXp5MrPjMo%2BHsfQS5YkjE7KIlRu4mV82%2BzEKwwmLPGxAY6pgF3c%2BEP4QvLjc5etM3iupTsHQ8n384iidvdIIdtMKCJpUfwff8Fm522Fgo6UhikHmBJyutIvR1zTt2uBoB3%2B%2FOXigGAXUuzEBR8rWKsuwEXcLCRVgGdJ7gJwbef6DJLHtJ%2B4mnIUrITI0Zl%2FbLTdcJiHmK6aRXX86oTht1DmVAZIrMVd2Qdm4DqAqk%2FKxHhIfimSejDxppI%2F490b%2Bb6WO1JJcJ09Pmk&X-Amz-Signature=1d280a8953d68a09cc137fafc72529d399fa58202295bf398d097d66e45f57ba&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Encoder Block은 크게 Multi-Head Attention Layer, Position-wise Feed-Forward Layer로 구성된다.

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/2934b9e2-c4eb-4789-b583-072f846976a0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46634J5UKV4%2F20250805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250805T060951Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJGMEQCIDNy%2Bm2lbT5BaTB8NQpKemYwPJZaqX4TG5mWC4tWS9MCAiBKkFkn7Ebw77QkKfzJsMFbJ8bWVMFbuoEBCBLDMueYiCr%2FAwhXEAAaDDYzNzQyMzE4MzgwNSIMRj9rhRfftAvh2osrKtwDchSWgPR7WnUUcaFJ5Mp1YPn62lLF0j4vqjnkKBMO20OB2VlVfvhiwT4ssqhp4Zw9pHtGKJjmYPDYtZ%2BIscF4QGCCnvnrnUBt%2Fr%2BdQTpoxajjQn%2BypDVDVzMNsy20xRvJm1sqvamlFlednGfP3vaL92ypHj%2Byo5zjKzZNLLgAJF6AujV1VhZfBo%2FXXmrPhtHOaP%2BSd7U9Tx7H8r%2FhZqvM%2BzklXG7ytztDnYd17X8vqS0RxcEzmXaJrV8JxGjFQsHf%2F31xcZYcXGgnKav8lv7XAm6gPwOJa1cCAdvTpmdWbqYWychCEU3RtG5%2BjMIYL3%2FEpkwV3Cg6pymNCqcBC2GGoSqjDuq5qBmAM0Av2fRL0fB4DZk6YDZyENyZAaV7ixKGzdQ5eFBrwk90iHokewU7GlDtg4iMs66fOh%2BMLpKJ2xHQRlEpxYmKNdPHP5xECdFPpoDu3bIkqGb8fnXig0PSkGPCsh9EL3jsH0aWRXVAhVLxQnEo4TIizcVN%2BWmzn1bM37SuFP2ZelnwO4BvZRocZyBKeT46%2BzuIAq96z3ciZpEqqXS%2Bwc5HKXnnYlkRjtwqp%2ByvdK5e%2BcTC3Gh69B%2B0BayXp5MrPjMo%2BHsfQS5YkjE7KIlRu4mV82%2BzEKwwmLPGxAY6pgF3c%2BEP4QvLjc5etM3iupTsHQ8n384iidvdIIdtMKCJpUfwff8Fm522Fgo6UhikHmBJyutIvR1zTt2uBoB3%2B%2FOXigGAXUuzEBR8rWKsuwEXcLCRVgGdJ7gJwbef6DJLHtJ%2B4mnIUrITI0Zl%2FbLTdcJiHmK6aRXX86oTht1DmVAZIrMVd2Qdm4DqAqk%2FKxHhIfimSejDxppI%2F490b%2Bb6WO1JJcJ09Pmk&X-Amz-Signature=da12bb556051618e48abdedfc14fae68c05ee945b2fecabef52dc5a7556032d7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/dac62052-f9b4-4944-8208-320b66c9da6e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46634J5UKV4%2F20250805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250805T060952Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJGMEQCIDNy%2Bm2lbT5BaTB8NQpKemYwPJZaqX4TG5mWC4tWS9MCAiBKkFkn7Ebw77QkKfzJsMFbJ8bWVMFbuoEBCBLDMueYiCr%2FAwhXEAAaDDYzNzQyMzE4MzgwNSIMRj9rhRfftAvh2osrKtwDchSWgPR7WnUUcaFJ5Mp1YPn62lLF0j4vqjnkKBMO20OB2VlVfvhiwT4ssqhp4Zw9pHtGKJjmYPDYtZ%2BIscF4QGCCnvnrnUBt%2Fr%2BdQTpoxajjQn%2BypDVDVzMNsy20xRvJm1sqvamlFlednGfP3vaL92ypHj%2Byo5zjKzZNLLgAJF6AujV1VhZfBo%2FXXmrPhtHOaP%2BSd7U9Tx7H8r%2FhZqvM%2BzklXG7ytztDnYd17X8vqS0RxcEzmXaJrV8JxGjFQsHf%2F31xcZYcXGgnKav8lv7XAm6gPwOJa1cCAdvTpmdWbqYWychCEU3RtG5%2BjMIYL3%2FEpkwV3Cg6pymNCqcBC2GGoSqjDuq5qBmAM0Av2fRL0fB4DZk6YDZyENyZAaV7ixKGzdQ5eFBrwk90iHokewU7GlDtg4iMs66fOh%2BMLpKJ2xHQRlEpxYmKNdPHP5xECdFPpoDu3bIkqGb8fnXig0PSkGPCsh9EL3jsH0aWRXVAhVLxQnEo4TIizcVN%2BWmzn1bM37SuFP2ZelnwO4BvZRocZyBKeT46%2BzuIAq96z3ciZpEqqXS%2Bwc5HKXnnYlkRjtwqp%2ByvdK5e%2BcTC3Gh69B%2B0BayXp5MrPjMo%2BHsfQS5YkjE7KIlRu4mV82%2BzEKwwmLPGxAY6pgF3c%2BEP4QvLjc5etM3iupTsHQ8n384iidvdIIdtMKCJpUfwff8Fm522Fgo6UhikHmBJyutIvR1zTt2uBoB3%2B%2FOXigGAXUuzEBR8rWKsuwEXcLCRVgGdJ7gJwbef6DJLHtJ%2B4mnIUrITI0Zl%2FbLTdcJiHmK6aRXX86oTht1DmVAZIrMVd2Qdm4DqAqk%2FKxHhIfimSejDxppI%2F490b%2Bb6WO1JJcJ09Pmk&X-Amz-Signature=caf32196b8872af6c456371c842eb4c33eec03c4e9c3f92a194670bf719e9ed3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

1. Input에는 Position Encoding + Embeding된 데이터가 들어온다.
1. Linear에서는 1번 Input Matrix에 대해 차원 축소와 출력 Matrix의 모양과 맞춰주는 역할을 한다. 
1. MatMUL에서는 Query와 Key 행렬의 내적을 통해 Attention Score Matrix 를 만든다. 
1. 이후에 Scale과 SoftMax를 통해서 각 유사도의 값의 합(항목별)이 1이 되도록 SoftMax해준다.
![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/c25b2651-1360-4dc3-8392-b5431fd36014/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46634J5UKV4%2F20250805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250805T060952Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJGMEQCIDNy%2Bm2lbT5BaTB8NQpKemYwPJZaqX4TG5mWC4tWS9MCAiBKkFkn7Ebw77QkKfzJsMFbJ8bWVMFbuoEBCBLDMueYiCr%2FAwhXEAAaDDYzNzQyMzE4MzgwNSIMRj9rhRfftAvh2osrKtwDchSWgPR7WnUUcaFJ5Mp1YPn62lLF0j4vqjnkKBMO20OB2VlVfvhiwT4ssqhp4Zw9pHtGKJjmYPDYtZ%2BIscF4QGCCnvnrnUBt%2Fr%2BdQTpoxajjQn%2BypDVDVzMNsy20xRvJm1sqvamlFlednGfP3vaL92ypHj%2Byo5zjKzZNLLgAJF6AujV1VhZfBo%2FXXmrPhtHOaP%2BSd7U9Tx7H8r%2FhZqvM%2BzklXG7ytztDnYd17X8vqS0RxcEzmXaJrV8JxGjFQsHf%2F31xcZYcXGgnKav8lv7XAm6gPwOJa1cCAdvTpmdWbqYWychCEU3RtG5%2BjMIYL3%2FEpkwV3Cg6pymNCqcBC2GGoSqjDuq5qBmAM0Av2fRL0fB4DZk6YDZyENyZAaV7ixKGzdQ5eFBrwk90iHokewU7GlDtg4iMs66fOh%2BMLpKJ2xHQRlEpxYmKNdPHP5xECdFPpoDu3bIkqGb8fnXig0PSkGPCsh9EL3jsH0aWRXVAhVLxQnEo4TIizcVN%2BWmzn1bM37SuFP2ZelnwO4BvZRocZyBKeT46%2BzuIAq96z3ciZpEqqXS%2Bwc5HKXnnYlkRjtwqp%2ByvdK5e%2BcTC3Gh69B%2B0BayXp5MrPjMo%2BHsfQS5YkjE7KIlRu4mV82%2BzEKwwmLPGxAY6pgF3c%2BEP4QvLjc5etM3iupTsHQ8n384iidvdIIdtMKCJpUfwff8Fm522Fgo6UhikHmBJyutIvR1zTt2uBoB3%2B%2FOXigGAXUuzEBR8rWKsuwEXcLCRVgGdJ7gJwbef6DJLHtJ%2B4mnIUrITI0Zl%2FbLTdcJiHmK6aRXX86oTht1DmVAZIrMVd2Qdm4DqAqk%2FKxHhIfimSejDxppI%2F490b%2Bb6WO1JJcJ09Pmk&X-Amz-Signature=6fc33751df2b5ee0912fdf85dc97f85ee9e7311e28aa5f89390bed4e0f38a37b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/34305e15-6d2f-4993-a64c-9ef01a463274/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46634J5UKV4%2F20250805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250805T060952Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJGMEQCIDNy%2Bm2lbT5BaTB8NQpKemYwPJZaqX4TG5mWC4tWS9MCAiBKkFkn7Ebw77QkKfzJsMFbJ8bWVMFbuoEBCBLDMueYiCr%2FAwhXEAAaDDYzNzQyMzE4MzgwNSIMRj9rhRfftAvh2osrKtwDchSWgPR7WnUUcaFJ5Mp1YPn62lLF0j4vqjnkKBMO20OB2VlVfvhiwT4ssqhp4Zw9pHtGKJjmYPDYtZ%2BIscF4QGCCnvnrnUBt%2Fr%2BdQTpoxajjQn%2BypDVDVzMNsy20xRvJm1sqvamlFlednGfP3vaL92ypHj%2Byo5zjKzZNLLgAJF6AujV1VhZfBo%2FXXmrPhtHOaP%2BSd7U9Tx7H8r%2FhZqvM%2BzklXG7ytztDnYd17X8vqS0RxcEzmXaJrV8JxGjFQsHf%2F31xcZYcXGgnKav8lv7XAm6gPwOJa1cCAdvTpmdWbqYWychCEU3RtG5%2BjMIYL3%2FEpkwV3Cg6pymNCqcBC2GGoSqjDuq5qBmAM0Av2fRL0fB4DZk6YDZyENyZAaV7ixKGzdQ5eFBrwk90iHokewU7GlDtg4iMs66fOh%2BMLpKJ2xHQRlEpxYmKNdPHP5xECdFPpoDu3bIkqGb8fnXig0PSkGPCsh9EL3jsH0aWRXVAhVLxQnEo4TIizcVN%2BWmzn1bM37SuFP2ZelnwO4BvZRocZyBKeT46%2BzuIAq96z3ciZpEqqXS%2Bwc5HKXnnYlkRjtwqp%2ByvdK5e%2BcTC3Gh69B%2B0BayXp5MrPjMo%2BHsfQS5YkjE7KIlRu4mV82%2BzEKwwmLPGxAY6pgF3c%2BEP4QvLjc5etM3iupTsHQ8n384iidvdIIdtMKCJpUfwff8Fm522Fgo6UhikHmBJyutIvR1zTt2uBoB3%2B%2FOXigGAXUuzEBR8rWKsuwEXcLCRVgGdJ7gJwbef6DJLHtJ%2B4mnIUrITI0Zl%2FbLTdcJiHmK6aRXX86oTht1DmVAZIrMVd2Qdm4DqAqk%2FKxHhIfimSejDxppI%2F490b%2Bb6WO1JJcJ09Pmk&X-Amz-Signature=846d9b533c06cc5daddb272289ddbeb7c29b308aef8f6fa5995042ded2271ac9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

마지막에 Value Matrix와 내적한다. 

조금 주요 부분을 리즈너블하게 설명을 하자면

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/2a36b0af-a461-4513-9bcc-7d2d30b5a238/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46634J5UKV4%2F20250805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250805T060952Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJGMEQCIDNy%2Bm2lbT5BaTB8NQpKemYwPJZaqX4TG5mWC4tWS9MCAiBKkFkn7Ebw77QkKfzJsMFbJ8bWVMFbuoEBCBLDMueYiCr%2FAwhXEAAaDDYzNzQyMzE4MzgwNSIMRj9rhRfftAvh2osrKtwDchSWgPR7WnUUcaFJ5Mp1YPn62lLF0j4vqjnkKBMO20OB2VlVfvhiwT4ssqhp4Zw9pHtGKJjmYPDYtZ%2BIscF4QGCCnvnrnUBt%2Fr%2BdQTpoxajjQn%2BypDVDVzMNsy20xRvJm1sqvamlFlednGfP3vaL92ypHj%2Byo5zjKzZNLLgAJF6AujV1VhZfBo%2FXXmrPhtHOaP%2BSd7U9Tx7H8r%2FhZqvM%2BzklXG7ytztDnYd17X8vqS0RxcEzmXaJrV8JxGjFQsHf%2F31xcZYcXGgnKav8lv7XAm6gPwOJa1cCAdvTpmdWbqYWychCEU3RtG5%2BjMIYL3%2FEpkwV3Cg6pymNCqcBC2GGoSqjDuq5qBmAM0Av2fRL0fB4DZk6YDZyENyZAaV7ixKGzdQ5eFBrwk90iHokewU7GlDtg4iMs66fOh%2BMLpKJ2xHQRlEpxYmKNdPHP5xECdFPpoDu3bIkqGb8fnXig0PSkGPCsh9EL3jsH0aWRXVAhVLxQnEo4TIizcVN%2BWmzn1bM37SuFP2ZelnwO4BvZRocZyBKeT46%2BzuIAq96z3ciZpEqqXS%2Bwc5HKXnnYlkRjtwqp%2ByvdK5e%2BcTC3Gh69B%2B0BayXp5MrPjMo%2BHsfQS5YkjE7KIlRu4mV82%2BzEKwwmLPGxAY6pgF3c%2BEP4QvLjc5etM3iupTsHQ8n384iidvdIIdtMKCJpUfwff8Fm522Fgo6UhikHmBJyutIvR1zTt2uBoB3%2B%2FOXigGAXUuzEBR8rWKsuwEXcLCRVgGdJ7gJwbef6DJLHtJ%2B4mnIUrITI0Zl%2FbLTdcJiHmK6aRXX86oTht1DmVAZIrMVd2Qdm4DqAqk%2FKxHhIfimSejDxppI%2F490b%2Bb6WO1JJcJ09Pmk&X-Amz-Signature=bed17a852403fc043eeb967ee69b18ff586a06a509bd207c2599475373479ad9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

1. Matmul에서 Query와 Key 간의 유사도를 계산한다, 각 단어(토큰) 간의 유사도를 계산해서 관련 있는 부분은 더 많은 정보를, 유사도가 적은 단어(토큰)은 적은 정보를 가져간다. 
1. 마지막에 Value를 내적하여 Attention Score Matrix를 적용한다.
1. 이걸 Multi Head 방식으로 여러 겹 쌓는 이유는 위 그림처럼 다양한 관점에서 더 복잡한 관계성을 파악할 수 있는 장점이 있기 때문이다. 
참조

https://www.blossominkyung.com/deeplearning/transformer-mha

https://tech.scatterlab.co.kr/vllm-implementation-details/

https://cpm0722.github.io/pytorch-implementation/transformer


