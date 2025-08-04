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
![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/d08779ff-3c8c-4b96-8118-7844ca4a7e40/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VM6NDHFA%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T072157Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJIMEYCIQCWIMW3oUmhhquja4oc7ZJZlVvs8gB2DPUGSQNktsEmOwIhAL8FcrkJlf3pqjOBtqLEeQE%2BpYgJ%2B6ASr6aZvECoAf0uKv8DCEAQABoMNjM3NDIzMTgzODA1Igxqd3Gm8Uqcj6iM8bUq3AM9P4UzDH4MF%2FxY5S3wkuffTWeP3RZz7MBTjaoeLCl4V8Zu4Q2PI6HMPoPavuY5HBIKiusiL0cKZnx6jN20knqWhhuaEgmPWs4%2FaTTQaMWyFmBc42VgPkVE16rphwe%2F0FlwD7Rd4dTIfwfVyeeeSHp0aSxsFs51o4lxK%2Bf0blMMUrd%2BhOFY6jyQHu1z%2FpmSMogIJ1shP%2F3d5MxmakusP%2FccnzO7lGvrOPBKAaaPMnQIQeSAjovjV4%2FpHtRs89avXIIt%2FggZBGPE09%2BHrdTpkRDVFvSFBSGAU4yuMSNUK4XDC4MfXZ2f7zZAlnsGUKYE%2FBLH9GbYSpqwWqLfz%2FScfK5Xqg9VwUMHhaJbTUk7qD2ck8%2BtX5Kk5xa5OElZi8TfI3GOTFf6GM5P7yay6dyQnGlDf6alOVqLeJLBScVGsjl6zxExn3J%2FOFbG2AmWlnzJgAo20d7Cap%2FekvqhVmnaxKd3Tref4xLksKDXK4GOuLDfdzZFHbJSSNcMabtkF%2BBM5xzWgpspEmPpOVQpibgEc09GYn5BAQW7TYunnbg%2BVh6HEgxp1AKud9OAcLJwx%2F05KcI0K5nAw4CQylkqyWq%2BMYYJN9XkOPY%2F2lT4bKYsgUwx%2BYf5yVIYoK%2FHvW5UMjDAt8HEBjqkAcdwuWd%2FykF%2B2Egl78tSBN6HEntkqtOINsSqHRU5CPbLOYTrcBWJALmD5UcKqPUi39pTNlwyV4xTftUJ5WJWV8Ok3J0trIT9%2BZZN1d4J3vxCJOUieQO93OzIf1tzJFb0E%2FiS2U%2BDqhrakt%2BmtNUkZo2Vd2xZj%2BF%2F0VNkjD8ob%2BR5A%2BigqQCeVn4CtxVs%2B9HiMB9STwlkAZA33L1Y8vo8y84ihglG&X-Amz-Signature=04d0fcdee126b7a4aed8330783a943077ae0f0f9fc9deffc680bbaf0290b3826&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 임시 볼륨 : 
- 로컬 볼륨 :
- 네트워크 볼륨 :
- 네트워크 볼륨 (클라우드 종속) :
# EmptyDir 을 활용한 파일 시스템 공유

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/0fd040f0-b611-4ac4-887d-76487068320b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VM6NDHFA%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T072157Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJIMEYCIQCWIMW3oUmhhquja4oc7ZJZlVvs8gB2DPUGSQNktsEmOwIhAL8FcrkJlf3pqjOBtqLEeQE%2BpYgJ%2B6ASr6aZvECoAf0uKv8DCEAQABoMNjM3NDIzMTgzODA1Igxqd3Gm8Uqcj6iM8bUq3AM9P4UzDH4MF%2FxY5S3wkuffTWeP3RZz7MBTjaoeLCl4V8Zu4Q2PI6HMPoPavuY5HBIKiusiL0cKZnx6jN20knqWhhuaEgmPWs4%2FaTTQaMWyFmBc42VgPkVE16rphwe%2F0FlwD7Rd4dTIfwfVyeeeSHp0aSxsFs51o4lxK%2Bf0blMMUrd%2BhOFY6jyQHu1z%2FpmSMogIJ1shP%2F3d5MxmakusP%2FccnzO7lGvrOPBKAaaPMnQIQeSAjovjV4%2FpHtRs89avXIIt%2FggZBGPE09%2BHrdTpkRDVFvSFBSGAU4yuMSNUK4XDC4MfXZ2f7zZAlnsGUKYE%2FBLH9GbYSpqwWqLfz%2FScfK5Xqg9VwUMHhaJbTUk7qD2ck8%2BtX5Kk5xa5OElZi8TfI3GOTFf6GM5P7yay6dyQnGlDf6alOVqLeJLBScVGsjl6zxExn3J%2FOFbG2AmWlnzJgAo20d7Cap%2FekvqhVmnaxKd3Tref4xLksKDXK4GOuLDfdzZFHbJSSNcMabtkF%2BBM5xzWgpspEmPpOVQpibgEc09GYn5BAQW7TYunnbg%2BVh6HEgxp1AKud9OAcLJwx%2F05KcI0K5nAw4CQylkqyWq%2BMYYJN9XkOPY%2F2lT4bKYsgUwx%2BYf5yVIYoK%2FHvW5UMjDAt8HEBjqkAcdwuWd%2FykF%2B2Egl78tSBN6HEntkqtOINsSqHRU5CPbLOYTrcBWJALmD5UcKqPUi39pTNlwyV4xTftUJ5WJWV8Ok3J0trIT9%2BZZN1d4J3vxCJOUieQO93OzIf1tzJFb0E%2FiS2U%2BDqhrakt%2BmtNUkZo2Vd2xZj%2BF%2F0VNkjD8ob%2BR5A%2BigqQCeVn4CtxVs%2B9HiMB9STwlkAZA33L1Y8vo8y84ihglG&X-Amz-Signature=02721459508913fc018401609872ea816be67abeb15d9a9977f18fd58bef1169&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## EmptyDir 연습문제

- 하나의 프로세스는 랜덤한 값을 생성 (count 이미지 사용)
- 하나의 프로세스는 랜덤한 값을 출력 (httpd이미지 사용)

