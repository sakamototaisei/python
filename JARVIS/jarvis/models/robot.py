import time

from jarvis.models.jan import play_jan
from jarvis.models.typing import play_typing
from jarvis.models.ec import play_ec
from jarvis.models.investment import play_investment


class Jarvis(object):

    def __init__(self) -> None:
        pass

    def typing_game_start(self):
        print('タイピングゲームを開始します')
        time.sleep(2)
        play_typing()

    def ec_scraping(self):
        print('最安値商品をお探します')
        time.sleep(2)
        play_ec()

    def investment(self):
        print('積立シュミレーションを開始します')
        time.sleep(2)
        play_investment()

    def qr_code(self):
        pass

    def janken_game(self):
        print('じゃんけんゲームを開始します')
        time.sleep(2)
        play_jan()

    def dictionary(self):
        pass
