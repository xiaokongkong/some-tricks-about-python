# 把单词中的每个字母映射为ascii码，并加起来，但无法解决易位同构的问题
def hash(astring,tablesize):
    sum=0
    for item in astring:
        sum=sum+ord(item)
    return sum%tablesize


# 解决易位同构的问题
def hash_anagram(astring,tablesize):
    sum=0
    for pos,item in enumerate(astring,1):
        sum=sum+pos*ord(item)
    return sum%tablesize

print(hash_anagram('cat',11))

def mod_(lt,num):
    for item in lt:
        print(item%num)
lt=[113 , 117 , 97 , 100 , 114 , 108 , 116 , 105 , 99]
mod_(lt,11)
99,100,2,113,114,5,116,117,105,97,108