# マージソート2

def sort(arr):
  if len(arr) > 1:
    res = []
    mid = len(arr) // 2
    L = arr[:mid]
    R = arr[mid:]
    print('L = {}, R = {}'.format(L, R))
    L = sort(L)
    R = sort(R)
    i = j = 0 # iはLを探索jはRを探索
    print('-' * 20)
    print('append前の L = {}, R = {}, res = {}'.format(L, R, res))
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
    print('append後の L = {}, R = {}, res = {}'.format(L, R, res))
    print('-' * 20)
    return res
  else:
    return arr

list_a = [2,7,4,5,2,1]
print(sort(list_a))