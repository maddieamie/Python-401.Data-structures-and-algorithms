from stacks_and_queues.queue import Queue

# 800 297 6877

# have the queue that holds the official list, then a temp queue
# need both an enqueue and dequeue method
# consider dequeueing the whole object instead

class AnimalShelter(Queue):
    def __init_(self, shelter_queue=Queue(), temp_queue=Queue(), reset_queue=Queue()):
        self.shelter_queue = shelter_queue
        self.temp_queue = temp_queue
        self.reset_queue = reset_queue

    def __repr__(self):
        node = self.shelter_queue.front
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        return " -> ".join(nodes)

    def __iter__(self):
        current_node = self.shelter_queue.front
        while current_node is not None:
            yield current_node
            current_node = current_node.next

    def enqueue(self, animal: tuple[str, str]) -> None:

        node = Animal(animal)
        if self.head is None:
            self.head = node
            self.front = node
            self.back = node
            node.next = None

        else:
            self.back.next = node
            self.back = node
            node.next = None


class Animal:
    def __init__(self, species=str, name=str, _next=None):
        self.species = species
        self.name = name
        self.next = _next

    def __repr__(self):
        return self


class Dog(Animal):
    def __init__(self):
        super().__init__()
        self.species = "dog"
        self.name = ""


class Cat(Animal):
    def __init__(self):
        super().__init__()
        self.species = "cat"
        self.name = ""

