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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/d442bc35-5a0e-44a5-94dc-6da6f0df5dd7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665GL5WXTF%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T072238Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIQD1d7DdTYVdKj9emLR6QdeOfD7HX9lGXVksWy30fYyBZAIgL0IZP7W3WGgc8IqAIRun9HXOe4d4EAZ5BJvQnthySPAq%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDM7Zrd2SEot0WD5JhCrcA5IiV%2BOIQVYQq5XVq0h4OxrXRB2l2g0nwdDtoD8%2BcIuQQA0yTEhRUic9Y2Dvyuoh8DusMnbv62lpNNXwX8PKUNRsw0wGSmL%2B5nS%2FiO%2BfuMSu01sbvXYOmwJrgiGPgGk38xFgttExB011c7h7oFq2Pasl3MxF4dC%2BREufPyK77g5G1Oo9ToDLQfj%2FYTFmxZI7V1GRhdxqsy9UaE%2FivgqnM3RUnd2cVqqKci0Z74AppKBPKA3RSRXiPXxasNZc%2FZbLm%2FN6Fgi5ELXyPyOKQkdx19fJk%2BvoRTcF10VpE5uKr%2Fyt6gSbLbdZqcbpkxBOldqU2m0gwj5Uc2JX4Z6%2B3x05R5UxJTBOdmvzhHVPTtk4iXPzFh5K%2BtWWf%2BuzNCvToI8XfNve7HZHKcFkLTFLpweANPg7XFkKrFQe3ZBMyMBGxL0n0aWVMspyLmdBLPX03SQjyrTWdlw5skjqlbTXevHHib1OQLgjW9dW03B2SQIyUeHLIjWhDHos6%2FCt757Z04%2BhqcaltJZp5y5gvtzA76ZOhKTF9o%2BalRsBoc%2BgsY6ZZr2%2BAPzLrMAP5W32lJJiicZ%2Fskr%2BGNeBPDF46NvWo5fZHmAqTgvMySAu%2BL%2FnDmCwMa5iP5zoL4LKYJJDhYSwMMO2wcQGOqUB1g%2B5oeF1fyYTpWuyfX8YRnN%2BxZoxedHdcHp0sqmUsJBkr53mCd23HuU1p47U3%2FFMBrxdLrcp%2Fmj%2B71fud%2B11rfNuePfU6TRm0h%2B1zS6RZIS1R7DO8NnDBqOP04rb3ussndD%2Bfmhth117eZqhR85kWehX6nd3nBgpGzozlgQeDCubciOKoQFDm6ZK0AOHKUfMezO5lD8mTsF7U0Kkm4RIGH1Pgi4L&X-Amz-Signature=01e003c38062324e82fb36b990c721fe9d681590df28a32e7174830adbe3b71b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 각 Node들 Setting

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/e6db513d-ec54-40ff-aa74-2487b0bcfe15/2b4553bb-feb8-4a69-bb16-afceeec78efe/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665GL5WXTF%2F20250804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250804T072238Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIQD1d7DdTYVdKj9emLR6QdeOfD7HX9lGXVksWy30fYyBZAIgL0IZP7W3WGgc8IqAIRun9HXOe4d4EAZ5BJvQnthySPAq%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDM7Zrd2SEot0WD5JhCrcA5IiV%2BOIQVYQq5XVq0h4OxrXRB2l2g0nwdDtoD8%2BcIuQQA0yTEhRUic9Y2Dvyuoh8DusMnbv62lpNNXwX8PKUNRsw0wGSmL%2B5nS%2FiO%2BfuMSu01sbvXYOmwJrgiGPgGk38xFgttExB011c7h7oFq2Pasl3MxF4dC%2BREufPyK77g5G1Oo9ToDLQfj%2FYTFmxZI7V1GRhdxqsy9UaE%2FivgqnM3RUnd2cVqqKci0Z74AppKBPKA3RSRXiPXxasNZc%2FZbLm%2FN6Fgi5ELXyPyOKQkdx19fJk%2BvoRTcF10VpE5uKr%2Fyt6gSbLbdZqcbpkxBOldqU2m0gwj5Uc2JX4Z6%2B3x05R5UxJTBOdmvzhHVPTtk4iXPzFh5K%2BtWWf%2BuzNCvToI8XfNve7HZHKcFkLTFLpweANPg7XFkKrFQe3ZBMyMBGxL0n0aWVMspyLmdBLPX03SQjyrTWdlw5skjqlbTXevHHib1OQLgjW9dW03B2SQIyUeHLIjWhDHos6%2FCt757Z04%2BhqcaltJZp5y5gvtzA76ZOhKTF9o%2BalRsBoc%2BgsY6ZZr2%2BAPzLrMAP5W32lJJiicZ%2Fskr%2BGNeBPDF46NvWo5fZHmAqTgvMySAu%2BL%2FnDmCwMa5iP5zoL4LKYJJDhYSwMMO2wcQGOqUB1g%2B5oeF1fyYTpWuyfX8YRnN%2BxZoxedHdcHp0sqmUsJBkr53mCd23HuU1p47U3%2FFMBrxdLrcp%2Fmj%2B71fud%2B11rfNuePfU6TRm0h%2B1zS6RZIS1R7DO8NnDBqOP04rb3ussndD%2Bfmhth117eZqhR85kWehX6nd3nBgpGzozlgQeDCubciOKoQFDm6ZK0AOHKUfMezO5lD8mTsF7U0Kkm4RIGH1Pgi4L&X-Amz-Signature=3ca09c72b01e54a02cb276fb537d509c233d3bab993f05bf9056c8f969863111&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


