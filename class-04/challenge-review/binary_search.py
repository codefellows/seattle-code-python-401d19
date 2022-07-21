def binary_search(nums, key, left=0, right=None):
    if right is None:
        right = len(nums) - 1

    # Base case:
    # if left passes right then we didn't find key
    # return -1
    if left > right:
        return -1

    # find mid_index halfway between left and right
    mid_index = (right - left) // 2 + left

    # find mid_value
    mid_value = nums[mid_index]

    if key < mid_value:
        # if key is smaller search left
        return binary_search(nums, key, left, mid_index - 1)
    elif key > mid_value:
        # if key is larger search right
        return binary_search(nums, key, mid_index + 1, right)
    else:
        # found it, return index
        return mid_index


def binary_search_iterative(nums, key):

    # start with left index at 0
    left = 0

    # start with right index at last index in list
    right = len(nums) - 1

    # repeat until left passes right
    while left <= right:

        # find index between left and right
        mid_index = (right - left) // 2 + left

        # find value at middle index
        mid_value = nums[mid_index]

        if key < mid_value:
            # if key is smaller update right to just left of middle index
            right = mid_index - 1
        elif key > mid_value:
            # if key is larger update left to just right of middle index
            left = mid_index + 1
        else:
            # if key not smaller or larger we must have found it
            # return middle index
            return mid_index

    return -1


# TESTS

# Key = 15
#                   L4R4
#   [11, 12, 13, 14, 15, 16, 17, 18]
#                    M4

num_list = [11, 12, 13, 14, 15, 16, 17, 18]
assert binary_search(num_list, 10) == -1
assert binary_search(num_list, 16) == 5
assert binary_search([1], 1) == 0
assert binary_search([1], 2) == -1

print("TESTS PASSED")
