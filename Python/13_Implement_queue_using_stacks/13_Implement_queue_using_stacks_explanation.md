# Implement Queue Using Stacks

***What is a Queue?***

A queue is a linear data structure that follows the First-In-First-Out (FIFO) principle. It represents a collection of elements in which the element that is added 
first is the first one to be removed. Think of it as a line of people waiting for a service, where the person who arrives first gets served first.
In a queue, elements are added at one end called the rear or back, and elements are removed from the other end called the front. This makes the queue operate like 
a real-world queue or line.


***What is a Stack?***

A stack is a linear data structure that follows the Last-In-First-Out (LIFO) principle. It represents a collection of elements in which the element that is added 
last is the first one to be removed. Think of it as a stack of books, where the last book placed on top is the first one to be taken off.
In a stack, elements are added and removed from the same end, which is typically referred to as the top of the stack. This means that the most recently added 
element is always at the top, and the least recently added element is at the bottom.


# Code Explaination:

- In this implementation, we use two stacks: stack1 and stack2.
- The push operation is simulated by first transferring all elements from stack1 to stack2, then pushing the new element to stack1, and finally transferring
  all elements back to stack1.
- The pop operation simply pops (or removes) the top element from stack1.
- The peek operation returns the top element of stack1 without removing it.
- The empty operation checks if stack1 is empty.
