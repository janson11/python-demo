import math

# 二分查找的运行时间为对数时间：O(log n)
# 一些常见的大O运行时间
# O(logn)也叫对数时间，这样的算法包括二分查找
# O(n)也叫线性时间，这样的算法包括简单查找。
# O(n*logn) 快速排序：一种速度较快的排序算法。
# O(n*2) 选择排序：一种速度较慢的排序算法。。
# O(n!) 旅行商问题的解决方案————一种非常慢算法。

def binary_search(list, item):
    count = 0
    low = 0
    high = len(list) - 1

    while low <= high:
        count += 1
        print("count:", count)
        # int 向下取整
        mid = int((low + high) / 2)
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_list = [1, 3, 5, 7, 9]
my_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

# 假设有一个包含128个名字的有序列表，你要使用二分查找在其中查找一个名字，请问最多需要几步才能找到?
# 128 -> 64 -> 32 -> 16 -> 8 -> 4 -> 2 -> 1 8步 2^8=128
# 256  9步 2^9=256

if __name__ == '__main__':
    # print(binary_search(my_list, 3))
    # print(binary_search(my_list, -1))
    print(binary_search(my_list1, 1))
    print(math.pow(2,9))
