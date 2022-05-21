import random


# ババ抜きの山札生成関数
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
# print(player1)
# print(player2)
# print(player3)


# カードの分配機能
initial_deck = create_initial_deck()

player1 = create_player('A')
player2 = create_player('B')
# player3 = create_player('C')
# player4 = create_player('D')
# player5 = create_player('E')
# players = [player1, player2, player3, player4, player5]
# print(players)


def initial_deal(initial_deck: list, *args: tuple) -> list:
    """
    Deal cards to players automatically
    """
    players = list(args)
    # 山札をシャッフルさせる
    random.shuffle(initial_deck)
    # divmod(int, int) 商と余りを求めてくれる組み込み関数
    q, mod = divmod(len(initial_deck), len(players))
    # print(q, mod)
    for i in range(len(players)):
        slice_n = q
        if i < mod:
            slice_n = q + 1
        players[i]["deck"] = initial_deck[:slice_n]
        del initial_deck[:slice_n]
    return players

players = initial_deal(initial_deck, player1, player2)

# print(len(players[0]["deck"]))
# print(len(players[4]["deck"]))

# カード整理(初回用)
def initial_putdown(deck: list) -> list:
    """
    Play(put down) matching cards.
    """
    while len(set(deck)) != len(deck):
        popped_card = deck.pop(0)
        # ペアがあった場合
        if popped_card in deck:
            deck.remove(popped_card)
        else:
            deck.append(popped_card)
    return deck

deck = players[0]["deck"]
print(deck)
print(initial_putdown(deck))