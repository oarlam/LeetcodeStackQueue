class Node:
    def __init__(self, data= None, n=None):
        self.data= data
        self.next = n
        self.tail = None

class Queue:
    """Queue"""
    def __init__(self):
        self.head = None
        self.tail = None

    def empty(self):
        '''empty'''
        return self.head is None

    def add(self, x):
        """add to end"""
        if self.head is None:
            self.head = Node(x)
            self.tail = self.head
        else:
            self.tail.next = Node(x)
            self.tail = self.tail.next

    def pop(self) -> int:
        if self.empty():
            raise IndexError("pop from empty queque")
        data = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return data

    def peek(self):
        if self.empty():
            raise IndexError
        return self.head.data


class MyStack:

    def __init__(self):
        self.que = Queue()

    def push(self, x: int) -> None:
        if self.que.empty():
            self.que.add(x)
        else:
            s1 = self.que
            s2 = Queue()
            while not s1.empty():
                el = s1.pop()
                s2.add(el)
            s1.add(x)
            while not s2.empty():
                el = s2.pop()
                s1.add(el)
            self.que = s1

    def pop(self) -> int:
        return self.que.pop()

    def top(self) -> int:
        return self.que.peek()

    def empty(self) -> bool:
        return self.que.empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
