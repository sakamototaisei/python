# じゃんけんアプリ覚えているかチェック
import time

from random import randint
from termcolor import colored

def play_jan():
    hands_dict = {
        1: 'グー',
        2: 'チョキ',
        3: 'パー'
    }


    def is_win(my_hand, enemy_hand):
        if my_hand == 1 and enemy_hand == 2:
            return True
        elif my_hand == 2 and enemy_hand == 3:
            return True
        elif my_hand == 3 and enemy_hand == 1:
            return True
        return False


    win_count = 0
    lose_count = 0


    while True:
        my_hand = input(colored('何を出しますか? グー:1, チョキ:2, パー:3 => ', 'green'))
        if my_hand not in('1', '2', '3'):
            print('正しく入力してください')
            continue
        my_hand = int(my_hand)
        enemy_hand = randint(1, 3)
        print('あなたは{}を出しました。JARVISは{}を出しました。'.format(hands_dict.get(my_hand), hands_dict.get(enemy_hand), 'green'))
        if my_hand == enemy_hand:
            print('あいこです')
        elif is_win(my_hand, enemy_hand):
            win_count += 1
            if win_count == 3:
                print(colored('3回勝ちました。あなたの勝利です', 'red'))
                break
            else:
                print('あなたは{}回勝ちました'.format(win_count))
        else:
            lose_count += 1
            if lose_count == 3:
                print(colored('3回負けました。ゲームオーバー', 'blue'))
                break
            else:
                print('あなたは{}回負けました。再チャレンジ'.format(lose_count))

    time.sleep(3)