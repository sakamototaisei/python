import math
import time

from termcolor import colored


def play_investment():

    with open('JARVIS/jarvis/templates/investment_template.txt', 'r') as f:
        template_text = f.read()
        print(colored(template_text, 'green'))

    period = int(input('積立期間(年): '))
    interest = int(input('想定利回り(%): '))
    amount = int(input('目標金額(万): '))

    interestNew = interest / 100
    coefficient = interestNew / ((1 + interestNew) ** period - 1)
    result = math.floor(amount * 10000 * coefficient / 12)

    print()
    print('毎月の積み立て金額はおよそ【' + str(result) + '万円】' + 'になります')

    time.sleep(3)