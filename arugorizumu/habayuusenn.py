# 幅優先探索

from collections import deque

edge = [[1], [2, 3], [4, 5], [6, 7],
        [], [], [], [8]]

queue = deque()           # キューを作成
queue.append(edge[0][0])  # 根を追加

# エッジのあるノードを追加しながら表示
while len(queue) > 0:
  i = queue.popleft()     # 先頭を取り出す
  print(i, end=' ')
  if i > len(edge):       # 葉がない場合は飛ばす
    continue
for j in edge[i]:         # 新たなノードを追加
  queue.append(j)

