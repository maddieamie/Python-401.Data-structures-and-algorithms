# Linked List Insertions
<!-- Description of the challenge -->
**append**
- arguments: new value
- adds a new node with the given value to the end of the list

**insert before**
- arguments: value, new value
- adds a new node with the given new value immediately before the first node that has the value specified

**insert after**
- arguments: value, new value
- adds a new node with the given new value immediately after the first node that has the value specified

**TargetError Class**
- if there is no node to insert before or after, raise an error that says there is no targeted node listed, or the node is missing
- if there is a node in the list, but not the node being named in the arguments, raise this error to indicate that the node given in arguments is not in the linked list or is a missing node
- if the list is empty, raise this error

## Whiteboard Process
<!-- Embedded whiteboard image -->

![Code Challenge 6: Figjam image, link below](Code%20Challenge%206.png)

[Figjam Link-- to navigate the image embedded above](https://www.figma.com/file/HRVBXiY07qfbTonAutIcmx/Code-Challenge-6?type=whiteboard&node-id=0%3A1&t=4vkf77BXUxQrbTqL-1)



## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

For all methods, the time big O for these is the length of the linked list that you must traverse to find the target node, or the last node of the list, so : O(n), where n is the length of the linked list. The space is still O(n), since all the nodes still exist in memory, but that memory is dynamic, so it need not take up a larger chunk of memory at once. 

## Solution
<!-- Show how to run your code, and examples of it in action -->
Terminal command: python3 linked_list_insertions.py

Terminal command: python3 -m pytest linked_list_insertions/



### Code Links


[Insertions](python/linked_list_insertions/linked_list_insertions.py)

