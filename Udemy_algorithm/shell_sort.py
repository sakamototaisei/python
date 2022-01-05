# シェルソート
from typing import List


def shell_sort(numbers: List[int]) -> List[int]:
    lne_numbers = len(numbers)
    gap = lne_numbers // 2

    while gap > 0:
        for i in range(gap, lne_numbers):
            temp = numbers[i]
            j = i
            while j >= gap and numbers[j-gap] > temp:
                numbers[j] = numbers[j-gap]
                j -= gap
            numbers[j] = temp
        gap //= 2

    return numbers


if __name__ == '__main__':
    # nums = [5, 6, 9, 2, 3]
    import random
    nums = [random.randint(0, 1000) for _ in range(10)]
    print(shell_sort(nums))