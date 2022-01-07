# キューを逆に並び替え
# キュー
from collections import deque
from typing import Any


class Queue(object):

    def __init__(self) -> None:
        self.queue = []
        self.reverse_list = []

    def enqueue(self, data: Any) -> None:
        self.queue.append(data)

    def dequeue(self) -> Any:
        if self.queue:
            return self.queue.pop(0)

# リバースさせる関数
def reverse(queue: deque) -> deque:
    new_queue = deque()
    while queue:
        new_queue.append(queue.pop())
    [queue.append(d) for d in new_queue]



if __name__ == '__main__':
    q = deque()
    q.append(1)
    q.append(2)
    q.append(3)
    q.append(4)
    print(q)
    reverse(q)
    print(q)
