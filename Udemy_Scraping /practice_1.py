limit = 100
list_a = []
for i in range(2, limit):
    for j in range(2, i):
        # print('i = {}, j = {}'.format(i, j))
        if i % j == 0:
            break
    else:
        print(i, end=' ')
        # list_a.append(i)
        # print('list_a = {}'.format(list_a))

