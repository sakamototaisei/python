import os

for curDir, dirs, files in os.walk('.'):
    for file in files:
        print(f'{curDir}/{file}')


print('------------------------')


lists = os.listdir('.')
lists.sort()
print(lists)


print('------------------------')

# 絶対パスの取得 abspath()
print(os.path.abspath('./Udemy_Python/udemy_4.py'))