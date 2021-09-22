# with クラス as a:
#   処理

# with：処理が連続していて全ての処理が必要な場合
# ・ファイルの書き込み処理(ファイル開く=>書き込む=>ファイルを閉じる)
# ・DBへのデータの書き込み処理(DBへコネクションを張る=>書き込む=>コネクションを閉じる)

class WithTest:
    def __init__(self, file_name):
        print('init called')
        self.__file_name = file_name # file_nameを渡して

    def __enter__(self):
        print('enter called')
        self.__file = open(self.__file_name, mode='w', encoding='utf-8') # fileをオープンする
        return self

    def write(self, msg):
      self.__file.write(msg) # fileに何か書き込む

    def __exit__(self, exc_type, exc_val, traceback): # 引数はエラーハンドリングのために記述している
        print('exit called')
        self.__file.close() # fileを閉じる


with WithTest('resources/output.txt') as t:
    print('withの中')
    t.write('あああああ')
