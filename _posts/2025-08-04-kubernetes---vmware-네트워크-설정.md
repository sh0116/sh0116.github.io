---
title: "Kubernetes - VMware 네트워크 설정"
date: 2025-08-04 06:05:00 +0900
categories: [kubernetes]
tags: [Kubernetes]
description: Kubernetes 기초
toc: true
comments: true
---

## vmware 고정 IP설정

Ubuntu, centOS 등 여러 OS와 버전마다 방법이 다르다.

## VMWARE 네트워크 NAT설정

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/d442bc35-5a0e-44a5-94dc-6da6f0df5dd7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RLQY3Q2P%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T071500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJIMEYCIQDJftAu82dMJEqPNDEH6WDKaeykfDIMwYp29PrAQd8%2BdAIhAMI42Sm3xstAv%2FiMesq9mxB654%2B4zfkdSnFPqhyQgSaSKv8DCEAQABoMNjM3NDIzMTgzODA1IgxFhjWSpdKR7muiEnIq3AN7m%2B2jknNRMTB3XsD%2F7a1%2FTLaXO4gfDEnLISVjRkrKrz8c8Skdz3Qvoc7MJf3vPNHwH02rYpD1yJozpzWRJCYG0JbrFPnOfXQuVW1DYo%2B45k%2BGQgMMHaQ2sM9SG7k9GXS2V8NxIPatdZ4LJf0YahlJpL%2BrB3nPmNPB6928YRLsuZvlrE1EOGqN8F1Bt1yjH%2BoID6Z1H02D16h%2Fiaohe6c3fCBaU405WXf5LOTuprczlSPzdCTGEVtyJMMkiqyLI2ayAUN39WpoADfRj8GUa535HD50DbH%2B8WgJb999Rug5R0w7Liq3wp8LoitfkrAJsZs%2FttU1RxBBhjOqUzQO7IIn6gBIDBfg32F0UyHceIXaxkQiAhQ6WKNeEaBJtyB0H0Vd3Zrt%2FaLjp6S8r6Gvkpzs1N%2FAL%2BS2Mldp%2B%2F6X6TmPSYx0ZuW8yvxCjYZRfF2Z4VlHxN3yrnj%2FA9gKNT6ACbuirq4wmY9P3390mq7nt8cPFCmVaiKibaS3ofcNlxH3bDMagzchSCZCSp%2B4mO7T69UcY6tooqVTdtqsnZwzA9qeaMLECc7iUxcZekC%2FWaMfZ7ZW4gphQeiNvhGjzaM20IsHTPZlwoBKqTQ%2FHtRb2PWM3uLzlDj7YqQ4duAWgTC%2Bt8HEBjqkAaLa%2BnLuqyvwBl7YMA9GaRA6a7MSzetKNIIc1hO8sjz9RGrYDydIXSFcDX%2FCzDUpvuyQTcyGz%2FQ6H5ekks7Q953ZV1Z%2FBs8YGo00xmyYFP253zr3zWYPuIxDh3V%2FnEvbYiBraN7EZt9pFlmAIJiknEOcN8qGbDEiQkJ75imnxma7ZIF1kaDGn4soV6b1YyDMvpT%2FREfh1Vin2l%2FqXCqw%2BMhYca1i&X-Amz-Signature=e922037144f4a3551a5c71c63d5a56d58a3689f5259571ab89472a734f169f36&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 각 Node들 Setting

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/2b4553bb-feb8-4a69-bb16-afceeec78efe/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RLQY3Q2P%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T071500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJIMEYCIQDJftAu82dMJEqPNDEH6WDKaeykfDIMwYp29PrAQd8%2BdAIhAMI42Sm3xstAv%2FiMesq9mxB654%2B4zfkdSnFPqhyQgSaSKv8DCEAQABoMNjM3NDIzMTgzODA1IgxFhjWSpdKR7muiEnIq3AN7m%2B2jknNRMTB3XsD%2F7a1%2FTLaXO4gfDEnLISVjRkrKrz8c8Skdz3Qvoc7MJf3vPNHwH02rYpD1yJozpzWRJCYG0JbrFPnOfXQuVW1DYo%2B45k%2BGQgMMHaQ2sM9SG7k9GXS2V8NxIPatdZ4LJf0YahlJpL%2BrB3nPmNPB6928YRLsuZvlrE1EOGqN8F1Bt1yjH%2BoID6Z1H02D16h%2Fiaohe6c3fCBaU405WXf5LOTuprczlSPzdCTGEVtyJMMkiqyLI2ayAUN39WpoADfRj8GUa535HD50DbH%2B8WgJb999Rug5R0w7Liq3wp8LoitfkrAJsZs%2FttU1RxBBhjOqUzQO7IIn6gBIDBfg32F0UyHceIXaxkQiAhQ6WKNeEaBJtyB0H0Vd3Zrt%2FaLjp6S8r6Gvkpzs1N%2FAL%2BS2Mldp%2B%2F6X6TmPSYx0ZuW8yvxCjYZRfF2Z4VlHxN3yrnj%2FA9gKNT6ACbuirq4wmY9P3390mq7nt8cPFCmVaiKibaS3ofcNlxH3bDMagzchSCZCSp%2B4mO7T69UcY6tooqVTdtqsnZwzA9qeaMLECc7iUxcZekC%2FWaMfZ7ZW4gphQeiNvhGjzaM20IsHTPZlwoBKqTQ%2FHtRb2PWM3uLzlDj7YqQ4duAWgTC%2Bt8HEBjqkAaLa%2BnLuqyvwBl7YMA9GaRA6a7MSzetKNIIc1hO8sjz9RGrYDydIXSFcDX%2FCzDUpvuyQTcyGz%2FQ6H5ekks7Q953ZV1Z%2FBs8YGo00xmyYFP253zr3zWYPuIxDh3V%2FnEvbYiBraN7EZt9pFlmAIJiknEOcN8qGbDEiQkJ75imnxma7ZIF1kaDGn4soV6b1YyDMvpT%2FREfh1Vin2l%2FqXCqw%2BMhYca1i&X-Amz-Signature=2706e0d773ae6c47acc01c31c667d9881a5b68ed592e58447ce3270457340ecc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## NetPlan 구성

/etc/netplan 폴더에 있는 yaml을 고쳐준다.

```bash
# Let NetworkManager manage all devices on this system
network:
  ethernets:
          ens33:
                  dhcp4: no
                  dhcp6: no
                  addresses:
                  - 192.168.75.151/24
                  gateway4: 192.168.75.2
                  nameservers:
                           addresses: [8.8.8.8]
  version: 2
```

addresses 부분은 본인이 원하는 고정 IP

gateway는 위에서 얻었던 IP값을 가져오면된다.

dhcp는 IP 동적할당으로 생각하면된다 → 따라서 no옵션

nameservers 는 DNS서버다 8.8.8.8은 google public DNS 서버입니다.

## Netplan 적용

```bash
sudo netplan apply
```


