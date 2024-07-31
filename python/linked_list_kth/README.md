# Linked List Insertions
<!-- Description of the challenge -->
**Kth from the end**
- argument: a number, `k`, as a parameter, which denotes how far the node is from the tail of the linked list.
- Return the **node’s value** that is `k` places from the tail of the linked list.
- You have access to the Node class and all the properties on the Linked List class as well as the methods created in previous challenges.
- This will use code from [Linked List Insertions](python/linked_list_insertions/linked_list_insertions.py)



## Whiteboard Process
<!-- Embedded whiteboard image -->

![Code Challenge 7: figjam image, link below](CodeChallenge7.png)

[Figjam Link for Code Challenge 7-- to navigate the image embedded above](https://www.figma.com/board/ezgXSaZoF7Q7zVVj7k77aa/Code-Challenge-7?node-id=0%3A1&t=z4csSQos6fpyNcmL-1)



## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

For all methods, the time big O for these is the length of the linked list that you must traverse to find the target node, or the last node of the list, so : O(n), where n is the length of the linked list. The space is still O(1), since all the nodes still exist in memory, but that memory is dynamic, so it need not take up a larger chunk of memory at once. 

## Solution
<!-- Show how to run your code, and examples of it in action -->

When testing, I hit some bugs on my condition for the inner loop. Originally, I had the code move the k_node move once k hit 0, but that means that it ran at 0, not the loop after. So to counteract, I changed it to when the value of k is at -1, so it will run the loop after 0, which is when I actually wanted it to start moving. Based on my looping logic, both my length variable and my k variable had to + 1 before the loop started, so that its first run of the loop would have the correct starting value. That is, the length variable  had to start at 1 instead of 0, and the k variable had to start at k+1 instead of just k. 

That being said, when it came to raising my custom error, for the comparison, I needed k to be greater than length -2, to account for the additions I made on both values before the loop. 

Terminal command: python3 -m linked_list_kth.linked_list_kth

![Test code in main module: you can find this in the linked_list_insertions.py file](..%2F..%2F..%2F..%2FDesktop%2FScreenshot%202024-05-09%20at%203.50.01%E2%80%AFPM.png)

![Terminal of code running in main: it returned  A -> B -> C -> D -> E -> Null
B
E
A](..%2F..%2F..%2F..%2F..%2F..%2Fvar%2Ffolders%2F43%2F54rn3fvx4l9_2f87gblfbccc0000gn%2FT%2FTemporaryItems%2FNSIRD_screencaptureui_abb0oY%2FScreenshot%202024-05-09%20at%203.49.14%E2%80%AFPM.png)


Terminal command : python3 -m pytest linked_list_kth/


![Terminal of tests passing: collected 9 items, 9 passed in pytest](..%2F..%2F..%2F..%2F..%2F..%2Fvar%2Ffolders%2F43%2F54rn3fvx4l9_2f87gblfbccc0000gn%2FT%2FTemporaryItems%2FNSIRD_screencaptureui_ltJH7I%2FScreenshot%202024-05-09%20at%203.40.59%E2%80%AFPM.png)

### Code Links


[Kth](python/linked_list_kth/linked_list_kth.py)