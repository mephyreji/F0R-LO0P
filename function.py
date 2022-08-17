def max_of_three(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
sum=max_of_three(1,2,3)
print(sum)
def max(a,b,c):
    sum=(a,b,c)
    return sum
sum=max(1,2,3)
print (sum)