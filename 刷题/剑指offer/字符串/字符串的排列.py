# 直接调库
from itertools import permutations

x = permutations('ABC', 3)
ans = [''.join(item) for item in x]
print(ans)


# 递归
def my_permutation(s):
    str_set = []
    ret = []

    def permutation(string):
        for i in string:
            str_tem = string.replace(i, '')
            str_set.append(i)
            if len(str_tem) > 0:
                permutation(str_tem)
            else:
                ret.append(''.join(str_set))
            print(str_set)
            str_set.pop()

    permutation(s)
    return ret


ans = my_permutation('ABC')
print(ans)