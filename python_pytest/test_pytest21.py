# 例外処理の実行
from translator import GoogleTranslator
import pytest


def test_mock_exception(mocker):
    # 意図的に例外を発生させる
    mock_obj = mocker.patch('translator.GoogleTranslator.get_language_id')
    mock_obj.side_effect = Exception('ConvertException') # 例外を設定

    with pytest.raises(Exception) as e: # 例外オブジェクトをeと指定取得
        trans = GoogleTranslator()
        text_translated = trans.convert('私の名前は佐藤です。', '日本語', '英語')
        print(text_translated)
    # eで例外を取得しているのでvalue.args[0]に具体的なエラーの中身が入っている
    print(e.value.args[0])