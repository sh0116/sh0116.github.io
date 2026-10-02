---
source: knowledge-base
origin: notion
title: "Kubernetes - Label & Seletetor "
area: "Kubernetes"
tags: ["area/kubernetes", "tech/kubernetes"]
created: "2025-08-04T06:05:00.000Z"
last_edited: "2025-08-04T06:27:00.000Z"
status: published
public: true
notion_id: "245172a5-56d6-800b-aa55-cb822e39af42"
notion_url: "https://www.notion.so/Kubernetes-Label-Seletetor-245172a556d6800baa55cb822e39af42"
type: note
updated: 2026-07-07
---

# Kubernetes - Label & Seletetor 

## 요약

Kubernetes 기초

Kubernetes 큰 주제 아래에서 세부 개념과 실습 절차를 연결하기 위한 노트입니다.

## 핵심 포인트

- Kubernetes 기초
- 레이블 Lable
- 레이블이란?
- 레이블을 이용한 포드 구성 ( 가로 app / 세로 rel )
- 레이블 생성 방법

## 지식 그래프

- [[wiki/mocs/Knowledge Base|Knowledge Base]]
- [[wiki/mocs/Kubernetes|Kubernetes]]

## 정리 내용

### 레이블 Lable
#### 레이블이란?
- 모든 리소스를 구성하는 매우 간단하면서도 강력한 쿠버네티스 기능
- 리소스에 첨부하는 임의의 키/값 쌍 (app: test)
- 레이블 셀렉터를 사용하면 각종 리소스를 필터링하여 선택할 수 있음
- 리소스는 한개 이상의 레이블을 가질수 있음
- 리소스를 만드는 시점에 레이블을 첨부
- 기존 리소스에도 레이블의 값 수정, 추가 가능
- 모든 사람이 쉽게 이해할 수 있는 체계적인 시스템을 구축 가능
  - app : 애플리케이션 구성요소, 마이크로 서비스 유형 지정
  - rel : 애플리케이션의 버전 지정 (release)
#### 레이블을 이용한 포드 구성 ( 가로 app / 세로 rel )
![[_attachments/notion/Kubernetes---Label-&-Seletetor/245172a556d6812c8e0ffdc12dddcbed.png]]
### 레이블 생성 방법
```go
yaml 파일 생성 후 
kubectl create -f 파일
```

![[_attachments/notion/Kubernetes---Label-&-Seletetor/245172a556d68198a6d7ebf15fb03c5d.png]]
```go
kubectl label pod 파드명 test=pod
```
> 신규 레이블 추가
```go
kubectl label pod 파드명 test=pod --overwrite
```
> 기존 레이블 수정
### 레이블 필터링하여 검색
```bash
kubectl get pod --show-labels   #labels 컬럼 생성
kubectl get pod -L app,rel      #app, rel key값을 컬럼으로 정렬

# 셀렉터를 통해 라벨을 식별하고 조회한다
kubectl get pod --show-labels -l 'env'  # 필터링
kubectl get pod --show-labels -l '!env' # not 필터링
kubectl get pod --show-labels -l 'env!=test' # key/value 비교
kubectl get pod --show-labels -l 'env!=test,rel=beta' # and연산
kubectl get pod --show-labels -l 'env in (test)' # key/value 비교
```
### 확장 가능한 쿠버네티스 레이블 예제 - 네이밍
![[_attachments/notion/Kubernetes---Label-&-Seletetor/245172a556d6811a886fdc2e2ceaf751.png]]
### 셀렉터 공식 문서 (일치성 기준 요건)
펼치기
#### 일치성 기준 요건
  일치성 기준 또는 불일치 기준 의 요구사항으로 레이블의 키와 값의 필터링을 허용한다. 일치하는 오브젝트는 추가 레이블을 가질 수 있지만, 레이블의 명시된 제약 조건을 모두 만족해야 한다. =,==,!= 이 세 가지 연산자만 허용한다. 처음 두 개의 연산자의 일치성(그리고 동의어), 나머지는 불일치 를 의미한다. 예를 들면,
  ```plain text
environment = production
tier != frontend

  ```
  전자는 environment를 키로 가지는 것과 production을 값으로 가지는 모든 리소스를 선택한다. 후자는 tier를 키로 가지고, 값을 frontend를 가지는 리소스를 제외한 모든 리소스를 선택하고, tier를 키로 가지며, 값을 공백으로 가지는 모든 리소스를 선택한다. environment=production,tier!=frontend 처럼 쉼표를 통해 한 문장으로 frontend를 제외한 production을 필터링할 수 있다.
  일치성 기준 레이블 요건에 대한 하나의 이용 시나리오는 파드가 노드를 선택하는 기준을 지정하는 것이다. 예를 들어, 아래 샘플 파드는 "accelerator=nvidia-tesla-p100" 레이블을 가진 노드를 선택한다.
  ```bash
apiVersion: v1
kind: Pod
metadata:
  name: cuda-test
spec:
  containers:
    - name: cuda-test
      image: "k8s.gcr.io/cuda-vector-add:v0.1"
      resources:
        limits:
          nvidia.com/gpu: 1
  nodeSelector:
    accelerator: nvidia-tesla-p100
  ```
#### 집합성 기준 요건
  집합성 기준 레이블 요건에 따라 값 집합을 키로 필터링할 수 있다. in,notin과 exists(키 식별자만 해당)의 3개의 연산자를 지원한다. 예를 들면,
  ```plain text
environment in (production, qa)
tier notin (frontend, backend)
partition
!partition

  ```
  - 첫 번째 예시에서 키가 environment이고 값이 production 또는 qa인 모든 리소스를 선택한다.
  - 두 번째 예시에서 키가 tier이고 값이 frontend와 backend를 가지는 리소스를 제외한 모든 리소스와 키로 tier를 가지고 값을 공백으로 가지는 모든 리소스를 선택한다.
  - 세 번째 예시에서 레이블의 값에 상관없이 키가 partition을 포함하는 모든 리소스를 선택한다.
  - 네 번째 예시에서 레이블의 값에 상관없이 키가 partition을 포함하지 않는 모든 리소스를 선택한다.
  마찬가지로 쉼표는 AND 연산자로 작동한다. 따라서 partition,environment notin (qa)와 같이 사용하면 값과 상관없이 키가 partition인 것과 키가 environment이고 값이 qa와 다른 리소스를 필터링할 수 있다. 집합성 기준 레이블 셀렉터는 일반적으로 environment=production과 environment in (production)을 같은 것으로 본다. 유사하게는 !=과 notin을 같은 것으로 본다.
  집합성 기준 요건은 일치성 기준 요건과 조합해서 사용할 수 있다. 예를 들어 partition in (customerA, customerB),environment!=qa
### API
#### LIST와 WATCH 필터링
  LIST와 WATCH 작업은 쿼리 파라미터를 사용해서 반환되는 오브젝트 집합을 필터링하기 위해 레이블 셀렉터를 지정할 수 있다. 다음의 두 가지 요건 모두 허용된다(URL 쿼리 문자열을 그대로 표기함).
  - 일치성 기준 요건: 
  ```bash
?labelSelector=environment%3Dproduction,tier%3Dfrontend
  ```
  - 집합성 기준 요건: 
  ```bash
?labelSelector=environment+in+%28production%2Cqa%29%2Ctier+in+%28frontend%29
  ```
  두 가지 레이블 셀렉터 스타일은 모두 REST 클라이언트를 통해 선택된 리소스를 확인하거나 목록을 볼 수 있다. 예를 들어, kubectl로 apiserver를 대상으로 일치성 기준 으로 하는 셀렉터를 다음과 같이 이용할 수 있다.
  ```bash
kubectl get pods -l environment=production,tier=frontend
  ```
  또는 집합성 기준 요건을 사용하면
  ```bash
kubectl get pods -l 'environment in (production),tier in (frontend)'
  ```
  앞서 안내한 것처럼 집합성 기준 요건은 더 보여준다. 예시에서 다음과 같이 OR 연산자를 구현할 수 있다.
  ```bash
kubectl get pods -l 'environment in (production, qa)'
  ```
  또는 exists 연산자에 불일치한 것으로 제한할 수 있다.
  ```bash
kubectl get pods -l 'environment,environment notin (frontend)'
  ```
### 레이블과 셀렉터 연습문제
- YAML 파일을 사용하여 app=nginx 레이블을 가진 포드를 생성하라.
- app=nginx를 가진 포드를 get하라
- get된 포드의 레이블의 app을 확인하라
- app=nginx레이블을 가진 포드에 team=dev1레이블을 추가하라
#### YAML 파일을 사용하여 app=nginx 레이블을 가진 포드를 생성하라.
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: practice-labels
  labels:
    app: nginx
spec:
  containers:
  - name: prac-nginx
    image: nginx
    ports:
    - containerPort: 8080
      protocol: TCP
```
#### app=nginx를 가진 포드를 get하라
```bash
kubectl get pod --show-labels -l 'app=nginx'
```
#### get된 포드의 레이블의 app을 확인하라
```bash
kubectl get pod -L app
```
#### app=nginx레이블을 가진 포드에 team=dev1레이블을 추가하라
```bash
kubectl label pod pod명 team=dev1 (만약 덮어쓰기면 --overwrite)
kubectl get pod -L app,team
```

## 출처

- 원문: https://www.notion.so/Kubernetes-Label-Seletetor-245172a556d6800baa55cb822e39af42
- Vault path: wiki/notes/kubernetes/Kubernetes---Label-&-Seletetor.md
