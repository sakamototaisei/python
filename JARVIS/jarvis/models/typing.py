# 英単語フラッシュカードアプリ
import random
from termcolor import colored
from inputimeout import inputimeout, TimeoutOccurred


def play_typing():
    print('英単語タイピングゲームです!\n早速ゲームを始めましょう!')

    # ジャンルを選択する
    animals = {
        'コウモリ': 'bat',
        'クマ': 'bear',
        'ビーバー': 'beaver',
        'ラクダ': 'camel',
        'ネコ': 'cat',
        'チンパンジー': 'chimpanzee',
        'シカ': 'deer',
        'イヌ': 'dog',
        'イルカ': 'dolphin',
        'ゾウ': 'elephant',
        'キツネ': 'fox',
        'ゴリラ': 'gorilla',
        'ハムスター': 'hamster',
        'ウマ': 'horse',
        'カンガルー': 'kangaroo',
        'コアラ': 'koala',
        'ライオン': 'lion',
        'サル': 'monkey',
        'パンダ': 'panda',
        'ペンギン': 'penguin',
        'ウサギ': 'rabbit',
        'カラス': 'crow'
    }

    fruits = {
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
        'パパイヤ': 'papaya',
        'グレープフルーツ': 'grapefruit',
        'パイナップル': 'pineapple',
        'イチゴ': 'strawberry',
        'スイカ': 'watermelon',
        'アセロラ': 'acerola',
        'アーモンド': 'almond',
        'ブルーベリー': 'blueberry',
        'クリ': 'chestnut',
        'ココナッツ': 'coconut',
        'ラズベリー': 'raspberry'
    }

    def question_choice():
        while True:
            mode = input('animalsモードか、fruitsモードを選択してください(整数入力). 1:animals, 2:fruits >>')
            if mode not in('1', '2'):
                print('正しく入力してください')
                continue
            # 使うdictを選択する
            if mode == '1':
                question_answer = animals
            elif mode == '2':
                question_answer = fruits
            return question_answer


    question = question_choice()

    template = '*'*15 + '\n英単語: {}\n日本語(仮名文字)を入力してください: \n' + '*'*15
    mistake_cnt = 0
    correct_cnt = 0

    while True:
        # ランダムに辞書から英単語を表示する
        word = random.choice(list(question.keys()))
        print(colored(template.format(word), 'green'))
        try:
            # 自分が英単語を入力する
            answer = inputimeout(prompt='>>', timeout=7)
            # 自分が入力した英単語と、答えがあっているかを確認する
            if answer == '0':
                print('終了します')
                break
            elif answer == question[word]:
                print(colored('正解', 'red'))
                correct_cnt += 1
                if correct_cnt == 10:
                    print('10回正解しました!!!合格です!!!')
                    break
            else:
                print(colored('不正解', 'blue'))
                mistake_cnt += 1
                print('-'*50)
                print('【 答え = {} 】'.format(question[word]))
                print('-'*50)
                if mistake_cnt == 3:
                    print('3回間違えました。ゲームオーバー。再チャレンジしてね!')
                    break
        except TimeoutOccurred:
            print(colored('不正解', 'blue'))
            mistake_cnt += 1
            print('-'*50)
            print('【 答え = {} 】'.format(question[word]))
            print('-'*50)
            if mistake_cnt == 3:
                print('3回間違えました。ゲームオーバー。再チャレンジしてね!')
                break
