# バブルソート

data = [1,3,2,5,4,2,1]

def sort(data):
  for i in range(len(data)-1, 0, -1):     # 後ろから順に比較していく
    for j in range(i):                    # 未整列の部分を比較
      if data[j] > data[j+1]:               # 隣り合う要素で前の方が大きい場合
        data[j], data[j+1] = data[j+1], data[j] # 要素を入れ替える

sort(data)
print(data)

# for i in range(6):
#   print(i)