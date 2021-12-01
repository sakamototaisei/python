# じゃんけんアプリ
from random import randint
import random


hands_dict = {
    '1': 'グー',
    '2': 'チョキ',
    '3': 'パー'
}

def is_win(my_hand, enemy_hand):
    if my_hand == '1' and enemy_hand == '2':
        return True
    elif my_hand == '2' and enemy_hand == '3':
        return True
    elif my_hand == '3' and enemy_hand == '1':
        return True
    return False

win_count = 0
lose_count = 0


while True:
    my_hand = input('何を出しますか?数字を入力してください 1:グー, 2:チョキ, 3:パー')
    if my_hand not in ('1', '2', '3'):
        print('正しく入力してください')
        continue
    enemy_hand = str(randint(1, 3))
    print(f'あなたは{hands_dict.get(my_hand)}を出しました。CPは{hands_dict.get(enemy_hand)}を出しました。')
    if my_hand == enemy_hand:
        print('あいこです')
    elif is_win(my_hand, enemy_hand):
        win_count += 1
        if win_count == 3:
            print('3回勝ちました。あなたの勝利です！')
            break
        else:
            print(f'{win_count}回勝ちました。')
    else:
        lose_count += 1
        if lose_count == 3:
            print('3回負けました。ゲームオーバー。')
            break
        else:
            print(f'{lose_count}回負けました。再チャレンジ。')

