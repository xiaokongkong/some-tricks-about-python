def get_sum(n):
    return sum(range(1, n+1))
def get_sum2(n):
    return reduce(lambda x,y:x+y,range(1,n+1))