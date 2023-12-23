#write a recursive function that accepts a number as its argument and returns the sum of digit.

def sumOf(num):
    if (num<10):
        return num
    else:
        return num%10 + sumOf(num//10)

n=int(input("Enter a two digit number you want sum of: "))
print(sumOf(n))
