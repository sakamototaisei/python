# # if文 bool() => 真偽値判定
# class ClassA():

#   def __init__(self, a):
#     self.a = a

#   def __bool__(self):
#     if self.a == 'a':
#       return True
#     return False


# var = ClassA('c')

# print('boolの計算結果: {}'.format(bool(var)))
# if var:
#   print('if文の中の処理')


# if and, not, or

# msg = 'yellow'
# if msg == 'blue':
#   print('進め')
# elif msg == 'red':
#   print('止まれ')
# else:
#   print('それ以外の処理')

# age = 50
# if age < 20:
#   print('未成年')
# elif age <= 40:
#   print('20以上、40以下です')
# elif age >= 60:
#   print('60以上です')
# else:
#   print('それ以外の年齢')

# gender = 'woman'
# age = 30
# if gender == 'man' or age < 20:
#   print('男性もしくは20未満です')

# if not gender == 'man':
#   print('男ではない')

# if gender != 'man':
#   print('男ではない')
# ーーーーーーーーーーーーーーーーーーーーーーーーーー

# allはオブジェクトの中が全てtrueの場合に処理をする
# anyはオブジェクトの一部がtrueの場合に処理をする

if all((30 < 10, True, 10, True)):
    print('allの中の処理')

if not any((30 < 20, 10 < 5, 'a' == 'b')):
    print('anyの中の処理')
