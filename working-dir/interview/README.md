# Interview 1
<!-- Description of the challenge -->

Ask the candidate to write a function to add up the sum of each row in a matrix of arbitrary size, and return an array with the appropriate values. The matrix will always be full of integers.
Negative values are possible.
All nulls will be counted as zeros.

## Whiteboard Process
<!-- Embedded whiteboard image -->

![Code Challenge 4.png](Code%20Challenge%204.png)


## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

The big O for space is the length of the array.
The big 0 for time is the n^2, where n is the length of the array times the length of each array inside the array of arrays. 

## Solution
Input is an array of arrays (a matrix). Create a new array for the output of the sum of each inner array. Then, loop through the outer array and then use sum to add up all the values of each inner array. 
