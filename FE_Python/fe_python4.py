"""
ファイル入力

readlines() : 中身を配列で読み込む
readline() : 1行ずつ読み込む
"""

file_path = 'FE_Python/input.csv'
f = open(file_path, 'r', encoding='utf-8')

# # 中身全体を読み込み
# line = f.read()
# print(line)

# lines = f.readlines()
# # 改行区切りで出力される
# print(lines)

# for x in lines:
#     # strip()指定したものを削除してくれる
#     print(x.strip('\n'))


print('----------------')


# line = f.readline()
# while line:
#     print(line.rstrip('\n'))
#     line = f.readline()
"""
上記の別解、セイウチ演算子版
"""
while (line := f.readline()):
    print(line.rstrip('\n'))


print('----------------')


"""
ファイルを閉じないと、メモリをくったり、他の処理でファイルを開けない場合がある
"""
f.close()

with open('FE_Python/input2.csv', 'r', encoding='utf-8') as f:
    # 中身を配列で読み込む
    # lines = f.readlines()
    # print(lines)

    while (line := f.readline()):
        print(line.rstrip('\n'))


print('----------------')


"""
ファイルの書き込み
w : 存在してなければ作成し、存在している場合は上書きされる

f.write(文字列) : ファイルに文字列を書き込み
f.writelines() : リストをそのまま繋げて書き込み
f.write('\n'.join(list)) : リストを改行させて書き込み

a : ファイルの追記モード
"""

file_path = 'FE_Python/output.csv'
# newline=改行コードのこと
f = open(file_path, 'w', encoding='utf-8', newline='\n')
f.write('あああ\nいいい\nううう')
f.close()

with open(file_path, 'a', encoding='utf-8', newline='\n') as f:
    list_a = [
        ['A', 'B', 'C'],
        ['あ', 'い', 'う']
    ]
    for x in list_a:
        print(x)
        f.write('\n')
        f.write(','.join(x))


print('----------------')


class WithTest(object):

    def __init__(self, file_name):
        print('init called')
        self.__file_name = file_name

    def __enter__(self):
        print('enter called')
        self.__file = open(self.__file_name, 'w', encoding='utf-8')
        # returnでWithTestのインスタンスを返す
        return self

    def write(self, msg):
        print('write colled')
        self.__file.write(msg)

    # __exit__の引数はエラーハンドリングのためのもの3つ必要
    def __exit__(self, exc_type, exc_val, traceback):
        print('exit called')
        self.__file.close()

# t : の中には__enter__からのreturnのインスタンスが返ってくる
with WithTest('FE_Python/output.txt') as t:
    print('withの中')
    t.write('あああああああああ')