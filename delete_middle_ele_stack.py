'''
Find middle element of stack and delete it
'''


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, data):
        return self.items.append(data)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


def delete_mid(st, n, curr_ele):

    if st.is_empty() or curr_ele == n:
        return

    # Remove first element
    x = st.peek()
    st.pop()

    # Remove other items
    delete_mid(st, n, curr_ele+1)

    # Put all elements back except middle
    if curr_ele != int(n/2):
        st.push(x)


st = Stack()
st.push('1')
st.push('2')
st.push('3')
st.push('4')
st.push('5')
st.push('6')
st.push('7')

delete_mid(st, st.size(), 0)
# Printing stack after deletion
# of middle.
while st.is_empty() == False:
    p = st.peek()
    st.pop()
    print (str(p) + " ")