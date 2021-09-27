# fp = open('sample.txt', 'w')
# fp.write('This is sample1.\n')
# fp.write('This is sample2.\n')
# fp.close()

# # fp = open('sample.txt', 'r', encoding='utf-8')
# # fp.read()
# with open('sample.txt', 'r') as fp:
#   data = fp.read()

# for line in data:
#   print(line, end='')

try:
  fp = open('sample.txt', 'r')
  line = fp.readline()
  num = int(line)
except OSError:
  print('OSのエラーです')
except (ValueError, ZeroDivisionError, TypeError):
  print('数値演算のエラー')
except Exception:
  print('一般的なエラーです')
else:
  print('結果は{}です。'.format(num))
finally:
  fp.close()