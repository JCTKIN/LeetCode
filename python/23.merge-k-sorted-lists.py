#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from queue import PriorityQueue

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = cur = ListNode()
        pq = PriorityQueue()
        c = 0
        for l in lists:
            if l:
                pq.put((l.val, c, l))
                c += 1
        while not pq.empty():
            val, _, node = pq.get()
            cur.next = ListNode(val)
            cur = cur.next
            node = node.next
            if node:
                pq.put((node.val, c, node))
                c += 1
        return head.next

# @lc code=end

