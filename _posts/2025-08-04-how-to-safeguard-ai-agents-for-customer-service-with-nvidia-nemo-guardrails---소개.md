---
title: "How to Safeguard AI Agents for Customer Service with NVIDIA NeMo Guardrails - 소개"
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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/b6671cd6-6d41-4c3a-a95a-a284fd8a8396/arcitecture-nvidia-nemo-guardrails-intelligent-virtual-ai-assistants-customer-service-2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V6FSSUAS%2F20250805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250805T061101Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJGMEQCICbnIoOAGfgYSo8dJnf1fl19vKdL%2B9hz52z7t%2FyOhp0fAiBaQcBfbH0mjrqJAnahWjF9wO65Dk9Tp0EsdSx%2BCNkF5yr%2FAwhXEAAaDDYzNzQyMzE4MzgwNSIM9da7SXDtgiTkG2wKKtwDyW%2BclB%2BNyEAshOzc9XpaemXzCtq2OuC%2FU%2F0qr8ODyP9ZZaEkOdTLK0h6KuN7VJseNLN%2BuRXB3XzrmT5syumCf6bqsGThsgSQjzk1DePqg8IPTdyg5QS2KyGAcXDp0B3Y2ZglNQRJbMltzbdXZfUw3H1w6lYHtdImoHxzbJFdGASOwNp%2FiCyysXWbMqdAx7X8yvn%2BjW1P6xsNz80GCXgn1b8aPNOBmjSvxwjE5ibBC5WnWQAgGJXlSMOc1QTXO5CWxVU7A8gHPSnF2d0msWo3G5qQK%2BfOtz5Zu53KKgoJ88qdeaPKxaZuOl4Hz64WB75eZ3bIjtEe1R%2BP1gKv1tfzu4B48EfXlTskZmhaAzeksxYm7ilK4nZrz8i9RDnWzh1aKAuVr48JYAIpDwmi6%2Bmc%2Bfd%2FzD%2BM6I45r2kN%2FPdM36KqhYDGj6fjqwwXDHZDiUTZp1m2vMETpmiY67befeS75Mk0kJtCUbXU2uwizcNTFclvAcjDnFHwLAZ0wxFGZZG3M8rWe7KAl8wl3R3myAfH0wfuS0dXiYpaMTrJwhRYrhHFFqvtHUrS4rJmuaVBSrDiYHmHfqnNhpKEpgmbUaua0idP4HE6fj4h8N9Z3X9QbtFTcIB943x0hZtK0EMw6rPGxAY6pgEXviynP2qWv7Yn%2FO9kcdQK91ZwXDsPiIVezO6yv7%2B3hdlvO4nOm8QF19VyEs9oA7OEpeOEn1DeI9wGhWrtXeuqq%2FSMn3ylkawfTcYxcagKd0ahAQfqmF0xVcjAlG1lKMWapJ7myIoTz6xyd9j0Wr9ZpPbWwIE7a%2B6Vd6%2FkaPCUoT%2Bxjdvu8XTrFkCeTHnHc6BlaxJAhFPnXI%2Bkom%2FrkmK1VZWoyrtE&X-Amz-Signature=5328e7ab0d9e65ad9c747aea32fea20721ee528a47a3926546555ce9676e47c3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

NVIDIA Tech Blog, figure 1

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/e47fdbc0-9809-4a57-929d-89d8c3a76b01/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V6FSSUAS%2F20250805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250805T061101Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJGMEQCICbnIoOAGfgYSo8dJnf1fl19vKdL%2B9hz52z7t%2FyOhp0fAiBaQcBfbH0mjrqJAnahWjF9wO65Dk9Tp0EsdSx%2BCNkF5yr%2FAwhXEAAaDDYzNzQyMzE4MzgwNSIM9da7SXDtgiTkG2wKKtwDyW%2BclB%2BNyEAshOzc9XpaemXzCtq2OuC%2FU%2F0qr8ODyP9ZZaEkOdTLK0h6KuN7VJseNLN%2BuRXB3XzrmT5syumCf6bqsGThsgSQjzk1DePqg8IPTdyg5QS2KyGAcXDp0B3Y2ZglNQRJbMltzbdXZfUw3H1w6lYHtdImoHxzbJFdGASOwNp%2FiCyysXWbMqdAx7X8yvn%2BjW1P6xsNz80GCXgn1b8aPNOBmjSvxwjE5ibBC5WnWQAgGJXlSMOc1QTXO5CWxVU7A8gHPSnF2d0msWo3G5qQK%2BfOtz5Zu53KKgoJ88qdeaPKxaZuOl4Hz64WB75eZ3bIjtEe1R%2BP1gKv1tfzu4B48EfXlTskZmhaAzeksxYm7ilK4nZrz8i9RDnWzh1aKAuVr48JYAIpDwmi6%2Bmc%2Bfd%2FzD%2BM6I45r2kN%2FPdM36KqhYDGj6fjqwwXDHZDiUTZp1m2vMETpmiY67befeS75Mk0kJtCUbXU2uwizcNTFclvAcjDnFHwLAZ0wxFGZZG3M8rWe7KAl8wl3R3myAfH0wfuS0dXiYpaMTrJwhRYrhHFFqvtHUrS4rJmuaVBSrDiYHmHfqnNhpKEpgmbUaua0idP4HE6fj4h8N9Z3X9QbtFTcIB943x0hZtK0EMw6rPGxAY6pgEXviynP2qWv7Yn%2FO9kcdQK91ZwXDsPiIVezO6yv7%2B3hdlvO4nOm8QF19VyEs9oA7OEpeOEn1DeI9wGhWrtXeuqq%2FSMn3ylkawfTcYxcagKd0ahAQfqmF0xVcjAlG1lKMWapJ7myIoTz6xyd9j0Wr9ZpPbWwIE7a%2B6Vd6%2FkaPCUoT%2Bxjdvu8XTrFkCeTHnHc6BlaxJAhFPnXI%2Bkom%2FrkmK1VZWoyrtE&X-Amz-Signature=fd8075da1c183d10d80e256ad272f25634dc6591e41bfae0a5445d1312fd6a82&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- **ContentSafety NIM : 부적절한 언어 탐지**
- **TopicControl NIM : 주제에 맞는 질문 제한**
- **RAG Enforcement : 검색 범위 한정**
- **JailbreakDetect NIM : LLM Jailbreak 탐지**
- **PII Detection : 데이터 보호**
# #4 결론

- **NVIDIA NeMo Guardrails와 NIM 마이크로서비스의 역할**
- **안전·보안 모델 3종**
- **적용 효과**

