# ボゴソート(適当に並び替える猿でもできるソート)
import random
from typing import List


#引数にlistで返り値にboolを返すことを書いている
def in_order(numbers: List[int]) -> bool:
    return all(numbers[i] <= numbers[i+1] for i in range(len(numbers)-1))
    # for i in range(len(numbers)-1):
    #     if numbers[i] > numbers[i+1]:
    #         return False
    # return True


def bogo_sort(numbers: List[int]) -> List[int]:
    # 並び順がTrueになったら抜ける
    while not in_order(numbers):
        # 中身をランダムに入れ替える
        random.shuffle(numbers)
    return numbers


if __name__ == '__main__':
    nums = [random.randint(0, 1000) for _ in range(10)]
    # 数値が大きいと、処理に時間がかかる
    print(bogo_sort(nums))