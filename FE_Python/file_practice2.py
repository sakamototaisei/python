"""
自分の簡単な記録を自動的に記述していくAPPによって作られたCSVを読み込んで
数値をデータ化して表示してくれる
"""

output_list = []

with open('FE_Python/sample.csv', 'r', encoding='utf-8') as f:
    while (line := f.readline()):
        record_list = line.split(',')
        output_list.append(record_list)

# 合計学習時間を自動出力
def sum_study(output_list):
    time_list = output_list[1:]
    result = 0
    for time in time_list:
        result += int(time[0])
    return result

# 平均睡眠時間を自動出力
def avg_sleep(output_list):
    sleep_list = output_list[1:]
    result = 0
    count = 0
    for sleep in sleep_list:
        result += int(sleep[2])
        count += 1
    return result / count

# その他の記述をなし以外の一覧を表示
def msg_record(output_list):
    msg_list = output_list[1:]
    result = []
    for msg in msg_list:
        if msg[3] != 'なし':
            result.append(msg[3])
    return result


print('------------------------')

result_time_study = sum_study(output_list)
print('現在合計で' + str(result_time_study) + '時間学習しました。')

print('------------------------')

result_avg_sleep = avg_sleep(output_list)
print('現在平均' + str(result_avg_sleep) + '時間寝ています。')

print('------------------------')

result_msg_list = msg_record(output_list)
for msg in result_msg_list:
    print('・' + msg)

print('------------------------')