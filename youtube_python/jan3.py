# じゃんけんアプリ練習
from random import randint

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


lose_count = 0
win_count = 0

while True:
    my_hand = input('何を出しますか? 1:グー 2:チョキ 3:パー')
    if my_hand not in ('1', '2', '3'):
        print('間違った入力です')
        continue
    enemy_hand = str(randint(1, 3))
    print('あなたの出した手は: {}, CPの出した手は: {}'.format(hands_dict.get(my_hand), hands_dict.get(enemy_hand)))
    if my_hand == enemy_hand:
        print('あいこです')
    elif is_win(my_hand, enemy_hand):
        win_count += 1
        if win_count == 3:
            print('3回勝ちました!あなたの勝利です！')
            break
        print('あなたは{}回勝ちました！'.format(str(win_count)))
    else:
        lose_count += 1
        if lose_count == 3:
            print('あなたは3回負けました。ゲームオーバー')
            break
        else:
            print('あなたは{}回負けました。再チャレンジ！'.format(str(lose_count)))

