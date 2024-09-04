# Binary Tree Max Value
<!-- Description of the challenge -->
Write the following method for the Binary Tree class

**find maximum value**
Arguments: none
Returns: number
Find the maximum value stored in the tree. You can assume that the values stored in the Binary Tree will be numeric.


## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

This time, I did a recursive method, because the trees are not true binary search trees, so we need to visit every value in the tree to find the max value. It turns out that I maybe did not need the additional comparison at the beginning of the function. I also gave find_maximum_value a default argument and then accounted for when it would not have one, just to give the code a bit more versatility. 

**Time: O(n)**
- for inserting and searching. Worst case is that you have to traverse the entire tree.

**Space: O(w)**
- for insertion/search, where width is the largest width of the tree. 

## Solution
<!-- Show how to run your code, and examples of it in action -->

Terminal command for general main module: python3 -m tree_max.tree_max

Terminal command for testing in pytest: python3 -m pytest tree_max/

![Test code in main module: collected 6 items
tree_max/test_tree_max.py .....  100%, 6 passed in 0.01s](python/tree_max/tests_passing.png)

### Code Links

[Custom Binary Tree](python/tree_max/binary_tree.py)

[Find Max Tree Value Code](python/tree_max/tree_max.py)

[Tests of Tree Max](python/tree_max/test_tree_max.py)