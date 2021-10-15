list_a = []
for i in range(1, 41):
    if i % 3 == 0 and '3' in str(i):
        list_a.append(i)

print('作成したリスト : {}'.format(list_a))


list_a = [1, 2, 3, 4, 5]

print('リスト内合計 : {}'.format(sum(list_a)))