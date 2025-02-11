import os
import re
import base64
from fastapi import APIRouter, Body

from dirs import results_dir

router = APIRouter()


@router.get('/get-page/')
async def get_pages():
    pages = []
    for file in os.listdir(results_dir):
        if os.path.isdir(os.path.join(results_dir, file)):
            pages.append(file)
    return pages


@router.post('/open-page/')
async def open_page(page_name: str = Body(..., embed=True)):
    global html_path, css_path
    page_path = os.path.join(results_dir, page_name)
    css_path = os.path.join(page_path, "static", "css")
    html_content = ""
    css_content = ""
    for file in os.listdir(page_path):
        if file.endswith(".html"):
            html_path = os.path.join(page_path, file)
            with open(html_path, 'r', encoding='utf-8') as f:
                html_content = f.read()
    for file in os.listdir(css_path):
        if file.endswith(".css"):
            css_path = os.path.join(css_path, file)
            with open(css_path, 'r', encoding='utf-8') as f:
                css_content = f.read()
    original_content = f"<style>{css_content}</style>{html_content}"

    def image_to_base64(image_path):
        image_path = f"results/{page_name}/" + image_path
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')

    src_pattern = re.compile(r'src="([^"]+)"')
    html_css_content = src_pattern.sub(lambda match: f'src="data:image/{os.path.splitext(match.group(1))[1][1:]};base64,{image_to_base64(match.group(1))}"', original_content)
    bg_pattern = re.compile(r"background-image: url\('([^']+)'\)")
    html_css_content = bg_pattern.sub(lambda match: f"background-image: url('data:image/{os.path.splitext(match.group(1))[1][1:]};base64,{image_to_base64(match.group(1))}')", html_css_content)
    link_pattern = re.compile(r'<link\s+rel="stylesheet"\s+href="[^"]+"\s*/?>', re.IGNORECASE)
    html_css_content = link_pattern.sub('', html_css_content)
    return {"status": "success", "html_css_content": html_css_content, "original_content": original_content}


# 处理修改请求
@router.post('/update-page/')
async def update_page(html_css_content: str = Body(..., embed=True)):
    global html_path, css_path
    css_content = re.search(r'<style.*?>(.*?)</style>', html_css_content, re.DOTALL).group(1)
    html_content = html_css_content.replace(css_content, '')
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css_content)
    return {"status": "success"}
