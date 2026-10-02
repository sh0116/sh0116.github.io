#!/usr/bin/env python3
"""Copy publishable notes from the private Obsidian vault into ./content.

Rules (fail closed):
  * only files under <vault>/wiki/ are considered
  * frontmatter must contain `public: true`
  * `draft: true` or `status: draft` is skipped
  * internal files (log.md, hot.md, meta/) are never published
  * a note containing a BLOCK pattern (secrets, server paths, private hosts)
    is NOT copied; it is listed in the report so a human can fix it
  * referenced attachments are copied from <vault>/_attachments
  * files previously published but no longer eligible are removed

Usage:
  python3 scripts/publish.py            # dry run, prints report
  python3 scripts/publish.py --apply    # write into ./content
"""
import argparse
import json
import os
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"
MANIFEST = ROOT / "scripts" / ".published.json"
ALLOW = ROOT / "scripts" / "publish-allow.txt"  # reviewed false positives: "<rel path>  <pattern name>"

EXCLUDE_NAMES = {"log.md", "hot.md"}
EXCLUDE_DIRS = {"meta"}

BLOCK = {
    "openai-key": r"sk-[A-Za-z0-9_-]{20,}",
    "github-token": r"gh[pousr]_[A-Za-z0-9]{20,}",
    "aws-key-id": r"AKIA[0-9A-Z]{16}",
    "slack-token": r"xox[abprs]-[A-Za-z0-9-]{10,}",
    "private-key": r"BEGIN (RSA |EC |OPENSSH |)PRIVATE KEY",
    "server-path": r"/home/pi\b",
    "tailscale-host": r"\.ts\.net\b",
    "tailscale-ip": r"\b100\.(6[4-9]|[7-9]\d|1[01]\d|12[0-7])\.\d{1,3}\.\d{1,3}\b",
    "private-email": r"[\w.+-]+@(naver|gmail|daum|kakao)\.com",
}
BLOCK_RE = {k: re.compile(v) for k, v in BLOCK.items()}

FM_RE = re.compile(r"\A---\n(.*?)\n---\n", re.S)
IMG_RE = re.compile(r"!\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]|!\[[^\]]*\]\(([^)\s]+)")


def frontmatter(text):
    m = FM_RE.match(text)
    return m.group(1) if m else ""


def fm_value(fm, key):
    m = re.search(rf"^{key}:\s*(.*?)\s*$", fm, re.M)
    return m.group(1).strip("\"'") if m else None


def load_allow():
    allowed = set()
    if ALLOW.exists():
        for line in ALLOW.read_text().splitlines():
            line = line.split("#")[0].strip()
            if line:
                parts = line.split()
                allowed.add((parts[0], parts[1] if len(parts) > 1 else "*"))
    return allowed


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--vault", default=os.environ.get("VAULT", str(Path.home() / "vault")))
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    vault = Path(args.vault)
    wiki = vault / "wiki"
    att_dir = vault / "_attachments"
    allowed = load_allow()

    selected, blocked, skipped = [], [], 0
    for p in sorted(wiki.rglob("*.md")):
        rel = p.relative_to(wiki)
        if p.name in EXCLUDE_NAMES or rel.parts[0] in EXCLUDE_DIRS:
            continue
        text = p.read_text(errors="ignore")
        fm = frontmatter(text)
        if fm_value(fm, "public") != "true" or fm_value(fm, "draft") == "true" or fm_value(fm, "status") == "draft":
            skipped += 1
            continue
        hits = []
        for name, rx in BLOCK_RE.items():
            if (str(rel), name) in allowed or (str(rel), "*") in allowed:
                continue
            for i, line in enumerate(text.splitlines(), 1):
                if rx.search(line):
                    hits.append((name, i))
                    break
        if hits:
            blocked.append((rel, hits))
        else:
            selected.append((p, rel, text))

    # attachments
    attachments = {}
    for p, rel, text in selected:
        for m in IMG_RE.finditer(text):
            ref = m.group(1) or m.group(2)
            if ref.startswith(("http://", "https://", "data:")):
                continue
            name = Path(ref).name
            hit = next(iter(att_dir.rglob(name)), None) if att_dir.exists() else None
            if hit:
                attachments[name] = hit

    print(f"vault: {vault}")
    print(f"publish: {len(selected)} notes, {len(attachments)} attachments | skipped (not public/draft): {skipped} | BLOCKED: {len(blocked)}")
    for rel, hits in blocked:
        print(f"  BLOCKED {rel}: " + ", ".join(f"{n}@L{ln}" for n, ln in hits))

    if not args.apply:
        print("dry run; use --apply to write")
        return 0

    old = set(json.loads(MANIFEST.read_text())) if MANIFEST.exists() else set()
    new = set()
    for p, rel, text in selected:
        dest = CONTENT / "wiki" / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(text)
        new.add(str(dest.relative_to(CONTENT)))
    for name, src in attachments.items():
        dest = CONTENT / "attachments" / name
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dest)
        new.add(str(dest.relative_to(CONTENT)))
    for stale in old - new:
        f = CONTENT / stale
        if f.exists():
            f.unlink()
    for d in sorted((CONTENT / "wiki").rglob("*"), reverse=True):
        if d.is_dir() and not any(d.iterdir()):
            d.rmdir()
    MANIFEST.write_text(json.dumps(sorted(new), ensure_ascii=False, indent=1))
    print(f"written to {CONTENT} (removed {len(old - new)} stale)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
