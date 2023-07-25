"""
给你一个大小为 m x n 的整数矩阵 mat 和一个整数 target 。
从矩阵的 每一行 中选择一个整数，你的目标是最小化所有选中元素之和与目标值 target 的 绝对差 。

返回 最小的绝对差 。

a 和 b 两数字的 绝对差 是 a - b 的绝对值。


示例一：
输入：mat = [[1,2,3],
            [4,5,6],
            [7,8,9]],
    target = 13
输出：0
解释：一种可能的最优选择方案是：
- 第一行选出 1
- 第二行选出 5
- 第三行选出 7
所选元素的和是 13 ，等于目标值，所以绝对差是 0 。


示例二：
输入：mat = [[1],[2],[3]], target = 100
输出：94
解释：唯一一种选择方案是：
- 第一行选出 1
- 第二行选出 2
- 第三行选出 3
所选元素的和是 6 ，绝对差是 94 。

示例三：
输入：mat = [[1,2,9,8,7]], target = 6
输出：1
解释：最优的选择方案是选出第一行的 7 。
绝对差是 1 。



m == mat.length
n == mat[i].length
1 <= m, n <= 70
1 <= mat[i][j] <= 70
1 <= target <= 800


"""
from typing import List


class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        def dfs(i, target):
            if target < 0:
                return False
            if i == m:
                return target == 0
            for j in range(n):
                if dfs(i + 1, target - mat[i][j]):
                    return True

        # 行数
        m = len(mat)
        # 列数
        n = len(mat[0])
        for i in range(1000000000):
            if dfs(0, target - i) or dfs(0, target + i):
                return i


def check(nums, target):
    result = []
    for i in range(nums.__len__()):
        if nums.__len__() > 1:
            check(nums[1:], target - nums[0][i])
        else:
            # 差的数组
            result.append((target - nums[0][i]).__abs__())
    result.sort()
    if result:
        return result[0]
    else:
        return None


if __name__ == '__main__':

    # d = Solution().minimizeTheDifference([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 13)
    # d = check([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 13)
    # print(d)
    a = False
    b = False
    c = a + b
    print(c)