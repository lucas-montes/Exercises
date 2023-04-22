import sys

from typing import List

sys.tracebacklimit = 0


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        We'll use two pointer (left, right). left will start at the node O, meaning that
        we'll create a previous node to head.
        First we move the right pointer n positions ahead of left.
        Then we move both pointers until right is at the end so left will be at the N-1th node.
        Then we just remove the next node where left is.
        """
        node = ListNode(0, head) # He is the node 0.
        left = node
        right = head
        # we move right n positions ahead of left
        while n>0 and right:
            right = right.next
            n -=1

        # we move the pointer until right is at the end
        while right:
            right = right.next
            left = left.next
        
        # we point the n-1th node no the n+1th node.
        # so the Nth node is gone.
        left.next = left.next.next
        return node.next


def run_test(expected, test_data, method):
    result = getattr(Solution(), method)(*test_data)
    assert (
        expected == result
    ), f"at test with params {test_data} result is {result} and the expected value: {expected}"
    print(f"{expected} success ✅")


#run_test(RESULT, [ARGS], 'removeNthFromEnd')
#run_test(RESULT, [ARGS], 'removeNthFromEnd')
#run_test(RESULT, [ARGS], 'removeNthFromEnd')

