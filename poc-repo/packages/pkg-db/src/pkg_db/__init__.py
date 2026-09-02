"""共有パッケージ。イメージへの焼き込みとimportの検証用。"""

__version__ = "0.1.0"


def ping() -> str:
    """呼び出せたことが分かればよい。"""
    return f"pkg-db {__version__} ok"
