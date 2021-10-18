
def findDigits(n):
    c=0
    x=n
    while n:
        r=n%10
        n=n//10
        if r==0:
            pass
        elif x%r==0:                                                        """hackerrank"""
            c+=1
    return c
