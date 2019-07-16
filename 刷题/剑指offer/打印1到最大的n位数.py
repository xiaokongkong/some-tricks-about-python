# 要求：输入n，打印出从1到最大的n位数
# 思路：Python中已经对大整数可以进行自动转换了，所以不需要考虑大整数溢出问题
def print_max_n(n):
    for num in range(10 ** n):
        print(num)
