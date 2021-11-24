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


print('----------------------')


"""
アルゴリズム

"""


for i in range(1, 101):
    if i % 5 == 0 and i % 3 == 0:
        print(i, 'FizzBuzz')
    elif i % 3 == 0:
        print(i, 'Fizz')
    elif i % 5 == 0:
        print(i, 'Buzz')
    else:
        print(i)


print('----------------------')


"""
線形探索
データ構造の中の要素を１ひとつ確認して探しているものを見つける。シンプルなアルゴリズム
"""


def ss(number_list, n):
    found = False
    for i in number_list:
        if i == n:
            found = True
            break
    return found

numbers = range(0, 100)
s1 = ss(numbers, 2)
print(s1)
s2 = ss(numbers, 202)
print(s2)


print('----------------------')


"""
回文 : 初めから読んでも終わりから読んでも同じ文章になる
"""

def palindrome(word):
    word = word.lower()
    print(word[::-1])
    return word[::-1] == word

print(palindrome('Mother'))
print(palindrome('Mom'))


print('----------------------')


"""
アナグラム : 単語の文字を並べ替えて別の単語を作ることです
"""

def anagram(w1, w2):
    w1 = w1.lower()
    w2 = w2.lower()
    return sorted(w1) == sorted(w2)

print(anagram('iceman', 'cinema'))
print(anagram('leaf', 'tree'))


print('----------------------')


"""
出現する文字列を教える
渡された文字列にどの文字が何回出現したかを教えるアルゴリズム
文字列を１文字ずつループで回し、各文字の出現回数を辞書型に記録

"""

def count_characters(string):
    count_dict = {}
    for c in string:
        if c in count_dict:
            count_dict[c] += 1
        else:
            count_dict[c] = 1

    print(count_dict)

count_characters('Dynasty')


print('----------------------')


from collections import defaultdict

def count_characters(string):
    count_dict = defaultdict(int)
    for c in string:
        count_dict[c] += 1

    print(count_dict)

count_characters('Dynasty')


print('----------------------')


"""
再帰
1 : 再帰法は、再帰終了条件を持たせなければならない
2 : 再帰法は、状態を変えながら再帰終了条件に進んでいかなければならない
3 : 再帰法は、再起的に関数自身を呼び出さなければならない
"""

def bottles_of_beer(bob):
    """ Prints Bottle of Beer on the Wall lyrics.

    :param bob: Must be a positive integer.
    """
    if bob < 1:
        print("""No more bottles of beer on the wall.
              No more bottles of beer.""")
        return
    tmp = bob
    bob -= 1
    print("""{} bottles of ber on the wall.
          {} bottles of beer.
          Take one down, pass it around,
          {} bottles of beer on the wall.
          """.format(tmp, tmp, tmp))
    bottles_of_beer(bob)

bottles_of_beer(10)