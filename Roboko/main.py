# レストランアンケートアプリ
import string

from termcolor import colored



while True:

    with open('Roboko/template/first.txt', 'r') as f:
        print(colored(f.read(), 'green'))
    user_name = input()

    with open('Roboko/template/question.txt', 'r') as f2:
        t = string.Template(f2.read())
        question = t.substitute(name=user_name)
        print(colored(question, 'green'))
    # このアンケートの結果をcsvファイルに加えていく必要がある
    favo_restaurant = input()

    with open('Roboko/template/last.txt', 'r') as f3:
        t2 = string.Template(f3.read())
        last = t2.substitute(name=user_name)
        print(colored(last, 'green'))
    break