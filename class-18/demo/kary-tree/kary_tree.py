from codefellows.dsa.queue import Queue


class KaryTree:
    def __init__(self, root=None):
        self.root = root

    def __str__(self):
        values = []

        def converter(node):
            values.append(str(node.value))

        self.breadth_first(action=converter)

        return " ".join(values)

    def clone(self):
        if not self.root:
            return

        q = Queue()
        q.enqueue(self.root)
        clone_root = Node(self.root.value)
        while q:
            exiting = q.dequeue()
            for child in exiting.children:
                q.enqueue(child)
                clone_node = Node(child.value)
                clone_root.children.append(clone_node)

        return KaryTree(root=clone_root)

    def breadth_first(self, action=lambda x: None):
        q = Queue()
        q.enqueue(self.root)

        while q:
            exiting = q.dequeue()
            action(exiting)
            for child in exiting.children:
                q.enqueue(child)

        return self


class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = [] if children is None else children

    def __str__(self):
        return str(self.value)


def double_the_odds(tree):
    clone = tree.clone()
    bfs = Queue()
    bfs.enqueue(clone.root)
    while bfs:
        exiting = bfs.dequeue()
        if exiting.value % 2:
            exiting.value *= 2
        for child in exiting.children:
            bfs.enqueue(child)

    return clone


def double_the_odds_too_fancy(tree):
    def doubler(node):
        node.value = node.value * (node.value % 2 + 1)

    return tree.clone().breadth_first(action=doubler)


if __name__ == '__main__':
    two = Node(2, [Node(5), Node(6), Node(7)])
    three = Node(3, [Node(8), Node(9), Node(10)])
    four = Node(4, [Node(11), Node(12)])
    five = Node(5)
    one = Node(1, [two, three, four])
    ktree = KaryTree(root=one)
    # print(ktree)
    # cloned = ktree.clone()
    # print(cloned)
    # vals = ktree.breadth_first()
    odd_doubled = double_the_odds(ktree)
    print(odd_doubled)
