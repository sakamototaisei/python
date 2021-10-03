# 選択ソート

data = [1,3,2,5,4,2,1]

def sort(data):
  for i in range(0, len(data)-1):           # 最初から順に選択していく
    min_1 = i                               # 最小値の位置をmin_1に決める
    for j in range(i+1, len(data)):         # 最小値を探すループ
      if data[min_1] > data[j]:             # より小さい値があれば、最小値を置き換える
        min_1 = j
    data[min_1], data[i] = data[i], data[min_1] # 最小値の場所と要素を入れ替える

sort(data)
print(data)
