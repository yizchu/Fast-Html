import os
import shutil
import tracemalloc
import logging
from fastapi import FastAPI
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from utils.init_html import init_html

tracemalloc.start()

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

temp_dir = os.path.join(os.path.dirname(__file__), 'temp')
new_dir = os.path.join(temp_dir, "new")


# 新建工程
@app.post('/new-page/')
async def create_pages(file: UploadFile = File(...)):
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)
    if not file.filename.lower().endswith(".psd"):
        raise HTTPException(400, "仅支持PSD格式文件")

    file_dir = os.path.join(new_dir, file.filename[:-4])
    with open(file_dir, "wb") as buffer:
        buffer.write(await file.read())

    return {"status": "success"}


@app.delete('/clear-temp/')
async def clear_temp():
    try:
        shutil.rmtree(new_dir)
    except:
        pass
    return {"status": "success"}


@app.post('/init-page/')
async def init_pages():
    files = []
    for file_name in os.listdir(new_dir):
        await init_html(file_name, os.path.join(new_dir, file_name))
        files.append(file_name)
    shutil.rmtree(new_dir)
    return {"status": "success", "file": files[0], "cnt": len(files)}


# 打开工程
@app.get('/open-page/')
async def open_pages():
    files = os.listdir(os.path.join(os.path.dirname(__file__), 'results'))
    return {"status": "success", "files": files}
