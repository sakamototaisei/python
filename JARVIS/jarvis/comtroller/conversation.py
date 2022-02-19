from jarvis.views import console
from jarvis.models import robot


def talk_about():
    console.start_template()

    # ここからもらった値によってジャービスに指示をして処理を実行させる
    Jarvis_function = robot.Jarvis()
    while True:
        console.middle_template()
        order = console.input_order()
        if order == '1':
            Jarvis_function.typing_game_start()
        if order == '6':
            Jarvis_function.ec_scraping()
        if order == '10':
            Jarvis_function.janken_game()
        if order == 'x':
            print('またいつでもお呼びください')
            break

