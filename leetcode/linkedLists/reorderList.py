from re import template
import sys

from typing import Optional

sys.tracebacklimit = 0


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"(value: {self.val}, next: {self.next.val if self.next else self.next})"


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        We'll use two pointers that go to the same direction
        one will go faster than the second one.
        We'll also "slice" the list in half so we know which are the
        nodes that should be moved at the beginning at which not.
        We iterate only twice.
        """
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        
        curr = slow.next
        prev = slow.next = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        first, second = head, prev

        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2


def run_test(expected, test_data, method, linked_list: bool = False):
    result = getattr(Solution(), method)(*test_data)
    if linked_list and result and expected:
        comparaison = expected.__dict__ == result.__dict__
    else:
        comparaison = expected == result
    assert (
        comparaison
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


run_test(
    create_list_node([1, 4, 2, 3]),
    [create_list_node([1, 2, 3, 4])],
    "reorderList",
    True,
)
