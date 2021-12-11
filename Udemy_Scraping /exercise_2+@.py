import newspaper


# url_itmedia = 'https://www.itmedia.co.jp/'
# url_thebridge = 'https://thebridge.jp/'

# def get_itmedia():
#     website = newspaper.build(url_itmedia, memoize_articles=False, MAX_SUMMARY=150)
#     i = 1
#     for article in website.articles:
#         article.download()
#         article.parse()
#         article.nlp()

#         print('記事', str(i), ':', article.title)
#         print(article.url)
#         print(article.summary)
#         print('\n')

#         if i > 9:
#             break
#         i += 1

# def get_thebridge():
#     website = newspaper.build(url_thebridge, memoize_articles=False, MAX_SUMMARY=150)
#     i = 1
#     for article in website.articles:
#         article.download()
#         article.parse()
#         article.nlp()

#         print('記事', str(i), ':', article.title)
#         print(article.url)
#         print(article.summary)
#         print('\n')

#         if i > 9:
#             break
#         i += 1

# get_itmedia()
# print('------------------------------')
# get_thebridge()


urls = ['https://www.itmedia.co.jp/', 'https://thebridge.jp/']

for url in urls:
    website = newspaper.build(url, memoize_articles=False, MAX_SUMMARY=150)
    i = 1
    for article in website.articles:
        article.download()
        article.parse()
        article.nlp()

        print('記事', str(i), ':', article.title)
        print(article.url)
        print(article.summary)
        print('\n')

        if i > 9:
            break
        i += 1