---
source: knowledge-base
origin: notion
title: "SSH 접속 시 RSA 충돌 문제 "
area: "트러블슈팅"
tags: ["area/troubleshooting", "os/linux", "protocol/ssh", "type/troubleshooting"]
created: "2025-08-04T06:05:00.000Z"
last_edited: "2025-08-04T06:30:00.000Z"
status: published
public: true
notion_id: "245172a5-56d6-80fe-9dae-cf3e893fa97b"
notion_url: "https://www.notion.so/SSH-RSA-245172a556d680fe9daecf3e893fa97b"
type: note
updated: 2026-07-07
---

# SSH 접속 시 RSA 충돌 문제 

## 요약

Linux Trouble Shooting

해결 절차를 블로그 글감으로 발전시키기 위한 트러블슈팅 노트입니다.

## 핵심 포인트

- Linux Trouble Shooting

## 지식 그래프

- [[wiki/mocs/Knowledge Base|Knowledge Base]]
- [[wiki/mocs/트러블슈팅|트러블슈팅]]

## 정리 내용

AWS EC2 서버에 접속하면 보통 탄력적 IP를 돌려 쓴다
이런 경우에 같은  IP에  SSH 접속 시 로컬 RSA에서 충돌이 난다.
(서버와 RSA공유키를 교환한 상태여서 저장된 경로 따라 갔더니 전혀 다른 서버가 나와서 해킹이라고 의심하는 경우입니다.)
> [!note] @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED! @@@@@@@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY! Someone could be eavesdropping on you right now (man-in-the-middle attack)! It is also possible that a host key has just been changed.
Man in the Middle Attack 이라는 중간자 공격이라는 에러가 발생하며 연결이 되지 않는다.
해결 방법 keygen초기화
```bash
ssh-keygen -R IP주소
```

## 출처

- 원문: https://www.notion.so/SSH-RSA-245172a556d680fe9daecf3e893fa97b
- Vault path: wiki/notes/troubleshooting/SSH-접속-시-RSA-충돌-문제.md
