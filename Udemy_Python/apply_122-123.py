"""
CRITICAL
ERROR
WARNING
INFO
DEBUG
"""
import logging

import logtest

logging.basicConfig(level=logging.INFO)

# logging.info('info')

# # これを使うときgetLogger(__name__)引数はこれが有効
# logger = logging.getLogger(__name__)
# # ここでlevelの設定をし直している
# logger.setLevel(logging.DEBUG)
# logger.debug('debug')

logger = logging.getLogger(__name__)
logger.info('from main')

logtest.do_something()