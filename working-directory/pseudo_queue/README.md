# Pseudo Queue with 2 Stacks
<!-- Description of the challenge -->
Create a new class called pseudo queue.
- Do not use an existing Queue.
- Instead, this PseudoQueue class will implement our standard queue interface (the two methods listed below),
- Internally, utilize 2 Stack instances to create and manage the queue

Methods:
**enqueue**
_Arguments: value_
- Inserts a value into the PseudoQueue, using a first-in, first-out approach.
**dequeue**
_Arguments: none_
- Extracts a value from the PseudoQueue, using a first-in, first-out approach.

- _This will use code from [Stack](working-directory/stacks_and_queues/stack.py)_



## Whiteboard Process
<!-- Embedded whiteboard image -->

![Code Challenge 11: figjam image, link below](working-directory/pseudo_queue/Code_Challenge_11_PseudoQueue.png)

[Figjam Link for Code Challenge 11-- to navigate the image embedded above](https://www.figma.com/board/YsUP3rNWVocBgIXKdxUm5J/Code-Challenge-11%3A-PseudoQueue?node-id=0-1&t=zz9qfvBSEYmMJj5V-1)



## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

In my code, I used two stacks within the enqueue method to simulate a queue. I also had the class of PseudoQueue hold a stack called pseudo_queue that I could update for each instance of the PseudoQueue class. 

**Time: O(1)**
-  because only deals with one node at a time for all of these methods, since the nodes being accessed are only on the top, and one at a time.

**Space: O(n)**
- because it will be the amount of space for each of the nodes in each stack is only stored once, and at most 2n if there are elements stored in two stacks during method operations.

## Solution
<!-- Show how to run your code, and examples of it in action -->

Terminal command for general main module: python3 -m pseudo_queue.pseudo_queue

Terminal command for testing in pytest: python3 -m pytest pseudo_queue/

![Test code in main module: collected 6 items
pseudo_queue/test_pseudo_queue.py ...... 100%, 6 passed in 0.01s](working-directory/pseudo_queue/Terminal_test_executions.png)

### Code Links


[PseudoQueue](working-directory/pseudo_queue/pseudo_queue.py)

[Tests of PseudoQueue](working-directory/pseudo_queue/test_psuedo_queue.py)