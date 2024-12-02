class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minstack or val <= self.minstack[-1]:
            self.minstack.append(val)
        else:
            self.minstack.append(self.minstack[-1])

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.minstack.pop()
        else:
            raise IndexError("Pop from an empty stack.")  # 빈 스택일 경우 예외 처리

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        raise IndexError("Top from an empty stack.")  # 빈 스택일 경우 예외 처리

    def getMin(self) -> int:
        if self.minstack:
            return self.minstack[-1]
        raise IndexError("GetMin from an empty stack.")  # 빈 스택일 경우 예외 처리