#Write a program to calculate power of a number using recursion

def pow(x,y):
    if y==0:
        return 1
    else:
        return x*pow(x,y-1)

a=int(input("Enter a number : "))
b=int(input("Enter power: "))
output=pow(a,b)
print(output)
