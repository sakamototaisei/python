# 例外処理：実行時に発生するエラーを制御して処理を行う

# try:
#   処理
# except エラー名:
#   例外発生時の処理

# FileNotFoundError:プログラムで指定されたファイルが見つからないエラー
# IndexError:配列などで指定されたインデックスに値が存在しないエラー
# TypeError:方に関するエラー
# ZeroDivisionError:0で割ろうとしたことによるエラー
# Exception:すべての例外

# try:
#     b = [10, 20, 30]
#     c = b.method_a()
#     a = b[4]
#     a = 10 / 0
# except ZeroDivisionError as e:
#     import traceback
#     traceback.print_exc()
#     # print(e, type(e))
#     pass
# except IndexError as e:
#     print('indexerror発生')
# except Exception as e:
#     print('Exception: ', e, type(e))
# else:
#     # a = 10 / 0
#     print('else処理エラーなし')
# finally:
#   print('finally処理成功してもエラーでも実行')

# print('処理が完了しました')


# 例外処理(else, finally) 例外処理後に実行される
# else:例外が発生しなかった場合に実行され、例外が発生した場合には執行されない
# finally:例外が発生した場合にも、しなかった場合にも実行される


# raise:例外を返す 例外自作
# class MyException(Exception):
#   pass


# def devide(a, b):
#   if b == 0:
#     raise MyException('0で割り切れません')
#   else:
#     return a / b

# try:
#   c = devide(10, 0)
# except Exception as e:
#   print(e, type(e))
# ーーーーーーーーーーーーーーーーーーーーーーーーーーーー
