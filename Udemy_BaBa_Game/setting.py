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
# カードの分配機能
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