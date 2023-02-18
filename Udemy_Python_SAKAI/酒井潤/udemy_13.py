# ---------------------------------------------------------------
# CSVファイルへの書き込みと読み込み

import csv

with open('test.csv', 'w') as csv_file:
    fieldnames = ['Name', 'Count']
    # csv.DictWriter()csvに書き込むためのオブジェクトを生成する
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    # 中身に書き込んでいく dict型で記述する
    writer.writerow({'Name': 'A', 'Count': 1})
    writer.writerow({'Name': 'B', 'Count': 2})


# 読み込みを行う
with open('test.csv', 'r') as csv_file:
    # csv.DictReader()で読み込むためのオブジェクトを生成する
    reader = csv.DictReader(csv_file)
    for row in reader:
        print(row['Name'], row['Count'])