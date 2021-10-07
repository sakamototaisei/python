# 深さ優先探索

node = ['', '+', 'X', '-', '6', '2', '3', '1']
edge = [[1], [2, 3], [4, 5], [6, 7]]


def deep_search(i):
    print(node[i], end=' ')
    if i < len(edge):           # 葉がない場合は飛ばす
        deep_search(edge[i][0])   # 左部分木を探索
    if i < len(edge) and len(edge[i]) == 2:
        deep_search(edge[i][1])   # 右部分木を探索


deep_search(edge[0][0])
