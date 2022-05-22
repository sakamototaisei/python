import random

import setting

if __name__ == '__main__':
    # プレイヤー生成
    player1 = setting.create_player('A', is_auto=False)
    player2 = setting.create_player('B')
    # ババ抜きの山札生成関数
    initial_deck = setting.create_initial_deck()
    # 山札をシャッフルし配る
    players = setting.initial_deal(initial_deck, player1, player2)
    # カード整理(初回用)
    deck1 = players[0]["deck"]
    deck2 = players[1]["deck"]
    # 手札を整理する
    print(setting.initial_putdown(deck1))
    print(setting.initial_putdown(deck2))

    # カードの引く順番決定機能