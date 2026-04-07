class Node:
    def __init__(self, data=None, n=None, count=1):
        self.data = data
        self.next = n
        self.count = count

class Stack:
    def __init__(self):
        self.head = None

    def push(self, x: int, count=1) -> None:
        new_node = Node(x, count=count)
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


class FreqStack:
    def __init__(self):
        self.stack = Stack()
        self.amount = {}
        self.max_amount = 0

    def push(self, val: int) -> None:
        count = self.amount.get(val, 0) + 1
        self.amount[val] = count
        self.max_amount = max(self.max_amount, count)
        self.stack.push(val, count)

    def pop(self) -> int:
        dummy = Node(0, count=0, n=self.stack.head)
        cur = dummy

        while cur.next:
            if cur.next.count == self.max_amount:
                val = cur.next.data
                cur.next = cur.next.next
                self.stack.head = dummy.next
                self.amount[val] -= 1
                self.max_amount = max(self.amount.values())
                return val

            cur = cur.next
