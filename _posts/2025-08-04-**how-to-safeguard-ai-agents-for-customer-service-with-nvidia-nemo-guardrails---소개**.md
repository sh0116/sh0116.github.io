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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/b6671cd6-6d41-4c3a-a95a-a284fd8a8396/arcitecture-nvidia-nemo-guardrails-intelligent-virtual-ai-assistants-customer-service-2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XG56HWXI%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T072114Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJGMEQCIAOJHtXFJRn6eG%2BolOPSaP7xFvxM75NuU6ddkgkPGzhQAiBGmUrVzuvnB3mGohh8snT%2Bx8BPtrHBgXkj59Ocl5zJHSr%2FAwhAEAAaDDYzNzQyMzE4MzgwNSIMIRQExWfuHhe9uiTXKtwDGgerOwNCyFFBoDyrMaqAg%2BMbNltXxZP%2FwuWTjHoNDEGUN1ee8zm%2FpJFRzMEwXDOFHUrY9OpsLBLllnvrmyp2XkHh%2FoQ6TGjNUHNy79mdNSXpnf286JWEcm3ZVCDX4LajhR8jQ1tzvVHKcOCNMHPAmahQcD%2FJp0O9HTreQZ0SwxrZZfIS8wWlm%2FZVK7giWa2ptFx96EUZbsFdKCBt6FRSbIsTPtN7aKFYhTZ3To5DmMPofr5C6owRIbZBwzFX27lXkNvwgSQTIGaOoEi92pfTCQxGzLcYn3lv%2FVRFMMJ0vDIbsNI5eOlPD7EPvgeAx44ISYS5cqcta9ZL3fuZ6H%2FQpkN8nsCPC3zYY0FyXbdNLC%2F%2Bc3WoonVWVIUKx8CPItpt%2FVH4CyWkcbwAarTyvLqfGk5OCMHXxG0rEkhKdI9iZyfiRN7TbdcCcYuk48gPf6vzVoqyXWBnl5Ga5f%2BeWo7AIBEvxKCloYKpUuGsryeeX9X0kW30Bx2Z90XgYCgVlK4iNAkmQf9eSlRLSDyUtaAwJoomBRVM80S7n6XCTF58miUly9NhqNgXzpM2tZfq4CU9G64AJOiFkDVdyG7oLT5SCRxAxm62t%2B2ZSw4V6eVBcbfQ761wyzomeOE4M1Mw9LfBxAY6pgGSfiY6mcaGXrsOQg2KtAjDUrZ64lNgOniLahWhnUiuHiIBYaCWkseFzT436n8%2B9C4a%2B%2F6DZrbju4durnqm9P3m1fKd3eE5hiNbOazOax%2FAIDC8be%2BGcmJTV4HuhjprDXrdfJ%2F%2BovMd97uTAy0WuTTBtMSgDKJvDigUAo9AaZ%2Bzw7MdF17XuS6GtM%2BDDxLCbqeA%2Br2mnibv3cbrKebYpUViXPaV5n%2FO&X-Amz-Signature=faaa306af13661ad1d803e4cd35d298fd37567a7c4138787980815491ac055bc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

NVIDIA Tech Blog, figure 1

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/e47fdbc0-9809-4a57-929d-89d8c3a76b01/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XG56HWXI%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T072114Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJGMEQCIAOJHtXFJRn6eG%2BolOPSaP7xFvxM75NuU6ddkgkPGzhQAiBGmUrVzuvnB3mGohh8snT%2Bx8BPtrHBgXkj59Ocl5zJHSr%2FAwhAEAAaDDYzNzQyMzE4MzgwNSIMIRQExWfuHhe9uiTXKtwDGgerOwNCyFFBoDyrMaqAg%2BMbNltXxZP%2FwuWTjHoNDEGUN1ee8zm%2FpJFRzMEwXDOFHUrY9OpsLBLllnvrmyp2XkHh%2FoQ6TGjNUHNy79mdNSXpnf286JWEcm3ZVCDX4LajhR8jQ1tzvVHKcOCNMHPAmahQcD%2FJp0O9HTreQZ0SwxrZZfIS8wWlm%2FZVK7giWa2ptFx96EUZbsFdKCBt6FRSbIsTPtN7aKFYhTZ3To5DmMPofr5C6owRIbZBwzFX27lXkNvwgSQTIGaOoEi92pfTCQxGzLcYn3lv%2FVRFMMJ0vDIbsNI5eOlPD7EPvgeAx44ISYS5cqcta9ZL3fuZ6H%2FQpkN8nsCPC3zYY0FyXbdNLC%2F%2Bc3WoonVWVIUKx8CPItpt%2FVH4CyWkcbwAarTyvLqfGk5OCMHXxG0rEkhKdI9iZyfiRN7TbdcCcYuk48gPf6vzVoqyXWBnl5Ga5f%2BeWo7AIBEvxKCloYKpUuGsryeeX9X0kW30Bx2Z90XgYCgVlK4iNAkmQf9eSlRLSDyUtaAwJoomBRVM80S7n6XCTF58miUly9NhqNgXzpM2tZfq4CU9G64AJOiFkDVdyG7oLT5SCRxAxm62t%2B2ZSw4V6eVBcbfQ761wyzomeOE4M1Mw9LfBxAY6pgGSfiY6mcaGXrsOQg2KtAjDUrZ64lNgOniLahWhnUiuHiIBYaCWkseFzT436n8%2B9C4a%2B%2F6DZrbju4durnqm9P3m1fKd3eE5hiNbOazOax%2FAIDC8be%2BGcmJTV4HuhjprDXrdfJ%2F%2BovMd97uTAy0WuTTBtMSgDKJvDigUAo9AaZ%2Bzw7MdF17XuS6GtM%2BDDxLCbqeA%2Br2mnibv3cbrKebYpUViXPaV5n%2FO&X-Amz-Signature=c59aa4d9d290be8f0dc1b38084ef9faea7daf55d806f408867efc36485d9742c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- **ContentSafety NIM : 부적절한 언어 탐지**
- **TopicControl NIM : 주제에 맞는 질문 제한**
- **RAG Enforcement : 검색 범위 한정**
- **JailbreakDetect NIM : LLM Jailbreak 탐지**
- **PII Detection : 데이터 보호**
# #4 결론

- **NVIDIA NeMo Guardrails와 NIM 마이크로서비스의 역할**
- **안전·보안 모델 3종**
- **적용 효과**

