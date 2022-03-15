class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [None] * k
        self.maxlen = k
        self.front = 0
        self.rear = 0

    def enQueue(self, value: int) -> bool:
        if self.q[self.rear] is None:
            self.q[self.rear] == value
            self.rear = (self.rear + 1) % self.maxlen
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if self.q[self.front] is None:
            return False
        else:
            self.q[self.front] = None
            self.front = (self.front + 1) % self.maxlen
            return True

    def Front(self) -> int:
        if self.q[self.front] == None:
            return -1
        else:
            self.q[self.front]

    def Rear(self) -> int:
        if self.q[self.rear - 1] == None:
            return -1
        else:
            self.q[self.rear - 1]

    def isEmpty(self) -> bool:
        if self.front == self.rear and self.q[self.front] is None:
            return True
        else:
            False

    def isFull(self) -> bool:
        if self.front == self.rear and self.q[self.front] is not None:
            return True
        else:
            False