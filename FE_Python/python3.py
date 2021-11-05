"""基本情報技術者 Python 対策"""

# 2進数=>10進数は先頭に0b
print(0b11)

# 8進数=>10進数は先頭に0o
print(0o11)

# 16進数=>10進数は先頭に0x
print(0x11)

print('----------------------------------')

# 10進数=>2進数
print(bin(3))

# 10進数=>8進数
print(oct(9))

# 10進数=>16進数
print(hex(17))

print('----------------------------------')


"""
代表的な文字列のメソッド

str.lstrip()        文字列の先頭の空白文字を除去する
str.rstrip()        文字列の末尾の空白文字を除去する
str.strip()         文字列の先頭及び末尾の空白文字を除去する
str.lower()         文字列の大文字を全て小文字にする
str.upper()         文字列の小文字を大文字にする
str.split(sep)      文字列をsepを区切り文字にして分割し、リストにする
"""

s = 'hello'
s1 = 'HELLO'
s2 = ' sakatai '
s3 = 'My name is sakatai'


print(s2.lstrip())
print(s2.rstrip())
print(s2.strip())
print(s1.lower())
print(s.upper())

l = s3.split(' ')
print(l)

print('----------------------------------')


"""
リストの主なメソッド

list.append()           リストの末尾に要素を1つ追加する
list.extend(iterable)   イテレーターを示す変数の全ての要素を対象の要素に追加し、リストを拡張する
list.insert(i, x)       添字のiで指定した位置に要素をxに挿入する
list.remove(x)          リストの中でxと等しい値を持つ最初の要素を削除する。該当する要素がなければValueErrorとなる
list.pop([i])           添字のiの位置にある要素をリストから削除し、その要素返す。添字を指定しないlist.pop()はリストの末尾の要素を追加して返す。
list.clear()            リストの中の全ての要素を削除する
list.index(x)           リストの中でxと等しい値を持つ最初の要素の位置をゼロから始まる添字で返す。該当する要素がなければValueErrorとなる
list.count(x)           リストでのxの出現回数を返す
list.sort(key, reverse) リストの項目をインプレース演算でソートする。key, reverseはオプションの引数で、ソート方法のカスタマイズに使用できる
list.reverse()          リストの要素をインプレース演算で逆順にする
"""


l = [1, 2, 3, 4, 5]
l2 = [6, 7, 8, 9, 10]

l.append(11)
print(l)

l.extend(l2)
print(l)

l.insert(2, 'sakatai')
print(l)

l.remove('sakatai')
print(l)

l.pop()
print(l)

print(l2)
l2.clear()
print(l2)

print(l.index(11))

print(l.count(11))

l.sort()
print(l)

l.reverse()
print(l)

del l[0]
print(l)

del l[2:5]
print(l)

del l[:]
print(l)


print('----------------------------------')
