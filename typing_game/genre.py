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