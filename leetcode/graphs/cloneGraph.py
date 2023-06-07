import copy
import sys
from typing import List

sys.tracebacklimit = 0


class Solution:
    # def cloneGraph(self, node: "Node") -> "Node":
    #    return copy.deepcopy(node)
    def cloneGraph(self, node: "Node") -> "Node":
        seen = {}

        def dfs(node):
            if node in seen:
                return seen[node]
            new_n = Node(node.val)
            seen[node] = new_n
            for n in node.neighbors:
                new_n.neighbors.append(dfs(n))
            return new_n

        return dfs(node) if node else None


def run_test(expected, test_data, method):
    result = getattr(Solution(), method)(*test_data)
    assert (
        expected == result
    ), f"at test with params {test_data} result is {result} and the expected value: {expected}"
    print(f"{expected} success ✅")


run_test(RESULT, [ARGS], "cloneGraph")
run_test(RESULT, [ARGS], "cloneGraph")
# run_test(RESULT, [ARGS], 'cloneGraph')
