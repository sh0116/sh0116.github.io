---
title: "Kubernetes - POD란?"
date: 2025-08-04 06:05:00 +0900
categories: [kubernetes]
tags: [Kubernetes]
description: Kubernetes 기초
toc: true
comments: true
---

## 포드, 팟, 파드 == pod의 특징

- 컨테이너의 공동 배포된 그룹이며 k8s 기본 빌딩 블록
- k8s 컨테이너를 개별적으로 배포하지 않고 컨테이너의 pod를 항상 배포하고 운영
- 일반적으로 단일 컨테이너지만 다수 컨테이너 포함도 가능
- 다수의 노드에서 실행되는것이 아니라 한 Node에서 독립적으로 실행
## POD 관리

- 장점
- 동일한 pod의 컨테이너 사이의 부분 격리
## 네트워크 구조

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/f38ce897-ad6d-434b-a035-f306e89b207f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SGZGZK4C%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T072314Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJGMEQCIDLoeI4S3VB1GEcYwSPORX5g32lQnGpRwgT9BTqVuiw0AiBZYD1U45gpAjkdJvm1FIYCV1PkSABap62MGJqH8O4tECr%2FAwhAEAAaDDYzNzQyMzE4MzgwNSIMsHKMTvBGdaz8%2BwNQKtwDko79f7FWDOnWtNSyz%2Fu3X%2BrlN4HnhSjcRG404pc04J9LF6xDpCpoO0IjaSlrWVxr8Y%2BTOIow7wUOMubXkPPzn4iT1LTllq24EiLCp9jtKP4yO1NhBuKLpgIwF7iIWl2AMoHO%2FO6hYy6CG0efctIw%2BBL4Gyrbo3X6JPYdhhM15WM1IKbtzfWAHcXJpPRBMeTmSZD3PU8Bt9OscdOYwfadNjrUgsUH4mhqxkVHjuUtkGciJXTTwC56%2BcUjbcJMm8hNbcoDVLh0LUFmASNIS2V%2F7uyv3%2FKmoNeSaiRSQ0ZEkN%2FZ3xfntWOPYINl4Ftu9dRUN3Ezq7ceTivnBmgVY3JM1l26PdFSWNbfrLxozyKJTieCzqPpltzO6QkPa89ff7OY%2Fd1F2bUNnztseXaKa%2FpIhKwEg6DLeB8Au3evvvanMo2yts%2B3f9oOeAtA7e4LWCzh9zOgsopt9WcI8Pl9lGT59%2F5%2Fi%2FmpcI24VvNdcxsqcJEolm0H5PHVlhTkFdyoKNmSo1yMdpWsblBnQzKBB2qMMPN0Ei15Qr2wdQIGeWuYY1xsaliT7x1RuLLn9LjdisYkO2AnHe%2BRb3lDPF80UsNQJ6fHwg9v7KYeteIcJBYRPMEj%2FtDM0%2BjygLZ3Fiwwv7bBxAY6pgFiWBeQeqQEmnEUJKL%2FFJ53gRVgdiDZOPR%2FUAMyJCx998DKChXjs0QgQNu%2BXnp92pIOWa%2BHptv8aAKhxlBdp51EgF6KYLRwpC7skMXg7DtCv1UK88v6SpTAVFYvi15Zb5%2BBAov%2FeZPNvEQmHfT0L7yyaMvyVxuI1RaxHoNfx0te0p6WQQXrSES%2BcRWkb2EMSFrwg4AZKpp1ZX5etE51L%2FAfMug9oCAv&X-Amz-Signature=fff0f0883000cbb2c5220f8cb10112a29ab5d7d8a9c72002930649de5afd2502&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 컨테이너를 POD 전체에 적절하게 구성하는 방법

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/811279dd-4730-40a6-bff1-b650bb32201c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SGZGZK4C%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T072314Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJGMEQCIDLoeI4S3VB1GEcYwSPORX5g32lQnGpRwgT9BTqVuiw0AiBZYD1U45gpAjkdJvm1FIYCV1PkSABap62MGJqH8O4tECr%2FAwhAEAAaDDYzNzQyMzE4MzgwNSIMsHKMTvBGdaz8%2BwNQKtwDko79f7FWDOnWtNSyz%2Fu3X%2BrlN4HnhSjcRG404pc04J9LF6xDpCpoO0IjaSlrWVxr8Y%2BTOIow7wUOMubXkPPzn4iT1LTllq24EiLCp9jtKP4yO1NhBuKLpgIwF7iIWl2AMoHO%2FO6hYy6CG0efctIw%2BBL4Gyrbo3X6JPYdhhM15WM1IKbtzfWAHcXJpPRBMeTmSZD3PU8Bt9OscdOYwfadNjrUgsUH4mhqxkVHjuUtkGciJXTTwC56%2BcUjbcJMm8hNbcoDVLh0LUFmASNIS2V%2F7uyv3%2FKmoNeSaiRSQ0ZEkN%2FZ3xfntWOPYINl4Ftu9dRUN3Ezq7ceTivnBmgVY3JM1l26PdFSWNbfrLxozyKJTieCzqPpltzO6QkPa89ff7OY%2Fd1F2bUNnztseXaKa%2FpIhKwEg6DLeB8Au3evvvanMo2yts%2B3f9oOeAtA7e4LWCzh9zOgsopt9WcI8Pl9lGT59%2F5%2Fi%2FmpcI24VvNdcxsqcJEolm0H5PHVlhTkFdyoKNmSo1yMdpWsblBnQzKBB2qMMPN0Ei15Qr2wdQIGeWuYY1xsaliT7x1RuLLn9LjdisYkO2AnHe%2BRb3lDPF80UsNQJ6fHwg9v7KYeteIcJBYRPMEj%2FtDM0%2BjygLZ3Fiwwv7bBxAY6pgFiWBeQeqQEmnEUJKL%2FFJ53gRVgdiDZOPR%2FUAMyJCx998DKChXjs0QgQNu%2BXnp92pIOWa%2BHptv8aAKhxlBdp51EgF6KYLRwpC7skMXg7DtCv1UK88v6SpTAVFYvi15Zb5%2BBAov%2FeZPNvEQmHfT0L7yyaMvyVxuI1RaxHoNfx0te0p6WQQXrSES%2BcRWkb2EMSFrwg4AZKpp1ZX5etE51L%2FAfMug9oCAv&X-Amz-Signature=bcb69f6d36aafe81cd65f402bc2c7b17884ea4ee16cedc6438fe6121fddc9e46&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

 

# POD 구성 Yaml파일

### 파일 구성 요소

- apiVersion : Kubernetes API버전을 가르킴
- Kind : 어떤 리소스 유형인지 (pod, service, replica) 
- MetaData : pod와 관련된 이름, NameSpace, label 그 밖의 정보 존재
- Spec : 컨테이너 볼륨 정보 등등
- 상태 : pod상태, 컨테이너 설명, IPC 등등
```yaml
apiVersion: v1
kind: Pod
metadata:
name: memory-demo
namespace: mem-example
spec:
containers:
  -name: memory-demo-ctr
image: polinux/stress
resources:
requests:
memory: "100Mi"
limits:
memory: "200Mi"
command: ["stress"]
args: ["--vm", "1", "--vm-bytes", "150M", "--vm-hang", "1"]
```


