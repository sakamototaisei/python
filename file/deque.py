from collections import deque

Q = deque() # deque型のインスタンスQを作成
Q.append('A')
Q.append('B')
Q.append('C')
print(Q)
print(Q.popleft())
print(Q)