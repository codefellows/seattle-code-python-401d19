from codefellows.dsa.binary_tree import BinarySearchTree
from codefellows.dsa.queue import Queue

"""
        10
    5       20
       7   12


breadth first = 10,5,20,7,12
"""
tree = BinarySearchTree(values=[10, 5, 20, 7, 12])


def breadth_first_search(tree):

    if tree.root is None:
        return 0

    node_sum = 0
    breadth = Queue()
    breadth.enqueue(tree.root)
    while len(breadth) > 0:
        front = breadth.dequeue()
        # do something
        node_sum += front.value

        if front.left:
            breadth.enqueue(front.left)
        if front.right:
            breadth.enqueue(front.right)

    return node_sum


result = breadth_first_search(tree)
print(result)
