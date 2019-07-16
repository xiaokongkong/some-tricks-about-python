def power(base, exponent):
    if euqal_zero(base) or exponent < 0:
        return ZeroDivisionError
    ret = power_value(base, exponent)
    if exponent < 0:
        return 1.0 / ret
    else:
        return ret


def equal_zero(num):
    if abs(num - 0.0) < 0.00000001:
        return True


def power_value(base, exponent):
    # 用右移代替除以2
    # 用位与运算符代替求余运算符，来判断一个数是奇数还是偶数
    if exponent == 0:
        return 1
    if exponent == 1:
        return base
    result = power_value(base, exponent >> 1)
    result *= result
    if exponent & 1 == 1:  # 如果是奇数，就要再乘一次base。
        # 假设exponent=3,3>>1=1,返回的是base,result*=result之后是两倍的base.
        # 因为是奇数，所以要再乘以一次base,才能最终得到3倍的base
        # 假设exponent=2,2>>1=1,返回的是base,result*=result之后是两倍的base.
        result *= base
    return result
