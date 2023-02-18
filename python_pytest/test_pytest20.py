# 例外処理の実行
from translator import GoogleTranslator
import pytest


# ポルトガル語は設定していないのでキーエラーとなるのでこれをクリアしたい
def test_convert():
    with pytest.raises(KeyError): # Exception TypeError ValueError
        trans = GoogleTranslator()
        trans.convert('私の名前は佐藤です。', '日本語', 'ポルトガル語')
