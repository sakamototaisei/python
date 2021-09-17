# for

# for i in range(5):
#   print(i)


# for _ in range(10): # _ は変数に値を格納するのではなくただループさせるだけの処理と強調したい場合に利用する
#   # print('A')
#   pass

# for i in range(2,20,3):
#   print(i)

# # sample = ['john', 'Paul', 'George', 'Ringo'] listでもできる
# sample = ('john', 'Paul', 'George', 'Ringo') # タプルでもできる
# for member in sample:
#   print(member)

# human = {
#   'Name': 'Taro',
#   'Age': 20,
#   'Gender': 'man'
# }
# for h in human:
#   # print(h) # キーを取得
#   print(h, human.get(h)) # キーと値を取得


# enumerate関数：配列に中の値とインデックスを同時に取得する
# zip関数：二つの配列の中の値を同時に取得する
# while:whileの中の式がtrueであるうちは処理を実行する

# fruits = ['grape', 'Pine', 'Apple']

# for index, value in enumerate(fruits):
#     print('index = {}'.format(index))
#     print('value = {}'.format(value))


# classA = ['Taro', 'Hanako', 'Jiro']
# classB = ['Katsuo', 'Wakame', 'Tara']

# for A, B in zip(classA, classB):
#     print('classA student: {}'.format(A))
#     print('classB student: {}'.format(B))


# count = 0
# while count < 10:  # countより小さい場合は処理を実行
#     print(count)
#     count += 1
