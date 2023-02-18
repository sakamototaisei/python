# 引数によって返り値を複数設定する
# translator.pyのGoogleTranslatorを呼び出してテスト
from translator import GoogleTranslator
import pytest

# 前処理の設定
@pytest.fixture(scope='module')
def trans():
    t = GoogleTranslator()
    print('create Translator')
    return t


def test_japanese_to_english(trans, mocker):
    # 返り値のパターン生成
    def param_select(param):
        if param == '日本語':
            return 'ja'
        else:
            return 'fr'
    # side_effect=param_selectで関数定義することにより引数のパターンを作成できる
    mocker.patch('translator.GoogleTranslator.get_language_id', side_effect = param_select)
    text_translated = trans.convert('私の名前は佐藤です。', '日本語', '英語')
    print(text_translated)
