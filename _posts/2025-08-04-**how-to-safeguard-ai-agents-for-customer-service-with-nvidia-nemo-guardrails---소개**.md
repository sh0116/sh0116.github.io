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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/b6671cd6-6d41-4c3a-a95a-a284fd8a8396/arcitecture-nvidia-nemo-guardrails-intelligent-virtual-ai-assistants-customer-service-2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46622RXKMCF%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T071504Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJIMEYCIQDptuJs4C9s%2BHjGsaDx9lulnRKxZG9jvlQu1TPoFN%2BGTgIhAN4KwZR3Vl7N1nwzPfmASc3WDg26tyk%2FUhoT5yjCV3JxKv8DCEAQABoMNjM3NDIzMTgzODA1IgzFNVzE9Cxkr0kkcEIq3APRzy7AY1bbvM8Atl9SV6DnzfPr%2FCu%2FyAAfCcreIblavPxQrWZRP9oF%2FF%2FXkH2fVlVCn1E0tsmfHtYfpfjstslqixANWfHfoQtV1oTHjmlXGeezinGaVXbiBnAICIdKY3So0HiV%2BMS%2BPbYgQLpaE5R%2BQDfol8sDafQJzmkizHoJjYlEfxTDpyGH%2BNYRoX9m42HkGzlMjtA84PRra2ZniyzflF9DYVuLP9L7P4%2FyVWGKqmWCRjH4QCO9sWos9DZ2K8teherwasTQGGSZUt5p4WhgDTnkvlm0DvBw2qy%2Fr96Qo24xpfxlZn0cGan6PzRNPmOQISJbCPU8WoUiS51ET0gjwiwSUYAZoOD92I3usD8iJoR8eb2%2BkQsWwn6%2B3pBt0zyk2KmJVL2YXqK96xN4U4UHrFp6nYn%2FS0SNhYGYfybkqO%2F7KyG1Nqdu3ZXo5jgdPucsduWXSJUQrWJU6O1gz8ZO%2F1Iu1l%2Fm1HCCQAB01XQVEVkQq3fY2o0M2YMPy08Z4AQ9mBgsW60eDpb2xJebvSFRteKP8Bm3pc5z%2F2aI%2FcVE%2FOYE5wXVu%2BzV1iATTEfOqNiqg7z3ByOZH6V2sFdiwYnC%2B17o3zBoRrehHkBrQyFMKbatcUXTzIjD7d8jvDCYt8HEBjqkARQy8V0ykuXkLtZU59pVkrXVLcH38iQonEOhSozfPUx6lXMN5QpvSUdkZM5VF4c4muyD66srV4C8j7vf96s0DcAtG8sju44e3ZcRKk2jHkrsrPl%2FZxAo8kMKnSA9ZPNaNUfsLJ%2BEW38gPPThS8O5WgCSlWZRYlh0SsmZgBA0sV8eBbp8fbJPoKZMw94v%2FBnc6QVn%2F0BVtEnbMqON53h2b3iflQ%2FQ&X-Amz-Signature=94a05aed2bfbeb514fbf31d486fb2ee7f2fa629a2dfb1d355b6e5285a7ace0e9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

NVIDIA Tech Blog, figure 1

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/e47fdbc0-9809-4a57-929d-89d8c3a76b01/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46622RXKMCF%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T071504Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJIMEYCIQDptuJs4C9s%2BHjGsaDx9lulnRKxZG9jvlQu1TPoFN%2BGTgIhAN4KwZR3Vl7N1nwzPfmASc3WDg26tyk%2FUhoT5yjCV3JxKv8DCEAQABoMNjM3NDIzMTgzODA1IgzFNVzE9Cxkr0kkcEIq3APRzy7AY1bbvM8Atl9SV6DnzfPr%2FCu%2FyAAfCcreIblavPxQrWZRP9oF%2FF%2FXkH2fVlVCn1E0tsmfHtYfpfjstslqixANWfHfoQtV1oTHjmlXGeezinGaVXbiBnAICIdKY3So0HiV%2BMS%2BPbYgQLpaE5R%2BQDfol8sDafQJzmkizHoJjYlEfxTDpyGH%2BNYRoX9m42HkGzlMjtA84PRra2ZniyzflF9DYVuLP9L7P4%2FyVWGKqmWCRjH4QCO9sWos9DZ2K8teherwasTQGGSZUt5p4WhgDTnkvlm0DvBw2qy%2Fr96Qo24xpfxlZn0cGan6PzRNPmOQISJbCPU8WoUiS51ET0gjwiwSUYAZoOD92I3usD8iJoR8eb2%2BkQsWwn6%2B3pBt0zyk2KmJVL2YXqK96xN4U4UHrFp6nYn%2FS0SNhYGYfybkqO%2F7KyG1Nqdu3ZXo5jgdPucsduWXSJUQrWJU6O1gz8ZO%2F1Iu1l%2Fm1HCCQAB01XQVEVkQq3fY2o0M2YMPy08Z4AQ9mBgsW60eDpb2xJebvSFRteKP8Bm3pc5z%2F2aI%2FcVE%2FOYE5wXVu%2BzV1iATTEfOqNiqg7z3ByOZH6V2sFdiwYnC%2B17o3zBoRrehHkBrQyFMKbatcUXTzIjD7d8jvDCYt8HEBjqkARQy8V0ykuXkLtZU59pVkrXVLcH38iQonEOhSozfPUx6lXMN5QpvSUdkZM5VF4c4muyD66srV4C8j7vf96s0DcAtG8sju44e3ZcRKk2jHkrsrPl%2FZxAo8kMKnSA9ZPNaNUfsLJ%2BEW38gPPThS8O5WgCSlWZRYlh0SsmZgBA0sV8eBbp8fbJPoKZMw94v%2FBnc6QVn%2F0BVtEnbMqON53h2b3iflQ%2FQ&X-Amz-Signature=bd1af1c4b5d757adacd045332566e641f95865424394f4ba9689e03e6e4ee1ab&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- **ContentSafety NIM : 부적절한 언어 탐지**
- **TopicControl NIM : 주제에 맞는 질문 제한**
- **RAG Enforcement : 검색 범위 한정**
- **JailbreakDetect NIM : LLM Jailbreak 탐지**
- **PII Detection : 데이터 보호**
# #4 결론

- **NVIDIA NeMo Guardrails와 NIM 마이크로서비스의 역할**
- **안전·보안 모델 3종**
- **적용 효과**

