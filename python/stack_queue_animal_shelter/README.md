# Stack + Queue Animal Shelter
<!-- Description of the challenge -->
Create a class called AnimalShelter which holds only dogs and cats.
The shelter operates using a first-in, first-out approach.

Implement the following methods:

**enqueue_12**
_Arguments_: animal
- animal can be either a dog or a cat object.
- It must have a species property that is either "cat" or "dog"
- It must have a name property that is a string.

**dequeue_12**
_Arguments_: pref
- pref can be either "dog" or "cat"
- Return: either a dog or a cat, based on preference.
- If pref is not "dog" or "cat" then return null.

- _This will use code from [Queue](python/stacks_and_queues/queue.py)_



## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

In my code, I created Animal Shelter as a subclass of the class Queue, imported from another module. I used both the inherited methods of enqueue/dequeue from that base class, and new iterations of them as enqueue_12 & dequeue_12. Because I chose to utilize the methods of the base class, it made sense to rename the enqueue & dequeue methods of this challenge. 

The dequeue_12 method utilizes Queue.dequeue() and Queue.enqueue() within it, because that covers a lot of the base logic of a generic queue. My logic in dequeue_12 was simply moving the nodes in the shelter_queue to a temp_queue, then reassigning the queues at the end so that the shelter_queue was temp_queue, and then temp_queue is reassigned back to a generic Queue() in that instance of the subclass. 

Initially in my draft logic, I kind of merged the original base class and the subclass into one thing. By using the base class methods separately in the new subclass AnimalShelter, I was able to them focus on the logic required to solve the challenge. It only took moving a whole node out but then returning its data. 

**Time: O(1)**
-  because only deals with one node at a time for all of these methods, since the nodes being accessed are only at the front of the queue.

**Space: O(n)**
- with the caveat that the class for Animal Shelter contains two Queue base classes, so in storage it takes 2n.

## Solution
<!-- Show how to run your code, and examples of it in action -->

Terminal command for general main module: python3 -m stack_queue_animal_shelter.stack_queue_animal_shelter

Terminal command for testing in pytest: python3 -m pytest stack_queue_animal_shelter/

![Test code in main module: collected 5 items
stack_queue_animal_shelter/test_stack_queue_animal_shelter.py .....  100%, 5 passed in 0.01s](python/stack_queue_animal_shelter/tests_passing.png)

### Code Links


[Animal Shelter Queue](python/stack_queue_animal_shelter/stack_queue_animal_shelter.py)

[Tests of Animal Shelter Queue](python/stack_queue_animal_shelter/test_stack_queue_animal_shelter.py)