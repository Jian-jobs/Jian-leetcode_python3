
# coding:utf-8


# 冒泡排序
# 1. 外层循环负责帮忙递减内存循环的次数【1, len-1】
# 2. 内层循环负责前后两两比较, index 的取值范围【0, len-2】 len-1-i 次，求最大值放到最后

def bubble_sort(nums):
    # [1, len-1]
    for i in range(1, len(nums)-1):
        print(i)
        # [0, len(nums)-i] j is index
        for j in range(len(nums)-i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                print(j, nums)
    return nums

if __name__ == "__main__":
    nums = [2, 6, 8, 5, 4, 9, 3, 7]
    bubble_sort(nums)
    print('result is: ', nums)

# reference: https://github.com/apachecn/awesome-algorithm/blob/master/src/py3.x/sort/BubbleSort.py