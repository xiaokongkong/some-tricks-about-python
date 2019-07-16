1、思路
这道题还是比较简单的。表示数值的字符串遵循如下模式：

[sign]integral-digits[.[fractional-digits]][e|E[sign]exponential-digits]

其中，('['和']'之间的为可有可无的部分)。

在数值之前可能有一个表示正负的'+'或者'-'。接下来是若干个0到9的数位表示数值的整数
部分（在某些小数里可能没有数值的整数部分）。如果数值是一个小数，那么在小数后面
可能会有若干个0到9的数位表示数值的小数部分。如果数值用科学记数法表示，接下来是
一个'e'或者'E'，以及紧跟着的一个整数（可以有正负号）表示指数。

判断一个字符串是否符合上述模式时，首先看第一个字符是不是正负号。如果是，在字符串
上移动一个字符，继续扫描剩余的字符串中0到9的数位。如果是一个小数，则将遇到小数
点。另外，如果是用科学记数法表示的数值，在整数或者小数的后面还有可能遇到'e'或者
'E'。

// 数字的格式可以用A[.[B]][e|EC]或者.B[e|EC]表示，
// 其中A和C都是整数（可以有正负号，也可以没有）
// 而B是一个无符号整数
bool isNumeric(char* string)
{
    // 非法输入处理
    if(string == NULL)
        return false;
    // 正负号判断
    if(*string == "+" || *string == "-")
        ++string;
    if(*string == '\0')
        return false;
    bool numeric = true;
    scanDigits(&string);
    # 如果scan结束，string='\0'的话，就进入到return
    # 否则，string的可能情况有： '.'| 'e'| 'E'| '其他无关字符'
    if(*string != '\0')
    {
        //  对于小数，跳过小数点，然后对下一位进行扫描，直到遇到e或者E
        if(*string == '.')
        {
            ++string;
            scanDigits(&string);
            if(*string == 'e' || *string == 'E')
                numeric = isExponential(&string);
        }
        // 对于整数
        else if(*string == 'e' || *string == 'E')
            numeric = isExponential(&string);
        else
            numeric = false;
    }
    return numeric && *string == '\0';
}
void scanDigits(char** string)
{
    // 扫描数字，对于合法数字，直接跳过
    // 直到string=='0'或者string='e'/'E',循环结束
    while(**string!='\0' && **string>='0' && **string<='9')
        ++(*string);
}

// 用来判断科学计数法表示的数值的结尾部分是否合法
bool isExponential(char** string)  # 因为进入到这一步的时候，开头是E/e，所以先往后移一位
{
    ++(*string);
    if(**string == '+' || **string == '-'){  # 如果是+/-，就往后移一位
        ++(*string);
    }
    if(**string == '\0'){  # 如果e后面没了，就返回false
        return false;
    }
    scanDigits(string);  # 扫描字符串
    return (**string == '\0') ? true:false;
}