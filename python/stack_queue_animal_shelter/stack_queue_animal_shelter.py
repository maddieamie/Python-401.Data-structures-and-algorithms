from stacks_and_queues.queue import Queue

from typing import Optional


class Animal:
    def __init__(self, species=str, name=str, _next: Optional['Animal'] = None):
        self.species = species
        self.name = name
        self.next = _next

    def __repr__(self) -> str:
        return f"{self.species}({self.name})"


class AnimalShelter(Queue):
    def __init__(self):
        super().__init__()
        self.shelter_queue = Queue()
        self.temp_queue = Queue()
        print(f"Initialized 1: {self.shelter_queue}, 2: {self.temp_queue}")

    def __repr__(self) -> str:
        node = self.shelter_queue.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        return " -> ".join(nodes)

    def __iter__(self):
        current_node = self.shelter_queue.head
        while current_node is not None:
            yield current_node
            current_node = current_node.next

    def enqueue_12(self, animal: Animal) -> None:
        self.shelter_queue.enqueue(animal)

    def reassign_queues(self):
        # Reassign self.temp to self.temp2
        self.shelter_queue = self.temp_queue
        # Create a new queue for self.temp2
        self.temp_queue = Queue()

    def dequeue_12(self, pref: str) -> Animal | None | str:
        if self.shelter_queue.head is None:
            return "Animal Shelter queue is empty"

        if pref not in ["cat", "dog"]:
            return None

        exit_node = None

        while self.shelter_queue.head:
            if pref == self.shelter_queue.head.data.species and exit_node is None:
                exit_node = self.shelter_queue.dequeue()
                print('exit node')
            if self.shelter_queue.head:
                remaining_node = self.shelter_queue.dequeue()
                print('remaining node')
                self.temp_queue.enqueue(remaining_node.data)

        self.reassign_queues()

        return exit_node.data


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


if __name__ == '__main__':
    q = AnimalShelter()
    cat1 = Cat()
    cat2 = Cat()
    dog1 = Dog()
    dog2 = Dog()
    q.enqueue_12(cat1)
    q.enqueue_12(cat2)
    q.enqueue_12(dog1)
    q.enqueue_12(dog2)
    q.dequeue_12("dog")
    print(q)

