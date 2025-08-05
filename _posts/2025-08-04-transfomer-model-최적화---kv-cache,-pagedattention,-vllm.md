---
title: "Transfomer model 최적화 - KV Cache, PagedAttention, vLLM"
date: 2025-08-04 06:05:00 +0900
categories: [기술소개]
tags: [Transfomer, LLM, AI]
description: Transfomer model 기술 소개
toc: true
comments: true
---

# Transfomer model 최적화 - KV Cache, PagedAttention, vLLM

Transfomer 모델을 최적화하기 위한 방식 KV Cache와 해당 방법의 단점을 보완한 Paged KV Cache방식 그리고 실제 응용 사례인 vLLM을 소개하는 페이지이다. 

## KV Cache

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/d2dedcd2-1e43-4280-baf2-bb42f853c099/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3WJWOHE%2F20250805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250805T061035Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQD%2FpXSCjdPFrKsh53mTZY3l2LxqiKbiEYlNEReLsMPgdQIhAOaH3N7fiPN4QXXLKaSgz1StSeDRmIMXaLqQKInAknwXKv8DCFcQABoMNjM3NDIzMTgzODA1IgxTLscZkLhXCExXs5wq3APVRWJkQhrGGUMpEtfaU1KdPebuVHwDbewfFivkXUkOdnKAl3eub%2FDXAQobnH3%2BUKLNvqv0B4xoDCWh9KUEvVgeo5NzSzNZsRPBL5FEXS08LX3eL3ZaofcMtveHtbXIspIp3XVqdcxo4HVpE%2BEq3OyTyX7aSzuBq5EzWMTnYRsu3OpRh5Sqtn5l9z3WjsN5mheUbmJxVc9aIHMqaHKHm5O7gdH5v1jBlgG5Iu1u2umzsRisadhI%2BjanlvmnxH6q912H0vCNJBDFNAClqB4jFiCLcIo5mBkDqaJpiqioNvodUcHVbonUr1zhqUf5yrx7q9q5PsHz2T5CFhcmyTCpAw%2FEUxhVvznZYVTzMnAD4BYJHyb5F1DuS%2B2HWVXwFaY%2F25rbb0Lm4uFeIQ%2BtyG8mqAaVICmA2%2BmS%2FWvlRUd%2B2nQiX%2BwYUEhLk1aFJItf5GPTm0DKCS3AkyAPIkuH33L8zxRW5GQ6TACDlfI%2Bai8IjZTw53GDaUy%2F2E4ON5j45yiKOEY9stWkao0A0eMCm4UtI%2F5XSh%2BCqhQvyU0q622zp5q7KHptBK9%2BzshL7zUdTD2G%2BcjEHnqJszbxdcxfa8hPozIi%2F0T2cIMPXrsaOI%2BM61kk9l%2BxX%2F3rcrGqu4PZtzDKs8bEBjqkAW4uPyNylEEZUdVnKZdvNPuBqe8LHohfMGKHTqjMRRTzO1XhxLKlXx7Z0CaJ0UfEsrwDgFwvWxvMDgy2DUWaJhkuvtTCCjh7PxbC5P1RRRt%2FgAp24IeM0ThbTAgyUaJwddzX8Om62owyLttXtRDqgp1uYTn4JyR%2FGvq9TqWkNZGXLnDjKZBpwfTznE2pkCRrhSdh0Yqj%2B%2Bll2ZXFJ8NE5xzGhWyo&X-Amz-Signature=da4edb2c034d4bfe01631f46bc1f47f6c2c1d7fcb677598595b1ff2808ef0459&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

트랜스포머 모델의 Attention 매커니즘을 짧게 소개하자면 Scaled Dot-Product Attention 연산을 여러 겹 올린 Multi-Head Attention 이 기본적이다.

이 모델 구조에서 Scaled Dot-Product Attention 연산을 반복적으로 수행하게 되는데 이 과정에서 중복된 연산이 많이 일어난다. 

Decoder에서 토큰을 생성하면서 Scaled Dot-Product Attention을 반복적으로 수행하는 과정 속에서 이전 토큰들의 계산을 중복적으로 계산을 하는데 이 과정을 Cache를 통해서 일정량의 저장비용을 통해 연산비용을 줄이는 기술이 KV Cache이다!

(KV Cahce인 이유는Key와 Value 영역의 정보를 Cache하기 때문에)

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/75f005c6-c2f9-45e8-ad7a-efb9ebedb50e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3WJWOHE%2F20250805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250805T061035Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQD%2FpXSCjdPFrKsh53mTZY3l2LxqiKbiEYlNEReLsMPgdQIhAOaH3N7fiPN4QXXLKaSgz1StSeDRmIMXaLqQKInAknwXKv8DCFcQABoMNjM3NDIzMTgzODA1IgxTLscZkLhXCExXs5wq3APVRWJkQhrGGUMpEtfaU1KdPebuVHwDbewfFivkXUkOdnKAl3eub%2FDXAQobnH3%2BUKLNvqv0B4xoDCWh9KUEvVgeo5NzSzNZsRPBL5FEXS08LX3eL3ZaofcMtveHtbXIspIp3XVqdcxo4HVpE%2BEq3OyTyX7aSzuBq5EzWMTnYRsu3OpRh5Sqtn5l9z3WjsN5mheUbmJxVc9aIHMqaHKHm5O7gdH5v1jBlgG5Iu1u2umzsRisadhI%2BjanlvmnxH6q912H0vCNJBDFNAClqB4jFiCLcIo5mBkDqaJpiqioNvodUcHVbonUr1zhqUf5yrx7q9q5PsHz2T5CFhcmyTCpAw%2FEUxhVvznZYVTzMnAD4BYJHyb5F1DuS%2B2HWVXwFaY%2F25rbb0Lm4uFeIQ%2BtyG8mqAaVICmA2%2BmS%2FWvlRUd%2B2nQiX%2BwYUEhLk1aFJItf5GPTm0DKCS3AkyAPIkuH33L8zxRW5GQ6TACDlfI%2Bai8IjZTw53GDaUy%2F2E4ON5j45yiKOEY9stWkao0A0eMCm4UtI%2F5XSh%2BCqhQvyU0q622zp5q7KHptBK9%2BzshL7zUdTD2G%2BcjEHnqJszbxdcxfa8hPozIi%2F0T2cIMPXrsaOI%2BM61kk9l%2BxX%2F3rcrGqu4PZtzDKs8bEBjqkAW4uPyNylEEZUdVnKZdvNPuBqe8LHohfMGKHTqjMRRTzO1XhxLKlXx7Z0CaJ0UfEsrwDgFwvWxvMDgy2DUWaJhkuvtTCCjh7PxbC5P1RRRt%2FgAp24IeM0ThbTAgyUaJwddzX8Om62owyLttXtRDqgp1uYTn4JyR%2FGvq9TqWkNZGXLnDjKZBpwfTznE2pkCRrhSdh0Yqj%2B%2Bll2ZXFJ8NE5xzGhWyo&X-Amz-Signature=fb121196cb3a9004fa392e3aa145e55f1c38b2d21d7638b242607f7a0e9cf521&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

결국 백터의 내적 계산을 반복적으로 수행하는 것 이기 때문에

K^t에서 Token1,2,3을 기억하고 있다면 Token 4의 Attention을 구할 때 굳이 1,2,3을 다시 계산할 필요가 없다. 

### KV 캐싱 문제점

### 참조


