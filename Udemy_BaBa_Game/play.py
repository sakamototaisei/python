# 引く順番の決定機能
def create_turn_index(passer_i: int, taker_i: int, players: list) -> tuple:
    """
    Create an index to determine if it is a passer or a taker.
    """
    passer_i = taker_i
    taker_i = taker_i + 1
    # passer_iインデックスが超えた場合は全てリセットしてあげる
    if passer_i >= len(players):
        passer_i = 0
        taker_i = 1
    # taker_iだけ超えた場合は先頭にリセットする
    elif taker_i >= len(players):
        taker_i = 0
    return passer_i, taker_i

players = ['Green', 'Yellow', 'Red']
# initial index
passer_i = 0
taker_i = 1
print(f'{players[passer_i]} --> {players[taker_i]}')

passer_i, taker_i = create_turn_index(passer_i, taker_i, players)
print(f'{players[passer_i]} --> {players[taker_i]}')

passer_i, taker_i = create_turn_index(passer_i, taker_i, players)
print(f'{players[passer_i]} --> {players[taker_i]}')


# カード選択機能
