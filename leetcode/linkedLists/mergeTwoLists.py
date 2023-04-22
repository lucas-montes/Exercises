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
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        result = current = ListNode()
        while list1 and list2:

            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            current = current.next

        current.next = list1 or list2

        return result.next


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


run_test(
    create_list_node([1, 1, 2, 3, 4, 4]),
    [create_list_node([1, 2, 4]), create_list_node([1, 3, 4])],
    "mergeTwoLists",
)
run_test(
    create_list_node([]), [create_list_node([]), create_list_node([])], "mergeTwoLists"
)
run_test(
    create_list_node([0]),
    [create_list_node([]), create_list_node([0])],
    "mergeTwoLists",
)
