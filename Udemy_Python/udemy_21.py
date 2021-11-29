"""
コードスタイルをチェックするツールの確認

pip install pep8        : 軽めのチェック
pip install flake8      : 厳しめチェック
pip install pylint      : もっと厳しくチェック

"""

import os

y           = 1
x = {'gjiosdjg',         'ajofigjoa'}


print('---------------------')


"""
スタイルルール

"""

# コロンいらない
x = 1;
y = 2;

# 80文字以内
x = 'igosjhsnbogjhblsnbo@ihjxbnlksjhsjbsgjgspjlkgjhs'


def test_func(x, y, z,
              giohakabgiujfbvadfnvjnvoifdshjavop='test'):
    """

    :param x:
    :param y:
    :param z:
    :param gioanfbsjhnbpshbjijgangaja@jgkgnoajggjjsgj:
    :return :

    URLは80文字超えてもOK
    See details at: http://sakatai-sahgaihp.com/document//fagbajnvgangjfoadgfjkadhgnkjsdfhgophsdfghsdgjhsoijg
    """

    print('test')


if (x and y) or (x or y):
    print('無駄な丸括弧はつけない')

    x = {
        'test': 'sss'
    }

word = 'hello'
word2 = '!'

new_word = f'{word}{word2}'
print(new_word)


sample_dict = {
    '名前': 'sakatai',
    '年齢': '25',
    '出身': '埼玉県'
}

print('私の名前は{}です'.format(sample_dict.get('名前')))

"""
文字列のシングルクォートかダブルクォートの使い分けはダブルの場合は中にシングルがあるかまたはスペシャルキャラクターがある場合がある
しかし企業やプロジェクトによって変わっていくる

"""

"""
クラスの名前はキャメルケース(大文字区切り)で記述する
変数や関数はスネークケースで(_区切り)記述する
グローバル変数はすべて大文字の_区切りで記述する
"""