# NumPy => 数値演算ライブラリ
import numpy as np
# Matplotlib => グラフを作成し、データを可視化するためのライブラリ
import matplotlib.pyplot as plt


x = np.arange(-5, 6, 1)
print(x)

y = x ** 2
print(y)

plt.plot(x, y)
plt.show()