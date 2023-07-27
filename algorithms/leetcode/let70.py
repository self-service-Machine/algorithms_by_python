"""
假设你正在爬楼梯。需要 n阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？



示例 1：

输入：n = 2
输出：2
解释：有两种方法可以爬到楼顶。
1. 1 阶 + 1 阶
2. 2 阶
示例 2：

输入：n = 3
输出：3
解释：有三种方法可以爬到楼顶。
1. 1 阶 + 1 阶 + 1 阶
2. 1 阶 + 2 阶
3. 2 阶 + 1 阶


提示：

1 <= n <= 45

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/climbing-stairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        dp = [0 for _ in range(n + 1)]
        dp[1], dp[2] = 1, 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 2] + dp[i - 1]

        return dp[n]


# 找零问题
def dp_mark_change(coin_value_list, change, min_coins):
    for cents in range(1, change + 1):
        coin_count = cents
        for j in [c for c in coin_value_list if c <= cents]:
            if min_coins[cents - j] + 1 < coin_count:
                coin_count = min_coins[cents - j] + 1
        min_coins[cents] = coin_count
    return min_coins[change]


if __name__ == '__main__':
    # n = 5
    # print(Solution().climbStairs(n))
    print(dp_mark_change([1, 5, 10, 21, 25], 63, [0] * 64))
