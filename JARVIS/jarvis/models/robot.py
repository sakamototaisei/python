import datetime
import string

from termcolor import colored


def start_talk():
    time_now = int(datetime.datetime.today().strftime('%H'))
    user_name = input('あなたの名前を入力してください : ')

    if time_now >= 18 or 1 <= time_now < 4:
        hello = 'こんばんは'
    elif 11 <= time_now < 18:
        hello = 'こんにちは'
    elif 4 <= time_now < 11:
        hello = 'おはようございます'


    with open('JARVIS/jarvis/templates/template.txt', 'r') as f:
        t = string.Template(f.read())
        template_text = t.substitute(name=user_name, hello=hello)
        print(colored(template_text, 'green'))