'''
计数排序：
输入：A[1...n]
输出B[1...n]
C[0...k]临时存储空间
'''


def COUNTING_SORT(A, k):
    n = len(A)
    B = [0 for i in range(n)]
    C = [0 for i in range(k)]  # 创建一个指定大小的list,并赋值0
    for j in range(1, len(A)):
        C[A[j]] = C[A[j]] + 1
    for i in range(1, k):
        C[i] = C[i] + C[i - 1]
    for j in range(len(A)+1, 1, -1):
        B[C[A[j]]] = A[j]
        C[A[j]] = C[A[j]] - 1
    return B


A = [2, 5, 3, 0, 2, 3, 0, 3]
# A = [6, 0, 2, 0, 1, 3, 4, 6, 1, 3, 2]
k = max(A)
print(COUNTING_SORT(A, k))
