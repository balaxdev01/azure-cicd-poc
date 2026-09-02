# ビルドコンテキストはリポジトリルート。
#   docker build -f apps/svc-a/backend/Dockerfile .
# packages/ を COPY してイメージへ焼き込む構成の検証。

FROM python:3.12-slim

WORKDIR /app

# 共有コードを先にコピー（変更頻度が低いのでレイヤキャッシュが効く）
COPY packages/ ./packages/

# アプリ本体
COPY apps/svc-a/backend/pyproject.toml ./
COPY apps/svc-a/backend/src/ ./src/

# 共有パッケージ → アプリの順にインストール
RUN pip install --no-cache-dir ./packages/pkg-db \
 && pip install --no-cache-dir fastapi uvicorn \
 && pip install --no-cache-dir --no-deps .

EXPOSE 8000

# Web として起動する場合のデフォルト。
# ジョブとして使う場合は Container Apps Jobs 側でコマンドを差し替える:
#   python -m svc_a.entrypoints.jobs
CMD ["uvicorn", "svc_a.entrypoints.http:app", "--host", "0.0.0.0", "--port", "8000"]
