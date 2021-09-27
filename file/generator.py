# def count_up():
#   n = 1
#   while True:
#     yield n
#     n += 1

# generator = count_up()
# for num in generator:
#   print(num, end=' ')
#   if num == 7:
#     break


# for num in generator:
#   print(num, end=' ')
#   if num == 15:
#     break

month_name = [(1, 'January'), (2, 'February'), (3, 'March')]
print(sorted(month_name, key = lambda x : x[1]))

def wrapping(contents):
  print('---start---')
  contents()
  print('---end---')

@wrapping
def contents():
  print('これが内容です')