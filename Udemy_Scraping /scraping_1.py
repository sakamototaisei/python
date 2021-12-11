from newspaper import Article
import nltk


url = 'https://www.reuters.com/world/us/most-reported-us-omicron-cases-have-hit-fully-vaccinated-cdc-2021-12-10/'
# Articleオブジェクトの生成し変数に格納
article = Article(url)
# 記事をダウンロードする
article.download()
# 解析を行う
article.parse()
# 記事の発行日
print(article.publish_date)
# 記事の作成者
print(article.authors)
# 記事の全文を表示
print(article.text)
# 記事のタイトルの表示
print(article.title)

print('-----------------------')
# 下記の一行は一度実行すればよい
# nltk.download('punkt')
# キーワードとサマリーを取得できるようになる
article.nlp()
# キーワード確認
print(article.keywords)
# サマリーの確認、要約を確認
print(article.summary)
