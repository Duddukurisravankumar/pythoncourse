from collections import deque
class MyStack:
    def __init__(self):
        self.queue = deque()    
    def push(self, x: int) -> None:
        self.queue.append(x)
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())
    def pop(self) -> int:
        return self.queue.popleft()
    def top(self) -> int:
        return self.queue[0]
    def empty(self) -> bool:
        return not self.queue
stack = MyStack()
stack.push(1)
stack.push(2)
stack.push(20)
stack.push(30)
stack.push(40)
print(MyStack)
print(stack.top())    # Output: 2
print(stack.pop())    # Output: 2
print(stack.empty())# Output: False
