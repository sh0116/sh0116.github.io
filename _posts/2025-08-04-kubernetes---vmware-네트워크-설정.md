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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/d442bc35-5a0e-44a5-94dc-6da6f0df5dd7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VFU3RXCR%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T072110Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJGMEQCIAkH1DvkFDjgel%2BbC0Z8hkyUK55poRWUg8pw4f7UnrhuAiBL2NRcH7ITFSY8jxIyIwZpdaLmfThLYqIdjylhMqHGgSr%2FAwhAEAAaDDYzNzQyMzE4MzgwNSIMmfAVWEo4%2BFg01oMmKtwDKrzS0lWK1g9XYIVU4ZGenFdheb88kgb%2BEsbw%2F%2FQSfrGOPJy7jY1QD1711oPC2achC%2Fa3sggbN%2BAmXSQE1ub718HQR6A7Jf81xR6kaLUchuejHqmlTwZMOkXCJHBmSlbgoPhUmhS%2F5cQMzMI159o4VBruWI3268X2c%2FQnJs7l%2F58jlxPzfexEODgAto0AmHOWIAOT1nLfZoHLyZ5dKogS9W51rlin5FuhmMyAgT%2FBkXjgrbWd52YFBOp9sau3pWQ8WGAg7ZEcoYcoNhfl6PnD5%2Fu6iYmNbAmZrs%2BpxGgpDbm1RyuKPPIVL5VwLfPJwTNU1TAaKy61GYDohV6dZMmMqAFaqSefXUr0ph77Cn2VtgyxXD3rWnAv5jXmQ%2BIEWRcC6wdHXsNDLSmjjx%2Bx%2FKNIakZyvDWmy2qMrTy7NR9Eo3toiKck%2BN5664aspeUgiK9Sa1WxPkpbeffhGsufXAd0K7Ry21MIEJWp%2Bl254RrI%2F5ry2FGuthQRId88X1fnavixqN%2B87fjEUUB8p9r7oGJJqQhrYVkZi6OjZQWsEZ91fquhk%2F2tw%2B5%2Bj1MuxiAtS579MDF6OvPo7LHTXGtWTpcTJx6eE6gru2l%2BNj71B2EY8DD4ljt3YhVtRT4sRg0wx7jBxAY6pgEC9LO%2FnfiqwB5FM6ZOMAJ9QCZ8zTk%2F9kMeYm%2BsTzik1P2tls3HTb4Zfm0CJsUfweakyRqrTDKzzYB33S6m8w3Oz7716T7ygqpqp1i8CpqrDoT0lPgP4QXGoV6Wt1m3cYadryXfAsasSpyZM2DcvHmkevzylEtoFtzMF7HiofolMtxww%2BjY2OpcaoJ5%2BtS33gLuRSdoMQwGv0fSIvJK9FatEuKYEy%2F2&X-Amz-Signature=83562c3badf96b2eeb99c83bac3751524e5db6941a5bfcd116711d3ac25086d5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 각 Node들 Setting

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/2b4553bb-feb8-4a69-bb16-afceeec78efe/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VFU3RXCR%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T072110Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJGMEQCIAkH1DvkFDjgel%2BbC0Z8hkyUK55poRWUg8pw4f7UnrhuAiBL2NRcH7ITFSY8jxIyIwZpdaLmfThLYqIdjylhMqHGgSr%2FAwhAEAAaDDYzNzQyMzE4MzgwNSIMmfAVWEo4%2BFg01oMmKtwDKrzS0lWK1g9XYIVU4ZGenFdheb88kgb%2BEsbw%2F%2FQSfrGOPJy7jY1QD1711oPC2achC%2Fa3sggbN%2BAmXSQE1ub718HQR6A7Jf81xR6kaLUchuejHqmlTwZMOkXCJHBmSlbgoPhUmhS%2F5cQMzMI159o4VBruWI3268X2c%2FQnJs7l%2F58jlxPzfexEODgAto0AmHOWIAOT1nLfZoHLyZ5dKogS9W51rlin5FuhmMyAgT%2FBkXjgrbWd52YFBOp9sau3pWQ8WGAg7ZEcoYcoNhfl6PnD5%2Fu6iYmNbAmZrs%2BpxGgpDbm1RyuKPPIVL5VwLfPJwTNU1TAaKy61GYDohV6dZMmMqAFaqSefXUr0ph77Cn2VtgyxXD3rWnAv5jXmQ%2BIEWRcC6wdHXsNDLSmjjx%2Bx%2FKNIakZyvDWmy2qMrTy7NR9Eo3toiKck%2BN5664aspeUgiK9Sa1WxPkpbeffhGsufXAd0K7Ry21MIEJWp%2Bl254RrI%2F5ry2FGuthQRId88X1fnavixqN%2B87fjEUUB8p9r7oGJJqQhrYVkZi6OjZQWsEZ91fquhk%2F2tw%2B5%2Bj1MuxiAtS579MDF6OvPo7LHTXGtWTpcTJx6eE6gru2l%2BNj71B2EY8DD4ljt3YhVtRT4sRg0wx7jBxAY6pgEC9LO%2FnfiqwB5FM6ZOMAJ9QCZ8zTk%2F9kMeYm%2BsTzik1P2tls3HTb4Zfm0CJsUfweakyRqrTDKzzYB33S6m8w3Oz7716T7ygqpqp1i8CpqrDoT0lPgP4QXGoV6Wt1m3cYadryXfAsasSpyZM2DcvHmkevzylEtoFtzMF7HiofolMtxww%2BjY2OpcaoJ5%2BtS33gLuRSdoMQwGv0fSIvJK9FatEuKYEy%2F2&X-Amz-Signature=c89ee6fd50b8407e9ab183637ad871d84abc6ac0e116d216cdd249d9e17206ba&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


