---
title: "Mac에서 Vscode update 이슈"
date: 2025-08-14 14:50:00 +0900
categories: [Trouble Shooting]
tags: [vscode, mac]
description: Mac에서 Vscode update 이슈 해결 방법
toc: true
comments: true
---

### 해결 방법

**Workaround:** Move Code out of Downloads and into the Applications folder.

⇒ 다운로드에 있는 Code 파일 Application 폴더로 옮기기

**Workaround 2:** If updates still don't work after moving Code to the Applications folder, you can 

⇒ 옮겨도 안되면 아래 명령어 실행

```bash
sudo chown $USER ~/Library/Caches/com.microsoft.VSCode.ShipIt/*
xattr -dr com.apple.quarantine /Applications/Visual\ Studio\ Code.app
```

### xattr 이슈 발생 시 

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


