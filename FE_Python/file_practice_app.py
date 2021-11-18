"""
自分の簡単な記録を自動的に記述していくAPP
"""

with open('FE_Python/sample.csv', 'a', encoding='utf-8', newline='\n') as f:
    record = input('学習時間,体重,睡眠時間,その他、の順で記述してください : ')
    print(record)
    record_list = record.split(',')
    print(record_list)
    for x in record_list:
        f.write(x.strip() + ',')
    f.write('\n')


