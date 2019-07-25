import itertools


def twentyfour(cards):
    for nums in itertools.permutations(cards):  # 四个数
        for ops in itertools.product('+-*/', repeat=3):  # 三个运算符（可重复！）
            # 构造三种中缀表达式 (bsd)
            bds1 = '({0}{4}{1}){5}({2}{6}{3})'.format(*nums, *ops)  # (a+b)*(c-d)
            bds2 = '(({0}{4}{1}){5}{2}){6}{3}'.format(*nums, *ops)  # (a+b)*c-d
            bds3 = '{0}{4}({1}{5}({2}{6}{3}))'.format(*nums, *ops)  # a/(b-(c/d))
            print('bds1 ',bds1)
            print('bds2 ',bds2)
            print('bds3 ',bds3)
            print('eval(bds1) ',eval(bds1))
            for bds in [bds1, bds2, bds3]:  # 遍历
                try:
                    if abs(eval(bds) - 24.0) < 1e-10:  # eval函数
                        return bds
                except ZeroDivisionError:  # 零除错误！
                    continue

    return 'Not found!'


cards = [[7, 8, 10, 10]]
for card in cards:
    print(twentyfour(card))
