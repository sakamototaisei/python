# zipfileの圧縮展開
import glob
import zipfile

# zipfileの作成
with zipfile.ZipFile('test.zip', 'w') as z:
    # z.write('test_dir')
    # z.write('test_dir/test.txt')
    for f in glob.glob('test_dir/**', recursive=True):
        print(f)
        z.write(f)

# zipfileの読み込み
with zipfile.ZipFile('test.zip', 'r') as z:
	# z.extractall('zzz2')
	with z.open('test_dir/test.txt') as f:
		print(f.read())