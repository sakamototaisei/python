import heapq
from typing import List


numbers = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
heap_data = []

# 一発でヒープさせる
heapq.heapify(numbers)
print(numbers)
# 大きいの引数の数指定で表示
print(heapq.nlargest(3, numbers))
# 上記の逆
print(heapq.nsmallest(3, numbers))

# for num in numbers:
#     heapq.heappush(heap_data, num)

# print(heap_data)

# while heap_data:
#     print(heapq.heappop(heap_data))

print('---------------')
from collections import Counter


def top_n_with_heap(words: List[int], n: int) -> List[int]:
    d = {}
    for word in words:
        d[word] = d.get(word, 0) + 1
    print(d)

    counter_word = Counter(words)
    # # トップ３のランキングが
    # print(counter_word.most_common(n))

    data = [(-counter_word[word], word) for word in counter_word]
    heapq.heapify(data)
    return ([heapq.heappop(data)[1] for _ in range(n)])

if __name__ == '__main__':
    w = ['python', 'c', 'java', 'go', 'python', 'c', 'go', 'python']
    print(top_n_with_heap(w, 3))
