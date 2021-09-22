# 2文探索

def binary_search(arr, target): # arrが昇順にソートされた配列、target:配列にある探索したい値
  left = 0 # 探索に左端
  right = len(arr) - 1 # 探索の右端
  for i in range(len(arr)): # 配列の長さぶん実行しれば十分
    search_idx = (left + right) // 2 # 中間地(探索のインデックス)
    if arr[search_idx] == target:
      return search_idx
    elif arr[search_idx] > target: # 探索地より大きかったら
      right = search_idx - 1
    elif arr[search_idx] < target:
      left = search_idx + 1
    if left > right:
      return -1

a = [1,2,3,4,5,6]
print(binary_search(a, 4))

