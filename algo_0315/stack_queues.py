class MyQueue:

    def __init__(self):
        # input stack
        self.stack1 = []
        # output stack
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:

    def peek(self) -> int:
        # output이 없으면
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def empty(self) -> bool:
        return len(self.stack1) == 0 and len(self.stack2) == 0
