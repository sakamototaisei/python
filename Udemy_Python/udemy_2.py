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
