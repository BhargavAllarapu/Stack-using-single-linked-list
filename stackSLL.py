class Node:
    def __init__(self, data):
        self.data = data
        self.nextval = None

class Stack:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False

    def push(self, data):
        if self.isEmpty():
            newNode = Node(data)
            self.head = newNode
        else:
            newNode = Node(data)
            lastNode = self.head
            self.head = newNode
            newNode.nextval = lastNode
        return None

    def top(self):
        if self.isEmpty():
            return "Stack is Empty"
        else:
            return self.head.data

    def pop(self):
        if self.isEmpty():
            return "Stack is empty... Nothing to pop."
        else:
            temp = self.head
            self.head = temp.nextval
            del temp
            return"Popped"

    def printStack(self):
        nodeA = self.head
        while nodeA is not None:
            print(nodeA.data)
            nodeA = nodeA.nextval
        return None

if __name__ == '__main__':
    st = Stack()
    print("Is Stack Empty : "+str(st.isEmpty()))
    print("pop : "+str(st.pop()))
    a = input("Push : ")
    st.push(a)
    b = input("Push : ")
    st.push(b)
    c = input("Push : ")
    st.push(c)
    d = input("Push : ")
    st.push(d)
    print("Is Stack Empty : "+str(st.isEmpty()))
    st.printStack()
    print("Top : "+str(st.top()))
    print("Pop : "+str(st.pop()))
    st.printStack()