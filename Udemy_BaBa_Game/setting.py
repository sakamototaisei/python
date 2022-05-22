import random

import setting_function

if __name__ == '__main__':
    player1 = setting_function.create_player('A', is_auto=False)
    player2 = setting_function.create_player('B')
    # ババ抜きの山札生成関数
    initial_deck = setting_function.create_initial_deck()
    players = setting_function.initial_deal(initial_deck, player1, player2)
    # カード整理(初回用)
    deck1 = players[0]["deck"]
    deck2 = players[1]["deck"]
    print(setting_function.initial_putdown(deck1))
    print(setting_function.initial_putdown(deck2))