"""
给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。



示例 1：


输入：head = [1,2,3,4]
输出：[2,1,4,3]
示例 2：

输入：head = []
输出：[]
示例 3：

输入：head = [1]
输出：[1]

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/swap-nodes-in-pairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        else:
            node = head
            head = head.next
            node.next = head.next
            head.next = node

            head.next.next = Solution().swapPairs(head.next.next)
            return head


if __name__ == '__main__':
    head = [1, 2, 3, 4]
    # ListNode()
    head_node = ListNode()
    l = ListNode()
    for i in head:
        if i == 1:
            head_node.val = i
            head_node.next = l
            continue
        l.val = i
        l.next = ListNode()
        l = l.next

    node = Solution().swapPairs(head_node)
    print()
