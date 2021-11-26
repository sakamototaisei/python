import os

for curDir, dirs, files in os.walk('.'):
    for file in files:
        # ディレクトリとファイル名の結合でパスの作成が可能に
        print(os.path.join(curDir, file))


print('------------------------')


lists = os.listdir('.')
lists.sort()
print(lists)


print('------------------------')

# 絶対パスの取得 abspath()
print(os.path.abspath('./Udemy_Python/udemy_4.py'))

# ファイル名の取得 basename()
print(os.path.basename('./Udemy_Python/udemy_4.py'))

# ファイル・ディレクトリの存在確認
print(os.path.exists('./Udemy_Python/udemy_4.py'))
print(os.path.exists('PYTHON'))
print(os.path.exists('FE_Python'))

print('------------------------')

# ディレクトリの存在確認
print(os.path.isdir('PYTHON'))
print(os.path.isdir('FE_Python'))

print('------------------------')

# ファイルに存在確認
print(os.path.isfile('./Udemy_Python/udemy_4.py'))
print(os.path.isfile('./Udemy_Python/udemy_48.py'))