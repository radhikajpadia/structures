'''
Design a Data Structure SpecialStack that supports all the stack operations like push(), pop(), isEmpty(), isFull() and
an additional operation getMin() which should return minimum element from the SpecialStack. All these operations of
SpecialStack must be O(1).

1. Initialize 2 stacks, one original and one auxillary
2. Enqueue, adds element to both initially
3. Enqueue again, add to stack 1, compare if > auxillary stack value, append auxillary stack value, else append
4. min ele is top element of auxillary stack
'''


class Stack:
    '''
    Define stack operations, initialize, is_empty, push, pop
    '''
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, data):
        return self.items.append(data)

    def pop(self):
        return self.items.pop()


class Operations:
    '''
    Initialize 2 stacks
    Enqueue to both stacks if both empty, if not, then append to aux_stack only if enqueue value < top value of aux_stack
    Top most element of aux_stack contains minimum element
    '''
    def __init__(self):
        self.original_stack = Stack()
        self.aux_stack = Stack()

    def is_empty(self):
        return self.original_stack.is_empty() and self.aux_stack.is_empty()

    def enqueue(self, data):
        if self.original_stack.is_empty() and self.aux_stack.is_empty():
            self.original_stack.push(data)
            self.aux_stack.push(data)
        else:
            ele_to_insert = data
            current_min_ele = self.aux_stack.pop()
            self.original_stack.push(ele_to_insert)
            if ele_to_insert < current_min_ele:
                self.aux_stack.push(ele_to_insert)
            else:
                self.aux_stack.push(current_min_ele)

    def get_min_ele(self):
        if self.aux_stack.is_empty():
            print 'Stack is empty!'
            exit()
        min_element = self.aux_stack.pop()
        return min_element


data_structure = Operations()
while True:
    print 'enqueue <value>'
    print 'minimum_element'
    act = raw_input('What do you want to do? ').split()
    operation = (act[0].split())[0]
    if operation == 'enqueue':
        data_structure.enqueue(int(act[1]))
    elif operation == 'minimum_element':
        value = data_structure.get_min_ele()
        if value:
            print 'Minimum element is ', value
            exit()
    else:
        break
