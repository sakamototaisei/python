# セクション8 ファイル操作とシステム
# ファイルの生成


s = """\
AAA
BBB
CCC
DDD
"""

# 'w'は上書きする。　'a'はappendつまり加える
# with open('test.txt', 'w') as f:
# ファイルに書き込む
    # f.write(s)
# print('My', 'name', 'is', 'Mike', sep='#', end='!', file=f)
# f.close()


print('--------------------')

# ---------------------------------------------------------------
# withステートメントでファイルをopenする
# ファイルを開くときはwithを使った方が良い、close()の記述も要らなくなる

print('--------------------')


# ---------------------------------------------------------------
# ファイルの読み込み

# with open('test.txt', 'r') as f:
    # # print(f.read())
    # while True:
    #     chunk = 2
    #     # ２文字ずつ読み込みしている
    #     line = f.read(chunk)

    #     # f.readline()でで一行ずつ読み込んでいく
    #     # line = f.readline()
    #     print(line)
    #     if not line:
    #         break

    # # tell()現在の位置を整数で返してくれる
    # print(f.tell())
    # print(f.read(1))
    # # seek()何文字目から読み出したいなんて時に使う
    # f.seek(5)

    # print(f.read(1))
    # f.seek(14)
    # print(f.read(1))
    # f.seek(15)
    # print(f.read(1))
    # f.seek(5)
    # print(f.read(1))


print('--------------------')


# ---------------------------------------------------------------
# seekを使って移動する



print('--------------------')


# ---------------------------------------------------------------
# 書き込みと読み込みモード

# 'w+' で読み書きが可能になる。 'r+' は読み込めるものがないとエラーになる
with open('test.txt', 'w+') as f:
    f.write(s)
    # 書き込んだ後はインデックス番号は末尾にあるためseek(0)で先頭から読み込みできるようにしてあげる
    f.seek(0)
    print(f.read())



print('--------------------')


# ---------------------------------------------------------------
# テンプレート

import string

s1 = """\

Hi $name.

$contents

Have a good day
"""

# string.Template() 変数は読み込み専用として扱う
t = string.Template(s1)
contents = t.substitute(name='Mike', contents='How are you?')
print(contents)


print('--------------------')


# ---------------------------------------------------------------
# CSVファイルへの書き込みと読み込み


