# Array-Reverse
<!-- Description of the challenge -->

Write a function that takes an array
and reverses it without using built in methods to solve the problem.
Function reverseArray will return an array with the items of the input
array in reverse order.

## Whiteboard Process
<!-- Embedded whiteboard image -->

![Code Challenge 1.png](Code%20Challenge%201.png)

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

I approached this problem by utilizing the index of an array and a loop to count backwards through it. I originally solved this problem using Javascript methods on arrays and then looking up methods that apply in Python, i.e. len, for i in _, and range. The algorithm, when fed to a chatbot, was able to reproduce the code in both Javascript and Python. Since this is a whiteboard only challenge, I also had it generate a suite of tests that would work with my test cases after I drafted them using Pytest. The Big 0 of time and space in this problem is the length of the array, since it needs to loop through it once to solve the problem. 

