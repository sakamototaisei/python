def eto_command(command):
    eto, year = command.split()
    eto_list = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]
    eto_number = (int(year) + 8) % 12
    eto_name = eto_list[eto_number]
    response = '{}年生マレノ干支ハ「{}」デス。'.format(year, eto_name)
    return response
