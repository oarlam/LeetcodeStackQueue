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
        self.checked = set()

    def push(self, val: int) -> None:
        count = 1
        cur = self.stack.head
        if val in self.checked:
            while cur:
                if cur.data == val:
                    count = cur.count + 1
                    break
                cur = cur.next
        else:
            count = 1
            self.checked.add(val)
        self.stack.push(val, count)

    def pop(self) -> int:
        cur = self.stack.head
        max_count = 0

        while cur:
            if cur.count > max_count:
                max_count = cur.count
            cur = cur.next

        dummy = Node(0, count=0, n=self.stack.head)
        cur = dummy

        while cur.next:
            if cur.next.count == max_count:
                ans = cur.next.data
                cur.next = cur.next.next
                self.stack.head = dummy.next

                return ans

            cur = cur.next

# Тестування логіки:
# obj = FreqStack()
# obj.push(5)
# obj.push(7)
# obj.push(5)
# obj.push(7)
# obj.push(4)
# obj.push(5)
# print(obj.pop()) # Виведе 5
# print(obj.pop()) # Виведе 7
# print(obj.pop()) # Виведе 5
# print(obj.pop()) # Виведе 4

