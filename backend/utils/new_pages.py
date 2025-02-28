import os
import shutil
from threading import Thread
from fastapi import UploadFile, File, HTTPException, APIRouter, Body

from dirs import new_dir
from tools.init_html import init_html

router = APIRouter()


@router.post("/new-page/")
async def create_pages(file: UploadFile = File(...)):
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)
    if not file.filename.lower().endswith(".psd"):
        raise HTTPException(400, "仅支持PSD格式文件")

    file_dir = os.path.join(new_dir, os.path.splitext(file.filename)[0])
    with open(file_dir, "wb") as buffer:
        buffer.write(await file.read())

    return {"status": "success"}


@router.delete("/clear-temp/")
async def clear_temp():
    try:
        shutil.rmtree(new_dir)
    except:
        pass
    return {"status": "success"}


@router.delete("/delete-temp/")
async def delete_temp(page_name: str = Body(..., embed=True)):
    try:
        os.remove(os.path.join(new_dir, os.path.splitext(page_name)[0]))
    except:
        pass
    return {"status": "success"}


@router.post("/init-page/")
async def init_pages():
    files = []
    threads = []
    for file_name in os.listdir(new_dir):
        thread = Thread(target=init_html, args=(file_name, os.path.join(new_dir, file_name)))
        files.append(file_name)
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    shutil.rmtree(new_dir)
    return {"status": "success", "file": files[0], "cnt": len(files)}
