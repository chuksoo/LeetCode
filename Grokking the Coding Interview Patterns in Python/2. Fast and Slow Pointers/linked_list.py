from linked_list_node import LinkedListNode


# Template for the linked list
class LinkedList:
    def __init__(self, values=None):
        self.head = None
        if values:
            self.create_linked_list(values)

    def create_linked_list(self, values):
        if not values:
            self.head = None
            return

        self.head = LinkedListNode(values[0])
        current = self.head
        for value in values[1:]:
            current.next = LinkedListNode(value)
            current = current.next
            
    # returns the number of nodes in the linked list
    def get_length(self, head):
        temp = head
        length = 0
        while(temp):
            length+=1
            temp = temp.next
        return length

    # returns the node at the specified position(index) of the linked list
    def get_node(self, head, pos):
        if pos != -1:
            p = 0
            ptr = head
            while p < pos:
                ptr = ptr.next
                p += 1
            return ptr

    
def display(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")