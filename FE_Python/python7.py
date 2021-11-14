"""
Pythonでのスタック、キューの表現

deque型のメソッド
deque.append(x)     dequeの末尾にxを追加
deque.appendleft(x) dequeの先頭にxを追加
deque.pop()         dequeの末尾を取り出し、その値を返す
deque.popleft()     dequeの先頭を取り出し、その値を返す
"""

from collections import deque
from typing import NewType

# deque型のインスタンスを作成
Q = deque()
Q.append('A')
Q.append('B')
Q.append('C')
print(Q)

print(Q.popleft())
print(Q)

print('---------------------------')

"""
線形探索 n
データを先頭から順番に探索していく単純なアルゴリズム
"""

def search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return i
    # 見つからない場合は-1を返す
    return -1

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# target = int(input('探索する数字を入力してください : '))
# print('要素番号{}にデータ{}を見つけました。'.format(search(data, target), target))


"""
2分探索 log n
データをあらかじめ整列させて、最初に真ん中のデータと探索するデータを比較する。
2つのデータの関係から前後どちらかのグループに目的のデータがあるかを予測し、そのグループの真ん中のデータと比較する
"""


def search_2(data, target):
    start, end = 0, len(data)-1
    while start <= end:
        i = (start + end) // 2
        if data[i] == target:
            return i
        elif data[i] < target:
            start = i + 1
        else:
            end = i - 1
    return -1

target = 3
print('要素番号{}にデータ{}を見つけました。'.format(search_2(data, target), target))

print('---------------------------')


""""
バブルソート n**
隣り合う要素を比較して大小の順が逆なら入れ替える操作を繰り返すアルゴリズム
"""

def bubble_sort(data):
    for i in range(len(data)-1, 0, -1):
        for j in range(i):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]


data = [1, 3, 2, 5, 4, 2, 1]
bubble_sort(data)
print('バブルソート : ',data)


print('---------------------------')


"""
挿入ソート n**
整列された列に、新たに要素を1つずつ適切な位置に挿入する操作を繰り返すアルゴリズム
"""


def sonyu_sort(data):
    for i in range(0, len(data)):
        for j in range(i-1, -1, -1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
            else:
                break


data = [1, 3, 2, 5, 4, 2, 1]
sonyu_sort(data)
print('挿入ソート : ',data)


print('---------------------------')


"""
選択ソート n**
未整列の部分から最大値(または最小値)を検索し、それを繰り返すことにで整列させていくアルゴリズムです
"""


def choice_sort(data):
    for i in range(0, len(data)-1):
        min_i = i
        for j in range(i+1, len(data)):
            if data[min_i] > data[j]:
                min_i = j
        data[min_i], data[i] = data[i], data[min_i]
        print(data)

data = [1, 3, 2, 5, 4, 2, 1]
choice_sort(data)
print('選択ソート : ',data)


print('---------------------------')


"""
シェルソート n log n
ある一定間隔おきに取り出した要素からなる部分列をそれぞれ整列させ、さらに間隔を狭めて同様の操作を繰り返し
最後に間隔を1にして完全に整列させるアルゴリズム
"""

def shell_sort(data):
    gaps = [7, 3, 1]
    for gap in gaps:
        for start in range(gap):
            for i in range(start, len(data), gap):
                for j in range(i-gap, -1, -gap):
                    if data[j] > data[j+gap]:
                        data[j], data[j+gap] = data[j+gap], data[j]
                    else:
                        break
        print(data)

data = [1, 3, 2, 5, 4, 2, 1]
shell_sort(data)
print('シェルソート : ',data)



print('-------------------------')


"""
ヒープソート n log n

heappush(heap, value) valueの値がヒープに挿入され、
heappop(heap)で、ヒープの中の最小値が取り出される
"""

from heapq import heappush, heappop

def sort(data):
    # からのヒープリストを作成
    heap = []

    while data:
        heappush(heap, data.pop())
    while heap:
        data.append(heappop(heap))


data = [1, 3, 2, 5, 4, 2, 1]
sort(data)
print(data)


print('-------------------------')


"""
再帰
"""

def f(n):
    if n <= 1:
        return n
    else:
        return n + f(n-1)

print(f(5))


print('-------------------------')


"""
クイックソート

"""


def sort(data):

    n = len(data)
    # 真ん中の値を利用
    pivot = data[n//2]
    print('pivot = {}'.format(pivot))
    left, right, middle = [], [], []

    for i in range(n):
        if data[i] < pivot:
            left.append(data[i])
        elif data[i] > pivot:
            right.append(data[i])
        else:
            middle.append(data[i])

    if left:
        left = sort(left)
    if right:
        right = sort(right)

    return left + middle + right


data = [1, 3, 2, 5, 4, 2, 1]
print(sort(data))


print('-------------------------')


"""
グラフのアルゴリズム

"""

edge = [[1], [2, 3], [4, 5], [6, 7],
        [], [], [], [8]]

# キューを作成
queue = deque()
# 根を追加
queue.append(edge[0][0])
print('queue = {}'.format(queue))


while len(queue) > 0:
    print('len(queue) = {}, queue = {}'.format(len(queue), queue))
    # 先頭を取り出す
    i = queue.popleft()
    print('popleft()  = {}'.format(i))
    # 歯がない場合は飛ばす
    if i >= len(edge):
        continue
    # 新たなノードを追加
    for j in edge[i]:
        queue.append(j)