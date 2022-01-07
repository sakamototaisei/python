# ハッシュテーブル
import hashlib
from typing import Any


class HashTable(object):

    def __init__(self, size=10) -> None:
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash(self, key) -> int:
        # encode()はkeyをバイナリーに変換しmd5に渡す。
        # hexdigest()は何度やっても同じ文字列ハッシュが返ってくる
        # ハッシュの文字列16進数をintに変換base=16
        return int(hashlib.md5(key.encode()).hexdigest(), base=16) % self.size

    def add(self, key, value) -> None:
        index = self.hash(key)
        for data in self.table[index]:
            if data[0] == key:
                data[1] = value
                break
        else:
            self.table[index].append([key, value])

    def print(self) -> None:
        for index in range(self.size):
            print(index, end=' ')
            for data in self.table[index]:
                print('-->', end=' ')
                print(data, end=' ')

            print()

    def get(self, key) -> Any:
        index = self.hash(key)
        for data in self.table[index]:
            if data[0] == key:
                return data[1]

    # Python的に追加するときに呼ばれる
    def __setitem__(self, key, value) -> None:
        self.add(key, value)

    # Python的に呼び出す時に呼ばれる
    def __getitem__(self, key) -> Any:
        return self.get(key)


if __name__ == '__main__':
    hash_table = HashTable()
    hash_table['car'] = 'Tesla'
    hash_table['car'] = 'Toyota'
    hash_table['pc'] = 'Mac'
    hash_table['sns'] = 'YouTube'
    # print(hash_table.table)
    hash_table.print()
    print(hash_table['sns'])