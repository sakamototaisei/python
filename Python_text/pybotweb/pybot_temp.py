import pandas
import pickle
from sklearn.metrics import r2_score


def temp_command(command):
    # コマンドを分割して地名を取り出す
    cmd, station = command.split()
    # 学習済みモデルのロード
    with open('/Users/sakamototaisei/Desktop/python/Python_text/trained-reg-model.pickle', 'rb') as b:
        reg = pickle.load(b)

    df = pandas.read_csv(
        '/Users/sakamototaisei/Desktop/python/Python_text/pybotweb/data.csv',
        encoding='shift_JIS'
    )
    df_stations = pandas.read_csv(
        '/Users/sakamototaisei/Desktop/python/Python_text/pybotweb/amedas_stations.csv',
        encoding='shift_JIS',
        # 0列目をindexにする
        index_col=0
    )
    # 気温のデータと結合する
    df = df.join(
        df_stations,
        # 気温のデータのstation列の値で結合する
        on='station'
    )

    # データの検索
    row = df[df['station'] == station]
    # レスポンス作成
    if len(row) > 0:
        mean = row['temp'].mean()
        # 少数を丸める
        rounded_mean = round(mean, 1)
        response = '平均気温は{}度でした'.format(rounded_mean)
    else:
        try:
            # 緯度はstation変数に入っている
            latitude = float(station)
            # 気温を予測する
            predicted = reg.predict([[latitude]])
            # 予測された気温を取り出す
            predicted_temp = predicted[0]
            rounded_temp = round(predicted_temp, 1)
            # pybotの返事を作る
            response = 'おそらく{}度くらい'.format(rounded_temp)
        # 緯度以外が指定された場合
        except ValueError:
            response = '緯度を入力してください'

        # response = 'データが見つかりません'

    return response


# result = temp_command('気温データ 東京')
# print(result)
