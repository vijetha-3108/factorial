def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n=int(input("Enter a number for which you want to get factorial:"))
if n<0:
    print("Enter a positive number:")
elif n==0:
    print("The factorial of 0 is 1")
else:
    print("The factorial of",n,"is:",factorial(n))
