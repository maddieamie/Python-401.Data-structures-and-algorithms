# don't forget to add in docstrings

class Node2:
    def __init__(self, data, _next=None):
        self.data = data
        self.next = _next

    def __repr__(self):
        return self.data


class LinkedList2:
    def __init__(self, head=None):
        self.head = head

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("Null")
        return " -> ".join(nodes)

    def __iter__(self):
        current_node = self.head
        while current_node is not None:
            yield current_node
            current_node = current_node.next

    def insert(self, value):
        node = Node2(value)
        node.next = self.head
        self.head = node

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
            string += f" {current_node} ->"
            current_node = current_node.next
        string += " Null"
        return string

    def append(self, value):
        node = Node2(value)
        current_node = self.head

        if current_node is None:
            self.head = node
            return

        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = node
        node.next = None

    def insert_before(self, existing_node, new_value):
        new_node = Node2(new_value)
        current_node = self.head

        if current_node is None:
            raise TargetError("Linked list is empty")

        if current_node.data == existing_node:
            self.insert(new_value)
            return

        while current_node.next is not None:
            if current_node.next.data == existing_node:
                new_node.next = current_node.next
                current_node.next = new_node
                return
            current_node = current_node.next

        raise TargetError('Target is not in the list')

    def insert_after(self, target_node, new):
        new_node = Node2(new)
        current_node = self.head

        if current_node is None:
            raise TargetError('Linked list is empty')

        while current_node is not None:
            if current_node.data == target_node:
                new_node.next = current_node.next
                current_node.next = new_node
                return
            current_node = current_node.next

        raise TargetError("Target is not in the list")

    def remove(self, target_node):
        previous_node = self.head

        if previous_node is None:
            raise TargetError("Linked list is empty")

        while previous_node:
            if previous_node.next.data == target_node:
                previous_node.next = target_node.next
                return
            previous_node = previous_node.next

        raise TargetError("Target is not in the list")


class TargetError(Exception):
    def __init__(self, message):
        self.message = message

        super().__init__(message)

    def __str__(self):
        return self.message


if __name__ == '__main__':
    new_list = LinkedList2()
    new_list.insert('huzzah')
    new_list.insert_after('huzzah', 'whee')
    new_list.insert_before('whee', 'ziggity')
    new_list.append('jippers')
    print(new_list.to_string())
    print(new_list)
