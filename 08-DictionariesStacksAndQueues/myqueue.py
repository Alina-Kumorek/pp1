#####
# Queue definition
##

queue = []

# add value at the top of the queue
def push(value):
    queue.append(value)
    
# remove the bottom element of the queue
# and return its value    
def pop():
    if not empty():
        return queue.pop(0)
    else:
        return None
    
# return true if the queue is empty
def empty():
    return len(queue) == 0

# display queue
def display():
    for i in range(len(queue)-1,-1,-1):
        print(queue[i])
    print()