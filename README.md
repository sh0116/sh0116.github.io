# FAST01

Obsidian 볼트(비공개)에서 LLM이 쓴 글 중 **공개로 표시한 것만** [Quartz](https://quartz.jzhao.xyz)로 배포하는 블로그.

## 흐름

1. 볼트 `wiki/` 아래 노트의 머리말에 `public: true`를 넣는다. (`draft: true` 또는 `status: draft`는 제외)
2. `python3 scripts/publish.py` 로 미리보기, `--apply` 로 `content/`에 복사한다.
   - 비밀키, 서버 경로, 내부 호스트, 개인 이메일이 있는 글은 복사되지 않고 목록으로 표시된다.
   - 검토 후 안전한 경우에만 `scripts/publish-allow.txt`에 `<상대경로> <패턴이름>` 으로 예외를 적는다.
3. `git add content && git commit && git push` 하면 GitHub Actions가 빌드해서 Pages에 배포한다.

## 로컬 미리보기

```bash
npm ci && npm run install-plugins
npx quartz build -d content --serve
```

이전 Jekyll 블로그는 `legacy-jekyll` 브랜치에 있다.
