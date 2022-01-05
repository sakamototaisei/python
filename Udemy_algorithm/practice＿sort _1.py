# ボゴソート
from typing import List
from warnings import formatwarning


# def in_order(numbers: List[int]) -> bool:
#     return all(numbers[i] <= numbers[i+1] for i in range(len(numbers)-1))


# def bogo_sort(numbers: List[int]) -> List[int]:
#     while not in_order(numbers):
#         random.shuffle(numbers)
#     return numbers


# if __name__ == '__main__':
#     import random
#     nums = [random.randint(0, 1000) for _ in range(10)]
#     print(bogo_sort(nums))


print('----------------------')


# バブルソート
def bubble_sort(numbers: List[int]) -> List[int]:
    for i in range(len(numbers)):
        for j in range(len(numbers) - 1 - i):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers

if __name__ == '__main__':
    import random
    nums = [random.randint(0, 1000) for i in range(10)]
    print('バブルソート')
    print(bubble_sort(nums))


print('----------------------')


# シェーカーソート
def cocktail_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    swapped = True
    start = 0
    end = len_numbers - 1
    while swapped:
        swapped = False
        for  i in range(start, end):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                swapped = True

        if not swapped:
            break

        swapped = False
        end -= 1

        for i in range(end-1, start-1, -1):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                swapped = True

        start += 1

    return numbers

if __name__ == '__main__':
    import random
    nums = [random.randint(0, 1000) for _ in range(10)]
    print('シェーカーソート')
    print(cocktail_sort(nums))


print('----------------------')


# コムソート
def comb_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    gap = len(numbers)
    swapped = True

    while gap != 1 or swapped:
        gap = int(gap /1.3)
        if gap < 1:
            gap = 1

        swapped = False

        for i in range(0, len_numbers - gap):
            if numbers[i] > numbers[i+gap]:
                numbers[i], numbers[i+gap] = numbers[i+gap], numbers[i]

    return numbers

if __name__ == '__main__':
    import random
    nums = [random.randint(0, 1000) for _ in range(10)]
    print('コムソート')
    print(comb_sort(nums))


print('----------------------')


# 選択ソート
def selection_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    for i in range(len_numbers):
        min_idx = i
        for j in range(i+1, len_numbers):
            if numbers[min_idx] > numbers[j]:
                min_idx = j

        numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]

    return numbers

if __name__ == '__main__':
    import random
    nums = random.randint