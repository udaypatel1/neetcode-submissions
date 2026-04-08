class MinStack:

    def __init__(self):

        self.st = []
        self.min_stack = []
        
    def push(self, val: int) -> None:

        self.st.append(val)

        if self.min_stack:
            if val <= self.min_stack[-1]:
                self.min_stack.append(val)

        else:
            self.min_stack.append(val)
        
    def pop(self) -> None:

        popped_node = self.st.pop(-1)
        if popped_node == self.min_stack[-1]:
            self.min_stack.pop(-1)

    def top(self) -> int:

        return self.st[-1]

    def getMin(self) -> int:

        return self.min_stack[-1]
        
