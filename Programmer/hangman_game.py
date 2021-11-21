"""
ハングマンゲームAPP

"""
print('-------------------------------')

def hangman(word):
    # 間違いの回数
    wrong = 0
    stages =  ['',
               '______      ',
               '|           ',
               '|     |     ',
               '|     0     ',
               '|    /|\    ',
               '|    / \    ',
               '|           '
               ]
    # wordの文字を１文字ずつ分解してリスト化したもので、答えなければいけない残りの文字を覚えておくものに使う
    rletters = list(word)
    # 文字列のリストで、プレイヤーにヒントを見せる記録しておくもの
    board = ['_'] * len(word)
    win = False
    print('ハングマンへようこそ!')

    # ゲームの手順を進めるループ
    while wrong < len(stages) - 1:
        print('\n')
        msg = '1文字を予想してね'
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print(' '.join(board))
        e = wrong + 1
        print('\n'.join(stages[0:e]))
        if '_' not in board:
            print('あなたの勝ち!')
            print(' '.join(board))
            win = True
            break
    if win == False:
        print('\n'.join(stages[0:wrong+1]))
        print('あなたの負け!正解は {}'.format(word))

hangman('cat')


print('-------------------------------')

