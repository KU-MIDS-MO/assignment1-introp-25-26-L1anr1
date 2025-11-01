def count_digits_greater_than(n, t):
    if (type(n) is int and n>=0) and (type(t) is int and t>=0 and t<=9):
        s = str(n)
        count = 0
        for i in range(len(s)):
            if int(s[i])>t:
                count+=1
        return count
    else:
        return -1
