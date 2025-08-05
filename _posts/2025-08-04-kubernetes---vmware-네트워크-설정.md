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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/d442bc35-5a0e-44a5-94dc-6da6f0df5dd7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZM5U2XBT%2F20250805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250805T061057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJHMEUCIBbMcjz45T66oP7CwqXuhhpjRXxyVehVtzVaATDFHC9lAiEA4c6l3EwdEVvReK0OsgRBu9qOrC4H%2FEBAqgiLVpqwiOkq%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDGWh26S2hxROO4f43yrcAyoooxPVwDxrMuydQyF%2BD8AzUHTKjVEqgkU0Qm8CQjWDztniXuTUivqwrLQQbNZrleUvDmnjEdtQxwTa8L%2FE%2F2NuDDkFC%2Bv31IOznQYStzVY4bX3NhKw7swLPi5vCoCmLRNYrFai1xxjdYRD1fKYK1jewgautV9CbLS85UCevIZ3s%2FTIBT0uOPT3v%2BdjRZtopMpB3pDso8hNJIyG3c0UotOqykeOCmHDkvXybRZR9q0RuG%2F27ly403pvfBgX3AsIbqx5cNboUVF0cjBukwTUGUV7UnIv99jWkBhldE0siaES4OrXGoKIZ7YNbDH9Kbg2o0FDht4fuyOzm7%2BR0LoavUL725AiDdvmmx4bo31etzbH13TIjewaJn90Ojuc1%2FK1QwBAx%2FXjjopjSq1CN3xbHqyhpenq5dgn9t%2F1fRfNZCRocX3hSxhojy0oZvt8JC12KpYSb6GXO%2BgOCEVovpCwmebrpGEWcPNmBI54GJLPu0KrPVQ2Lrnn%2F2umDatRoiyZEv5LugW8n0M1Q5rgxF0ABL7LNb%2FJZlbgnr4a7zLbg0cn3XEFQSNw12Kqk9gusfNLfN3DvrA4QRZOoHFgcb87%2B%2Fo4nHYpskF7Yc2EFsM59Db2eBVh5WOvHmiNMO53MJazxsQGOqUB4fAZMpOd8fjYPV42nUbWRjRYolPBjo0KwXl8hM9gXSXcprrDyIVhVeT1geaW%2F0IKqoR%2FDINP2M9AIJdk9Vjs1Oh93Y93rmY8QtHy7fegfAWyH1S4nZWTrGHg5wQTaKecdT7z7ov7igXe5lrsWM%2BNZ5XuWULBIOasDTj1hX4%2B4UfY2EZH3VNDxBbtbN3jCMWo%2ByniH9S2LsiNW%2FHfa3paGQaz9v39&X-Amz-Signature=7ace0aa14bf03ac7a99e7af40edd241ac3e8765b9ac18717816d24253534367f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 각 Node들 Setting

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/2b4553bb-feb8-4a69-bb16-afceeec78efe/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZM5U2XBT%2F20250805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250805T061057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJHMEUCIBbMcjz45T66oP7CwqXuhhpjRXxyVehVtzVaATDFHC9lAiEA4c6l3EwdEVvReK0OsgRBu9qOrC4H%2FEBAqgiLVpqwiOkq%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDGWh26S2hxROO4f43yrcAyoooxPVwDxrMuydQyF%2BD8AzUHTKjVEqgkU0Qm8CQjWDztniXuTUivqwrLQQbNZrleUvDmnjEdtQxwTa8L%2FE%2F2NuDDkFC%2Bv31IOznQYStzVY4bX3NhKw7swLPi5vCoCmLRNYrFai1xxjdYRD1fKYK1jewgautV9CbLS85UCevIZ3s%2FTIBT0uOPT3v%2BdjRZtopMpB3pDso8hNJIyG3c0UotOqykeOCmHDkvXybRZR9q0RuG%2F27ly403pvfBgX3AsIbqx5cNboUVF0cjBukwTUGUV7UnIv99jWkBhldE0siaES4OrXGoKIZ7YNbDH9Kbg2o0FDht4fuyOzm7%2BR0LoavUL725AiDdvmmx4bo31etzbH13TIjewaJn90Ojuc1%2FK1QwBAx%2FXjjopjSq1CN3xbHqyhpenq5dgn9t%2F1fRfNZCRocX3hSxhojy0oZvt8JC12KpYSb6GXO%2BgOCEVovpCwmebrpGEWcPNmBI54GJLPu0KrPVQ2Lrnn%2F2umDatRoiyZEv5LugW8n0M1Q5rgxF0ABL7LNb%2FJZlbgnr4a7zLbg0cn3XEFQSNw12Kqk9gusfNLfN3DvrA4QRZOoHFgcb87%2B%2Fo4nHYpskF7Yc2EFsM59Db2eBVh5WOvHmiNMO53MJazxsQGOqUB4fAZMpOd8fjYPV42nUbWRjRYolPBjo0KwXl8hM9gXSXcprrDyIVhVeT1geaW%2F0IKqoR%2FDINP2M9AIJdk9Vjs1Oh93Y93rmY8QtHy7fegfAWyH1S4nZWTrGHg5wQTaKecdT7z7ov7igXe5lrsWM%2BNZ5XuWULBIOasDTj1hX4%2B4UfY2EZH3VNDxBbtbN3jCMWo%2ByniH9S2LsiNW%2FHfa3paGQaz9v39&X-Amz-Signature=312359a73d2c5dea18bbc09162de617fe3dbf0b7770bb0e59478f507fbb6ca5a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


