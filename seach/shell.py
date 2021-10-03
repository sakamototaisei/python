# シェルソート

data = [1, 3, 2, 5, 4, 2, 1, 6, 8]


def sort(data):
    gaps = [7, 3, 1]                               # ギャップの値をあらかじめ決めておく
    for gap in gaps:                               # gapをだんだん狭めて繰り返す
        for start in range(gap):                   # gap分離れた複数の組みを順番にソート
            print('s = {}, gap = {}'.format(start, gap))
            for i in range(start, len(data), gap):  # gapの幅で飛ばしながら挿入ソート
                # print(i)
                for j in range(i-gap, -1, -gap):   # 終値を-1に設定(0まで実行)
                    print('j = {}, i = {}, gap = {}'.format(j, i, gap))
                    print('-'*20)
                    if data[j] > data[j+gap]:        # gap分離れた要素で前の方が大きい場合
                        data[j], data[j+gap] = data[j+gap], data[j]  # 要素を入れ替える
                        print('入れ替え処理が行われました')
                        print('-'*20)
                    else:
                        break                      # 挿入する部分が見つかれば終わり


sort(data)
print(data)
