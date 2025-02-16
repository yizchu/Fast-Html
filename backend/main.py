import tracemalloc
import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from utils import new_pages, open_pages

tracemalloc.start()

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(new_pages.router)
app.include_router(open_pages.router)
