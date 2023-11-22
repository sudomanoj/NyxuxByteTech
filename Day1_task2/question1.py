def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
    
n = int(input('Enter a number to calculate factorial: '))
factorial = fact(n)
print(f'Factorial of {n} is {factorial}')