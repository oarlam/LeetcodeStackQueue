class Node:
    def __init__(self, data= None, n=None):
        self.data= data
        self.next = None

class MyQueue:
    def __init__(self):
        self.head = None

    def push(self, x: int) -> None:
        if self.head is None:
            self.head = Node(x)
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = Node(x)

    def pop(self) -> int:
        data = self.head.data
        self.head = self.head.next
        return data

    def peek(self) -> int:
        return self.head.data

    def empty(self) -> bool:
        if self.head is None:
            return True
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
