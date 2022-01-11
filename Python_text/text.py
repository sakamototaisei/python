from janome.tokenizer import Tokenizer
from math import log


# # 単純にわかち書きを行う
# t = Tokenizer(wakati=True)
# text = '東京都で美味しいビールを飲もう。'
# tokens = t.tokenize(text)
# # token_list = list(tokens)
# # len(token_list)
# print(tokens)
# for token in tokens:
#     print(token)

t = Tokenizer()
sentences = [
    'おいしいビールを飲む', 'コーヒーを飲む', 'おいしいクラフトビールを買う'
]

# 上記のリストをわかち書き変換してリスト化する
words_list = []
for sentence in sentences:
    words_list.append(list(t.tokenize(sentence, wakati=True)))

print(words_list)

# わかち書きした中で重複してないリストを作る
unique_words = []
for words in words_list:
    for word in words:
        if word not in unique_words:
            unique_words.append(word)

print(unique_words)

# ユニークなwordの出現回数をリスト化する
bow_list = []
for words in words_list:
    words = list(words)
    bag_of_words = []
    for unique_word in unique_words:
        num = words.count(unique_word)
        bag_of_words.append(num)
    bow_list.append(bag_of_words)

print(bow_list)

# 上記の出現回数をもとにIDF計算をする
num_of_sentences = len(sentences)
idf = []
for i in range(len(unique_words)):
    count = 0
    for bow in bow_list:
        #  Bag of Wordsに存在すれば1を足す
        if bow[i] > 0:
            count += 1
            # 単語のIDF計算 0で割ることを避けるために両方に1を加えている
    idf.append(log((num_of_sentences + 1) / (count + 1)))
# 単語を含む文章がどれくらいあるか(出てこないほど値が大きい)
print(idf)

# TF-IDFの計算

# コーヒを飲むのBag of Words
bow = bow_list[1]
num_of_words = sum(bow)
tfidf = []
for i, value in enumerate(bow):
    tf = value / num_of_words
    tfidf.append(tf * (idf[i] + 1))
# 特徴的なのは値が高い
print(tfidf)