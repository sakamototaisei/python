# レストランアンケートアプリ
import csv
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
    favo_restaurant = input()

    with open('Roboko/template/last.txt', 'r') as f3:
        t2 = string.Template(f3.read())
        last = t2.substitute(name=user_name)
        print(colored(last, 'green'))
    break

# 文字列の先頭を大文字変換
favo_restaurant = favo_restaurant.title()


# 質問結果をcsvへ書き込み
with open('Name_Count.csv', 'a') as csv_file:
    fieldnames = ['NAME', 'COUNT']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'Name': favo_restaurant, 'Count': 1})