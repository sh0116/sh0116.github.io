import argparse
import os
import requests
import datetime
import json

from github import Github, Auth
from notion_client import Client

# GitHub 설정
auth = Auth.Token(os.environ['PERSONAL_GITHUB_ACCESS_KEY'])
g = Github(auth=auth, verify=False)
repo = g.get_repo(f"{os.environ['REPO_OWNER']}/{os.environ['REPO_NAME']}")

# Notion 설정
notion_token = os.environ['NOTION_KEY']
notion = Client(auth=notion_token)
database_id = os.environ['NOTION_DATABASE_ID']

SYNCED_FILE = "github-issues-integration-notion_src/notion_synced.json"

def sync_github_to_notion():
    """
    GitHub Issue → Notion 동기화
    """
    print("🔄 Syncing GitHub Issues to Notion...")

    issues = repo.get_issues(state='all')
    query = notion.databases.query(database_id=database_id)
    notion_issues = {page["properties"]["Title"]["title"][0]["text"]["content"]: page["id"] for page in query["results"] if "Title" in page["properties"]}

    for issue in issues:
        properties = {
            "Title": {
                "title": [
                    {
                        "text": {
                            "content": issue.title,
                        },
                    },
                ],
            },
            "Description": {
                "rich_text": [
                    {
                        "text": {
                            "content": issue.body or "No description",
                        },
                    },
                ],
            },
            "Links": {
                "url": issue.html_url
            },
            "Created At": {
                "date": {
                    "start": issue.created_at.isoformat(),
                    "end": issue.closed_at.isoformat() if issue.closed_at else None,
                },
            },
            "State": {
                "select": {
                    "name": issue.state,
                },
            },
        }

        if issue.title in notion_issues:
            notion.pages.update(page_id=notion_issues[issue.title], properties=properties)
        else:
            notion.pages.create(parent={"database_id": database_id}, properties=properties)

    print("✅ GitHub Issues successfully synced to Notion!")

def download_images(image_urls):
    """
    Notion에서 이미지 다운로드
    """
    image_dir = "notion_images"
    os.makedirs(image_dir, exist_ok=True)
    downloaded_files = []

    for url in image_urls:
        filename = os.path.join(image_dir, os.path.basename(url.split("?")[0]))  # URL에서 파일명 추출
        response = requests.get(url, stream=True)

        if response.status_code == 200:
            with open(filename, 'wb') as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            downloaded_files.append(filename)

    return downloaded_files

def get_plain_text(rich_text):
    """
    Notion rich_text 리스트에서 'text.content' 값들만 순수하게 이어붙여 반환.
    """
    return "".join([t.get("text", {}).get("content", "") for t in rich_text])

def convert_rich_text_to_markdown(rich_text):
    """
    Notion의 rich_text를 Markdown 형식으로 변환 (Jekyll 호환성 확보)
    """
    markdown_text = ""

    for text in rich_text:
        if "text" in text:
            content = text["text"]["content"]
        else:
            # 해당 객체를 JSON 문자열로 변환
            content = f"[RAW: {json.dumps(text, ensure_ascii=False)}]"

        annotations = text.get("annotations", {})

        # 스타일 적용 (HTML 태그 대신 Markdown 문법 사용)
        if annotations.get("code"):
            content = f"`{content}`"
        if annotations.get("bold"):
            content = f"**{content}**"
        if annotations.get("italic"):
            content = f"*{content}*"
        if annotations.get("strikethrough"):
            content = f"~~{content}~~"

        # HTML 태그는 제거: underline, color 등은 무시하거나 markdown 강조로 대체
        # underline은 GitHub/Chirpy에서 지원되지 않음 → bold 처리
        if annotations.get("underline"):
            content = f"**{content}**"

        # 색상 무시 (Jekyll 마크다운은 <span style=...> 등 비호환)
        markdown_text += content

    return markdown_text

def fetch_table_blocks(table_block_id):
    """
    Notion의 테이블 블록을 Markdown 표로 변환
    """
    # 테이블 내부 행 가져오기
    table_rows = notion.blocks.children.list(block_id=table_block_id)["results"]

    if not table_rows:
        return "**[Table Error]** (No table data found)\n\n"

    rows = []

    # 테이블 행 처리
    for row in table_rows:
        if row["type"] == "table_row":
            row_cells = [
                convert_rich_text_to_markdown(cell) if cell else " "
                for cell in row["table_row"]["cells"]
            ]
            rows.append(row_cells)

    if not rows:
        return "**[Table Error]** (No table rows found)\n\n"

    # Markdown 표 생성
    table_width = len(rows[0])  # 첫 행의 컬럼 개수
    markdown_table = ""

    # 헤더 처리 (첫 번째 행을 헤더로 사용)
    header = "| " + " | ".join(rows[0]) + " |"
    separator = "| " + " | ".join(["---"] * table_width) + " |"
    markdown_table += header + "\n" + separator + "\n"

    # 나머지 행 추가
    for row in rows[1:]:
        markdown_table += "| " + " | ".join(row) + " |\n"

    return markdown_table + "\n"

def fetch_page_blocks(page_id):
    """
    Notion 페이지의 모든 블록을 가져와서 Markdown으로 변환
    """
    blocks = notion.blocks.children.list(block_id=page_id)
    markdown_content = ""

    for block in blocks["results"]:
        block_type = block["type"]

        if block_type in ["paragraph", "bulleted_list_item", "numbered_list_item", "quote", "heading_1", "heading_2", "heading_3", "code"]:
            rich_text = block[block_type]["rich_text"]
            if not rich_text:
                continue  # 빈 블록은 무시

        if block_type == "paragraph":
            markdown_content += convert_rich_text_to_markdown(rich_text) + "\n\n"

        elif block_type == "heading_1":
            markdown_content += f"# {convert_rich_text_to_markdown(rich_text)}\n\n"

        elif block_type == "heading_2":
            markdown_content += f"## {convert_rich_text_to_markdown(rich_text)}\n\n"

        elif block_type == "heading_3":
            markdown_content += f"### {convert_rich_text_to_markdown(rich_text)}\n\n"

        elif block_type == "bulleted_list_item":
            markdown_content += f"- {convert_rich_text_to_markdown(rich_text)}\n"

        elif block_type == "numbered_list_item":
            markdown_content += f"1. {convert_rich_text_to_markdown(rich_text)}\n"

        elif block_type == "quote":
            markdown_content += f"> {convert_rich_text_to_markdown(rich_text)}\n\n"

        elif block_type == "code":
            language = block["code"]["language"]
            if language=="plain text":language="text"
            code_text = convert_rich_text_to_markdown(block["code"]["rich_text"])
            markdown_content += f"```{language}\n{code_text}\n```\n\n"

        elif block_type == "image":
            image_data = block["image"]
            image_type = image_data.get("type")

            if image_type == "file":
                image_url = image_data["file"]["url"]
            elif image_type == "external":
                image_url = image_data["external"]["url"]
            else:
                image_url = "UNKNOWN_IMAGE_URL"

            markdown_content += f"![Image]({image_url})\n\n"

        # Bookmark 블록 처리
        elif block_type == "bookmark":
            bm = block["bookmark"]
            url = bm["url"]
            # caption이 있다면 텍스트로 변환
            caption_rich = bm.get("caption", [])
            if caption_rich:
                text = convert_rich_text_to_markdown(caption_rich)
            else:
                text = url
            markdown_content += f"[{text}]({url})\n\n"

        elif block_type == "table":
            markdown_content += fetch_table_blocks(block["id"])

    return markdown_content

def load_synced_data_from_repo():
    """
    GitHub의 notion_synced.json을 불러오며, 파일이 없으면 빈 파일을 생성 후 반환.
    """
    SYNCED_FILE = "github-issues-integration-notion_src/notion_synced.json"

    try:
        contents = repo.get_contents(SYNCED_FILE)
        content_str = contents.decoded_content.decode()
        return json.loads(content_str)
    except Exception as e:
        print(f"⚠️ Synced file not found. Creating new empty sync file... ({e})")
        # 파일이 없다면 빈 JSON 생성
        empty_json = "{}"
        repo.create_file(
            SYNCED_FILE,
            "🆕 Create empty synced Notion data",
            empty_json
        )
        print("🆕 Created empty synced data on GitHub")
        return {}

def save_synced_data_to_repo(data):
    """
    GitHub의 github-issues-integration-notion_src/notion_synced.json 파일을 업데이트하거나 생성
    """
    json_content = json.dumps(data, ensure_ascii=False, indent=2)

    try:
        contents = repo.get_contents(SYNCED_FILE)
        repo.update_file(
            contents.path,
            "🔄 Update synced Notion data",
            json_content,
            contents.sha
        )
        print("🔁 Updated synced data on GitHub")
    except Exception as e:
        repo.create_file(
            SYNCED_FILE,
            "🆕 Create synced Notion data",
            json_content
        )
        print("🆕 Created synced data on GitHub")

def sync_notion_to_github():
    """
    Notion → GitHub Markdown 파일 변환 & Chirpy 블로그 _posts에 업로드
    수정 여부를 확인하여 중복 업로드 방지
    """
    print("🔄 Syncing Notion Pages to GitHub as Chirpy posts...")

    query = notion.databases.query(database_id=database_id)
    synced_data = load_synced_data_from_repo()
    updated_data = {}

    for page in query["results"]:
        page_id = page["id"]
        last_edited_time_str = page.get("last_edited_time")

        if not last_edited_time_str:
            print(f"❗️ Skip page with missing last_edited_time: {page_id}")
            continue

        if synced_data.get(page_id) == last_edited_time_str:
            continue  # 이미 동기화된 페이지와 수정시간이 동일하면 skip

        # ✅ 제목 추출
        #title_key = next((key for key in page["properties"] if page["properties"][key]["type"] == "title"), None)
        #title = convert_rich_text_to_markdown(page["properties"][title_key]["title"]) if title_key else "Untitled"
        #title = title.strip()

        title_key = next((k for k,v in page["properties"].items() if v["type"] == "title"), None)
        if title_key:
            # 마크다운 없이 텍스트만
            title = get_plain_text(page["properties"][title_key]["title"]).strip()
        else:
            title = "Untitled"

        # ✅ description 추출
        description = page["properties"]["Description"]["rich_text"][0]["text"]["content"]

        # ✅ Category 추출
        category_key = "Category"
        notion_categories = []
        if category_key in page["properties"] and page["properties"][category_key]["type"] == "select":
            select_obj = page["properties"][category_key]["select"]
            notion_categories = [select_obj["name"]] if select_obj else []

        categories_yaml = "[" + ", ".join(notion_categories) + "]" if notion_categories else "[Notion, Sync]"

        # ✅ 페이지 내용 추출
        content = fetch_page_blocks(page_id)
        if not content:
            content = "No content"

        # ✅ 날짜 처리
        created_date = datetime.datetime.strptime(page["created_time"], "%Y-%m-%dT%H:%M:%S.%fZ")
        created_date_str = created_date.strftime("%Y-%m-%d")
        created_datetime_str = created_date.strftime("%Y-%m-%d %H:%M:%S")

        slug = title.lower().replace(" ", "-").replace("/", "-")

        # ✅ 태그 추출
        tags_key = next((key for key in page["properties"] if page["properties"][key]["type"] == "multi_select" and key != category_key), None)
        notion_tags = []

        if tags_key:
            notion_tags = [tag["name"] for tag in page["properties"][tags_key]["multi_select"]]

        # 태그 기본값 설정
        tags_yaml = "[" + ", ".join(notion_tags) + "]" if notion_tags else "[notion, automation]"

        # ✅ Chirpy용 Front Matter
        front_matter = f"""---
title: \"{title}\"
date: {created_datetime_str} +0900
categories: {categories_yaml}
tags: {tags_yaml}
description: {description}
toc: true
comments: true
---
"""

        markdown_content = front_matter + "\n" + content + "\n"

        # 이하 파일 업로드 로직은 기존 유지
        # ✅ 업로드 경로
        md_filename = f"_posts/{created_date_str}-{slug}.md"

        try:
            contents = repo.get_contents(md_filename)
            repo.update_file(contents.path, f"Update post from Notion: {title}", markdown_content, contents.sha)
            print(f"🔁 Updated: {title}")
        except:
            repo.create_file(md_filename, f"Create post from Notion: {title}", markdown_content)
            print(f"🆕 Created: {title}")

        # ✅ 최신 수정시간 저장
        updated_data[page_id] = last_edited_time_str

    # ✅ 동기화 완료된 페이지 정보 저장
    if updated_data:
        synced_data.update(updated_data)
        save_synced_data_to_repo(synced_data)

    print("✅ Notion Pages successfully synced to GitHub as blog posts!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sync GitHub Issues and Notion Pages")
    parser.add_argument("mode", choices=["sync_github_to_notion", "sync_notion_to_github"], help="Select sync mode")

    args = parser.parse_args()

    if args.mode == "sync_github_to_notion":
        sync_github_to_notion()
    elif args.mode == "sync_notion_to_github":
        sync_notion_to_github()
