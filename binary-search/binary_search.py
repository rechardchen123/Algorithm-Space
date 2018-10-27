'''
实现二分查找（binary search）
二分查找关键的三个下标点（L,M,R）
每次查找减半，时间性能是O(logn)
非常高效，但是在查找两端的元素的时候，是时间性能最低下的.
'''
import math

def binary_search(list, find_key):
    list.sort()
    left_index = list.index(min(list))
    right_index = list.index(max(list))

    while (left_index < right_index):
        middle_index = math.floor(left_index + (right_index - left_index) / 2)
        if (find_key < list[middle_index]):
            right_index = middle_index - 1
        elif (list[middle_index] < find_key):
            left_index = middle_index + 1
        else:
            return middle_index
    return find_key, list.index[find_key]


test = [18, 23, 29, 10, 11, 12, 16, 33, 54, 48, 68, 77, 98, 84]
find_key = 29
result = binary_search(test, find_key)
print(result)
