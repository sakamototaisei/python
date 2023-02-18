"""ロギングの書き方"""
import logging


logger = logging.getLogger(__name__)

logger.error('Api call is failed')

"""
システムで重要な関数の中にロギングを記述したりする
トラブル態様、システムのトラブルの箇所解析してトラブル解決の助けになる

"""
logger.error({
    'action': 'create',
    'status': 'fail',
    'message': 'Api call is failed'
})