# tempfile
import tempfile

# ファイルを作って最後には自動で消してくれる
with tempfile.TemporaryFile(mode='w+') as t:
    t.write('hello')
    t.seek(0)
    print(t.read())

# ファイルを作ってくれる版
with tempfile.NamedTemporaryFile(delete=False) as t:
    print(t.name)
    with open(t.name, 'w+') as f:
        f.write('test\n')
        f.seek(0)
        print(f.read())

# 一時的にディレクトリを作ってくれる版
with tempfile.TemporaryDirectory() as td:
    print(td)

temp_dir = tempfile.mkdtemp()
print(temp_dir)