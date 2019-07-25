'''
解的长度是固定的。

这里特别注意：每个元素的状态数目不同！！！
'''

n = 3
a = [['帽1', '帽2', '帽3', '帽4'],
     ['衣1', '衣2', '衣3', '衣4', '衣5'],
     ['裤1', '裤2', '裤3']]

x = [0] * n  # 一个解，长度固定，3元数组
X = []  # 一组解

def conflict(k):
    return False


def match(k):
    global n, a, x, X
    if k >= n:
        print(x)
    else:
        for i in a[k]:
            x[k] = i
            if not conflict(k):
                match(k + 1)
            '''
            等同于
            最开始定义 x=[]    
            x.append(i) 
            if not conflict(k):
                match(k + 1)
            x.pop()
            '''


match(0)
