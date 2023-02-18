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
    mock_obj = mocker.patch('translator.GoogleTranslator.get_language_id')
    mock_obj.side_effect = param_select

    text_translated = trans.convert('私の名前は佐藤です。', '日本語', '英語')
    print(text_translated)
    # mock_obj変数の引数の一覧を取得している
    mock_args = mock_obj.call_args_list
    print(mock_args)
    # assert mock_args[0][0][0] == '日本語' # 引数1
    # assert mock_args[1][0][0] == '英語' # 引数2
