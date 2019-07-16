def fibonacci(n):
    if n == 0 or n == 1:
        return n
    fibOne = 0
    fibTwo = 1
    fibN = 0
    for i in range(2, n):
        fibN = fibOne + fibTwo
        fibOne = fibTwo
        fibTwo = fibN
    return fibN