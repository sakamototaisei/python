"""
戦争カードゲーム

"""

# カードクラス
class Card(object):

    suits = ['spades', 'hearts', 'diamonds', 'clubs']

    values = [None, None,
             '2', '3', '4', '5', '6', '7', '8', '9', '10',
             'Jack', 'Queen', 'King', 'Ace']

    def __init__(self, value, suit):
        """スート(マーク)も値も数値"""
        self.value = value
        self.suit = suit

    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            return self.suit < c2.suit
        return False

    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            return self.suit > c2.suit
        return False

    def __repr__(self):
        v = self.values[self.value] + ' of ' + self.suits[self.suit]
        return v


# デッキクラス
from random import shuffle

class Deck(object):

    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i, j))
        # カードのリストをシャッフルしている
        shuffle(self.cards)

    def draw(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()


# プレイヤーを表すクラス
class Player(object):

    def __init__(self, name):
        self.name = name
        # プレイヤーがその時何を持っているか
        self.card = None
        # なんか勝利しているか
        self.wins = 0


# ゲーム自体を表すクラス
class Game(object):

    def __init__(self):
        name1 = input('プレイヤー１の名前 ')
        name2 = input('プレイヤー２の名前 ')
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def print_winner(self, winner):
        w = 'このラウンドは {} が勝ちました'
        print(w.format(winner.name))

    def print_draw(self, p1, p2):
        d = '{} は {}, {} は {} を引きました'
        print(d.format(
            p1.name, p1.card, p2.name, p2.card))

    def play_game(self):
        cards = self.deck.cards
        print('戦争をはじめます!')
        while len(cards) >= 2:
            m = 'q で終了、　それ以外はのキーでPlay : '
            response = input(m)
            if response == 'q':
                break
            self.p1.card = self.deck.draw()
            self.p2.card = self.deck.draw()
            self.print_draw(self.p1, self.p2)
            if self.p1.card > self.p2.card:
                self.p1.wins += 1
                self.print_winner(self.p1)
            else:
                self.p2.wins += 1
                self.print_winner(self.p2)
        win = self.winner(self.p1, self.p2)
        print('ゲーム終了、 {} の勝利です!'.format(win))

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return '引き分け'


game = Game()
game.play_game()