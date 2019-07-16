'''
https://blog.csdn.net/yi_afly/article/details/52012593
将n的各个位分为两类：个位与其它位。
对个位来说：

若个位大于0，1出现的次数为round*1+1
若个位等于0，1出现的次数为round*1

对其它位来说：
记每一位的权值为base，位值为weight，该位之前的数是former，举例如图：

则：
若weight为0，则1出现次数为round*base
若weight为1，则1出现次数为round*base+former+1
若weight大于1，则1出现次数为rount*base+base


如503
个位：
个位大于0，1出现的次数为50*1+1=51次。也就是个位前面，从0到50，一共51次
其他位：
十位：10位为0，1出现的次数为5*10，百位从0到5一共是6轮，百位是0的时候，十位会出现10次1，因为010~019，一共是10次，
     而当前的十位是0，表示还没能出现510~519等数，所以round=5
百位：0*100+100，0是因为前面没有千位了，不然如果是1503的话，百位上1出现的次数是1*100，代表1100~1199，共100次，
     后面的加100，表示，100~199，出现了100次1

'''


def count(n):
    if n < 1:
        return 0
    count = 0
    base = 1  # base一开始是1，表示个位，然后逐步乘10，表示十位/百位等
    round = n
    while round > 0:
        weight = round % 10
        round //= 10
        count += round * base
        if weight == 1:
            count += n % base + 1
        elif weight > 1:
            count += base
        base *= 10
    return count

print(count(503))
