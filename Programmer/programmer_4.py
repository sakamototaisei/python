"""
独学プログラマー

第４部
"""

# データ構造
class Stack(object):

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        last = len(self.items) - 1
        return self.items[last]

    def size(self):
        return len(self.items)

stack = Stack()
# print(stack.is_empty())

# stack.push(1)
# print(stack.is_empty())

# item = stack.pop()
# print(item)
# print(stack.is_empty())

# for i in range(0, 6):
#     stack.push(i)

# print(stack.peek())
# print(stack.size())

for c in 'Hello':
    stack.push(c)

reverse = ''

while stack.size():
    reverse += stack.pop()

print(reverse)


print('----------------------')


"""
キュー
"""

class Queue(object):

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

a_queue = Queue()
# print(a_queue.is_empty())

for i in range(5):
    a_queue.enqueue(i)

while a_queue.size():
    print(a_queue.dequeue())

print()
print(a_queue.size())