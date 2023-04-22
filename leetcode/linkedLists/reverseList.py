import sys

from typing import Optional

sys.tracebacklimit = 0


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        return f"value: {self.val}, next: {self.next.val if self.next else self.next}"


class Solution:
    #Recursive: Time O(n), Memory O(n)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        new_head = head
        if head.next:
            new_head = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        return new_head

    # Iteration: Time O(n) Memory (1)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous, current = None, head
        while current:
            following = current.next
            current.next = previous
            previous = current
            current = following
        return previous

def run_test(expected, test_data, method):
    result = getattr(Solution(), method)(*test_data)
    assert (
        expected == result
    ), f"at test with params {test_data} result is {result} and the expected value: {expected}"
    print(f"{expected} success ✅")

def create_list_node(heads):
    prev_node = first_node = None
    for value in heads:
        c_node = ListNode(val=value)
        if prev_node:
            prev_node.next = c_node
        else:
            first_node = c_node
        prev_node = c_node
    return first_node

#run_test(create_list_node([5,4,3,2,1]), [create_list_node([1,2,3,4,5])], 'reverseList')
run_test(create_list_node([2,1]), [create_list_node([1,2])], 'reverseList')
run_test(None, [create_list_node([])], 'reverseList')

