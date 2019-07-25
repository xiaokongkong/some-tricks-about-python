n = 8
x = []
X = []


def conflict(k):
    global x
    for i in range(k):
        # x[i]==x[k] 同一行
        # abs(x[i]-x[k])==abs(i-k) 同一斜线
        if x[i] == x[k] or abs(x[i] - x[k]) == abs(i - k):
            return True
    return False


def queens(k):
    global n, x, X
    if k >= n:
        X.append(x[:])
        print(x)
    else:
        for i in range(n):
            x.append(i)
            if not conflict(k):
                queens(k + 1)
            x.pop()


def show(x):
    global n
    for i in range(n):
        print('. ' * x[i] + 'X ' + '. ' * (n - x[i] - 1))


queens(0)
print(X[-1],'\n')
show(X[-1])
