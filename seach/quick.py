# クイックソート

data = [1, 3, 2, 5, 4, 2, 1]


def sort(data):
    n = len(data)
    pivot = data[n//2]                    # 今回はの基準には、真ん中の値を利用
    print('n = {}'.format(n))
    print('pivot = {}'.format(pivot))
    print('-'*10)
    left, right, middle = [], [], []
    for i in range(n):
        if data[i] < pivot:               # 基準値より小さい場合は、左部分列leftに追加
            left.append(data[i])
        elif data[i] > pivot:             # 基準値より大きい場合は、右部分裂rightに追加
            right.append(data[i])
        else:
            middle.append(data[i])        # 基準値と同じ場合には、部分列middleに追加
    if left:
        print('middle = {}'.format(middle))
        print('left = {}'.format(left))
        print('right = {}'.format(right))
        print('left再帰')
        left = sort(left)                 # 再帰でleftを分割
        print('-'*20)
        print('left再後')
        print('middle = {}'.format(middle))
        print('left = {}'.format(left))
        print('right = {}'.format(right))
        print('-'*20)
    if right:
        print('middle = {}'.format(middle))
        print('left = {}'.format(left))
        print('right = {}'.format(right))
        print('right再帰')
        right = sort(right)               # 再帰でrightを分割
        print('-'*20)
        print('right再後')
        print('middle = {}'.format(middle))
        print('left = {}'.format(left))
        print('right = {}'.format(right))
        print('-'*20)
    return left + middle + right          # 順番に部分を連結させて、戻り値とする


data = sort(data)
print(data)
