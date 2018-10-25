'''
归并排序：
有如下一个list=[5,2,4,7,1,3,2,6]
利用归并排序实现,采用divide and conqure(分治法的思想)
为[1,2,2,3,4,5,6,7]
1.先找到最小问题规模时的求解方法；
2.然后考虑随着问题规模增大时的求解方法；
3.找到求解的递归函数式后（各种规模或因子），设计递归程序即可
'''


def merge_sort(seq):
    '''归并排序'''
    if len(seq) <= 1:
        return seq
    mid = int(len(seq) / 2)  # 将列表分成两个小的列表
    # 分别对左右两个列表进行处理，分别返回两个排序好的列表
    left = merge_sort(seq[:mid])
    right = merge_sort(seq[mid:])
    # 对排序好的两个列表合并，产生一个新的排序好的列表
    return merge(left, right)


def merge(left, right):
    '''合并两个已排序好的列表，产生一个新的已排序好的列表'''
    result = []  # 新的已排序好的列表
    i = 0
    j = 0  # 下标
    # 对两个列表中的元素 两两对比
    # 将最小的元素，放到result中，并对当前列表下标加1
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


seq = [5, 2, 4, 7, 1, 3, 2, 6]
print("排序前", seq)
result = merge_sort(seq)
print("排序后", result)
