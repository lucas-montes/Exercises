# Trees

Generally use recursivity to traverse them.
Ex:
To get the depth we do:

```python
def traverse(node):
    if not node:
        return 0
    return 1 + max(traverse(node.left), traverse(node.right))
```

if there is a node we add 1. For that we check that there is a node, if there isn't we return 0. we perform the same operation for both sides, recursively. Meaning that for each node we repete
the left/right split and we add the results.
