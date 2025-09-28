---
title: "[NVIDIA DCGM Issue]Error starting nv-hostengine: DCGM initialization error"
date: 2025-09-28 22:43:00 +0900
categories: [Trouble Shooting]
tags: [GPU, NVIDIA]
description: 

toc: true
comments: true
---

```scss
Warning #2: dcgm-exporter doesn't have sufficient privileges to expose profiling metrics. To get profiling metrics with dcgm-exporter, use --cap-add SYS_ADMIN
time="2021-12-14T17:28:56Z" level=info msg="Starting dcgm-exporter"
CacheManager Init Failed. Error: -17
time="2021-12-14T17:28:56Z" level=fatal msg="Error starting nv-hostengine: DCGM initialization error"
```

## TL;DR

> dcgm-exporter 실행 시 발생하는 DCGM initialization error #34는 MIG 모드 활성화된 GPU에서 권한 부족으로 인해 발생

## 배경/문제 정의

- **문제 현상**: `nvcr.io/nvidia/k8s/dcgm-exporter` 컨테이너 실행 시 다음 오류 발생
- **환경 조건**:
- **dcgm-exporter 목적**: NVIDIA GPU 상태를 Prometheus로 수집 가능하게 하는 Exporter
## 원인/아키텍처

- DCGM (Data Center GPU Manager)은 NVIDIA GPU의 헬스 및 성능 정보를 제공하는 백엔드 시스템
- `nv-hostengine`는 DCGM의 데몬 프로세스로, GPU와의 로우레벨 통신을 수행함
- **MIG 모드 활성화 시**: DCGM은 MIG 인스턴스를 관리하기 위해 **추가적인 시스템 권한**이 필요
- 기본 Docker 런타임은 이러한 권한을 제한하여, `17` (Permission Denied) 오류 유발 → Error #34 발생
💡

> Error #34는 내부적으로 nv-hostengine이 DCGM 초기화에 실패했음을 의미하며, 이는 MIG 설정과 권한 부족이 복합적으로 작용

## 구현 가이드

### Docker에서 해결

```bash
docker run \
  --gpus all \
  --rm \
  -p 9400:9400 \
  --cap-add=SYS_ADMIN \
  --security-opt seccomp=unconfined \
  nvcr.io/nvidia/k8s/dcgm-exporter:2.3.1-2.6.1-ubuntu20.04
```

### Kubernetes에서 해결

```yaml
securityContext:
  capabilities:
    add:
      - SYS_ADMIN
  seccompProfile:
    type: Unconfined
```

- 위 `securityContext`는 Pod 혹은 Container 수준에서 설정 가능
- MIG 사용 여부에 따라 GPU 리소스 요청 시 MIG-compatible scheduler 사용 필요
## 운영/성능/모니터링

- `-cap-add=SYS_ADMIN`은 높은 권한을 부여하므로, 보안적으로 검토 필요
- `dcgm-exporter`는 GPU 성능/헬스 상태를 `/metrics`로 노출하며, Prometheus 설정 필요
- MIG 인스턴스가 변경되면 `dcgm-exporter` 재시작 권장
## 보안/리스크

⚠️

> SYS_ADMIN 권한은 거의 root 수준이며, 컨테이너 탈출 가능성 등의 보안 위협이 존재

- 가능한 경우 MIG를 비활성화하고 default GPU 모드에서 dcgm-exporter 사용 검토
## 체크리스트

## FAQ

Q: MIG가 꺼져 있으면 이 문제가 발생하지 않나요?

A: 대부분의 경우 MIG가 꺼져 있으면 SYS_ADMIN 권한 없이도 dcgm-exporter가 정상 작동합니다.

Q: `--cap-add=SYS_ADMIN` 없이 MIG 모드에서 실행할 수 있는 방법은 없나요?

A: 현재 DCGM은 MIG 환경에서 로우레벨 접근이 필요하므로 최소 SYS_ADMIN 수준의 권한이 요구됩니다.

Q: MIG를 비활성화하면 GPU 성능에 영향이 있나요?

A: MIG는 GPU 리소스 분할을 위한 기능으로, 단일 워크로드에 GPU를 할당할 경우 불필요합니다.

## 참고

- dcgm-exporter GitHub Issues #158

