class Node:
    def __init__(self, data= None, n=None):
        self.data= data
        self.next = n

class Stack:
    def __init__(self):
        self.head = None

    def push(self, x: int) -> None:
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node

    def pop(self) -> int:
        if self.empty():
            raise IndexError("pop from empty stack")
        data = self.head.data
        self.head = self.head.next
        return data

    def peek(self) -> int:
        if self.empty():
            raise IndexError("peek from empty stack")
        return self.head.data

    def empty(self) -> bool:
        return self.head is None

class MyQueue:
    def __init__(self):
        self.stack = Stack()

    def push(self, x: int) -> None:
        if self.stack.empty():
            self.stack.push(x)
        else:
            s1 = self.stack
            s2 = Stack()
            while not s1.empty():
                el = s1.pop()
                s2.push(el)
            s1.push(x)
            while not s2.empty():
                el = s2.pop()
                s1.push(el)
            self.stack = s1

    def pop(self) -> int:
        return self.stack.pop()

    def peek(self) -> int:
        return self.stack.head.data

    def empty(self) -> bool:
        return self.stack.empty()


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
