---
source: knowledge-base
origin: notion
title: "kubectl - 자동 완성 기능"
area: "Kubernetes"
tags: ["area/kubernetes", "tech/kubernetes"]
created: "2025-08-04T06:05:00.000Z"
last_edited: "2025-08-04T06:27:00.000Z"
status: published
public: true
notion_id: "245172a5-56d6-80d5-bec9-df04c3d13a8f"
notion_url: "https://www.notion.so/kubectl-245172a556d680d5bec9df04c3d13a8f"
type: note
updated: 2026-07-07
---

# kubectl - 자동 완성 기능

## 요약

Kubernetes 기초

Kubernetes 큰 주제 아래에서 세부 개념과 실습 절차를 연결하기 위한 노트입니다.

## 핵심 포인트

- Kubernetes 기초
- kubectl 자동완성 활성화 기능
- bash-completion 설치
- alias k = kubectl & 자동완성 기능 실행
- ubuntu버전

## 지식 그래프

- [[wiki/mocs/Knowledge Base|Knowledge Base]]
- [[wiki/mocs/Kubernetes|Kubernetes]]

## 정리 내용

- https://kubernetes.io/ko/docs/tasks/tools/included/optional-kubectl-configs-bash-linux/
### kubectl 자동완성 활성화 기능
~/.bashrc 에 바로 추가함
#### bash-completion 설치
bash-completion은 많은 패키지 관리자에 의해 제공된다([여기](https://github.com/scop/bash-completion#installation) 참고). apt-get install bash-completion 또는 yum install bash-completion 등으로 설치할 수 있다.
위의 명령은 bash-completion의 기본 스크립트인 /usr/share/bash-completion/bash_completion 을 생성한다. 패키지 관리자에 따라, ~/.bashrc 파일에서 이 파일을 수동으로 소스(source)해야 한다.
확인하려면, 셸을 다시 로드하고 type _init_completion 을 실행한다. 명령이 성공하면, 이미 설정된 상태이고, 그렇지 않으면 ~/.bashrc 파일에 다음을 추가한다.
```bash
source /usr/share/bash-completion/bash_completio
```
#### alias k = kubectl & 자동완성 기능 실행
```bash
echo 'source <(kubectl completion bash)' >>~/.bashrc
echo 'alias k=kubectl' >>~/.bashrc
echo 'complete -o default -F __start_kubectl k' >>~/.bashrc
```
### ubuntu버전
```yaml
apt-get install bash-completion
source /usr/share/bash-completion/bash_completion >> ~/.bashrc
echo 'source <(kubectl completion bash)' >>~/.bashrc
echo 'alias k=kubectl' >>~/.bashrc
echo 'complete -o default -F __start_kubectl k' >>~/.bashrc

source ~/.bashrc
```

## 출처

- 원문: https://www.notion.so/kubectl-245172a556d680d5bec9df04c3d13a8f
- Vault path: wiki/notes/kubernetes/kubectl---자동-완성-기능.md
