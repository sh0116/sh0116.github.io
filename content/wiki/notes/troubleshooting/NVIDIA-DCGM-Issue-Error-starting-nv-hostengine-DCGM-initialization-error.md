---
source: knowledge-base
origin: notion
title: "[NVIDIA DCGM Issue]Error starting nv-hostengine: DCGM initialization error"
area: "트러블슈팅"
tags: ["area/troubleshooting", "hardware/gpu", "type/troubleshooting", "vendor/nvidia"]
created: "2025-09-28T22:43:00.000Z"
last_edited: "2025-09-28T22:47:00.000Z"
status: published
public: true
notion_id: "27c172a5-56d6-8079-bc9d-d282e61053ed"
notion_url: "https://www.notion.so/NVIDIA-DCGM-Issue-Error-starting-nv-hostengine-DCGM-initialization-error-27c172a556d68079bc9dd282e61053ed"
type: note
updated: 2026-07-07
---

# [NVIDIA DCGM Issue]Error starting nv-hostengine: DCGM initialization error

## 요약

해결 절차를 블로그 글감으로 발전시키기 위한 트러블슈팅 노트입니다.

## 핵심 포인트

- 문제 현상: nvcr.io/nvidia/k8s/dcgm-exporter 컨테이너 실행 시 다음 오류 발생
- TL;DR
- 배경/문제 정의
- 원인/아키텍처
- 구현 가이드

## 지식 그래프

- [[wiki/mocs/Knowledge Base|Knowledge Base]]
- [[wiki/mocs/트러블슈팅|트러블슈팅]]

## 정리 내용

```scss
Warning #2: dcgm-exporter doesn't have sufficient privileges to expose profiling metrics. To get profiling metrics with dcgm-exporter, use --cap-add SYS_ADMIN
time="2021-12-14T17:28:56Z" level=info msg="Starting dcgm-exporter"
CacheManager Init Failed. Error: -17
time="2021-12-14T17:28:56Z" level=fatal msg="Error starting nv-hostengine: DCGM initialization error"
```
### TL;DR
> dcgm-exporter 실행 시 발생하는 DCGM initialization error #34는 MIG 모드 활성화된 GPU에서 권한 부족으로 인해 발생
  Docker 컨테이너에 SYS_ADMIN 권한 부여(--cap-add=SYS_ADMIN) 및 seccomp=unconfined 설정으로 해결 가능
  Kubernetes 환경에서는 securityContext에 해당 권한 추가 필요
### 배경/문제 정의
- 문제 현상: nvcr.io/nvidia/k8s/dcgm-exporter 컨테이너 실행 시 다음 오류 발생
  ```plain text
Error starting nv-hostengine: DCGM initialization error #34

  ```
- 환경 조건:
  - NVIDIA A100 GPU (MIG 모드 일부 활성화)
  - Docker 환경 (Ubuntu 20.04, AMD CPU)
  - 드라이버 버전 495.29.05, CUDA 11.5
- dcgm-exporter 목적: NVIDIA GPU 상태를 Prometheus로 수집 가능하게 하는 Exporter
### 원인/아키텍처
- DCGM (Data Center GPU Manager)은 NVIDIA GPU의 헬스 및 성능 정보를 제공하는 백엔드 시스템
- nv-hostengine는 DCGM의 데몬 프로세스로, GPU와의 로우레벨 통신을 수행함
- MIG 모드 활성화 시: DCGM은 MIG 인스턴스를 관리하기 위해 추가적인 시스템 권한이 필요
- 기본 Docker 런타임은 이러한 권한을 제한하여, 17 (Permission Denied) 오류 유발 → Error #34 발생
💡
> Error #34는 내부적으로 nv-hostengine이 DCGM 초기화에 실패했음을 의미하며, 이는 MIG 설정과 권한 부족이 복합적으로 작용
### 구현 가이드
#### Docker에서 해결
```bash
docker run \
  --gpus all \
  --rm \
  -p 9400:9400 \
  --cap-add=SYS_ADMIN \
  --security-opt seccomp=unconfined \
  nvcr.io/nvidia/k8s/dcgm-exporter:2.3.1-2.6.1-ubuntu20.04
```
#### Kubernetes에서 해결
```yaml
securityContext:
  capabilities:
    add:
      - SYS_ADMIN
  seccompProfile:
    type: Unconfined
```
- 위 securityContext는 Pod 혹은 Container 수준에서 설정 가능
- MIG 사용 여부에 따라 GPU 리소스 요청 시 MIG-compatible scheduler 사용 필요
### 운영/성능/모니터링
- -cap-add=SYS_ADMIN은 높은 권한을 부여하므로, 보안적으로 검토 필요
- dcgm-exporter는 GPU 성능/헬스 상태를 /metrics로 노출하며, Prometheus 설정 필요
- MIG 인스턴스가 변경되면 dcgm-exporter 재시작 권장
### 보안/리스크
⚠️
> SYS_ADMIN 권한은 거의 root 수준이며, 컨테이너 탈출 가능성 등의 보안 위협이 존재
  따라서 신뢰할 수 있는 노드에서만 적용하거나, 노드 격리를 고려해야 함
- 가능한 경우 MIG를 비활성화하고 default GPU 모드에서 dcgm-exporter 사용 검토
### 체크리스트
- [x] MIG 모드 사용 여부 확인 (nvidia-smi)
- [x] Docker 컨테이너에 SYS_ADMIN 권한 부여
- [x] seccomp profile 해제 (unconfined)
- [ ] Kubernetes 배포 시 securityContext 설정 반영
- [ ] Prometheus와 연동 테스트 완료
### FAQ
Q: MIG가 꺼져 있으면 이 문제가 발생하지 않나요?
A: 대부분의 경우 MIG가 꺼져 있으면 SYS_ADMIN 권한 없이도 dcgm-exporter가 정상 작동합니다.
Q: --cap-add=SYS_ADMIN 없이 MIG 모드에서 실행할 수 있는 방법은 없나요?
A: 현재 DCGM은 MIG 환경에서 로우레벨 접근이 필요하므로 최소 SYS_ADMIN 수준의 권한이 요구됩니다.
Q: MIG를 비활성화하면 GPU 성능에 영향이 있나요?
A: MIG는 GPU 리소스 분할을 위한 기능으로, 단일 워크로드에 GPU를 할당할 경우 불필요합니다.
### 참고
- [dcgm-exporter GitHub Issues #158](https://github.com/NVIDIA/dcgm-exporter/issues/158)

## 출처

- 원문: https://www.notion.so/NVIDIA-DCGM-Issue-Error-starting-nv-hostengine-DCGM-initialization-error-27c172a556d68079bc9dd282e61053ed
- Vault path: wiki/notes/troubleshooting/NVIDIA-DCGM-Issue-Error-starting-nv-hostengine-DCGM-initialization-error.md
