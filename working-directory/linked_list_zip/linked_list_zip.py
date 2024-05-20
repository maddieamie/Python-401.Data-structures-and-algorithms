from linked_list_insertions.linked_list_insertions import LinkedList2, Node2, TargetError


# Define a new method for LinkedList2
def zip_lists(list1, list2):
    output_list = LinkedList2()
    linked1_node = list1.self.head
    linked2_node = list2.self.head

    while linked1_node is not None or linked2_node is not None:
        if linked1_node is not None:
            output_list.append(linked1_node.data)
        if linked2_node is not None:
            output_list.append(linked2_node.data)
        linked1_node = linked1_node.next
        linked2_node = linked2_node.next

    print(output_list)

    return output_list


# Add the new method to LinkedList2
LinkedList2.zip_lists = zip_lists

# Testing the new method
if __name__ == "__main__":
    # Create an instance of LinkedList2
    List3 = LinkedList2()
    List3.insert('C')
    List3.insert('B')
    List3.insert('A')

    List4 = LinkedList2()
    List4.insert('1')
    List4.insert('2')
    List4.insert('3')

    print('list3:', List3.to_string())
    print('list4:', List4.to_string())
    # Call the new method kth_from_end
    zip_lists(List3, List4)

