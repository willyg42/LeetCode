def stringToInteger(s):
    num = 0
    i = 0
    sign = 1
    
    while i < len(s) and s[i] == ' ':
        i += 1
    
    if i < len(s) and s[i] == '+':
        i += 1
    elif i < len(s) and s[i] == '-':
        sign = -1
        i += 1
        
    while i < len(s) and s[i].isdigit():
        num *= 10
        num += int(s[i])
        i += 1
    
    num = sign * num
    
    if num < -2**31:
        return -2**31
    if num > 2**31 - 1: 
        return 2**31 - 1
    
    return num


if __name__ == '__main__':
    assert stringToInteger('42') == 42
    assert stringToInteger('-42') == -42
    assert stringToInteger('-91283472332') == -2147483648
    assert stringToInteger('') == 0
    assert stringToInteger('+-12') == 0
