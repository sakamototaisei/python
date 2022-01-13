import pandas


def temp_command(command):
    # コマンドを分割して地名を取り出す
    cmd, station = command.split()

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
        response = 'データが見つかりません'

    return response


# result = temp_command('気温データ 東京')
# print(result)
