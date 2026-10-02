---
source: knowledge-base
origin: notion
title: "토이 프로젝트 - Github 잔디 깍기 도구 "
area: "프로젝트"
tags: ["area/projects", "tool/github", "type/project"]
created: "2025-08-04T06:05:00.000Z"
last_edited: "2026-05-30T06:51:00.000Z"
status: published
public: true
notion_id: "245172a5-56d6-800f-b44b-f9a7321f1e1b"
notion_url: "https://www.notion.so/Github-245172a556d6800fb44bf9a7321f1e1b"
type: note
updated: 2026-07-07
---

# 토이 프로젝트 - Github 잔디 깍기 도구 

## 요약

잔디깍기

개념, 구현 맥락, 후속 학습거리를 지식 그래프에 연결하기 위한 정리 노트입니다.

## 핵심 포인트

- https://github.com/sh0116/GithubContributionVisualizer
- Github Contribution Visualizer
- 예시
- Github Repo

## 지식 그래프

- [[wiki/mocs/Knowledge Base|Knowledge Base]]
- [[wiki/mocs/프로젝트|프로젝트]]

## 정리 내용

## Github Contribution Visualizer
깃허브 잔디 깍다가 Notion 에 가시화하고 싶은 마음이 생겼는데 마땅한 도구가 없어 만들기로 했다. AWS ec2 기반의 Flask 컨테이너를 배포하여 엔드포인트를 구성했다. 컨테이너의 주요 기능은 사용자의 UserName과 Image의 크기를 입력하면 해당 유저의 커밋 기록과 기본 정보를 크롤링하여 가시화하여 이미지로 반환한다. 
### 예시
![[_attachments/notion/토이-프로젝트---Github-잔디-깍기-도구/245172a556d6810497ebd653df7fc81e.png]]
위 사진은 노션에서 이미지 링크 임베드를 통해서 가져온 이미지이다. 실시간으로 링크에 접속하면 커밋 기록을 크롤링하여 이미지로 반환한다. 
이 이미지는 연속으로 얼마나 잔디를 깍았는지 보여준다. 
#### Github Repo
- https://github.com/sh0116/GithubContributionVisualizer

## 출처

- 원문: https://www.notion.so/Github-245172a556d6800fb44bf9a7321f1e1b
- Vault path: wiki/notes/projects/토이-프로젝트---Github-잔디-깍기-도구.md
