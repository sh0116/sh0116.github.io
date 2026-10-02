---
source: knowledge-base
origin: notion
title: "Mac에서 Vscode update 이슈"
area: "트러블슈팅"
tags: ["area/troubleshooting", "os/macos", "tool/vscode", "type/troubleshooting"]
created: "2025-08-14T14:50:00.000Z"
last_edited: "2025-08-14T14:55:00.000Z"
status: published
public: true
notion_id: "24f172a5-56d6-80ec-a256-dc4c2a515487"
notion_url: "https://www.notion.so/Mac-Vscode-update-24f172a556d680eca256dc4c2a515487"
type: note
updated: 2026-07-07
---

# Mac에서 Vscode update 이슈

## 요약

Mac에서 Vscode update 이슈 해결 방법

해결 절차를 블로그 글감으로 발전시키기 위한 트러블슈팅 노트입니다.

## 핵심 포인트

- Mac에서 Vscode update 이슈 해결 방법
- 해결 방법
- xattr 이슈 발생 시

## 지식 그래프

- [[wiki/mocs/Knowledge Base|Knowledge Base]]
- [[wiki/mocs/트러블슈팅|트러블슈팅]]

## 정리 내용

#### 해결 방법
Workaround: Move Code out of Downloads and into the Applications folder.
⇒ 다운로드에 있는 Code 파일 Application 폴더로 옮기기
Workaround 2: If updates still don't work after moving Code to the Applications folder, you can 
⇒ 옮겨도 안되면 아래 명령어 실행
```bash
sudo chown $USER ~/Library/Caches/com.microsoft.VSCode.ShipIt/*
xattr -dr com.apple.quarantine /Applications/Visual\ Studio\ Code.app
```
#### xattr 이슈 발생 시 
아래와 같은 권한 이슈가 생긴다면 CLI를 실행하고 있는 인터프리터에 문제가 있는 것임.
Full Disk Access 권한이 없는 것
>> mac 설정 → 보안 설정 → 전체 디스크 접근 권한 → (현재 사용중인 CLI 툴) 추가
```bash
xattr -dr com.apple.quarantine /Applications/Visual\ Studio\ Code.app

xattr: [Errno 1] Operation not permitted: '/Applications/Visual Studio Code.app/Contents/Frameworks/Code Helper (Renderer).app/Contents/MacOS/Code Helper (Renderer)'
xattr: [Errno 1] Operation not permitted: '/Applications/Visual Studio Code.app/Contents/Frameworks/Code Helper (Renderer).app/Contents/MacOS'
xattr: [Errno 1] Operation not permitted: '/Applications/Visual Studio Code.app/Contents/Frameworks/Code Helper (Renderer).app/Contents/Info.plist'
xattr: [Errno 1] Operation not permitted: '/Applications/Visual Studio Code.app/Contents/Frameworks/Code Helper (Renderer).app/Contents/PkgInfo'
xattr: [Errno 1] Operation not permitted: '/Applications/Visual Studio Code.app/Contents/Frameworks/Code Helper (Renderer).app/Contents'
xattr: [Errno 1] Operation not permitted: '/Applications/Visual Studio Code.app/Contents/Frameworks/Code Helper (Renderer).app'
xattr: [Errno 1] Operation not permitted: '/Applications/Visual Studio Code.app/Contents/Frameworks'
xattr: [Errno 1] Operation not permitted: '/Applications/Visual Studio Code.app/Contents/Info.plist'
xattr: [Errno 1] Operation not permitted: '/Applications/Visual Studio Code.app/Contents/PkgInfo'
xattr: [Errno 1] Operation not permitted: '/Applications/Visual Studio Code.app/Contents'
xattr: [Errno 1] Operation not permitted: '/Applications/Visual Studio Code.app'
```

## 출처

- 원문: https://www.notion.so/Mac-Vscode-update-24f172a556d680eca256dc4c2a515487
- Vault path: wiki/notes/troubleshooting/Mac에서-Vscode-update-이슈.md
