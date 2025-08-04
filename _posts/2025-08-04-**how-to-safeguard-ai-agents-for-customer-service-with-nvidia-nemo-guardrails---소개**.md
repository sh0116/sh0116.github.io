---
title: "**How to Safeguard AI Agents for Customer Service with NVIDIA NeMo Guardrails - 소개**"
date: 2025-08-04 06:05:00 +0900
categories: [기술소개]
tags: [LLM, NVIDIA]
description: NVIDIA NeMo Guardrails 소개
toc: true
comments: true
---

# #1 NeMo Guardrails란

- NVIDIA에서 개발한 오픈 소스 LIB로, LLM 기반 Application 에 안전 장치(가드레일)을 설치하여 모델에서 예상하지 못한 대답이나 민감정보를 노출하지 않도록 제어하는 기술임
# #2 NeMo Guardrails 기능 및 특징

- **룰(규칙) 기반 프레임워크**
- **대화 흐름 관리**
- **세분화된 컨텐츠 필터링 **
- **개인정보 보호와 보안**
- **멀티 모달 확장 **
# #3 NeMo Guardrails 예시

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/b6671cd6-6d41-4c3a-a95a-a284fd8a8396/arcitecture-nvidia-nemo-guardrails-intelligent-virtual-ai-assistants-customer-service-2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MSX3CTA%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T072245Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJIMEYCIQCAS3rVbfssLXQueemE2ni8fftxn0nEpQA50XStxsMrqwIhAPG8kk6S8goboSGRKF4aI8rw2pPEPQ3%2F334DsudR1NsUKv8DCEAQABoMNjM3NDIzMTgzODA1IgzaRi5aapbYYq43KrQq3APqtGxY5n3QvT1%2FWslrxnz2IZxS4TVVtTFi55x3yNADp34VkhoOHf0EymtZJ5hWKsuCL9W9txo%2BqbSpVnuzDySwXr1YqJDtPzaHL2qQCnO2Zvt4XuSGFBbGQ36gjhBAI3DkZu2csHacQbgSLSw%2B6eNy9l%2FFh8UPgQeVYcOSYplZ6uMIy6ni5oge7C7zk%2BIfpLCPCvBllds41O9Tc5aEMbBZV7lo5bnwTvkefnJWbzJmQ5LVYoWdlIAX67wnbfI9OqPVDZkt9OirFaieur7dvOSAFKYn5DTLXDF7p1cz8WbTLwrAnUe8%2FTcQd%2FKX7fQB3iMqLHiXAW3vf9No0wI0w%2BVcj6g9KwzVoRb9uDk7frZlBAayT%2BS4q3%2BMIOjAuCUKzlIA5HAWspklSiLiwdtBsAUb8uJrBvu7iiBI3IqPnP8b7WAbEI2IsmRfpHZ2hosOrde7Mz6zWSr8l0P1rvuQFRDj8vsH9Vcl2Yw3mJ0eIRXFRbYw5vRxiUlRjvK4eVziiEFgT3KO8i2bjyItbCvajw1ppXq%2Fj2Ide%2B577Nq5hzVsIeVD3z882D6umg64OmIed6DY2fqMNNgvTjJeK8Ou%2FwUkOCwuOXcleuHAOrh1OicFQLNZukm12KViCbOwgDC8tsHEBjqkAfdbNGrIQNgelRytREvAZKu1AplZDzFqAEA7%2Fd4xe8QYceilmeBh6AdWgzQZ30I0M6LnX%2F9DXTo4dfNHwv7zOa8MZqFVLR5hQuncln7hyISWMl0IUij28zLmurIy%2BL8b7oYrrKJ7OAvFruHjQlD5rrLUuAaEY7h9LH91koluLfmCGsasYU90gxilk3q0Q8AoP%2Bl%2Bp92pupTKlR5OiivQLjv%2FSUTK&X-Amz-Signature=de2e3c26cafb4cc7ebfdf5b8a43e03cf84ff3e62cff151f688003db6b34256c4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

NVIDIA Tech Blog, figure 1

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/e47fdbc0-9809-4a57-929d-89d8c3a76b01/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MSX3CTA%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T072245Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJIMEYCIQCAS3rVbfssLXQueemE2ni8fftxn0nEpQA50XStxsMrqwIhAPG8kk6S8goboSGRKF4aI8rw2pPEPQ3%2F334DsudR1NsUKv8DCEAQABoMNjM3NDIzMTgzODA1IgzaRi5aapbYYq43KrQq3APqtGxY5n3QvT1%2FWslrxnz2IZxS4TVVtTFi55x3yNADp34VkhoOHf0EymtZJ5hWKsuCL9W9txo%2BqbSpVnuzDySwXr1YqJDtPzaHL2qQCnO2Zvt4XuSGFBbGQ36gjhBAI3DkZu2csHacQbgSLSw%2B6eNy9l%2FFh8UPgQeVYcOSYplZ6uMIy6ni5oge7C7zk%2BIfpLCPCvBllds41O9Tc5aEMbBZV7lo5bnwTvkefnJWbzJmQ5LVYoWdlIAX67wnbfI9OqPVDZkt9OirFaieur7dvOSAFKYn5DTLXDF7p1cz8WbTLwrAnUe8%2FTcQd%2FKX7fQB3iMqLHiXAW3vf9No0wI0w%2BVcj6g9KwzVoRb9uDk7frZlBAayT%2BS4q3%2BMIOjAuCUKzlIA5HAWspklSiLiwdtBsAUb8uJrBvu7iiBI3IqPnP8b7WAbEI2IsmRfpHZ2hosOrde7Mz6zWSr8l0P1rvuQFRDj8vsH9Vcl2Yw3mJ0eIRXFRbYw5vRxiUlRjvK4eVziiEFgT3KO8i2bjyItbCvajw1ppXq%2Fj2Ide%2B577Nq5hzVsIeVD3z882D6umg64OmIed6DY2fqMNNgvTjJeK8Ou%2FwUkOCwuOXcleuHAOrh1OicFQLNZukm12KViCbOwgDC8tsHEBjqkAfdbNGrIQNgelRytREvAZKu1AplZDzFqAEA7%2Fd4xe8QYceilmeBh6AdWgzQZ30I0M6LnX%2F9DXTo4dfNHwv7zOa8MZqFVLR5hQuncln7hyISWMl0IUij28zLmurIy%2BL8b7oYrrKJ7OAvFruHjQlD5rrLUuAaEY7h9LH91koluLfmCGsasYU90gxilk3q0Q8AoP%2Bl%2Bp92pupTKlR5OiivQLjv%2FSUTK&X-Amz-Signature=6de23557d9b006cffd142913ba687c54d975c3fbc472be6685daf3bfb1038892&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- **ContentSafety NIM : 부적절한 언어 탐지**
- **TopicControl NIM : 주제에 맞는 질문 제한**
- **RAG Enforcement : 검색 범위 한정**
- **JailbreakDetect NIM : LLM Jailbreak 탐지**
- **PII Detection : 데이터 보호**
# #4 결론

- **NVIDIA NeMo Guardrails와 NIM 마이크로서비스의 역할**
- **안전·보안 모델 3종**
- **적용 효과**

