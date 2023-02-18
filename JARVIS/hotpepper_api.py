import pandas as pd
import requests

import secret

URL = secret.URL
API_KEY = secret.API_KEY

try:
    keyword = input('検索キーワードを入力してください : ')
    count = int(input('検索件数を整数入力してください(最高100まで) : '))
    params = {
        'key': API_KEY,
        'keyword': keyword,
        'format': 'json',
        'count': count
    }

    res = requests.get(URL, params)
    result = res.json()
    items = result['results']['shop']
    df = pd.DataFrame(items)
    df = df[['address', 'name', 'urls', 'wifi']]

    for i in range(len(df['urls'])):
        df['urls'][i] = df['urls'][i]['pc']

    keyword = ''.join(keyword.split())
    df.to_csv('JARVIS/storage_csv/hotpepper_'+keyword+'.csv', index=False)
    print('CSVファイルの書き出しが完了しました')
except Exception as e:
    print('エラーが発生しております')
    print(e)
finally:
    print('実行を終了します')
