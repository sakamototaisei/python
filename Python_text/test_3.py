from collections import Counter
from janome.tokenizer import Tokenizer


BEGIN = '__BEGIN__'
END = '__END__'


def get_three_words_list(sentence):
    t = Tokenizer()
    # 文を単語にわかち書き
    words = list(t.tokenize(sentence, wakati=True))
    # 前後に開始、終了マークを追加
    words = [BEGIN] + words + [END]

    three_words_list = []
    for i in range(len(words) - 2):
        # ３つの単語を取り出す
        three_words_list.append(tuple(words[i:i+3]))
    return three_words_list

sentences = ['おいしいビールを飲もう', 'ビールを飲もう', 'おいしいビールは生']
three_words_list = []
# 複数の文を順番に処理
for sentence in sentences:
    three_words_list += get_three_words_list(sentence)
# 出現回数を数える
three_words_count = Counter(three_words_list)
print(three_words_count)




def generate_makov_dict(three_words_count):
    """マルコフ連鎖での文章生成用の辞書データを生成する"""
    markov_dict = {}
    for three_words, count in three_words_count.items():
        # 前半２つの単語と次の単語に分割
        tow_words = three_words[:2]
        next_word = three_words[2]
        # 辞書に存在しない場合は殻のデータを生成
        if tow_words not in markov_dict:
            markov_dict[tow_words] = {'words': [], 'weights': []}
        markov_dict[tow_words]['words'].append(next_word)
        markov_dict[tow_words]['weights'].append(count)
    return markov_dict

markov_dict = generate_makov_dict(three_words_count)
# for k, v in markov_dict.items():
#     print(k, v)






from collections import defaultdict


def get_first_word_and_count(three_words_count):
    """最初の単語を選択するための辞書データを生成する"""
    firstd_word_count = defaultdict(int)

    for three_words, count in three_words_count.items():
        # BERGINで始まるもののみを取り出す
        if three_words[0] == BEGIN:
            next_word = three_words[1]
            # 出現回数を加算
            firstd_word_count[next_word] += count

    return firstd_word_count
# 最初の単語と出現回数の辞書が作成されます
print(get_first_word_and_count(three_words_count))





def get_first_words_weights(three_words_count):
    """最初の単語と重みのリストを作成する"""
    firstd_word_count = get_first_word_and_count(three_words_count)
    # 単語と重み(出現回数)を格納するリスト
    words = []
    weights = []
    for word, count in firstd_word_count.items():
        # 単語と重みをリストに追加
        words.append(word)
        weights.append(count)

    return words, weights

first_words, first_weights = get_first_words_weights(three_words_count)
print(first_words, first_weights)






import random


def generate_text(first_words, first_weights, markov_dict):
    """入力された辞書型データをもとに文章を生成する"""
    # 最初の単語を取得
    first_word = random.choices(first_words, weights=first_weights)[0]
    # 文章生成用の単語を格納するリスト
    generate_words = [BEGIN, first_word]
    while True:
        # 最後の二つを取得
        pair = tuple(generate_words[-2:])
        # 次の単語と重みのリストを取得
        words = markov_dict[pair]['words']
        weights = markov_dict[pair]['weights']
        # 次の単語を取得
        next_word = random.choices(words, weights=weights)[0]
        # 文章が終了した場合はループを抜ける
        if next_word == END:
            break
        generate_words.append(next_word)

    return ''.join(generate_words[1:])

# for _ in range(5):
#     text = generate_text(first_words, first_weights, markov_dict)
#     print(text)





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
# print('文の数:', len(sentences))
# print(sentences[:10])





from tqdm import tqdm


three_words_list = []
# tqdmで進捗バーを表示
for sentence in tqdm(sentences):
    three_words_list += get_three_words_list(sentence)
three_words_count = Counter(three_words_list)
# 3単語の組の種類を確認
len(three_words_count)




markov_dict = generate_makov_dict(three_words_count)
print(len(markov_dict))
first_words, first_weights = get_first_words_weights(three_words_count)
print(len(first_words))



for _ in range(5):
    sentence = generate_text(first_words, first_weights, markov_dict)
    print(sentence)



import pickle

# ファイルをバイナリ書き込みモードで開く
with open('markov-dict.pickle', 'wb') as f:
    # 3つのデータをタプルにまとめる
    data = (first_words, first_weights, markov_dict)
    # dataをpickle化して書き込む
    pickle.dump(data, f)