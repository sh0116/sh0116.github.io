---
source: knowledge-base
origin: notion
title: "Kubernetes - Statefulset"
area: "Kubernetes"
tags: ["area/kubernetes", "tech/kubernetes"]
created: "2025-08-04T06:05:00.000Z"
last_edited: "2025-08-04T06:27:00.000Z"
status: published
public: true
notion_id: "245172a5-56d6-8037-99ca-d112928f3949"
notion_url: "https://www.notion.so/Kubernetes-Statefulset-245172a556d6803799cad112928f3949"
type: note
updated: 2026-07-07
---

# Kubernetes - Statefulset

## 요약

Kubernetes 기초

Kubernetes 큰 주제 아래에서 세부 개념과 실습 절차를 연결하기 위한 노트입니다.

## 핵심 포인트

- Kubernetes 기초
- 스테이트풀셋 Statefulset
- Statefulset의 장점
- Headless서비스 작성 요령
- 정의

## 지식 그래프

- [[wiki/mocs/Knowledge Base|Knowledge Base]]
- [[wiki/mocs/Kubernetes|Kubernetes]]

## 정리 내용

## 스테이트풀셋 Statefulset
- 안정적이고 고유한 네트워크 식별자가 필요한 경우
- 안정적이고 지속적인 스토리지를 사용해야 하는 경우
- 질서 정연한 포드의 배치와 확장을 원하는 경우
  - 이름이 랜덤이 아닌 순서대로 생성됨
- 포드의 자동 롤링 업데이트를 사용하기 원하는 경우
### Statefulset의 장점
- 스테이트풀셋과 곤련된 볼륨은 삭제되지 않음 (관리필요)
- 포드의 스토리지는 PV나 스토리지 클래스로 프로비저닝 수행해야함
- 롤링 업데이트를 수행하는 경우 수동으로 복구해야 할 수 있음
  - 롤링 업데이트 수행 시 기존의 스토리지와 충돌로인해 애플리케이션이 오류가 발생할 수 있다.
- 포드 네트워크 ID를 유지하기 위해 헤드레스(headless)서비스 필
> [!note] 상태를 유지할 수 있다는 장점이 있지만, 포드를 각각 따로 관리해야 한다는 문제점이 동반된다. 따라서 스테이트풀셋을 사용할 건지 디플로이먼트를 사용 할 것인지는 프로젝트 상황에 따라서 달라진다.
### Headless서비스 작성 요령
쿠버네티스 서비스 생성 시 .spec.clusterIP 필드 값을 None으로 설정하면 클러스터 IP가 없는 서비스를 만들 수 있습니다. 이런 서비스를 '헤드리스 서비스(Headless Service)'라고 합니다. 헤드리스 서비스의 경우 클러스터 IP가 할당되지 않고, kube-proxy가 이렇나 서비스를 처리하지 않으며, 로드 밸런싱 또는 프록시 동작을 수행하지 않습니다. DNS가 자동으로 구성되는 방법은 서비스에 셀렉터가 정의되어 있는지 여부에 달려있습니다.
#### 정의
- ClusterIP가 없는 서비스로 단일 진입점이 필요 없을 때 사용
- Service와 연결된 Pod의 endpoint로 DNS 레코드가 생성됨
  - 쿠버네티스 coreDNS에 등록되며 DNS resolving Service로 요청이 가능해진다.
- Pod의 DNS 주소: pod-ip-addr.namespace.pod.cluster.local
```yaml
apiVersion: v1
kind: Service
metadata:
  name: headless-service
spec:
  type: ClusterIP
  clusterIP: None
  selector:
    app: webui
  ports:
  - protocol: TCP
    port: 80
    targetPort: 80
```

## 출처

- 원문: https://www.notion.so/Kubernetes-Statefulset-245172a556d6803799cad112928f3949
- Vault path: wiki/notes/kubernetes/Kubernetes---Statefulset.md
