# NumPy => 数値演算ライブラリ
import numpy as np
# Matplotlib => グラフを作成し、データを可視化するためのライブラリ
import matplotlib.pyplot as plt
# Pandas => データ加工や集計のためのライブラリ
import pandas as pd


x = np.arange(-5, 6, 1)
print(x)

y = x ** 2
print(y)

plt.plot(x, y)
plt.show()



df = pd.read_csv('FE2019a_distribution.csv', index_col=0, parse_dates=['Score'])
print(df)

print('午前の合計人数', df['AM'].sum())
print('午後の合計人数', df['PM'].sum())

plt.plot(df.index, df['AM'], label='AM') # 午前の折れ線グラフ
plt.plot(df.index, df['PM'], label='PM') # 午前のあれ先グラフ
plt.legend()

plt.show()