from linked_list_insertions.linked_list_insertions import LinkedList2, Node2, TargetError


# Define a new method for LinkedList2
def kth_from_end(self, k):
    if isinstance(k, int) is False:
        raise TargetError('k is not an integer')

    if k < 0:
        raise TargetError('k is out of range of linked list')

    current_node = self.head
    k_node = self.head
    length = 1
    k_position = k + 1

    while current_node is not None:
        length += 1
        k_position -= 1
        # print('current', current_node)
        # print('k_node', k_node)
        # print('k', k_position)
        if k_position <= -1:
            k_node = k_node.next

        current_node = current_node.next

    if k > length - 2:
        raise TargetError('k param exceeds the length of the linked list, or is out of range of linked list')

    print(k_node)
    return str(k_node)


# Add the new method to LinkedList2
LinkedList2.kth_from_end = kth_from_end

# Testing the new method
if __name__ == "__main__":
    # Create an instance of LinkedList2
    List3 = LinkedList2()
    List3.insert('E')
    List3.insert('D')
    List3.insert('C')
    List3.insert('B')
    List3.insert('A')

    print(List3.to_string())
    # Call the new method kth_from_end
    List3.kth_from_end(3)  # Output: B
    List3.kth_from_end(0) # Output: E
    List3.kth_from_end(4) # Output: A
    # List3.kth_from_end(5)
    # List3.kth_from_end(6)


