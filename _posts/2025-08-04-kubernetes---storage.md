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
![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/d08779ff-3c8c-4b96-8118-7844ca4a7e40/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TRTZ363L%2F20250805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250805T002714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJGMEQCIEqVzZjZxFeuI%2FdLAv%2Fn6neFHbeVEszttuwyYqNAAXEKAiAcf0zrMF0JKy0H8kTa%2FoqshUesRS%2F0vStUe2geaeZyCCr%2FAwhQEAAaDDYzNzQyMzE4MzgwNSIMaMk4oYwd%2F4pePDp2KtwDxcjbkB4u4NoKGgbK3N0NLz0LuVfSIornKsqu1GFV9p9x44oK2clkeA4M%2FYD4%2Bw4U%2FZqUlzqVO%2B6xBYiH4PJ9w1D2w4qf3LSln1bi5eD%2Fkj3%2BKoDytUnAeyVRl3kmo2RBUbDAQqmlgic9p2X4bZtVp20fkISoys%2FftTVM2zolGLLCre9L8u1t5HcSBMysPexVPXtN7jOZcQGQPC6gsA6ccfcfPI6bdOhvfachuCt3usfC%2F8VF6%2B2ZK1e2tamvhnYYbVgNXVzfwGZGdCOmD7L8pSiIOn4N3lPjvb7I689vPt5rSnU5ovUJZHy3xYHbJHkR85lUd%2F0zmJB%2F7CEw3q5zhk%2BMBiURAib5yeQmL9DFi9elJpmuGXVdB1QX4O3G%2B9BLa36O4PWjnOgvQZNFDcinKTIwFbRbNtg0R3JA2xpzrhbYe94dEvXG40iunneKdkFLlcrYJHiFjfwEqJTRutk7asxF402ef%2BWHt17SbU1jXo0aWXCgb3hl9CO14HAHtGA0x4owXKoxnYEK6l4MGz8jGsHZlu9ip4FE047g8SSbX7oH3WQByavfYekooFS2aWJYyWyK56S5FkolOUStJOGdDPfSj7TwX13tdkHXnppokc5o2HluPGo87l73ASMwqvTExAY6pgGH%2F5Z2Zj0IC1VXH5ompDDKRKgklHp0Axh%2BzewENMPLTqKQoqnc%2BfuWCmOrpH5EkqjIrjlyAqT471rPSc1URTnA9a0k%2F3Xj342v6Or1%2F56fnLsMitZWHyNolg7KqyVFMom5I0Vdi7hWzH6EZo%2BbOlKUEWX7vFiztn%2FosuXXls5godP06FU5YWM%2B7n6TJp6R1PisoKrcOKd%2FKdpG%2BoN%2Bx%2BAbc5OpaD7B&X-Amz-Signature=17151fa7d4960f7fb131637c964ee0d3c30e55433cb831b8e9c317fe0c8db2db&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 임시 볼륨 : 
- 로컬 볼륨 :
- 네트워크 볼륨 :
- 네트워크 볼륨 (클라우드 종속) :
# EmptyDir 을 활용한 파일 시스템 공유

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/0fd040f0-b611-4ac4-887d-76487068320b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TRTZ363L%2F20250805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250805T002714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJGMEQCIEqVzZjZxFeuI%2FdLAv%2Fn6neFHbeVEszttuwyYqNAAXEKAiAcf0zrMF0JKy0H8kTa%2FoqshUesRS%2F0vStUe2geaeZyCCr%2FAwhQEAAaDDYzNzQyMzE4MzgwNSIMaMk4oYwd%2F4pePDp2KtwDxcjbkB4u4NoKGgbK3N0NLz0LuVfSIornKsqu1GFV9p9x44oK2clkeA4M%2FYD4%2Bw4U%2FZqUlzqVO%2B6xBYiH4PJ9w1D2w4qf3LSln1bi5eD%2Fkj3%2BKoDytUnAeyVRl3kmo2RBUbDAQqmlgic9p2X4bZtVp20fkISoys%2FftTVM2zolGLLCre9L8u1t5HcSBMysPexVPXtN7jOZcQGQPC6gsA6ccfcfPI6bdOhvfachuCt3usfC%2F8VF6%2B2ZK1e2tamvhnYYbVgNXVzfwGZGdCOmD7L8pSiIOn4N3lPjvb7I689vPt5rSnU5ovUJZHy3xYHbJHkR85lUd%2F0zmJB%2F7CEw3q5zhk%2BMBiURAib5yeQmL9DFi9elJpmuGXVdB1QX4O3G%2B9BLa36O4PWjnOgvQZNFDcinKTIwFbRbNtg0R3JA2xpzrhbYe94dEvXG40iunneKdkFLlcrYJHiFjfwEqJTRutk7asxF402ef%2BWHt17SbU1jXo0aWXCgb3hl9CO14HAHtGA0x4owXKoxnYEK6l4MGz8jGsHZlu9ip4FE047g8SSbX7oH3WQByavfYekooFS2aWJYyWyK56S5FkolOUStJOGdDPfSj7TwX13tdkHXnppokc5o2HluPGo87l73ASMwqvTExAY6pgGH%2F5Z2Zj0IC1VXH5ompDDKRKgklHp0Axh%2BzewENMPLTqKQoqnc%2BfuWCmOrpH5EkqjIrjlyAqT471rPSc1URTnA9a0k%2F3Xj342v6Or1%2F56fnLsMitZWHyNolg7KqyVFMom5I0Vdi7hWzH6EZo%2BbOlKUEWX7vFiztn%2FosuXXls5godP06FU5YWM%2B7n6TJp6R1PisoKrcOKd%2FKdpG%2BoN%2Bx%2BAbc5OpaD7B&X-Amz-Signature=599970029ae289141c9cf052992991b246af53ae6cb63b1a3409717d027310a7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## EmptyDir 연습문제

- 하나의 프로세스는 랜덤한 값을 생성 (count 이미지 사용)
- 하나의 프로세스는 랜덤한 값을 출력 (httpd이미지 사용)

