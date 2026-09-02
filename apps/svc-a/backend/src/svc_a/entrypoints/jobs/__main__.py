"""ジョブ向けエントリポイント。同一イメージ・別コマンドで起動する検証のジョブ側。"""

import logging
import sys

from pkg_db import ping

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)


def main() -> int:
    logger.info("ジョブ開始")
    logger.info(f"共有コード呼び出し: {ping()}")
    logger.info("ジョブ完了")
    return 0


if __name__ == "__main__":
    sys.exit(main())
