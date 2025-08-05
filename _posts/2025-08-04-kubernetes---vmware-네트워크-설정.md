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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/d442bc35-5a0e-44a5-94dc-6da6f0df5dd7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TW3RQVUK%2F20250805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250805T002810Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJHMEUCIH61Ff4VIaE%2Fd7o0JMyTJ5VMKwD42IXY%2BEmck8M1FFeIAiEAtQU8JoegTckwNp%2B17v1d5cNYNCgHKeNyHQ2NfHC0360q%2FwMIUBAAGgw2Mzc0MjMxODM4MDUiDMq8hLCotLtGEVeTiSrcA9wCStcKLBQegCNgD%2BdWZSd87qNn2FHFh7wu4US41w3%2FRJ9tD5HTlAKUGCXM45nCMNSIObeTFu1n33vwT2YiKvo0dtjRrAOS9%2BUNj68myZCfdoRek8A%2FS5fa2DBR67HHjKN2CnxNYgMEPqvXKuID%2Fwg2koyP%2BeclgYm5bOVbBMKLjcuNi3%2Bj3kqWudp3s7%2Fhp7COEpCxjHJ7ycj%2FvG2ZC2Z7Y9wDoVRzLkKV9oP7SXEGGRAbFTGiU66oqotMPrnQfCI3M0PqEml2W8UzkEbARvEpCiask8fp4fL%2F4hgvljoHanor7IXvjoFld0p4MY7g%2BMBIgKdrgb670YBrI0xu1n%2BSA5DLiWcKrLAG6Hzm53odpzkRUBpXm40%2F0Welt0rQkpCp9CgD9Q0%2FXuZiY50bv9%2BbSHtv0r2PremSPBMFkN%2FYyaltOJJtb%2BTHU5%2Fj4hmHecJU67anIKvsGUqzYiZie2xKdZH1xyD9t05jDrjY7IwqGDD2xDYE2SkXzvXuyAs0mnTEyiQW3RUbrDPR%2BotC%2Ff9yq5jhzH87laugUC%2BopfHU2pCf7rIfyl62B%2BikTnJo1fl%2BvclbM%2FW0oe9GNy8AX3zSreAThRz%2FNRtc%2BV0EpG49MRn33CDHdmnUSq1HMOXzxMQGOqUBJeNHcwLFeTXmOcv0cp7AkCAfjdRw0zlWErpaqmK0CQ2%2FqkwniaqgFsDTUexVCv1hnRB%2F3n%2FlfVM3jhDpzws5TNHdgNxPdLsM5oFCzOBZI6SM%2FxQlVvvUpTDifKaUfZ0RfE5NvU1MjhxlRgWedgbg2D7liHkL4abN4EiYML9f5afOdGrS9R14vL4drSewwEk3B6t33%2FRAU9JC1zcoU6JVvSJQyY1q&X-Amz-Signature=441edcfb9408e2b1aa20616639390202bf059d502246e17f6b19ffd40d9307f7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 각 Node들 Setting

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/2b4553bb-feb8-4a69-bb16-afceeec78efe/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TW3RQVUK%2F20250805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250805T002810Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJHMEUCIH61Ff4VIaE%2Fd7o0JMyTJ5VMKwD42IXY%2BEmck8M1FFeIAiEAtQU8JoegTckwNp%2B17v1d5cNYNCgHKeNyHQ2NfHC0360q%2FwMIUBAAGgw2Mzc0MjMxODM4MDUiDMq8hLCotLtGEVeTiSrcA9wCStcKLBQegCNgD%2BdWZSd87qNn2FHFh7wu4US41w3%2FRJ9tD5HTlAKUGCXM45nCMNSIObeTFu1n33vwT2YiKvo0dtjRrAOS9%2BUNj68myZCfdoRek8A%2FS5fa2DBR67HHjKN2CnxNYgMEPqvXKuID%2Fwg2koyP%2BeclgYm5bOVbBMKLjcuNi3%2Bj3kqWudp3s7%2Fhp7COEpCxjHJ7ycj%2FvG2ZC2Z7Y9wDoVRzLkKV9oP7SXEGGRAbFTGiU66oqotMPrnQfCI3M0PqEml2W8UzkEbARvEpCiask8fp4fL%2F4hgvljoHanor7IXvjoFld0p4MY7g%2BMBIgKdrgb670YBrI0xu1n%2BSA5DLiWcKrLAG6Hzm53odpzkRUBpXm40%2F0Welt0rQkpCp9CgD9Q0%2FXuZiY50bv9%2BbSHtv0r2PremSPBMFkN%2FYyaltOJJtb%2BTHU5%2Fj4hmHecJU67anIKvsGUqzYiZie2xKdZH1xyD9t05jDrjY7IwqGDD2xDYE2SkXzvXuyAs0mnTEyiQW3RUbrDPR%2BotC%2Ff9yq5jhzH87laugUC%2BopfHU2pCf7rIfyl62B%2BikTnJo1fl%2BvclbM%2FW0oe9GNy8AX3zSreAThRz%2FNRtc%2BV0EpG49MRn33CDHdmnUSq1HMOXzxMQGOqUBJeNHcwLFeTXmOcv0cp7AkCAfjdRw0zlWErpaqmK0CQ2%2FqkwniaqgFsDTUexVCv1hnRB%2F3n%2FlfVM3jhDpzws5TNHdgNxPdLsM5oFCzOBZI6SM%2FxQlVvvUpTDifKaUfZ0RfE5NvU1MjhxlRgWedgbg2D7liHkL4abN4EiYML9f5afOdGrS9R14vL4drSewwEk3B6t33%2FRAU9JC1zcoU6JVvSJQyY1q&X-Amz-Signature=d10d7c4b89274ae6ed81e11a59d64dbce1498c8dcc07fd9903ac8b7ae04653f5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


