# python
class Solution:
    def __init__(self):
        self.stackA=[]  // 第一个栈
        self.stackB=[]  //第二个栈
    def push(self,node):
        self.stackA.append(node)
    def pop(self):
        if self.stackB:  # 如果B中有元素
            return self.stackB.pop()
        elif not self.stackA: # 如果A\B中都没有元素
            return None
        else:  # 如果B中没有元素，A中有元素，就把A中的元素存到B中
            while self.stackA:
                self.stackB.append(self.stackA.pop())
            return self.stackB.pop()