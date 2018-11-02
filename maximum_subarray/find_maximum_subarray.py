'''
寻找一个数组中的最大子数组，采用递归的思想来计算
过程中才用分治的策略。
只有当数组中包含负数的时候，最大子数组才有意义，因为如果都大于0，最大子数组必然是整个数组的和
'''
import math

def find_maximum_subarray(array, low, high):
    '''
    寻找最大子数组的函数
    :param array:需要寻找子数组的原数组
    :param low: 最小值的下标
    :param high:最大值的下标
    :return:最大子数组的和及其开始的下标
    '''
    '''
    递归调用
    '''
    if low == high:
         return (low, high, array[low])  # 基础情形当数组中只有一个元素的时候
    else:
        mid = math.floor(low + (high - low) / 2) #向下取整
        left_low, left_high, left_sum = find_maximum_subarray(array, low, mid)
        right_low, right_high, right_sum = find_maximum_subarray(array, mid + 1, high)
        cross_low, cross_high, cross_sum = find_max_crossing_subarray(array, low, mid, high)

    if left_sum >= right_sum and left_sum >= cross_sum:
        return (left_low, left_high, left_sum)
    elif right_sum >= left_sum and right_sum >= cross_sum:
        return right_low, right_high, right_sum
    else:
        return cross_low, cross_high, cross_sum


def find_max_crossing_subarray(array, low, mid, right):
    left_sum = array[mid]
    sum = 0
    max_left = mid
    for i in range(mid,low,-1):
        sum = sum + array[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i
    max_right = mid+1
    right_sum = array[mid+1]
    sum = 0
    for j in range(mid + 1, right,1):
        sum = sum + array[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j
    return max_left, max_right, left_sum + right_sum

array = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
low_boundary = 0
high_boundary = len(array)-1
print(find_maximum_subarray(array, low_boundary, high_boundary))



