# 用有序字典来记录每个字符即出现的次数
from collections import OrderedDict


def occur_once(strings):
    if not strings:
        return None
    dt = OrderedDict()
    for s in strings:
        if s in dt.keys():
            dt[s] = dt[s] + 1
        else:
            dt[s] = 1
        # 或者
        # dt[s] = dt[s]+1 if dt.get(s) else 1

    for key, value in dt.items():
        if value == 1:
            return key


print(occur_once('agebaccdeff'))
# 如果不用有序字典的话，那么在最后遍历的时候，就按照strings的每个字符来遍历