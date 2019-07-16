# 判断一个序列是不是栈的弹出序列的规律
# 如果下一个弹出的数字刚好是栈顶数字，那么直接弹出；
# 如果下一个弹出的数字不在栈顶，我们把压栈序列中还没有入站的数字压入辅助栈，直到把下一个需要弹出的数字压入栈顶为止
# 如果所有的数字都压入栈了，仍然没有找到下一个弹出的数字，那么该序列不可能是一个弹出序列

# 思路：使用一个辅助栈, 如果辅助栈栈顶元素不等于出栈元素，则从入栈中找该值，直到入栈为空
# 如果最后出栈序列为空，则是入栈的弹出序列值

def IsPopOrder(push_stack, pop_stack):
    stack = []
    index = 0
    while push_stack:
        stack.append(push_stack.pop(0))
        print(stack)
        while stack and stack[-1] == pop_stack[index]:
            stack.pop()
            index += 1
            print(stack)
    return not stack

def IsPopOrder_(push_stack, pop_stack):
    stack = []
    while push_stack:
        stack.append(push_stack.pop(0)) # 往stack中加元素，直到加进去的元素等于pop_stack[0]
        while stack and stack[-1] == pop_stack[0]:
            stack.pop()
            pop_stack.pop(0)
            print(stack)
            print(pop_stack)
    return not stack  # 最后，stack应该为空,not [] 就是True,不为空的话，就是false

push_stack = [1,2,3,4,5]
pop_stack = [2,5,4,3,1]
print(IsPopOrder_(push_stack, pop_stack))