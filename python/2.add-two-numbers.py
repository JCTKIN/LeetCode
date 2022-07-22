#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum = self.decimalize(l1) + self.decimalize(l2)
        node = self.toListNode(sum)
        return node

    def decimalize(self, l: Optional[ListNode])  -> int:
        val = l.val
        index = 1
        while l.next is not None:
            l = l.next
            val += l.val * (10 ** index)
            index += 1
        return val

    def toListNode(self, num: int) -> Optional[ListNode]:
        num_list = [int(n) for n in str(num)]
        head = ListNode(num_list[0])
        for n in num_list[1:]:
            head = ListNode(n, head)
        return head
        
# @lc code=end

