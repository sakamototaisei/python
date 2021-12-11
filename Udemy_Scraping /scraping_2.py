import newspaper
import csv
import datetime


csv_date = datetime.datetime.today().strftime('%Y%m%d')
csv_file_name = 'bloomberg_' + csv_date + '.csv'

f = open(csv_file_name, 'w', encoding='utf-8')
writer = csv.writer(f, lineterminator='\n')
csv_header = ['記事番号', 'タイトル', 'URL', 'サマリー']
writer.writerow(csv_header)

url = 'https://www.bloomberg.co.jp/'
website = newspaper.build(url, memoize_articles=False, MAX_SUMMARY=300)
i = 0
for article in website.articles:
    csv_list = []

    article.download()
    article.parse()
    article.nlp()

    print('記事', str(i), ':', article.title)
    print(article.url)
    print(article.summary)
    print('\n')

    csv_list.append(str(i))
    csv_list.append(article.title)
    csv_list.append(article.url)
    csv_list.append(article.summary)
    writer.writerow(csv_list)

    if i > 9:
        break
    i += 1
f.close()