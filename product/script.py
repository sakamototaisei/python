import math
from menuitem import MenuItem
from food import Food
from drink import Drink


food1 = Food('サンドイッチ', 500, 330)
food2 = Food('チョコケーキ', 400, 450)
food3 = Food('シュークリーム', 200, 180)

foods = [food1, food2, food3]



print('食べ物のメニュー')
index = 0
for food in foods:
    print(str(index) + '. ' + food.info())
    index += 1

print('--------------------------')

order = int(input('メニュー番号を入力してください'))
selected_menu = menu_items[order]
print('選択されたメニュー: ', selected_menu.name)

count = int(input('個数を入力してください(3つ以上で1割引): '))
result = math.floor(selected_menu.get_total_price(count))
print('合計は' + str(result) + '円です')