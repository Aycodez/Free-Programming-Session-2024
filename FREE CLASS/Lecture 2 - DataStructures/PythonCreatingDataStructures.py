from PythonDataStructures import *

# Let's create a stack
stack = Stack()
stack.push(5)  # Pushing 5 elements into the stack
print('After pushing elements into the stack:')
stack.display_stack()

stack.pop(2)  # popping 2 elements from the stack
print('After popping elements from the stack:')
stack.display_stack()

# Let's create a queue
q = Queue(10)
q.enqueue(5)  # Adding 5 elements into the stack
print('After enqueue:')
q.display_queue()

q.dequeue(2)  # removing 2 elements from the stack
print('\nAfter dequeue: ')
q.display_queue()

# Creating a linked list
l = LinkedList()
l.add_nodes(3)  # creating 3 nodes
l.display_list()
