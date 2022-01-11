import numpy
from PIL import (
    Image,
    ImageEnhance,
    ImageOps,
)
import pickle


def moji_command(image):
    if not image:
        return '画像ヲシテイシテクダサイ'

    # 学習済みモデルのロード
    with open('./trained-model.pickle', 'rb') as b:
        clf = pickle.load(b)

    # 前処理
    im = Image.open(image.file)  # アップロードされた画像をPillowで開く
    im = ImageEnhance.Brightness(im).enhance(2)  # 明暗をはっきりさせる
    im = im.convert(mode='L')  # モノクロームに変換する
    im = im.resize((8, 8))  # 8ピクセルに四方縮小する
    im = ImageOps.invert(im)  # 明暗を反転させる
    X_bin = numpy.asarray(im) # numpy ndarrayに変換
    X_bin = X_bin.reshape(1, 64) # 8x8のnumpy ndarrayを1x64に変換
    X_bin = X_bin * (16 / 255) # 0～255の値を0～16に変換

    # 予測
    y_pred = clf.predict(X_bin)
    y_pred = y_pred[0]
    return 'コノ数字ハ「{}」デス'.format(y_pred)
