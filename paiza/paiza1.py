import numpy as np

inp = 'A A'
print('入力値', inp)
s = list(inp)
return_list = []
# 英字から5進数変換
for i in s:
    l = list(i)
    for j in l:
        if j == 'A':
            a = '0'
            return_list.append(a)
        elif j == 'B':
            b = '1'
            return_list.append(b)
        elif j == 'C':
            c = '2'
            return_list.append(c)
        elif j == 'D':
            d = '3'
            return_list.append(d)
        elif j == 'E':
            e = '4'
            return_list.append(e)
        else:
            z = ' '
            return_list.append(z)
s = ''.join(return_list)
s1 = s.split()
s2 = []
for i in s1:
    s2.append(int(i))

s3 = []
for i in s2:
    # 5進数から10進数に変換
    s3.append(int(str(i), base=5))
# 10進数から5進数に変換
l2 = np.base_repr(sum(s3), base=5)
return_list2 = list(l2)

# 5進数から英数字
res = []
for s in return_list2:
    if s == '0':
        a = 'A'
        res.append(a)
    elif s == '1':
        b = 'B'
        res.append(b)
    elif s == '2':
        c = 'C'
        res.append(c)
    elif s == '3':
        d = 'D'
        res.append(d)
    elif s == '4':
        e = 'E'
        res.append(e)
print('出力値', ''.join(res))