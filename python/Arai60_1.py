# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                return True
        return False


# セットを使った解法。メモリ使用量が多い。
# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         seen = set()
#         cur = head

#         while cur:
#             if cur in seen:
#                 return True
#             seen.add(cur)
#             cur = cur.next
#         return False
