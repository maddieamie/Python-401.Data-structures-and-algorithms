# Linked List Implementation
<!-- Description of the challenge -->
1. Create a Linked List class
2. Within your Linked List class, include a head property.
- Upon instantiation, an empty Linked List should be created.
-The class should contain the following methods
2a. insert
- Arguments: value
- Returns: nothing
- Adds a new node with that value to the head of the list with an O(1) Time performance.
2b. includes
- Arguments: value
- Returns: Boolean
- Indicates whether that value exists as a Node’s value somewhere within the list.
2c. to string
- Arguments: none
- Returns: a string representing all the values in the Linked List, formatted as:
- "{ a } -> { b } -> { c } -> NULL"

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

For this challenge, I took the approach of drafting out pseudocode to meet the requirements for the challenge.
Then, I wrote tests to try to make instances of these codes and ran them. When they failed, I made adjustments to my pseudocode until it became more actionable. I built out the Node class first, and then the LinkedList class, followed by each method in the LinkedList class. 

### Big O 
.includes method = O(n) of time -- it is the length of the linked list
.insert method = 0(1) in time & space -- for space, because no additional space other than input is being used. for time, because it is only being inserted at the beginning of the linked list. 

## Solution
<!-- Show how to run your code, and examples of it in action -->

[Code Solution](linked.py)

[Code Tests with Pytest](test_linked.py)

![Pytests running](runningtests.png)
