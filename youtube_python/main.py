# 英単語フラッシュカードアプリ
import random
from termcolor import colored


fruits = {
    'リンゴ': 'apple',
    'バナナ': 'banana',
    'モモ': 'peach',
    'さくらんぼ': 'cherry',
    'グレープフルーツ': 'grapefruit',
    'ブドウ': 'grapes',
    'キウイ': 'kiwi',
    'レモン': 'lemon',
    'ライム': 'lime',
    'マンゴー': 'mango',
    'メロン': 'melon',
    'オレンジ': 'orange',
    'パパイヤ': 'papaya',
    'パイナップル': 'pineapple',
    'イチゴ': 'strawberry',
    'スイカ': 'watermelon'
}


template = '*'*15 + '\n英単語: {}\n日本語(仮名文字)を入力してください: \n' + '*'*15

mistake_cnt = 0
correct_cnt = 0


while True:
    # 英単語を表示する
    word = random.choice(
        list(fruits.keys())
    )
    print(colored(
        template.format(word), 'green')
    )

    # 自分が英語を入力する
    answer = input()

    # 自分が入力した日本語と、答えがあっているかを確認する
    if answer == '0':
        print('終了します')
        break
    elif answer == fruits[word]:
        print(colored('正解', 'red'))
        correct_cnt += 1
        if correct_cnt == 10:
            print('10回正解しました!!!合格です!!!')
            break
    else:
        print(colored('不正解', 'blue'))
        mistake_cnt += 1
        if mistake_cnt == 3:
            print('3回間違えました。ゲームオーバー。再チャレンジしてね!')
            break
