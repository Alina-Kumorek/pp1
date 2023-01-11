# Following the example of stack.py, create a queue.py module in which define queue handling.
# Then write a program that imports the queue.py module. Add and remove values from the queue. Display its content.

# I named the module myqueue.py, becouse queue.py was conflicting with things.

import myqueue

myqueue.push(2)
myqueue.push(4)
myqueue.push(6)

myqueue.display()

myqueue.pop()

myqueue.display()