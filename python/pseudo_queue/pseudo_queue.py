from stacks_and_queues.stack import Stack
from linked_list_insertions.linked_list_insertions import Node2


class PseudoQueue(Stack):
    def __init__(self, stack_1=Stack(), stack_2=Stack(), boat=None, pseudo_queue=Stack()):
        self.stack_1 = stack_1
        self.stack_2 = stack_2
        self.pseudo_queue = pseudo_queue
        self.boat = boat

    def __repr__(self):
        node = self.stack_1.top
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        return " -> ".join(nodes)

    def __iter__(self):
        current_node = self.stack_1.top
        while current_node is not None:
            yield current_node
            current_node = current_node.next

    def enqueue(self, value):
        self.boat = Node2(value)

        while self.pseudo_queue.top:
            temp = self.pseudo_queue.pop()
            self.stack_1.push(temp)
        self.stack_1.push(self.boat)

        print('stack 1:', self.stack_1)

        while self.stack_1.top:
            temp = self.stack_1.pop()
            self.stack_2.push(temp)

        print('stack 2:', self.stack_2)

        new = self.stack_2
        print('new stack:', new)
        self.pseudo_queue = new
        print('pseudo_queue after assigning it new:', self.pseudo_queue)
        self.stack_2 = Stack()
        self.stack_1 = Stack()
        print('stacks after assigning it blank:', self.stack_2, self.stack_1)

    def dequeue(self):
        return str(self.pseudo_queue.pop())


if __name__ == '__main__':
    q = PseudoQueue()
    q.enqueue("1")
    q.enqueue("2")
    q.enqueue("3")
    q.dequeue()
    print(q.__repr__())