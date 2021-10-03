# ヒープソート

from heapq import heappush, heappop # ヒープを扱う標準ライブラリheapqを利用

data = [1,3,2,5,4,2,1]

def sort(data):
  heap = []                     # 空のヒープリストを作成
  while data:                   # dataから要素を取り出して、ヒープに入れる
    heappush(heap, data.pop())  # dataの最後の要素を取り出して、heappushでheapに入れる
  while heap:                   # heapから順に要素を取り出して、dataに戻す
    data.append(heappop(heap))  # heapから最小値を取り出して、dataの最後に追加する

sort(data)
print(data)