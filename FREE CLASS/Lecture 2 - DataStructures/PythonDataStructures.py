class Stack:
    MAXSIZE = 100 # setting size of stack

    def __init__(self):
        self.top = -1
        self.items = [0] * self.MAXSIZE # creating an empty stack of size MAXSIZE

    def isfull(self):
        return self.top == self.MAXSIZE - 1

    def isempty(self):
        return self.top == -1

    def push(self, num_push):
        for i in range(num_push):
            if self.isfull():  # checking to see if stack is full
                return "Stack Overflow"
            self.top += 1
            number_push = int(input("Enter element to add to stack: "))
            self.items[self.top] = number_push
        return f"{num_push} elements added to the stack"

    def pop(self, num_pop):
        for i in range(num_pop):
            if self.isempty():
                return "Stack Underflow"
            del self.items[self.top]
            self.top -= 1

    def display_stack(self):
        print("Stack: ")
        head = self.top
        while head >= 0:
            print(f'|  {self.items[head]}  |')
            head -= 1

    @classmethod
    def change_stacksize(cls, size):
        cls.MAXSIZE = size


# Creating a queue data structure
class Queue:
    def __init__(self, capacity):
        self.front = 0
        self.rear = -1
        self.array = [0] * capacity # creating an empty queue of size capacity
        self.max = capacity
        self.size = 0

    def isfull(self):
        return self.rear == self.max - 1

    def is_empty(self):
        return self.size == 0

    def enqueue(self, num_times):
        for i in range(num_times):
            # checking to see if the queue is full
            if self.isfull():
                return "Queue Overflow"
            data = int(input("Enter element to add to queue: "))
            self.rear += 1
            self.array[self.rear] = data
            self.size += 1
        print(self.size)

        # return f"{num_times} elements added to the queue"

    def dequeue(self, num_times):
        for i in range(num_times):
            if self.is_empty():
                return "Empty Queue"

            self.front += 1
            self.size -= 1

    def display_queue(self):
        front = self.front
        size = self.size
        print('Queue: ', end=' ')
        # checking to see if the queue is empty
        while size > 0:
            print(f'| {self.array[front]} | ', end=' ')
            # print(f'| {self.array[self.front]} | ', end=' ')
            # self.front += 1
            # self.size -= 1
            front += 1
            size -= 1

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    """

        This class helps to create a singly-linked list
        :return: A linked list
        """
    def __init__(self):
        self._head = None
        self._tail = None

    def add_nodes(self, num_nodes: int) -> None:
        for i in range(num_nodes):
            value = int(input(f"Enter value for {i + 1} node: "))
            newNode = Node(value)
            if self._head is None:
                self._head = newNode
                self._tail = self._head
            else:
                self._tail.next = newNode
                self._tail = newNode


    def display_list(self) -> str:
        if self._head is None:
            return "Empty list"
        ptr = self._head
        print("Linked list: ", end="")
        while ptr is not None:
            print(ptr.value, end=' ')
            ptr = ptr.next


