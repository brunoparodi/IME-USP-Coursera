def x(n):
    if n == 0:
        print(n)
    else:
        #print(n)
        x(n-1)
        print(n)
    #print(n)
x(10)

def x1(n, m):
    if n == m or m == 0:
        return 1
    else:
        return x1(n-1,m) + x1(n-1,m+1)

print(x1(5,3))

##def x2(n):
##    if n >= 0 or n <= 2:
##        return n
##    else:
##        return x2(n-1) + x2(n-2) + x2(n-3)
##
##print(x2(6))
