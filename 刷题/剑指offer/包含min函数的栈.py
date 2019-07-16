class Stack:
    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, val):
        self.stack.append(val)  # 压入数据栈
        if self.min and self.min[-1] < val:
            # 如果min存在，且min的栈顶小于val,就再一次压入min的栈顶
            self.min.append(self.min[-1])
        else:
            # 否则，压入val,作为min的栈顶
            self.min.append(val)

    def pop(self):
        if self.stack:
            # 如果栈存在，弹出min的栈顶，并返回stack的栈顶
            self.min.pop()
            # 因为min中是存在重复元素的，
            # 所以这里相当于回到了被弹出元素在压入栈之前的情况
            return self.stack.pop()
        return None

    def min(self):
        # 如果min存在的话，就返回栈顶元素，否则返回空
        return self.min[-1] if self.min else None

