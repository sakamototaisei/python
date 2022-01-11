from datetime import date, datetime


def today_command():
    today = date.today()
    response = '今日ノ日付ハ {} デス'.format(today)
    return response


def now_command():
    now = datetime.now()
    response = '現在日時ハ {} デス'.format(now)
    return response


def weekday_command(command):
    try:
        data = command.split()
        year = int(data[1])
        month = int(data[2])
        day = int(data[3])
        one_day = date(year, month, day)

        weekday_str = '月火水木金土日'
        weekday = weekday_str[one_day.weekday()]

        response = '{} ハ {}曜日デス'.format(one_day, weekday)
    except IndexError:
        response = '3ツノ値(年月日)ヲ指定シテクダサイ'
    except ValueError:
        response = '正シイ日付ヲ指定シテクダサイ'
    return response
