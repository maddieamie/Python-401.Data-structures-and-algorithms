# Binary Search 
<!-- Description of the challenge -->

Write a function called BinarySearch which takes in 2 parameters: a sorted array and the search key. Without utilizing any of the built-in methods available to your language, return the index of the array’s element that is equal to the value of the search key, or -1 if the element is not in the array.

## Whiteboard Process
<!-- Embedded whiteboard image -->

![Code Challenge 3.png](Code%20Challenge%203.png)


## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

The big O for space is the length of the array.
The big 0 for time is the log n, where n is the length of the array. 

## Solution
A binary search goes through the indexes of a sorted array, assigning the left, right, and middle of the indexes. If the middle is more or less than the search key you are looking for in the sorted array, the half where the search key must not lie is eliminated until it becomes the center of the array. When the search key is in the center, its index is returned. If it is not in the array, it returns a negative 1. 
