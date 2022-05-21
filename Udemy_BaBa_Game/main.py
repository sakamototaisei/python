"""
list
1~13
egara(str)
4 suit each card
add baba
53 card
"""
# ババ抜きの山札生成関数
from venv import create


def create_initial_deck() -> list:
    """
    Create a list object containing 53 cards.
    The X card is a baba(joker).
    """
    initial_deck = []
    for n in range(1, 14):
        if n == 1:
            egara = 'A'
        elif n == 11:
            egara = 'J'
        elif n == 12:
            egara = 'Q'
        elif n == 13:
            egara = 'K'
        else:
            egara = str(n)
        initial_deck.append(egara)
    initial_deck = initial_deck * 4
    initial_deck.append('X')
    return initial_deck

# sample = create_initial_deck()
# print(sample)

# プレイヤーの作成
def create_player(name: str, is_auto: bool = True) -> dict:
    """
    Create a player dict.
    """
    return {
        'name': name,
        'deck': [],
        'is_win': False,
        'is_auto': is_auto
    }

player1 = create_player('sakatai', is_auto=False)
player2 = create_player('Apple')
player3 = create_player('Banana')
print(player1)
print(player2)
print(player3)
