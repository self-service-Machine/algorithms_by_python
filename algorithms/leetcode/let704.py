"""
给定一个n个元素有序的（升序）整型数组nums 和一个目标值target ，写一个函数搜索nums中的 target，如果目标值存在返回下标，否则返回 -1。


示例 1:

输入: nums = [-1,0,3,5,9,12], target = 9
输出: 4
解释: 9 出现在 nums 中并且下标为 4

示例2:

输入: nums = [-1,0,3,5,9,12], target = 2
输出: -1
解释: 2 不存在 nums 中因此返回 -1


提示：

你可以假设 nums中的所有元素是不重复的。
n将在[1, 10000]之间。
nums的每个元素都将在[-9999, 9999]之间。

"""
from typing import List


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        left, right = 0, n-1

        while left <= right:
            mid = (left + right) >> 1
            if nums[mid] > target:
                right = mid -1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return -1


if __name__ == '__main__':
    nums = [-1,0,3,5,9,12]
    # nums = [9]
    target = 2
    print(Solution().search(nums, target))

    # nums.sort()
    # d = Solution().search(nums, target)
    # print(d)
