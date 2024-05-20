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

![Code Challenge 7: figjam image, link below](CodeChallenge7.png)

[Figjam Link for Code Challenge 7-- to navigate the image embedded above](https://www.figma.com/board/ezgXSaZoF7Q7zVVj7k77aa/Code-Challenge-7?node-id=0%3A1&t=z4csSQos6fpyNcmL-1)



## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

For all methods, the time big O for these is the length of the linked list that you must traverse to find the target node, or the last node of the list, so : O(n), where n is the length of the linked list. The space is still O(1), since all the nodes still exist in memory, but that memory is dynamic, so it need not take up a larger chunk of memory at once. 

## Solution
<!-- Show how to run your code, and examples of it in action -->

Terminal command: python3 -m linked_list_kth.linked_list_kth

![Test code in main module: you can find this in the linked_list_insertions.py file](..%2F..%2F..%2F..%2FDesktop%2FScreenshot%202024-05-09%20at%203.50.01%E2%80%AFPM.png)

![Terminal of code running in main: it returned  A -> B -> C -> D -> E -> Null
B
E
A](..%2F..%2F..%2F..%2F..%2F..%2Fvar%2Ffolders%2F43%2F54rn3fvx4l9_2f87gblfbccc0000gn%2FT%2FTemporaryItems%2FNSIRD_screencaptureui_abb0oY%2FScreenshot%202024-05-09%20at%203.49.14%E2%80%AFPM.png)


Terminal command : python3 -m pytest linked_list_kth/


![Terminal of tests passing: collected 9 items, 9 passed in pytest](..%2F..%2F..%2F..%2F..%2F..%2Fvar%2Ffolders%2F43%2F54rn3fvx4l9_2f87gblfbccc0000gn%2FT%2FTemporaryItems%2FNSIRD_screencaptureui_ltJH7I%2FScreenshot%202024-05-09%20at%203.40.59%E2%80%AFPM.png)