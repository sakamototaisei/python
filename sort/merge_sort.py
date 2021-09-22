# マージソート

def merge_sort(arr):
  if len(arr) > 1:
    res = [] # 返り値の配列
    mid = len(arr) // 2 # 配列の真ん中の値
    L = arr[:mid] # [5,7,6,4] => [5,7]
    R = arr[mid:] # [5,7,6,4] => [6,4]
    L = merge_sort(L)
    R = merge_sort(R)
    i = j = 0 # iはLを探索するインデックス、jはRの探索するインデックス
    while i < len(L) and j < len(R):
      if L[i] < R[j]:
        res.append(L[i])
        i += 1
      elif L[i] > R[j]:
        res.append(R[j])
        j += 1
      else:
        res.append(L[i])
        i += 1
    while i < len(L):
      res.append(L[i])
      i += 1
    while j < len(R):
      res.append(R[j])
      j += 1
    return res
  else:
    return arr

list_a = [5,7,6,4]
print(merge_sort(list_a))