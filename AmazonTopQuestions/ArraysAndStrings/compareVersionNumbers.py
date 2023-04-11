def compareVersionNumbers(version1, version2):
    l1 = [int(s) for s in version1.split('.')]
    l2 = [int(s) for s in version2.split('.')]
    l, r = 0, 0
    while l < len(l1) or r < len(l2):
        lval = l1[l] if l < len(l1) else 0
        rval = l2[r] if r < len(l2) else 0
        if lval < rval:
            return -1
        elif lval > rval:
            return 1
        l += 1
        r += 1
    return 0


if __name__ == '__main__':
    assert compareVersionNumbers('0.0.0', '00.00.00') == 0
    assert compareVersionNumbers('0.1', '1.0') == -1
    assert compareVersionNumbers('1.0.0', '1.0.0.0') == 0