def factorial(n):
    if n<0:
        return "invalid input"
    if n == 0:
        return 1
    return n*factorial(n-1)


n=int(input("enter number : "))
print(factorial(n))
