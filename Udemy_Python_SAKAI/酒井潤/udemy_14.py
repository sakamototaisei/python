# ファイルの操作
import os
import pathlib
import glob
import shutil

# print(os.path.exists('test.txt'))
# print(os.path.isfile('test.txt'))

# print(os.path.isdir('Udemy_Python'))
# os.rename('test.txt', 'renamed.txt')

# symlink.txtはrenamed.txtとリンクしている
# os.symlink('renamed.txt', 'symlink.txt')

# os.mkdir('test_dir')
# os.rmdir('test_dir')

# pathlibはからのファイルの生成ができる
# pathlib.Path('empty.txt').touch()
# os.remove('empty.txt')

# os.mkdir('test_dir')
# os.mkdir('test_dir/test_dir2')
# # listdir()中身を返してくれる
# # print(os.listdir('test_dir'))

# pathlib.Path('test_dir/test_dir2/empty.txt').touch()

# shutilでファイルをコピーすることもできる
# shutil.copy('test_dir/test_dir2/empty.txt',
#             'test_dir/test_dir2/empty2.txt')
# # # glob.glob()で中身を出力してくれる
# print(glob.glob('test_dir/test_dir2/*'))

# # 強制的にディレクトリを消せるので扱いには注意する
# shutil.rmtree('test_dir')

# 今のディレクトリの位置を表示する
print(os.getcwd())