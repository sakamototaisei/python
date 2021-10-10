# 数式処理

import numpy as np
import matplotlib.pyplot as plt

a, b = 1, 1
t = np.arange(2, 20, 1) # tを2から順に増やしてみる
f = a / (t + 1)                     # 関数f(t)を計算
g = b / (t ** 2 -t)                 # 関数g(t)を計算
lim = g / t

plt.plot(t, lim)                    # tとlimの関係を表示
plt.show()