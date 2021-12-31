list_a = [5, 3, 2, 8, 9, 6, 1, 4, 7]

def bubble_sort(numbers_list):
    for i in range(len(numbers_list)):
        for j in range(len(numbers_list) - 1 -i):
            if numbers_list[j] > numbers_list[j+1]:
                numbers_list[j], numbers_list[j+1] = numbers_list[j+1], numbers_list[j]
    return numbers_list

print(list_a)
print(bubble_sort(list_a))