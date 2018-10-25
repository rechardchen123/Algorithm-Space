'''
元素去重问题
输入：数组/向量
输出：去除数组/向量中重复的元素
算例：7，9，3，9，2，1，7，2
结果：1,2,3,7,9
'''
# 先测试
list = [7, 8, 3, 9, 2, 1, 7, 2]
# 先进行排序预处理
list.sort()
list1 = []
# 采用双边界控制算法
# 首先命名左边界为0的位置
min = min(list)
left_bound = list.index(min)
# while (left_bound < len(list)):
#     right_bound = left_bound + 1
#     for right_bound in range(len(list)):
#         if list[right_bound] != list[left_bound]:
#             calculate_num = right_bound - left_bound
#             break
#             print(list1.append(list[left_bound]), calculate_num)
#             left_bound = right_bound

if left_bound < len(list):
    right_bound = left_bound + 1
    for right_bound in range(len(list)):
        if list[right_bound] != list[left_bound]:
            list1.append(list[left_bound])
            left_bound = right_bound
        else:
            continue

list1.append(list[-1])
print(list1)
