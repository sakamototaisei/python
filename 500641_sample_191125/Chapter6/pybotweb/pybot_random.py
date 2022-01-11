import random


def choice_command(command):
    data = command.split()
    choiced = random.choice(data[1:])
    response = '「{}」ガ選バレマシタ'.format(choiced)
    return response


def dice_command():
    num = random.randrange(1, 7)
    response = '「{}」ガ出マシタ'.format(num)
    return response
