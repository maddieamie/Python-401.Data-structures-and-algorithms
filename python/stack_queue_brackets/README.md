# Stack + Queue Brackets
<!-- Description of the challenge -->
Write a function called validate brackets
**Arguments**: string
**Return**: boolean
 - representing whether or not the brackets in the string are balanced

_There are 3 types of brackets:_

- Round Brackets : ()
- Square Brackets : []
- Curly Brackets : {}

- _This will use code from [Stack](python/stacks_and_queues/stack.py)_

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

I enumerated the string characters so that the node being pushed to a stack would contain the data and the index of the character. Essentially, the logic is to push to the stack for an opening bracket and then pop for a closing bracket. Then, I used conditional logic to make sure that the index of the closing bracket was not before the opening bracket, the stack is not empty when trying to pop from it upon coming across a closing bracket, and making sure that the brackets match the appropriate bracket type. 


**Time: O(1)**
-  because only deals with one node at a time for all of these methods, since the nodes being accessed are only at the top of the stack.
- However, this method overall may use also 0(n^2), because I am calling on two iterative methods of a dictionary to access the keys and values. 

**Space: O(n)**
- For the space of the character string list and the space of the Stack individually, O(2n) for both of those combined in memory. 

## Solution
<!-- Show how to run your code, and examples of it in action -->

Terminal command for general main module: python3 -m stack_queue_brackets.stack_queue_brackets

Terminal command for testing in pytest: python3 -m pytest stack_queue_brackets/

![Test code in main module: collected 9 items
stack_queue_brackets/stack_queue_brackets.py .....  100%, 9 passed in 0.01s](python/stack_queue_brackets/tests_passing.png)

### Code Links

[Stack Queue Brackets](python/stack_queue_brackets/stack_queue_brackets.py)

[Tests of Stack Queue Brackets](python/stack_queue_brackets/test_stack_queue_brackets.py)