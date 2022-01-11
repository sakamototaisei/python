"""
新しく足し算の機能の追加
"""
def sum_command(command):
    data = command.split()
    command_args = data[1:]
    result = 0
    for num in command_args:
        result += int(num)
    response = '合計は「{}」です。'.format(result)
    return response