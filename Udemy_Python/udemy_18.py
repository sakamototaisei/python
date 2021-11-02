# subprocessでコマンドを実行する
import subprocess

# ターミナルのlsコマンドと同じ結果となる
subprocess.run(['ls', '-al'])
print('------------------------')
# これも上記と同じ結果となるがLinuxなどの知識がないと理解できない
# subprocess.run('ls -al', shell=True)

p1 = subprocess.Popen(['ls', '-al'], stdout=subprocess.PIPE)
p2 = subprocess.Popen(['grep', 'test'], stdin=p1.stdout, stdout=subprocess.PIPE)
p1.stdout.close()
output = p2.communicate()[0]
print(output)