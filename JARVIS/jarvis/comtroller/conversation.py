from jarvis.views import console
from jarvis.models import robot


def talk_about():
    console.start_template()

    # ここからもらった値によってジャービスに指示をして処理を実行させる
    while True:
        console.middle_template()
        order = console.input_order()
        if order == '1':
            TypingGame = robot.Jarvis()
            TypingGame.typing_game_start()
        elif order == 'x':
            print('またいつでもお呼びください')
            break

