# 翻转单词顺序
# 要求：翻转一个英文句子中的单词顺序，标点和普通字符一样处理
# 思路: Python中字符串是不可变对象，不能用书中的方法，可以直接转化成列表然后转回去
def reverse_words(sentence):
    tmp = sentence.split()
    return ''.join(tmp[::-1])




# 左旋转字符串
# 思路: 把字符串的前面的若干位移到字符串的后面
def rotate_string(sentence,n):
    if not sentence:
        return ''
    return sentence[n:] + sentence[:n]