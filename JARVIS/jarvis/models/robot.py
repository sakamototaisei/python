import time

from jarvis.models.jan import play_jan
from jarvis.models.typing import play_typing
from jarvis.models.ec import play_ec


class Jarvis(object):

    def __init__(self) -> None:
        pass

    def typing_game_start(self):
        print('タイピングゲームをはじめます')
        time.sleep(2)
        play_typing()

    def ec_scraping(self):
        print('最安値商品をお探します')
        time.sleep(2)
        play_ec()

    def investment(self):
        pass

    def qr_code(self):
        pass

    def janken_game(self):
        print('じゃんけんゲームをはじめます')
        time.sleep(2)
        play_jan()

    def dictionary(self):
        pass
