'''
define class queue - initialize, is_empty, enqueue, dequeue
define class stack - initialize 2 queues, push and pop

Stack is LIFO
Queue is FIFO

Push enqueues to queue 1, then every element of queue 2 is dequeued and enqueued to queue 1, names of queue 1 and queue 2 are switched
Dequeue pops from queue 2 and returns dequeued value

The method is_empty returns True only if queue2 is empty.

PUSH expensive.
'''


class Queue:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, data):
        return self.items.append(data)

    def dequeue(self):
        return self.items.pop(0)


class Stack:

    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()

    def is_empty(self):
        return self.queue2.is_empty()

    def push(self, data):
        self.queue1.enqueue(data)
        while not self.queue2.is_empty():
            x = self.queue2.dequeue()
            self.queue1.enqueue(x)
        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self):
        return self.queue2.dequeue()


s = Stack()
while True:
    print('push <value>')
    print('pop')
    print('quit')
    act = raw_input('What would you like to do? ').split()
    operation = (act[0].split())[0]
    print operation
    if operation == 'push':
        s.push(int(act[1]))
    elif operation == 'pop':
        if s.is_empty():
            print 'Stack is empty'
            exit()
        else:
            print 'Popped value is ', s.pop()
    else:
        exit()
