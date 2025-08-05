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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/b6671cd6-6d41-4c3a-a95a-a284fd8a8396/arcitecture-nvidia-nemo-guardrails-intelligent-virtual-ai-assistants-customer-service-2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGUUEK7U%2F20250805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250805T002814Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJHMEUCIE5gCh%2FCYopAZKS34wyPPmCPLZlAUTfAHUG7vQXp2ShHAiEAwBbya%2BOPLDEyZ00SPAwrbaycHU2XC3%2F2bfeS5rdt70Aq%2FwMIUBAAGgw2Mzc0MjMxODM4MDUiDDMOB5BYijGDPOjfDyrcA%2FCuJ13N42aHbquPMJfw8X2EE79AmFp8OIA0ATQIQELbJIC8X0znRX1GwZBG2ZiCF5Gxpav7KioAvtqqfpt11O331Ysw%2Fl9W0T6iGRDozZpQQ5Y3QNHNHgQWaE6ikrl%2FYwt3M5cEvVjeRG%2Fcg%2Fc9WTmusOCv61kPnhny39fT2dk8mNgifRoRv50OwwWyj01%2FZzGg8nOtov1ml6KAeYtG%2FeqQySMP73ypDO20V37uiy0R8C%2FVPK5i5JpAd4PeKnNGARaIhx98vLlLitDpfQGcJAqmEjvbtg2Sp1u3cY5vZ1Lw41qiuIqR51Slo%2FgEsTfLDXnJX4JaCy%2FK5FIwijj4xnoDpBh3UcufUpSX2exGlUPNJYARuYk8VrthTCZCXZUrsDKZQ6utZXa7%2FloCc%2FK2ywEdqDsm%2FQ%2FEi0Y5CTZbWiK01S%2B3RTwayj7Gm2QiGVdfRbBAtZPzpIEIErFQkoK6KMkshxija%2BuQ7uYkrEfStJ%2FICjVycIzlhOVYrQw6ws%2B41JEzlnNk1LdWJoQlitVrFDZ8KsPK3f6%2F%2BvAjKK7a5wZuxbZUgt84B0Z0HibxV3pi2CiGCOlnZG2fRyCll9TGpWdCDsq%2BpSxZq4ugNi7LcVnuSpG76kPs3OntxR4dMNP0xMQGOqUB3Maj3ezD%2FQmdvG5blC%2FsgwumQtkZHBeJb7urq2JsH3wER1CURTEzrvf8XFiHQ7Pt1kgmQLkOEAi5EgjhLU1M44PEAcK8UNW%2FIiLWzuGcE2XulPc5%2BNRgbcyQo0%2F3ylyEoHsYTEvnvrG%2F6Y3mv0LkgW01OKypGpXK6eQXMI%2Fqr8nPQS7kgEdh%2BTDGImkqWXY7fWXj%2FsoPGGAUBX6MijiQ7roa1kve&X-Amz-Signature=b281aa4fdd29f9949578e947b1e05144daed7bedc477b71458c8b0464c554a75&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

NVIDIA Tech Blog, figure 1

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/e47fdbc0-9809-4a57-929d-89d8c3a76b01/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGUUEK7U%2F20250805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250805T002814Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJHMEUCIE5gCh%2FCYopAZKS34wyPPmCPLZlAUTfAHUG7vQXp2ShHAiEAwBbya%2BOPLDEyZ00SPAwrbaycHU2XC3%2F2bfeS5rdt70Aq%2FwMIUBAAGgw2Mzc0MjMxODM4MDUiDDMOB5BYijGDPOjfDyrcA%2FCuJ13N42aHbquPMJfw8X2EE79AmFp8OIA0ATQIQELbJIC8X0znRX1GwZBG2ZiCF5Gxpav7KioAvtqqfpt11O331Ysw%2Fl9W0T6iGRDozZpQQ5Y3QNHNHgQWaE6ikrl%2FYwt3M5cEvVjeRG%2Fcg%2Fc9WTmusOCv61kPnhny39fT2dk8mNgifRoRv50OwwWyj01%2FZzGg8nOtov1ml6KAeYtG%2FeqQySMP73ypDO20V37uiy0R8C%2FVPK5i5JpAd4PeKnNGARaIhx98vLlLitDpfQGcJAqmEjvbtg2Sp1u3cY5vZ1Lw41qiuIqR51Slo%2FgEsTfLDXnJX4JaCy%2FK5FIwijj4xnoDpBh3UcufUpSX2exGlUPNJYARuYk8VrthTCZCXZUrsDKZQ6utZXa7%2FloCc%2FK2ywEdqDsm%2FQ%2FEi0Y5CTZbWiK01S%2B3RTwayj7Gm2QiGVdfRbBAtZPzpIEIErFQkoK6KMkshxija%2BuQ7uYkrEfStJ%2FICjVycIzlhOVYrQw6ws%2B41JEzlnNk1LdWJoQlitVrFDZ8KsPK3f6%2F%2BvAjKK7a5wZuxbZUgt84B0Z0HibxV3pi2CiGCOlnZG2fRyCll9TGpWdCDsq%2BpSxZq4ugNi7LcVnuSpG76kPs3OntxR4dMNP0xMQGOqUB3Maj3ezD%2FQmdvG5blC%2FsgwumQtkZHBeJb7urq2JsH3wER1CURTEzrvf8XFiHQ7Pt1kgmQLkOEAi5EgjhLU1M44PEAcK8UNW%2FIiLWzuGcE2XulPc5%2BNRgbcyQo0%2F3ylyEoHsYTEvnvrG%2F6Y3mv0LkgW01OKypGpXK6eQXMI%2Fqr8nPQS7kgEdh%2BTDGImkqWXY7fWXj%2FsoPGGAUBX6MijiQ7roa1kve&X-Amz-Signature=abed97949fce419c06b016791b4dd8b6f47a8f843f91f17df9685fe94f7b4f49&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- **ContentSafety NIM : 부적절한 언어 탐지**
- **TopicControl NIM : 주제에 맞는 질문 제한**
- **RAG Enforcement : 검색 범위 한정**
- **JailbreakDetect NIM : LLM Jailbreak 탐지**
- **PII Detection : 데이터 보호**
# #4 결론

- **NVIDIA NeMo Guardrails와 NIM 마이크로서비스의 역할**
- **안전·보안 모델 3종**
- **적용 효과**

