import numpy
from PIL import (
    Image,
    ImageEnhance,
    ImageOps
)
import pickle


def moji_command():
    # if not image:
    #     return '画像を指定してください'

    # 学習済みのモデルのロード
    with open('Python_text/pybotweb/trained-model.pickle', 'rb') as b:
        clf = pickle.load(b)


    # 前処理
    # アップされた画像をPillowで開く
    im = Image.open('Python_text/mydigit.jpg')
    # 明暗をはっきりさせる
    im = ImageEnhance.Brightness(im).enhance(3)
    # モノクロームに変換する
    im = im.convert(mode='L')
    # 8ピクセルに四方縮小する
    im = im.resize((8, 8))
    # 明暗を反転させる
    im = ImageOps.invert(im)
    # Numpy ndarrayに変換
    X_bin = numpy.asarray(im)
    # 8x8のNumPy ndarrayを1x64に変換
    X_bin = X_bin.reshape(1, 64)
    # 0~255の値を0~16に変換
    X_bin = X_bin * (16 / 255)

    # 予測
    y_pred = clf.predict(X_bin)
    y_pred = y_pred[0]
    return 'この数字は「{}」です'.format(y_pred)


# with open('Python_text/pybotweb/trained-model.pickle', 'rb') as b:
#     clf = pickle.load(b)
# print(clf)

result = moji_command()
print(result)