"""Web向けエントリポイント。同一イメージをWeb/ジョブで使う検証のWeb側。"""

from fastapi import FastAPI
from pkg_db import ping

app = FastAPI(title="svc-a backend")


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "shared": ping()}
