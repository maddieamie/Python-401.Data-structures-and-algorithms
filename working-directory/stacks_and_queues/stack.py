from typing import Any

from linked_list_insertions.linked_list_insertions import Node2


class Stack:
    def __init__(self, top=None, size=0):
        self.top = top
        self.max_size = 15
        self.size = size

    def __repr__(self):
        node = self.top
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        nodes.append("Null")
        return " -> ".join(nodes)

    def __iter__(self):
        current_node = self.top
        while current_node is not None:
            yield current_node
            current_node = current_node.next

    def push(self, value: Any) -> None:
        if self.size >= self.max_size:
            raise IndexError(f"Stack is full. Limit of stack size is {self.max_size} nodes.")
        node = Node2(value)

        if self.top is None:
            self.top = node
            node.next = None
            self.size += 1
        else:
            node.next = self.top
            self.top = node
            self.size += 1

    def pop(self) -> Any:
        if self.top is None:
            raise Exception("Stack is empty")

        dead_node = self.top
        self.top = self.top.next
        dead_node.next = None
        self.size -= 1

        return dead_node.data

    def peek(self) -> Any:
        if self.top is None:
            raise Exception("Stack is empty")

        return self.top.data

    def get_size(self) -> tuple[str, str]:
        return 'Size of stack: ' + str(self.size), 'Max size allowed: ' + str(self.max_size)

    def is_empty(self) -> bool:
        if self.top is None:
            return True
        else:
            return False

