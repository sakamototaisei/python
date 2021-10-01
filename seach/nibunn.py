# 2分探索を行う関数

data = [1,2,3,4,5,6,7,8,9]
target = 4

def search(data, target):
  start, end = 0, len(data) - 1 # 探索するデータの始点startと終点endを設定
  while start <= end:
    i = (start + end) // 2      # 真ん中のデータをiとする
    if data[i] == target:       # 見つかった時はその位置iを返す
      return i
    elif data[i] < target:      # targetの値の方が大きい場合は後のグループを探索
      start = i + 1
    else:                       # そうでない場合は前のグループを探索
      end = i - 1
  return -1                     # 見つからない時は-1を返す

print('要素番号{}にデータ{}を見つけました'.format(search(data, target), target))


