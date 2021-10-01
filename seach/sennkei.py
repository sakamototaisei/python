# 線形探索を行う関数

data = [1,2,3,4,5,6,7,8,9]
target = 4

def search(data, target):
  for i in range(len(data)): # 先頭から順番に探索
    if data[i] == target: # 見つかった時はその位置のiを返す
      return i
  return -1 # 見つからない場合は-1を返す

print('要素番号{}にデータ{}を見つけました'.format(search(data, target), target))


