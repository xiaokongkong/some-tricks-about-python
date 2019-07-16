# 要求：不用加减乘除做加法
# 方法一：使用位运算，Python中大整数会自动处理，因此对carry需要加个判断
# 方法二：使用sum

def bit_add(n1, n2):
    carry = 1
    while carry:
        s = n1 ^ n2
        carry = 0xFFFFFFFF & ((n1 & n2) << 1)
        carry = -(~carry -1) & 0xFFFFFFFF) if carry > 0x7FFFFFFF else carry
        n1 = s
        n2 = carry
    return n1

def add2(n1, n2):
    return sum([n1, n2])


# C++
int Add(int num1, int num2)
{
    int sum, carry;
    do{
        sum = num1 ^ num2;
        carry = (num1 & num2) << 1; //考虑进位
        num1 = sum;
        num2 = carry;
    }while(num2 != 0)
    return num1;
}


不使用新的变量，交换两个变量的值
# 基于加减法
a = a + b;
b = a - b;
a = a - b;
# 基于异或运算
a = a ^ b;
b = a ^ b;
a = a ^ b;