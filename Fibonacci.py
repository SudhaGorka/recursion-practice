#Write a program of fibonacci series.

def fibo(n):
    if n<=1:
        return n
    else:
        return (fibo(n-1)+fibo(n-2))

nterms=10
if nterms<=10:
    print()
else:
    print()
for i in range (nterms):
        print(fibo(i))

