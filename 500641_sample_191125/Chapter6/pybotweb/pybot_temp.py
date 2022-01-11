import pandas

def temp_command(command):
    cmd, station = command.split()  # コマンドの入力の解釈
    # データの読み込み
    df = pandas.read_csv(  # 気温データを開く
        './data.csv',
        encoding='Shift_JIS',
    )
    df_stations = pandas.read_csv(  # 地点データを開く
        './amedas_stations.csv',
        encoding='Shift_JIS',
        index_col=0,  # 0列目（地点名）をIndexにする
    )
    df = df.join(  # 気温データに地点データを結合する
        df_stations,
        on='station'  # 気温データのstation列の値で結合する
    )
    row = df[df['station'] == station]
    # レスポンスを作成
    if len(row) > 0:
        mean = row['temp'].mean()
        rounded_mean = round(mean, 1)  # 小数を丸める
        response = '平均気温ハ{}度デシタ'.format(rounded_mean)
    else:
        response = 'データガミツカラナイ'
    return response
