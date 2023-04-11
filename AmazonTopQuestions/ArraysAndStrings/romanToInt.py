def romanToInt(s):
    romanToIntMap = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = romanToIntMap[s[-1]]
    for i in range(len(s) - 2, -1, -1):
        if romanToIntMap[s[i]] < romanToIntMap[s[i + 1]]:
            total -= romanToIntMap[s[i]]
        else:
            total += romanToIntMap[s[i]]
    return total


if __name__ == '__main__':
    assert romanToInt('MCMXCIV') == 1994