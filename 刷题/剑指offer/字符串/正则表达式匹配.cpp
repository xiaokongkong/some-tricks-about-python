public Solution{
public:
    bool match(char* str, char* pattern)
    {
        // 指针为空，返回false
        if(str == NULL || pattern == NULL)
            return false;
        return matchCase(str, pattern);
    }

private:
    bool matchCase(char* str, char* pattern){
        // str和pattern都运行到了结尾，返回true
        if(*str == '\0' && *pattern == '\0')
            return true;
        // str没有到结尾，但pattern到了结尾，返回false
        // pattern到了结尾，但str到了结尾，则根据后续判断进行，需要对‘*’做处理
        if(*str != '\0' && *pattern == '\0')
            return false;
        // 如果pattern的下一个字符是‘*’，则进入状态机的匹配
        if(*(pattern + 1) == '*'){
            // 如果str和pattern相等，或者pattern是‘.’，并且str没有到结尾，则继续匹配
            if(*str == *pattern || (*pattern == '.' && *str != '\0')){
                // 进入下一个状态，就是匹配到了一个
                return matchCase(str+1, pattern+2) ||
                        // 保持当前状态，就是继续拿这个‘*’去匹配
                        matchCase(str+1, pattern) ||
                        // 跳过这个‘*’
                        matchCase(str, pattern+2);
            }
            // 如果str和pattern不相等，则跳过当前pattern的字符和‘*’，进入新一轮的匹配
            else{
                // 跳过这个‘*’
                return matchCase(str, pattern+2);
            }
        }
        // 如果str和pattern相等，或者pattern是‘.’，并且str没有到结尾，则继续匹配
        if(*str == *pattern || (*pattern == '.' && *str != '\0'))
            return matchCase(str + 1, pattern + 1);
        return false;
    }
};