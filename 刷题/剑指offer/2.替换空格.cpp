class Solution:
public:
    void replaceSpace(char *str, int length)
    {
        int count=0;
        for(int i=0;i<length;i++)  // 从前向后记录字符串中的空格数
        {
            if(str[i]=='')
                count++;
        }
        for(int i=length-1;i>=0;i--)  // 从后向前替换空格
        {
            if(str[i]!=' ')
                str[i+2*count]=str[i];
            else{
                count--;
                str[i+2*count]='%';
                str[i+2*count+1]='2';
                str[i+2*count+2]='0';
            }
        }
    }