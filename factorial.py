#write a program to calculate factorial using recursion

def fact(n):
    if n<=1:
        return 1
    else:
        return n*fact(n-1)

result=fact(8)
print("Factorial of 8 is: ",result)
