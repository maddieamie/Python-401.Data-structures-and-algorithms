# Binary Search Tree
<!-- Description of the challenge -->
**Node**

Create a Node class that has properties for the value stored in the node, the left child node, and the right child node.

**Create a Binary Tree class**
Define a method for each of the depth first traversals:
1. pre order
2. in order
3. post order
Each depth first traversal method should return an array of values, ordered appropriately.

**Binary Search Tree**

This class should be a sub-class (or your languages equivalent) of the Binary Tree Class, with the following additional _methods:_

**Add**
Arguments: value
Return: nothing
- Adds a new node with that value in the correct location in the binary search tree.

**Contains**
Argument: value
Returns: boolean indicating whether or not the value is in the tree at least once.

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

I attempted to do these methods with a different iterative method instead of just plain recursion, but I don't know if that's better or not. 

**Time: O(n)**
- for inserting and searching. Worst case is that you have to traverse the entire tree.

**Space: O(w)**
- for insertion/search, where width is the largest width of the tree. 

## Solution
<!-- Show how to run your code, and examples of it in action -->

Terminal command for general main module: python3 -m binary_search_tree.binary_search_tree

Terminal command for testing in pytest: python3 -m pytest binary_search_tree/

![Test code in main module: collected 9 items
binary_search_tree/test_binary_search_tree.py .....  100%, 9 passed in 0.01s](python/binary_search_tree/tests_passing.png)

### Code Links

[Binary Search Tree](python/binary_search_tree/binary_search_tree.py)

[Tests of Binary Search Tree](python/binary_search_tree/test_binary_search_tree.py)