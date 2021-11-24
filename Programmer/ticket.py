"""
チケット行列

映画のチケットを買う待ち行列をプログラミンングで表現
"""

import time
import random


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


# チケット行列をプログッラミングで表現した関数
def simulate_line(till_show, max_time):
    """
    till_show : 整数で、あと何秒で映画が始まるかを表現
    max_time  : 整数で、ある人がチケットを買うのにかかる最大の秒数を表しています
    """
    pq = Queue()
    tix_sold = []

    for i in range(100):
        pq.enqueue('person' + str(i))

    t_end = time.time() + till_show
    now = time.time()
    while now < t_end and not pq.is_empty():
        now = time.time()
        r = random.randint(0, max_time)
        time.sleep(r)
        person = pq.dequeue()
        print(person)
        tix_sold.append(person)
    return tix_sold

sold = simulate_line(5, 1)
print(sold)