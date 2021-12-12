"""
Pandas : データを効率的扱うために開発されたPythonのライブラリ。データの取り込み加工分析に使う

read_html : 指定されたURL上の表(tableタグ)を取得する
pd.read_html(URL, その他任意の引数)header:ヘッダに指定する行, index_col:インデックスに指定する列, skiprows:読み飛ばす行数
戻り値 : DataFrameをリストで返す

文字列を数値に変換する
pandas.to_numeric(arg, errors)

NaNが含まれている行を削除する
DataFrame.dropna(axis, inplace)

文字列を日付型に変換する
datetime.strptime(文字列, 日付の書式)

DataFrameにインデックスwi設定する
DataFrame.set_index(列名, 任意の引数)

DataFrame(Series)からグラフを描画する
DataFrame(Series).plot(任意の引数)
kind='line'折れ線グラフ 'bar'棒グラフ 'scatter'散布図 'pie'円グラフ

DataFrame(Series)をcsvファイルに出力する
DataFrame(Series).to_csv(保存先のディレクトリ+csvファイル名)
"""
import pandas as pd
import requests
from datetime import datetime as dt


url = 'https://finance.yahoo.com/quote/AAPL/history?p=AAPL'
# 引数のheader=0にすることで最初に読み込まれるものがヘッダに指定できる
data = pd.read_html(requests.get(url, headers={'User-agent': 'Mozilla/5.0'}).text, header=0)
# １つ目のテーブルを呼び出している
# print(data[0].head())
# print(data[0].tail())

# 文字列を数値に変換し,変換できないものはNaNに変換している
data[0]['Adj Close**'] = pd.to_numeric(data[0]['Adj Close**'], errors='coerce')
# NaNの行を削除している。inplace=Trueで変更を保存している
data[0].dropna(inplace=True)
# print(data[0].head())
# print(data[0].tail())

# 新たに日付変換したものw列に追加している
data[0]['Date2'] = [dt.strptime(i, '%b %d, %Y') for i in data[0]['Date']]
data[0].set_index('Date2', inplace=True)
# print(data[0].head())
print(data[0]['Adj Close**'].dtype)

print(data[0]['Adj Close**'].plot(title='AAPL Stock Price', grid=True))

# 株価情報をcsvファイルに保存している
data[0].to_csv('AAPL_Stock.csv')