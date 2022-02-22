# sum函数的代码
def sum(arr):
    total = 0
    for x in arr:
        total += x
    return total


# 编写前述sum函数的递归
def sumRecursion(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + sumRecursion(arr[1:])


# 编写一个递归函数来计算列表中包含的元素数
def calc_len_of_list(nums):
    if len(nums) == 0:
        return 0
    else:
        nums.pop()
        return 1 + calc_len_of_list(nums)


# 找出列表中最大的数字
def find_the_biggest(list):
    if (len(list)) == 0:
        return 0;
    elif (len(list)) == 1:
        return list[0]
    else:
        biggest = list[len(list) - 1]
        if biggest >= find_the_biggest(list[0:len(list) - 1]):
            return biggest
        else:
            return find_the_biggest(list[0:len(list) - 1])


# 快速排序
def quicksort(array):
    if len(array) < 2:
        # 基线条件，为空或者只包含一个元素的数组是有序的
        return array
    else:
        # 递归条件
        pivot = array[0]
        # 由所有小于或等于基准值的元素组成的子数组
        less = [i for i in array[1:] if i <= pivot]
        # 由所有大于基准值的元素组成的子数组
        greater = [i for i in array[1:] if i >= pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


if __name__ == '__main__':
    arr = [1, 2, 3, 4]
    print(sum(arr))
    print(sumRecursion(arr))
    print(calc_len_of_list([1, 3, 5, 8, 12, 6, 7]))
    print(find_the_biggest([8, 5, 2]))
    print("++++++++")
    print(quicksort([10, 5, 2, 3]))
