from codefellows.dsa.binary_tree import BinarySearchTree

"""
        10
    5       20
       7   12

"""
tree = BinarySearchTree(values=[10, 5, 20, 7, 12])


def depth_first_search(tree):
    # return sum of all values in tree

    def walk(root):
        if root is None:
            return 0

        # my value + left sum + right sum
        return root.value + walk(root.left) + walk(root.right)

    return walk(tree.root)


result = depth_first_search(tree)
print(result)
