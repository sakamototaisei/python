# セクション4 データ構造
# リスト型

l = [1, 20, 4, 50, 2, 1, 2]
print(l)
print(l[0])
print(l[-1])
print(l[-2])
print(l[2:])
print(len(l))

print('--------------------')

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(n[::2])
print(n[::-1])

print('--------------------')

a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)
print(x[0])
print(x[1])
print(x[0][1])    # ネストしたリストのbを取得したい場合

print('--------------------')

# ---------------------------------------------------------------
# リストの操作

s = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
s[0] = 'x'
print(s)

print(s[2:5])
s[2:5] = ['C', 'D', 'E']
print(s)

s[2:5] = []
print(s)

s[:] = []
print(s)

print('--------------------')

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n.append(100)         # リストの最後に追加
print(n)

n.insert(0, 200)      # 引数にインデックス番号で挿入場所を指定できる
print(n)

print(n.pop())
print(n.pop(0))
print(n)
del n[0]
print(n)
# del n     del で全部消すこともできるから理解して使う
# print(n)
print('--------------------')

n = [1, 2, 2, 2, 3]
n.remove(2)
print(n)
n.remove(2)
print(n)
n.remove(2)
print(n)
# n.remove(2)         # 消すものがない場合エラーになる

print('--------------------')

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]

x = a + b
print(x)
print(a)              # aとbはそのまま
print(b)
print('--------------------')
a += b                # aにbを加えて上書きされる
print(a)
print(b)
print('--------------------')

x = [1, 2, 3, 4, 5]
y = [6, 7, 8, 9, 10]
x.extend(y)           # extend() xにyを加えて拡張される
print(x)

print('--------------------')


# ---------------------------------------------------------------
# リストのメソッド

r = [1, 2, 3, 4, 4, 5, 1, 2, 3]
# index() 第一引数の値がリストのどこのインデックス番号に存在するか探す。第二引数でどこのインデックス番号から探すか指定できる
print(r.index(3, 3))

print(r.count(3))
print(r)

if 5 in r:
    print('exist')

print('--------------------')

r.sort()        # sort() 1~並び替えする
print(r)
r.sort(reverse=True)
print(r)
r.reverse()     # reverse() 上記の逆順に並び替えを行う
print(r)

print('--------------------')

s = 'My name is Mike.'
to_split = s.split(' ')     # split() 引数の条件でリストの条件で作成できる
print(to_split)

x = ' ### '.join(to_split)      # join() リストを' 'で繋げてくれる
print(x)

print('--------------------')


# ---------------------------------------------------------------
# リストのコピー

i = [1, 2, 3, 4, 5]
j = i
j[0] = 100
print('i =', i)
print('j =', j)

x = [1, 2, 3, 4, 5]
# y = x[:] これでもコピーできる
y = x.copy()
y[0] = 100
print('x =', x)
print('y =', y)

x = 20
y = x
y = 5
print(id(x))
print(id(y))
print(x)
print(y)

print('--------------------')

x = ['a', 'b']
y = x
y[0] = 'p'
print(id(x))
print(id(y))
print(x)
print(y)

print('--------------------')


# ---------------------------------------------------------------
# リストの使い方

seat = []
min = 0
max = 5
print(min <= len(seat) < max)
seat.append('p')
seat.append('p')
print(min <= len(seat) < max)
seat.append('p')
seat.append('p')
print(min <= len(seat) < max)
seat.append('p')
seat.append('p')
print(min <= len(seat) < max)
seat.pop(0)
print(min <= len(seat) < max)
seat.pop(0)
print(min <= len(seat) < max)

print('--------------------')


# ---------------------------------------------------------------
# タプル 値を書き換えられない 読み込みくらい

t = (1, 2, 3, 4, 1, 2)
print(t)
print(type(t))
print(t.count(1))

t = ([1, 2, 3], [4, 5, 6])
print(t)
print(t[0][0])
t[0][0] = 100       # これだと値を変えられる
print(t)
print(type(t))

t = 1, 2, 3         # ()これなくてもタプルとなる
print(t)
t = 1               # int型
t = (1)             # int型
t = 1,              # ,でtuple型になる
print(type(t))

new_tuple = (1, 2, 3) + (4, 5, 6)

print(new_tuple)

print('--------------------')


# ---------------------------------------------------------------
# タプルのアンバッキング

num_tuple = (10, 20)

x, y = num_tuple
print(x, y)

min, max = 0, 100
print(min, max)

i = 10
j = 20
print(f'入れ替え前 i = {i}, j = {j}')
tmp = i
i = j
j = tmp
print(f'入れ替え後 i = {i}, j = {j}')
print('--------------------')

a = 100
b = 200
print(f'アンパッキング前 a = {a}, b = {b}')
a, b = b, a
print(f'アンパッキング後 a = {a}, b = {b}')

print('--------------------')


# ---------------------------------------------------------------
# タプルの使い方

chose_from_two = ('A', 'B', 'C')

answer = []
answer.append('A')
answer.append('C')

print(chose_from_two)
print(answer)

print('--------------------')


# ---------------------------------------------------------------
# 辞書型

d = {'x': 10, 'y': 20}
print(d)
print(type(d))
print(d['x'])
print(d['y'])
d['x'] = 100
print(d)
d['x'] = 'xxx'
print(d)
d['z'] = 200
print(d)
d[1] = 10000
print(d)

print(dict(a=10, b=20))                 # 辞書型の生成
print(dict([('a', 10), ('b', 20)]))     # 辞書型の生成2

print('--------------------')


# ---------------------------------------------------------------
# 辞書型のメソッド

d = {'x': 10, 'y': 20}
print(d.keys())
print(d.values())
d2 = {'x': 1000, 'j': 500}
d.update(d2)
print(d)

print(d.get('x'))       # get()　ある場合は値を、ない場合はNoneを返す
r = d.get('z')
print(type(r))

d.pop('x')
print(d)
del d['y']              # del は全消しすることもできるから気をつける
print(d)

d = {'a': 100, 'b': 200}
print('a' in d)         # キーの確認ができる
print('j' in d)

print('--------------------')


# ---------------------------------------------------------------
# 辞書のコピー

x = {'a': 1}
y = x
y['a'] = 1000
print(x)
print(y)
print('--------------------')
x = {'a': 1}
y = x.copy()        # リスト同様参照渡しでcopy()を使う
y['a'] = 1000
print(x)
print(y)

print('--------------------')


# ---------------------------------------------------------------
# 辞書型の使う方 値を検索して持ってきたいとき　スピードが速い　本の目次的な

fruits = {
    'apple': 100,
    'banana': 200,
    'orange': 300,
}

print(fruits['apple'])

print('--------------------')


# ---------------------------------------------------------------
# 集合型 重複を許さない

a = {1, 2, 2, 3, 4, 4, 5, 6}    # a = {1, 2, 3, 4, 5, 6}

print(a)
print(type(a))

b = {2, 3, 3, 6, 7}             # b = {2, 3, 6, 7}
print(b)
print(a - b)                    # {1, 4, 5}
print(b - a)                    # {7}
print(a & b)                    # {2, 3, 6}
print(a | b)                    # {1, 2, 3, 4, 5, 6, 7}
print(a ^ b)                    # {1, 4, 5, 7}

print('--------------------')


# ---------------------------------------------------------------
# 集合のメソッド

s = {1, 2, 3, 4, 5}
s.add(6)                # 最後に追加できる
print(s)
s.remove(6)             # 集合の中身を指定して削除できる
print(s)
s.clear()               # 中身を全消し      からはset()で帰ってくる
print(s)

a = {}
print(type(a))

print('--------------------')


# ---------------------------------------------------------------
# 集合の使い方 ユニークの値を取得したいときに使う

my_friends = {'A', 'C', 'D'}
A_friends = {'B', 'D', 'E', 'F'}
print(my_friends & A_friends)

f = ['apple', 'banana', 'apple', 'banana']
kind = set(f)
print(kind)