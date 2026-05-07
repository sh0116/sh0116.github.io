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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/d442bc35-5a0e-44a5-94dc-6da6f0df5dd7/Untitled.png)

## 각 Node들 Setting

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/2b4553bb-feb8-4a69-bb16-afceeec78efe/Untitled.png)

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


