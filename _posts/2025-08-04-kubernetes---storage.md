---
title: "Kubernetes - Storage"
date: 2025-08-04 06:05:00 +0900
categories: [kubernetes]
tags: [Kubernetes]
description: Kubernetes 기초
toc: true
comments: true
---

# 쿠버네티스 Storage 개념

### 불륨(Volume)

- 컨테이너가 외부 스토리지에 엑세스하고 공유하는 방법
- POD의 컨테이너에는 고유의 분리된 파일 시스템이 존재
- Volume은 POD의 컴포넌트이며 POD의 스펙에 의해 정의
- 독립적인 쿠버네티스의 오브젝트가 아니며 스스로 생성, 삭제 불가
- 각 컨테이너의 파일 시스템의 불륨을 마운트하여 생성
![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/d08779ff-3c8c-4b96-8118-7844ca4a7e40/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665X7DVEQD%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T072030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIQCvAFrThKOUteQACqkUqtPMV4ybyaS0n1tEy61GZ0GC5gIgGwfyv3aRarRJQU4vs8T%2BGED0l5Xj7adLtc%2ByaiY1G1Uq%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDFJu9k1OjnMy7CDeiSrcAx76GJPrvQC%2Bkui2YF2u1p%2FJDG7idW27ByyWtnDR5d%2BFgYyZhBqGErIX%2Bd%2FFvT9mRI1REk3W9XBrJPV0tmonkC5h32Xgu5GT8153gI%2B3PVrHYAQ9gtis5aVP9zTBy%2F5P9vpWLVvqPfxXbLo%2FHsJi22k3a7soG1mpqqBO9ge%2Fj%2BaiSOYbu5M7pE0OquRjUEjayWS8rAOEgcruFGS%2B%2FXea1DvO%2BzFAi97LiB94EuonsJ65%2BWv6hGr0wQsBX9q53MK4dTwTOILVHK%2F1vMBU30aG%2FZsqHJ7nZ0dnMQusWXYlJkZJojYZgxNjoZX0x7sQgNrUlWsVYK%2BaZU4rSGG0DY%2FOVEWOKBExXlqaR5%2F1UbiqMh039Y9bA0N%2F%2Bbpc10StMsqdQgMzVI32qR9CRmOHPby25hai8AsXJRAKXeQVxiGhNB5DCfZmcesor8vPenUkNv%2BIAuOFe%2FyF9W8pzGTNV6g1Q1pWZuANaJWQWRZca%2FkT25UZHQL830vc1JqW7EQueXFPDsvbrISq9Whw9qyoRIVehLR%2FqHi%2FhiTrR%2BX5F9sqBP7YDIUU1nE%2BCymwDsZBjKgDlzbjKo6hcrnWq7GwAEEjDR9yrv3KE5s%2BeLg%2BtInTqAVn4tpRIHYJCNfi7cwSMKO3wcQGOqUBMe6CDAsEbEGdvnG4ctrfeCjoC7bVDq281eK9xF53sNiZn%2Bnq6BICOUc3%2FSWZnaEgfe1nssCE6gm3nPmroS7k%2BBUHa%2FDvwSyFHnSiEmfgc4KdEWimspQYU69t%2Ff1SYrmAjACzz6%2FKrCzludmla5mIWQypbHxWIpwy%2BytrYtWvKIKTyufZXlDnqFH%2B%2BxnhCDwV%2FdqyBq9ULtMYx4h9GqpceL%2FcyxiA&X-Amz-Signature=3823123535469aae2cecfd8209f158828819bca6f468e61e12f096cdb3525ab9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 임시 볼륨 : 
- 로컬 볼륨 :
- 네트워크 볼륨 :
- 네트워크 볼륨 (클라우드 종속) :
# EmptyDir 을 활용한 파일 시스템 공유

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/0fd040f0-b611-4ac4-887d-76487068320b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665X7DVEQD%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T072030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIQCvAFrThKOUteQACqkUqtPMV4ybyaS0n1tEy61GZ0GC5gIgGwfyv3aRarRJQU4vs8T%2BGED0l5Xj7adLtc%2ByaiY1G1Uq%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDFJu9k1OjnMy7CDeiSrcAx76GJPrvQC%2Bkui2YF2u1p%2FJDG7idW27ByyWtnDR5d%2BFgYyZhBqGErIX%2Bd%2FFvT9mRI1REk3W9XBrJPV0tmonkC5h32Xgu5GT8153gI%2B3PVrHYAQ9gtis5aVP9zTBy%2F5P9vpWLVvqPfxXbLo%2FHsJi22k3a7soG1mpqqBO9ge%2Fj%2BaiSOYbu5M7pE0OquRjUEjayWS8rAOEgcruFGS%2B%2FXea1DvO%2BzFAi97LiB94EuonsJ65%2BWv6hGr0wQsBX9q53MK4dTwTOILVHK%2F1vMBU30aG%2FZsqHJ7nZ0dnMQusWXYlJkZJojYZgxNjoZX0x7sQgNrUlWsVYK%2BaZU4rSGG0DY%2FOVEWOKBExXlqaR5%2F1UbiqMh039Y9bA0N%2F%2Bbpc10StMsqdQgMzVI32qR9CRmOHPby25hai8AsXJRAKXeQVxiGhNB5DCfZmcesor8vPenUkNv%2BIAuOFe%2FyF9W8pzGTNV6g1Q1pWZuANaJWQWRZca%2FkT25UZHQL830vc1JqW7EQueXFPDsvbrISq9Whw9qyoRIVehLR%2FqHi%2FhiTrR%2BX5F9sqBP7YDIUU1nE%2BCymwDsZBjKgDlzbjKo6hcrnWq7GwAEEjDR9yrv3KE5s%2BeLg%2BtInTqAVn4tpRIHYJCNfi7cwSMKO3wcQGOqUBMe6CDAsEbEGdvnG4ctrfeCjoC7bVDq281eK9xF53sNiZn%2Bnq6BICOUc3%2FSWZnaEgfe1nssCE6gm3nPmroS7k%2BBUHa%2FDvwSyFHnSiEmfgc4KdEWimspQYU69t%2Ff1SYrmAjACzz6%2FKrCzludmla5mIWQypbHxWIpwy%2BytrYtWvKIKTyufZXlDnqFH%2B%2BxnhCDwV%2FdqyBq9ULtMYx4h9GqpceL%2FcyxiA&X-Amz-Signature=b71de711acac2980472b6b6bbcfe3ff87c35738c4c9efd03dd3b02c1b2d1130e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## EmptyDir 연습문제

- 하나의 프로세스는 랜덤한 값을 생성 (count 이미지 사용)
- 하나의 프로세스는 랜덤한 값을 출력 (httpd이미지 사용)

