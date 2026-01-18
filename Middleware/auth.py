from fastapi import HTTPException, Request
from typing import List
import os

OLLAMA_TOKEN = os.getenv("OLLAMA_TOKEN", "").split(",")

async def api_key_auth(request: Request):
    if not OLLAMA_TOKEN:
        return
    key = request.headers.get("Authorization")
    if key not in OLLAMA_TOKEN:
        raise HTTPException(status_code=403, detail="Invalid OLAMA_TOKEN")
