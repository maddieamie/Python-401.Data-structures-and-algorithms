# Linked List Insertions
<!-- Description of the challenge -->
**Write a function called `zip_lists`**
- Arguments: 2 linked lists
- Return: New Linked List, zipped as noted below
- Zip the two linked lists together into one so that the nodes alternate between the two lists and return a reference to the zipped list.
- Try and keep additional space down to O(1)
- This will use code from [Linked List Insertions](working-directory/linked_list_insertions/linked_list_insertions.py)



## Whiteboard Process
<!-- Embedded whiteboard image -->

![Code Challenge 8: figjam image, link below](Code%20Challenge%208.png)

[Figjam Link for Code Challenge 8-- to navigate the image embedded above](https://www.figma.com/board/RuhisIY5qCMABhHFUoOD07/Code-Challenge-8?node-id=0%3A1&t=FZKCqSPnCWX1Bq80-1)



## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

In my code, I used one `while` loop and then an `if` conditional for each of the linked lists, then had each `if` conditional move across the nodes of both lists. Since my code wanted me to use the first list argument first in the zipping process, I put that one first in the while loop and list2 second. I suppose you could add more conditions. 

**Time: O(n+m)**
- because you need to traverse both of the linked lists, even though I have it in a nested while loop

**Space: O(n+m)**
- this accounts for the space needed to store the nodes of the new linked list, which will have a number of nodes equal to the sum of the nodes in the two input lists

## Solution
<!-- Show how to run your code, and examples of it in action -->

Terminal command: python3 -m linked_list_zip.linked_list_zip

![Test code in main module: returns list3:  A -> B -> C -> Null
A -> B -> C -> Null
list4:  1 -> 2 -> 3 -> Null
1 -> 2 -> 3 -> Null
zip_lists: A -> 1 -> B -> 2 -> C -> 3 -> Null](working-directory/linked_list_zip/Working_in_if_name_equals_main.png)


Terminal command : python3 -m pytest linked_list_zip/

![Terminal of tests passing: collected 6 items, 6 passed in pytest](working-directory/linked_list_zip/Passing_in_terminal.png)