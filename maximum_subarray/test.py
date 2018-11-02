def max_child(arr, low, heigh):
    if low == heigh:
        return arr[low]
    mid = (heigh + low) // 2
    # print("mid:" ,mid)
    m1 = max_child(arr, low, mid)
    # print("m1:", m1)
    m2 = max_child(arr, mid + 1, heigh)
    # print("m2:", m2)

    now_left = arr[mid]
    left = arr[mid]
    for i in range(mid - 1, low - 1, -1):
        now_left = now_left + arr[i]
        if now_left > left:
            left = now_left

    now_right = arr[mid + 1]
    right = arr[mid + 1]
    for j in range(mid + 2, heigh + 1):
        now_right = now_right + arr[j]
        if now_right > right:
            right = now_right
    m3 = left + right
    # print("m3:", m3)
    result = max(m1, m2, m3)
    return result


arr = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
print(max_child(arr, 0, len(arr) - 1))
