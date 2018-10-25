'''
元素去重问题
输入：数组/向量
输出：去除数组/向量中重复的元素
算例：7，9，3，9，2，1，7，2
结果：1,2,3,7,9
方法：先进行排序的预处理，再双边界控制算法，即左右下标做循环的方式进行
'''
import random
# 先测试
# list = [7, 8, 3, 9, 2, 1, 7, 2]
#
# list.sort()
# list1 = []
#
# min = min(list)
# left_bound = list.index(min)
#
# if left_bound < len(list):
#     right_bound = left_bound + 1
#     for right_bound in range(len(list)):
#         if list[right_bound] != list[left_bound]:
#             list1.append(list[left_bound])
#             left_bound = right_bound
#         else:
#             continue
# #最后一个元素不会输出，而手动添加到列表中
# list1.append(list[-1])
# print(list1)


# 随机生成的大的数据列
list2 = [random.randint(0,50)for _ in range(50)]
print(list2)
list3 = []
list2.sort()

miniminze_index_list2 = min(list2)
left_bound_list2 = list2.index(miniminze_index_list2)

if left_bound_list2 < len(list2):
    right_bound_list2 = left_bound_list2 + 1
    for right_bound_list2 in range(len(list2)):
        if list2[right_bound_list2] != list2[left_bound_list2]:
            list3.append(list2[left_bound_list2])
            left_bound_list2 = right_bound_list2
        else:
            continue

list3.append(list2[-1])
print(list3)