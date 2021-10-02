挿入ソート

data = [1, 3, 2, 5, 4, 2, 1]


def sort(data):
    for i in range(0, len(data)):       # 最初から順に整列させていく
        print('iの値は = {}'.format(i))
        for j in range(i-1, -1, -1):      # 一番後ろの要素を挿入する場所を探す
            print('1回目の値検出  jのinx={} jの値は{}'.format(j, data[j]))
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]  # 要素を入れ替える
                print('2回目の値検出  入れ替え処理  jのinx={} jの値は{},   jのinx[j+1]={} j+1の値は{}'.format(j, data[j], j+1, data[j+1]))
            else:
                break                         # 挿入する部分が見つからなければ終わり


sort(data)
print(data)


list_a = [5,4,3,2,1,0]
# for i in range(0, len(list_a)): # 0 ~ 6まで
#   # print('i = {}'.format(i))
for j in range(5, -1, -1):
    print('j = {}'.format(list_a[j]))
