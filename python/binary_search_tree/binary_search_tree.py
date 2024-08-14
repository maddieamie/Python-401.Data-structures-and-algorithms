class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.visited = False


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, node):
        self.items.append(node)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Queue is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Queue is empty")

    def size(self):
        return len(self.items)

    def __str__(self):
        return str([node.data for node in self.items])


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, node):
        self.items.append(node)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty")

    def size(self):
        return len(self.items)

    def __str__(self):
        return str([node.data for node in self.items[::-1]])


class BinaryTree(Queue, Stack):

    def __init__(self):
        super().__init__()
        self.search_queue = Queue()
        self.list_stack = Stack()
        self.root = None

    def pre_order(self) -> list:
        if not self.root:
            return []

        return_list = []

        self.list_stack.push(self.root)

        while not self.list_stack.is_empty():
            travel = self.list_stack.pop()
            return_list.append(travel.data)

            if travel.right:
                self.list_stack.push(travel.right)
            if travel.left:
                self.list_stack.push(travel.left)

        return return_list

    def recursive_pre_order(self, node) -> list:

        if not node:
            node = self.root
            # max = node.value


        return_list = []

        return_list.append(node.value)
        # condition
        # do thing if condition

        if node.left:
            return_list.extend(self.recursive_pre_order(node.left))
            # condition
            # do thing if condition
        if node.right:
            return_list.extend(self.recursive_pre_order(node.right))
            # condition
            # do thing if condition

        return return_list



    def in_order(self) -> list:
        if not self.root:
            return []

        return_list = []
        self.list_stack.push(self.root)
        travel = self.root

        while not self.list_stack.is_empty() or travel:
            while travel:
                self.list_stack.push(travel)
                travel = travel.left

            travel = self.list_stack.pop()
            return_list.append(travel.data)
            travel = travel.right

        return return_list

    def post_order(self) -> list:
        if not self.root:
            return []

        return_list = []
        self.list_stack.push(self.root)
        last_node_visited = None

        while not self.list_stack.is_empty():
            travel = self.list_stack.peek()
            if (not travel.left and not travel.right) or \
                    (last_node_visited and (last_node_visited == travel.left or last_node_visited == travel.right)):
                travel = self.list_stack.pop()
                return_list.append(travel.data)
                last_node_visited = travel
            else:
                if travel.right:
                    self.list_stack.push(travel.right)
                if travel.left:
                    self.list_stack.push(travel.left)

        return return_list


class BinarySearchTree(BinaryTree):
    def __init__(self):
        super().__init__()

    def add(self, value) -> None:
        new_node = Node(value)

        if not self.root:
            self.root = new_node
        else:
            traversal = self.root
            while True:
                if value < traversal.data:
                    if traversal.left is None:
                        traversal.left = new_node
                        break
                    traversal = traversal.left
                elif value > traversal.data:
                    if traversal.right is None:
                        traversal.right = new_node
                        break
                    traversal = traversal.right
                else:
                    break

    def contains(self, value) -> bool:
        traversal = self.root
        while traversal:
            if value < traversal.data:
                traversal = traversal.left
            elif value > traversal.data:
                traversal = traversal.right
            else:
                return True
        return False


