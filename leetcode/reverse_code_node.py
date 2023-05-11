"""
leetcode 2 两数之和
Example:
输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.
"""


class listNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumber(self, l1: listNode, l2: listNode) -> listNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        # 获取节点
        dummy = listNode(0)
        p = dummy
        # 进位变量
        carry = 0

        while l1 and l2:
            # 将两个节点的value和上一次相加的值取余为和list的当前位
            p.next = listNode((l1.val + l2.val + carry) % 10)
            # 将相加的和整除10的商作为下一位进位值
            carry = (l1.val + l2.val + carry) // 10
            # 两节点均向后移动
            l1 = l1.next
            l2 = l2.next
            p = p.next

        if l2:
            while l2:
                p.next = listNode((l2.val + carry) % 10)
                carry = (l2.val + carry) // 10
                l2 = l2.next
                p = p.next

        if l1:
            while l1:
                p.next = listNode((l1.val + carry) % 10)
                carry = (l1.val + carry) // 10
                l2 = l2.next
                p = p.next

        if carry == 1:
            p.next = listNode(1)

        return dummy.next
