from codefellows.dsa.linked_list import LinkedList


def reverse_linked_list(linked):

    previous = None
    current = linked.head

    while current:
        upcoming = current.next
        current.next = previous
        previous = current
        current = upcoming

    linked.head = previous
    return linked




letters = LinkedList(values="abcdefghij")
reversed_letters = reverse_linked_list(letters)
print(reversed_letters)

"""
{ a } -> { b } -> { c } -> { d } -> { e } -> { f } -> { g } -> { h } -> { i } -> { k } -> { j } -> NULL
"""
