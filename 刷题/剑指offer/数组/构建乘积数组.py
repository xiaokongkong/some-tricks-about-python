# 给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1]
# 其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。
# 不能使用除法。
# python使用reduce
def multiply(A):
    B = []
    if len(A) == 0:
        return B
    else:
        for i in range(len(A)):
            tmp = A[i]
            A[i] = 1
            B.append(reduce(lambda x,y:x*y,A))
            A[i] = tmp
    return B

# 以i为对角线，mult的值是1,A[0],A[0]*A[1],...,A[0]*...*A[n-2],表示前半部分
# for a in A[i+1:]表示的是后半部分
def multiply(A):
    mult = 1
    B = [1] * len(A)
    for i in range(len(A)):
        mult = mult * A[i-1] if i>0 else mult  # i=0,mult=mult; i>0,mult=mult*A[i-1]
        for a in A[i+1:]:
            B[i] = B[i] * a
        B[i] = B[i] *mult
    return B