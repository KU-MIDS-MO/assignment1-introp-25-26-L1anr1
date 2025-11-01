def is_strictly_increasing_digits(n):
    if type(n) is int and n>=0:
        s = str(n)
        for i in range(len(s)-1):
            if s[i]>=s[i+1]:
                return False
        return True
    else:
        return -1
