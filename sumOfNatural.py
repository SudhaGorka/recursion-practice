#write a recursive function that calculate sum of first n nattural numbers.
def sum_of(n):
    if n==0:
        return 0
    else:
        return (n+sum_of(n-1))

num=int(input("Enter a positive integer number: "))
print(sum_of(num))
