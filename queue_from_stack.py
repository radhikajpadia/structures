'''
1. define class Stack with stack operations push, pop, is_empty
2. define class Queue which has 2 stacks, and queue operations, enqueue and dequeue

Stack is LIFO
Queue is FIFO

Enqueue -> push 1 to stack 1
Enqueue -> push 2 to stack 1
Stack 1 here has 1,2
Dequeue ->
Check if stack 2 is empty, stack 1 is not empty
Pop from stack 1, push to stack 2 (2 gets popped, adds to stack 2)
                                  (1 gets popped, adds to stack 2)
Stack 2 now becomes 2,1
So dequeued element = 1
Hence, FIFO


POP expensive.
'''


class Stack:
    # define stack
    def __init__(self):
        self.items = []

    # define check for empty stack
    def is_empty(self):
        return self.items == []

    # define push operation
    def push(self, data):
        return self.items.append(data)

    # define pop operation
    def pop(self):
        return self.items.pop()


class Queue:
    def __init__(self):
        self.stack_1 = Stack()
        self.stack_2 = Stack()

    # check if both stacks are empty
    def is_empty(self):
        return self.stack_1.is_empty() and self.stack_2.is_empty()

    # push to stack 1
    def enqueue(self, data):
        self.stack_1.push(data)

    # check if stack2 empty, stack 1 has values, push values from stack 1 to stack 2, pop from stack 2
    # In de-queue operation, if stack2 is empty then all the elements are moved to stack2 and finally
    # top of stack2 is returned.
    def dequeue(self):
        if self.stack_2.is_empty():
            while not self.stack_1.is_empty():
                popped = self.stack_1.pop()
                self.stack_2.push(popped)
        return self.stack_2.pop()


queue = Queue()
while True:
    print('enqueue <value>')
    print('dequeue')
    print('quit')
    act = raw_input('What would you like to do? ').split()
    operation = (act[0].split())[0]
    if operation == 'enqueue':
        queue.enqueue(int(act[1]))
    elif operation == 'dequeue':
        if queue.is_empty():
            print('Queue is empty')
        else:
            dequeued_ele = queue.dequeue()
            print('Dequeued element is ', int(dequeued_ele))
    else:
        break

