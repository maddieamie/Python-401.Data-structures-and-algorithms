class Node:
    def __init__(self, value, _next=None):
        self.value = value
        self.next = _next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        return node.value

    def includes(self, value):
        current_node = self.head

        while current_node is not None:
            if current_node.value == value:
                return True
            current_node = current_node.next
        return False

    def to_string(self):
        current_node = self.head
        string = ""
        while current_node is not None:
            string += f" {current_node.value} ->"
            current_node = current_node.next
        string += ("Null")
        return string


if __name__ == "__main__":
    list0 = LinkedList()
    list0.insert(34)
    list0.insert(35)
    list0.insert(36)
    list0.to_string()
    list0.includes(35)
