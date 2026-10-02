---
source: knowledge-base
origin: notion
title: "single 모드 접속 및 패스워드 변경"
area: "트러블슈팅"
tags: ["area/troubleshooting", "os/linux", "type/troubleshooting"]
created: "2025-08-04T06:05:00.000Z"
last_edited: "2025-08-04T06:30:00.000Z"
status: published
public: true
notion_id: "245172a5-56d6-80ec-b381-d2e88394c8df"
notion_url: "https://www.notion.so/single-245172a556d680ecb381d2e88394c8df"
type: note
updated: 2026-07-07
---

# single 모드 접속 및 패스워드 변경

## 요약

Linux Trouble Shooting

해결 절차를 블로그 글감으로 발전시키기 위한 트러블슈팅 노트입니다.

## 핵심 포인트

- Linux Trouble Shooting
- 참고자료

## 지식 그래프

- [[wiki/mocs/Knowledge Base|Knowledge Base]]
- [[wiki/mocs/트러블슈팅|트러블슈팅]]

## 정리 내용

Centos7 기준입니다.
비밀번호를 까먹어도 접속해서 바꾸는것도 가능한데
나의 경우는 etc/profile 잘못건들여서 아예 접속이 안되는 경우였다.
이럴경우 sigle부팅을 통해서 profile을 롤백하면 된다.
1. os 진입
1. e 버튼을 눌러 edit모드 진입
1. 화면내용의 rhgb quiet 부분을 아래와 같이 변경합니다
  ![[_attachments/notion/single-모드-접속-및-패스워드-변경/245172a556d68120820fc993d6974ea5.png]]
1. init=/bin/bash 로 변경
  1. rhgb quiet을 init=/bin/bash 로 변경합니다
  ![[_attachments/notion/single-모드-접속-및-패스워드-변경/245172a556d681c8bb0fd639d536e953.png]]
1. init=/bin/bash 로 변경후 Ctrl + x 을 눌러 싱글모드로 진입합니다
1. single 모드로 진입후 / 를 마운트 합니다
  1. mount -o remount,rw /
    ![[_attachments/notion/single-모드-접속-및-패스워드-변경/245172a556d681808175f86955b66b9a.png]]
1. root 패스워드를 변경합니다
  ![[_attachments/notion/single-모드-접속-및-패스워드-변경/245172a556d681b692a3fff23e39f5e8.png]]
1. touch /.autorelabel
  1. touch /.autorelabel
  1. selinux 와 관련된 부분입니다서버에Selinux 기능을 [ disable ] 꺼놨다면 위 명령을 안하셔도 됩니다Selinux 기능을 [ enforcing ] 적용이 되어있다면 위 명령을 실행하셔야 합니다
  ![[_attachments/notion/single-모드-접속-및-패스워드-변경/245172a556d68133904bee6467ebb541.png]]
1. reboot
### 참고자료
> [!note] [https://blog.servis.co.kr/index.php/2021/08/05/centos7-single/](https://blog.servis.co.kr/index.php/2021/08/05/centos7-single/)

## 출처

- 원문: https://www.notion.so/single-245172a556d680ecb381d2e88394c8df
- Vault path: wiki/notes/troubleshooting/single-모드-접속-및-패스워드-변경.md
