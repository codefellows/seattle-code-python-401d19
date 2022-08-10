from codefellows.dsa.queue import Queue


class KaryTree:
    def __init__(self, root=None):
        self.root = root

    def __str__(self):

        if not self.root:
            return "EMPTY"

        values = []
        breadth = Queue()

        breadth.enqueue(self.root)

        while breadth: # aka not is_empty
            front = breadth.dequeue()
            values.append(str(front.value))
            for child in front.children:
                breadth.enqueue(child)

        return " ".join(values)

    def clone(self):
        # return a clone of the tree with new nodes keeping the values
        if not self.root:
            return KaryTree()

        breadth = Queue()
        breadth.enqueue(self.root)
        clone_root = None
        while breadth:
            front = breadth.dequeue()
            clone_front = Node(front.value)
            if not clone_root:
                clone_root = clone_front
            for child in front.children:
                breadth.enqueue(child)
                # create a clone node
                clone_node = Node(child.value)
                clone_front.children.append(clone_node)

        return KaryTree(root=clone_root)


class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = [] if children is None else children

    def __str__(self):
        return str(self.value)


def double_the_odds(source_tree):
    """
    :param source_tree:
    :return: new tree with odd values doubled
    """
    tree = source_tree.clone()

    # breadth first search
    breadth = Queue()
    breadth.enqueue(tree.root)

    while breadth:  # aka not empty, your code should use is_empty method
        front = breadth.dequeue()
        # do something with front
        # double the odd values
        if front.value % 2 == 1:
            front.value *= 2

        # enqueue front's children
        for child in front.children:
            breadth.enqueue(child)

    return tree  # TODO: we want a NEW tree


if __name__ == '__main__':
    two = Node(2, [Node(5), Node(6), Node(7)])
    three = Node(3, [Node(8), Node(9), Node(10)])
    four = Node(4, [Node(11), Node(12)])
    five = Node(5)
    one = Node(1, [two, three, four])
    ktree = KaryTree(root=one)
    print(ktree)

    odd_doubled = double_the_odds(ktree)
    assert odd_doubled.root.value == 2
    assert ktree.root.value == 1
    assert len(odd_doubled.root.children) == 3

    print("TESTS PASSED")
