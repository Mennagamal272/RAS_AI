def sumn(n):
    if n<=0:
        return "invalid input"
    if n == 1:
        return 1
    return n+sumn(n-1)


n=int(input("enter number : "))
print(sumn(n))
