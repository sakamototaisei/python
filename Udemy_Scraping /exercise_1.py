"""
単一の記事の取得

タスク１；newspaperからArticleをインポートしてください
タスク２：Articleを使って記事のダウンロードと解析を行い、記事の発行日を表示してください
タスク３：記事の著者を表示してください
タスク４：記事の本文を表示してください

練習サイトURL：https://diamond-rm.net/
"""
from newspaper import Article
from newspaper.utils import memoize_articles


url = 'https://diamond-rm.net/management/100673/'

# Article(url, memoize_articles=False)最新の記事を取得できるようになる
article = Article(url, memoize_articles=False)
article.download()
article.parse()
# 発行日
print(article.publish_date)
# 著者
print(article.authors)
# 記事のタイトル
print(article.title)
# 記事の本文
print(article.text)