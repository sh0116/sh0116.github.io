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

def convert_rich_text_to_markdown(rich_text):
    """
    Notion의 rich_text를 Markdown 형식으로 변환
    """
    markdown_text = ""

    for text in rich_text:
        content = text["text"]["content"]
        annotations = text.get("annotations", {})

        # 스타일 적용
        if annotations.get("bold"):
            content = f"**{content}**"
        if annotations.get("italic"):
            content = f"*{content}*"
        if annotations.get("underline"):
            content = f"<u>{content}</u>"
        if annotations.get("strikethrough"):
            content = f"~~{content}~~"
        if annotations.get("code"):
            content = f"`{content}`"

        # 색상이 지정된 경우
        color = annotations.get("color")
        if color and color not in ["default"]:
            content = f'<span>$\\color{{{color}}} {content}$</span>'

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
            code_text = convert_rich_text_to_markdown(block["code"]["rich_text"])
            markdown_content += f"```{language}\n{code_text}\n```\n\n"

        elif block_type == "image":
            image_url = block["image"]["file"]["url"]
            markdown_content += f"![Image]({image_url})\n\n"

        elif block_type == "table":
            markdown_content += fetch_table_blocks(block["id"])

    return markdown_content

def load_synced_data():
    if not os.path.exists(SYNCED_FILE):
        return {}
    with open(SYNCED_FILE, "r") as f:
        return json.load(f)

def save_synced_data(data):
    with open(SYNCED_FILE, "w") as f:
        json.dump(data, f)

def sync_notion_to_github():
    """
    Notion → GitHub Markdown 파일 변환 & Chirpy 블로그 _posts에 업로드
    수정 여부를 확인하여 중복 업로드 방지
    """
    print("🔄 Syncing Notion Pages to GitHub as Chirpy posts...")

    query = notion.databases.query(database_id=database_id)
    synced_data = load_synced_data()
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
        title_key = next((key for key in page["properties"] if page["properties"][key]["type"] == "title"), None)
        title = convert_rich_text_to_markdown(page["properties"][title_key]["title"]) if title_key else "Untitled"
        title = title.strip()

        # ✅ 페이지 내용 추출
        content = fetch_page_blocks(page_id)
        if not content:
            content = "No content"

        # ✅ 날짜 처리
        created_date = datetime.datetime.strptime(page["created_time"], "%Y-%m-%dT%H:%M:%S.%fZ")
        created_date_str = created_date.strftime("%Y-%m-%d")
        created_datetime_str = created_date.strftime("%Y-%m-%d %H:%M:%S")

        slug = title.lower().replace(" ", "-").replace("/", "-")

        # ✅ Chirpy용 Front Matter
        front_matter = f"""---\ntitle: "{title}"\ndate: {created_datetime_str} +0900\ncategories: [Notion, Sync]\ntags: [notion, automation]\ndescription: "Notion 동기화된 게시글입니다."\ntoc: true\ncomments: true\n---\n"""

        markdown_content = front_matter + "\n" + content + "\n"

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
    synced_data.update(updated_data)
    save_synced_data(synced_data)

    print("✅ Notion Pages successfully synced to GitHub as blog posts!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sync GitHub Issues and Notion Pages")
    parser.add_argument("mode", choices=["sync_github_to_notion", "sync_notion_to_github"], help="Select sync mode")

    args = parser.parse_args()

    if args.mode == "sync_github_to_notion":
        sync_github_to_notion()
    elif args.mode == "sync_notion_to_github":
        sync_notion_to_github()
