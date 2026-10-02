---
source: knowledge-base
origin: notion
title: "Kubernetes - VMware 네트워크 설정"
area: "Kubernetes"
tags: ["area/kubernetes", "tech/kubernetes"]
created: "2025-08-04T06:05:00.000Z"
last_edited: "2025-08-04T06:27:00.000Z"
status: published
public: true
notion_id: "245172a5-56d6-805b-bcf2-f47454883dfc"
notion_url: "https://www.notion.so/Kubernetes-VMware-245172a556d6805bbcf2f47454883dfc"
type: note
updated: 2026-07-07
---

# Kubernetes - VMware 네트워크 설정

## 요약

Kubernetes 기초

Kubernetes 큰 주제 아래에서 세부 개념과 실습 절차를 연결하기 위한 노트입니다.

## 핵심 포인트

- Kubernetes 기초
- vmware 고정 IP설정
- VMWARE 네트워크 NAT설정
- 각 Node들 Setting
- NetPlan 구성

## 지식 그래프

- [[wiki/mocs/Knowledge Base|Knowledge Base]]
- [[wiki/mocs/Kubernetes|Kubernetes]]

## 정리 내용

### vmware 고정 IP설정
Ubuntu, centOS 등 여러 OS와 버전마다 방법이 다르다.
### VMWARE 네트워크 NAT설정
![[_attachments/notion/Kubernetes---VMware-네트워크-설정/245172a556d681b88545efc70d5bd5ae.png]]

![[_attachments/notion/Kubernetes---VMware-네트워크-설정/245172a556d68160ac17c1f4cbce1e27.png]]
![[_attachments/notion/Kubernetes---VMware-네트워크-설정/245172a556d6811a8cb1cef0abc1a808.png]]
### 각 Node들 Setting
![[_attachments/notion/Kubernetes---VMware-네트워크-설정/245172a556d68106aa9afb255bbeaae4.png]]

NAT설정한 VMnet을 연결
![[_attachments/notion/Kubernetes---VMware-네트워크-설정/245172a556d681dfa420c7a3ae295f17.png]]
### NetPlan 구성
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
### Netplan 적용
```bash
sudo netplan apply
```

## 출처

- 원문: https://www.notion.so/Kubernetes-VMware-245172a556d6805bbcf2f47454883dfc
- Vault path: wiki/notes/kubernetes/Kubernetes---VMware-네트워크-설정.md
