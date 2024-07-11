class MyQueue:

    def __init__(self):
        self.s1 = [] # Use only pop and append for stack ops
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)
        print("s1:", self.s1, "s2:", self.s2)


    def pop(self) -> int:
        if len(self.s2) == 0:
            for _ in range(len(self.s1)):
                self.s2.append(self.s1.pop())

        print("s1:", self.s1,"s2:", self.s2)
        return self.s2.pop()


    def peek(self) -> int:
        if len(self.s2) == 0:
            for _ in range(len(self.s1)):
                self.s2.append(self.s1.pop())

        print("s1:", self.s1,"s2:", self.s2)
        return self.s2[-1]

    def empty(self) -> bool:
        if len(self.s2) or len(self.s1):
            return False
        else:
            return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()