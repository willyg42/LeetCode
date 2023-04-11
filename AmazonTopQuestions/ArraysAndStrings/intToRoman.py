def intToRoman(num):
    romanToIntMap = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), 
                         (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
    res = []
    i = 0
    while num > 0:
        if num >= romanToIntMap[i][0]:
            res.append(romanToIntMap[i][1]) 
            num -= romanToIntMap[i][0]
        else:
            i += 1
    return ''.join(res)


if __name__ == '__main__':
    assert intToRoman(3) == 'III'
    assert intToRoman(58) == 'LVIII'
    assert intToRoman(1994) == 'MCMXCIV'