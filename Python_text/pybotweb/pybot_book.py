def book_command(command):
    cmd, keyword = command.split(maxsplit=1)
    results = []
    with open('book_data.tsv', encoding='utf-8') as f:
        for line in f:
            cols = line.split('\t')
            if keyword in cols[0]:
                results.append(line)

        if len(results) > 0:
            response = '<br>'.join(results)
            # 1件以上見つかった場合は改行して連結させる
            response = '<br>' + response
        else:
            response = '「{}」が含まれる書籍は見つかりませんでした'.format(keyword)
        return response