# マージソート

data = [1, 3, 2, 5, 4, 2, 1]
# print(data[:3]) # [1,3,2]が表示


def sort(data):
    if len(data) <= 1:               # 長さが1以下の場合は分割できないため終了
        return data

    # 分割操作
    print('-'*20 + '分割スタート')
    mid = len(data) // 2            # 真ん中を計算
    print('mid = {}'.format(mid))
    left = sort(data[:mid])         # 再帰で前半分を分割してleftに
    print('left = {}'.format(left))
    right = sort(data[mid:])        # さいきで後半を分割してrightに
    print('right = {}'.format(right))


    # 統合操作
    print('-'*20 + 'マージスタート')
    merge, l, r = [], 0, 0          # mergeに統合
    while l < len(left) and r < len(right):  # leftとrightの両方に要素がある場合
        if left[l] <= right[r]:     # 左側<=右側の場合
            merge.append(left[l])   # 左側をmergeに加える
            l += 1
        else:
            merge.append(right[r])  # 右側をmergeに加える
            r += 1
        print('merge = {}'.format(merge))
    print('余り処理 l = {}, r = {}'.format(l, r))
    if l < len(left):               # 左側が余った場合に残りを追加
        merge.extend(left[l:])
    elif r < len(right):         # 右側が余った場合に残りを追加
        merge.extend(right[r:])
    print('余り処理終了しました left = {}, right = {}'.format(left, right))
    return merge


data = sort(data)
print(data)