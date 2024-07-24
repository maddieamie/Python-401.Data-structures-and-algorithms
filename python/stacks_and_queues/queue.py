from typing import Any

from linked_list_insertions.linked_list_insertions import Node2, LinkedList2


class Queue(LinkedList2):
    def __init__(self, head: Any = None, back: Any = None):
        self.head = head
        self.front = self.head
        self.back = back
        self.size = 0
        self.max_size = 8

    def __iter__(self):
        current_node = self.front
        while current_node is not None:
            yield current_node
            current_node = current_node.next

    def enqueue(self, value: Any) -> None:
        if self.size >= self.max_size:
            raise IndexError(f"Queue is full. Limit of queue size is {self.max_size} nodes.")

        node = Node2(value)
        if self.head is None:
            self.head = node
            self.front = node
            self.back = node
            node.next = None

        else:
            self.back.next = node
            self.back = node
            node.next = None

        self.size += 1

    def dequeue(self) -> Any:
        if self.head is None:
            raise Exception("Queue is empty")

        dead_node = self.head
        self.head = dead_node.next
        self.front = self.head
        dead_node.next = None
        self.size -= 1

        # return dead_node.data
        return dead_node

    def peek(self) -> Any:
        if self.head is None:
            raise Exception("Queue is empty")

        return self.head.data

    def get_size(self) -> tuple[str, str]:
        return 'Size of queue: ' + str(self.size), 'Max size allowed: ' + str(self.max_size)

    def is_empty(self) -> bool:
        if self.head is None:
            return True
        else:
            return False

    def contains(self, value: Any) -> bool:
        self.includes(value)



