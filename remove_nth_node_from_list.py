# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current_node = head

        length = 0
        # find length
        while True:
            if current_node is None:
                break
            length += 1
            current_node = current_node.next

        if length == n:
            return head.next

        n = length - n

        node_to_remove = head
        previous_node = None

        while n > 0:
            previous_node = node_to_remove
            node_to_remove = node_to_remove.next
            n -= 1
        
        previous_node.next = node_to_remove.next
        return head


# --- Helper functions for testing ---

def list_to_linkedlist(arr):
    dummy = ListNode(0)
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def linkedlist_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


# --- Testing ---
s = Solution()

head = list_to_linkedlist([1,2,3,4,5])
res = s.removeNthFromEnd(head, 2)
print(linkedlist_to_list(res))