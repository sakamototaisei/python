# 英単語フラッシュカードアプリ
import random
from termcolor import colored
from inputimeout import inputimeout, TimeoutOccurred


head_fruits = {
    'グレープフルーツ': 'grapefruit',
    'パイナップル': 'pineapple',
    'イチゴ': 'strawberry',
    'スイカ': 'watermelon',
    'アセロラ': 'acerola',
    'アーモンド': 'almond',
    'ブルーベリー': 'blueberry',
    'クリ': 'chestnut',
    'ココナッツ': 'coconut',
    'ザクロ': 'pomegranate',
    'スモモ': 'prune',
    'ラズベリー': 'raspberry'
}

easy_fruits = {
    'リンゴ': 'apple',
    'バナナ': 'banana',
    'モモ': 'peach',
    'さくらんぼ': 'cherry',
    'ブドウ': 'grapes',
    'キウイ': 'kiwi',
    'レモン': 'lemon',
    'ライム': 'lime',
    'マンゴー': 'mango',
    'メロン': 'melon',
    'オレンジ': 'orange',
    'パパイヤ': 'papaya'
}



template = '*'*15 + '\n英単語: {}\n日本語(仮名文字)を入力してください: \n' + '*'*15

mistake_cnt = 0
correct_cnt = 0

while True:
    mode = input('easyモードか、headモードを選択してください(整数入力). 1:easy, 2:head >>')
    if mode not in('1', '2'):
        print('正しく入力してください')
        continue
    # ランダムに辞書から英単語を表示する
    if mode == '1':
        word = random.choice(
            list(easy_fruits.keys())
        )
        print(colored(
            template.format(word), 'green')
        )
    elif mode == '2':
        word = random.choice(
            list(head_fruits.keys())
        )
        print(colored(
            template.format(word), 'green')
        )

    try:
        # 自分が英単語を入力する
        answer = inputimeout(prompt='>>', timeout=7)
        # 自分が入力した英単語と、答えがあっているかを確認する
        if answer == '0':
            print('終了します')
            break
        elif answer == easy_fruits[word] or answer == head_fruits[word]:
            print(colored('正解', 'red'))
            correct_cnt += 1
            if correct_cnt == 5:
                print('5回正解しました!!!合格です!!!')
                break
        else:
            print(colored('不正解', 'blue'))
            mistake_cnt += 1
            if mistake_cnt == 3:
                print('3回間違えました。ゲームオーバー。再チャレンジしてね!')
                break
    except TimeoutOccurred:
        print(colored('不正解', 'blue'))
        mistake_cnt += 1
        if mistake_cnt == 3:
            print('3回間違えました。ゲームオーバー。再チャレンジしてね!')
            break
