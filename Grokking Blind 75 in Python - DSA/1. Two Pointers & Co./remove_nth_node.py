from linked_list import LinkedList
from print_list import print_list_with_forward_arrow
def remove_nth_from_end(head, n):
    # Calculate the length of the linked list by traversing it
    length = 0
    current = head
    while current:
        length += 1
        current = current.next

    # Calculate the position of the node to be removed
    position = length - n

    # Handle edge case where the head needs to be removed
    if position == 0:
        return head.next

    # Find the node before the target node
    ptr = head
    for _ in range(position - 1):
        ptr = ptr.next

    # Relink the nodes to remove the target node
    ptr.next = ptr.next.next

    return head

if __name__ == "__main__":
    print(remove_nth_from_end([1,2,3,4,5], 2))