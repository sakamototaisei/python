"""書籍から文字を自動生成"""
import io
import re
import requests
import zipfile



# 人間失格のファイルのURL
url = 'https://www.aozora.gr.jp/cards/000035/files/301_ruby_5915.zip'
res = requests.get(url)
# ファイルの中身を取得
content = res.content
# バイナリをファイルのように変換
f = io.BytesIO(content)
# zipファイルを開く
zipf = zipfile.ZipFile(f)
# ファイル一覧を取得
namelist = zipf.namelist()

print(namelist)

# zipファイルを展開しデータを取り出す
data = zipf.read(namelist[0])
# 文字列にデコードする
original_text = data.decode('Shift_JIS')
# print(original_text[:500])

first_sentence = '私は、その男の写真を三葉、見たことがある。'
last_sentence = '神様みたいないい子でした'
# 青空文庫の説明文を削除
_, text = original_text.split(first_sentence)
text, _ = text.split(last_sentence)
text = first_sentence + text + last_sentence

# 不要な文字列を削除
text = text.replace('|', '').replace(' ', '')
text = re.sub(' 《\w+》', '', text)
text = re.sub(' [#\w+]', '', text)
text = text.replace('\r', '').replace('\n', '')
text = re.sub('[、「」?]', '', text)
text = re.sub(' (\w+)', '', text)
text = re.sub(' [\w+]', '', text)

# 。で文章を分割
sentences = text.split('。')
print('文の数:', len(sentences))
print(sentences[:10])