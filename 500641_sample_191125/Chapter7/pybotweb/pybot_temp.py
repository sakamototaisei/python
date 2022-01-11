import pandas
import pickle

def temp_command(command):
    cmd, station = command.split()
    # 学習済みモデルのロード
    with open('./trained-reg-model.pickle', 'rb') as b:
        reg = pickle.load(b)  # 学習済みモデルを開く
    # データの読み込み
    df = pandas.read_csv(
        './ch6-8.csv',
        encoding='Shift_JIS',
    )
    df_stations = pandas.read_csv(
        './amedas_stations.csv',
        encoding='Shift_JIS',
        index_col=0,
    )
    df = df.join(
        df_stations,
        on='station'
    )
    row = df[df['station'] == station]
    # レスポンスを作成
    if len(row) > 0:
        mean = row['temp'].mean()
        rounded_mean = round(mean, 1)  # 小数を丸める
        response = '平均気温ハ{}度デシタ'.format(rounded_mean)
    else:
        try:
            latitude = float(station)  # 数値以外が入力されるとValueErrorが発生する
            predicted = reg.predict([[latitude]])
            predicted_temp = predicted[0]
            rounded_temp = round(predicted_temp, 1)
            response = 'タブン{}度クライ'.format(rounded_temp)
        except ValueError:  # 緯度以外が指定された場合
            response = '緯度ヲ入力シテクダサイ'
    return response
