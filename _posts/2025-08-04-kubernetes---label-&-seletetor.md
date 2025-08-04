---
title: "Kubernetes - Label & Seletetor"
date: 2025-08-04 06:05:00 +0900
categories: [kubernetes]
tags: [Kubernetes]
description: Kubernetes 기초
toc: true
comments: true
---

## 레이블 Lable

### 레이블이란?

- 모든 리소스를 구성하는 매우 간단하면서도 강력한 쿠버네티스 기능
- 리소스에 첨부하는 임의의 키/값 쌍 (app: test)
- 레이블 셀렉터를 사용하면 각종 리소스를 필터링하여 선택할 수 있음
- 리소스는 한개 이상의 레이블을 가질수 있음
- 리소스를 만드는 시점에 레이블을 첨부
- 기존 리소스에도 레이블의 값 수정, 추가 가능
- 모든 사람이 쉽게 이해할 수 있는 체계적인 시스템을 구축 가능
### 레이블을 이용한 포드 구성 ( 가로 app / 세로 rel )

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/36ef8101-8194-496b-b5ba-d12aeda22c71/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TKDLBXPR%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T072023Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIFm%2FFL0aFxO7lU8cBtSnV89RLQU4BxdHQCdLTcW%2FXkmJAiEApdAa28mujtmkj%2FGc%2BgtQtLVmrOQhRa%2FWqTLNDoRwGp8q%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDM8zjh32XuD14Rf2zCrcA64KcOC%2BBy0OOi%2FY4no92etgyxi0UIe4QDVHJOgfsjL%2FLMBIKJbBNEAgxF2ByVWL%2Fm3Fnsyhn%2BtnTVrPVPpqd4eOw%2FaemKSUwfXL2ls1B5squfJByDbQ1CILj4QVDIG1Fk5sEocz9XCc1iDcl4NdyljRyX2bHCBcootwKsHe4lvKD2hd%2FmjKlNX8g3wu2nh%2Bbb8K2rxMIO%2BYTL2QbIsZ1wIqwraUTzU87nj3%2FXZM38hvyMj1YCoUh%2Bi%2BoW%2FfP68Ny%2B1vvWxS6q4jkJFWUWuZKcVm6DKsDdIN41A5gdfAC3VAiTtDzfdA2E7MlzwyR4jizAZxChvku1%2FfOWvMSFi8wpJdYoVnC9q8fUANZtbQUm3lP6GxCYaxIBN1%2BsHYveptA0UBgafbqhelQYpv9shsaXiSl01zdVTDlR%2FpqVzoLYvsTkvZu0h0WGpTyRalP56FnbwCvl5x6WoILW%2B0QYJhlbPUba%2BaV%2FddWfqDGmI8tNO%2FdC4t3k4t%2FebyfIun8gsuCoOoY1EVokD36H2eNOpZh%2BmbcprqmkYnb0D9yDKVqHMGSlX5F3m0g3yh%2F8IUSOSUdQ4VM%2BwaQJJRJeccqopzkf2k23UrWG8Ej3sDzkLI81aSfTsykXgbx78xCVW6MOO3wcQGOqUBsI7myflXZ5ZkXovoeTZ914SUf9Wsjbapuk3v8jdOoEGIgPz7iK6NJ%2Fv3ThVdPDRI%2F36RA5fBMRN9I5acNHMpZe%2BlobHGGbxYqaTh6Zj2tGz8namNVV5%2Fjjv%2Bn0HOlIWZ3%2FUzcSzVARFbj9pWxdxtEkN9Z9%2FY5cb3oWb%2Fxmv%2BfQl8Gy4m0RcZ8D2EvXBzjpMq6RFS7n16dj0IWyUEPuNyAQeNzifq&X-Amz-Signature=52142e4b6306c8af87b681cc9ce1a2151a6da819f4b8a796d800b9ff22ec3c74&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 레이블 생성 방법

```go
kubectl label pod 파드명 test=pod
```

> 신규 레이블 추가

```go
kubectl label pod 파드명 test=pod --overwrite
```

> 기존 레이블 수정

## 레이블 필터링하여 검색

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

## 확장 가능한 쿠버네티스 레이블 예제 - 네이밍

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/1cdbb02a-3553-46c6-9579-1a21449b0d12/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TKDLBXPR%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T072024Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIFm%2FFL0aFxO7lU8cBtSnV89RLQU4BxdHQCdLTcW%2FXkmJAiEApdAa28mujtmkj%2FGc%2BgtQtLVmrOQhRa%2FWqTLNDoRwGp8q%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDM8zjh32XuD14Rf2zCrcA64KcOC%2BBy0OOi%2FY4no92etgyxi0UIe4QDVHJOgfsjL%2FLMBIKJbBNEAgxF2ByVWL%2Fm3Fnsyhn%2BtnTVrPVPpqd4eOw%2FaemKSUwfXL2ls1B5squfJByDbQ1CILj4QVDIG1Fk5sEocz9XCc1iDcl4NdyljRyX2bHCBcootwKsHe4lvKD2hd%2FmjKlNX8g3wu2nh%2Bbb8K2rxMIO%2BYTL2QbIsZ1wIqwraUTzU87nj3%2FXZM38hvyMj1YCoUh%2Bi%2BoW%2FfP68Ny%2B1vvWxS6q4jkJFWUWuZKcVm6DKsDdIN41A5gdfAC3VAiTtDzfdA2E7MlzwyR4jizAZxChvku1%2FfOWvMSFi8wpJdYoVnC9q8fUANZtbQUm3lP6GxCYaxIBN1%2BsHYveptA0UBgafbqhelQYpv9shsaXiSl01zdVTDlR%2FpqVzoLYvsTkvZu0h0WGpTyRalP56FnbwCvl5x6WoILW%2B0QYJhlbPUba%2BaV%2FddWfqDGmI8tNO%2FdC4t3k4t%2FebyfIun8gsuCoOoY1EVokD36H2eNOpZh%2BmbcprqmkYnb0D9yDKVqHMGSlX5F3m0g3yh%2F8IUSOSUdQ4VM%2BwaQJJRJeccqopzkf2k23UrWG8Ej3sDzkLI81aSfTsykXgbx78xCVW6MOO3wcQGOqUBsI7myflXZ5ZkXovoeTZ914SUf9Wsjbapuk3v8jdOoEGIgPz7iK6NJ%2Fv3ThVdPDRI%2F36RA5fBMRN9I5acNHMpZe%2BlobHGGbxYqaTh6Zj2tGz8namNVV5%2Fjjv%2Bn0HOlIWZ3%2FUzcSzVARFbj9pWxdxtEkN9Z9%2FY5cb3oWb%2Fxmv%2BfQl8Gy4m0RcZ8D2EvXBzjpMq6RFS7n16dj0IWyUEPuNyAQeNzifq&X-Amz-Signature=c1c8876e17d0a43fb3986151530d3112c959255e6c395968396c00bfefa73608&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 셀렉터 공식 문서 (일치성 기준 요건)

## 레이블과 셀렉터 연습문제

- YAML 파일을 사용하여 app=nginx 레이블을 가진 포드를 생성하라.
- app=nginx를 가진 포드를 get하라
- get된 포드의 레이블의 app을 확인하라
- app=nginx레이블을 가진 포드에 team=dev1레이블을 추가하라
### YAML 파일을 사용하여 app=nginx 레이블을 가진 포드를 생성하라.

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

### app=nginx를 가진 포드를 get하라

```bash
kubectl get pod --show-labels -l 'app=nginx'
```

### get된 포드의 레이블의 app을 확인하라

```bash
kubectl get pod -L app
```

### app=nginx레이블을 가진 포드에 team=dev1레이블을 추가하라

```bash
kubectl label pod pod명 team=dev1 (만약 덮어쓰기면 --overwrite)
kubectl get pod -L app,team
```


