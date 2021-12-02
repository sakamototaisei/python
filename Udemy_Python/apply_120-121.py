# ロギング
"""
CRITICAL
ERROR
WARNING
INFO
DEBUG
"""
import logging


print('------------------------------------')
# 表示させレベルを設定できる。デフォルトはcriticalからwarningまで。filename='ファイル名'でファイルに出力できる
# logging.basicConfig(filename='test.log', level=logging.DEBUG)
# ロギングのメッセージをカスタマイズできる
# formatter = '%(levelname)s:%(message)s'
formatter = '%(asctime)s:%(message)s'
logging.basicConfig(level=logging.INFO, format=formatter)


# logging.critical('critical')
# logging.error('error')
# logging.warning('warning')
# logging.info('info')
# logging.debug('debug')

# logging.info('info {}'.format('test'))
# logging.info('info %s %s' % ('test', 'test2'))
logging.info('info %s %s', 'test', 'test2')


print('------------------------------------')