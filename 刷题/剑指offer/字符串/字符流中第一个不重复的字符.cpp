// 将字节流保存起来，通过哈希表统计字符流中每个字符出现的次数，顺便将字符流保存
// 在string中，然后再遍历string，从哈希表中找到第一个出现一次的字符。
class Solution{
public:
    void Insert(char ch)
    {
        s += ch;
        count[ch]++;
    }
    char FirstAppearingOnce()
    {
        int length = s.size();
        for(int i=0;i<length;i++)
        { // 找到第一个出现一次的字符，就返回
            if(count[s[i]]==1)
                return s[i];
        }
    }
    return '#';

private:
    string s;
    int count[256] = {0};

}

class Solution:
    def __init__(self):
        self.count={}
        self.s=''
    def insert(self, char):
        self.s += char
        if char not in self.count.keys():
            self.count[char] = 1
        else:
            self.count[char] += 1
        # self.count[char] = self.count[char]+1 if self.count.get(char) else 1
    def first_appearing_once(self):
        for item in self.s:
            if self.count[item] == 1:
                return item
        return '#'