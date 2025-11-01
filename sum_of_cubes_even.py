def sum_of_cubes_even(n):
    if type(n) is int and n>=0:
        if n>2000:
            print("WARNING!!!")
        sum = 0
        for i in range(n+1):
            if i%2==0:
                sum+=i**3
        f = float(sum)
        return f
else:
    return -1
