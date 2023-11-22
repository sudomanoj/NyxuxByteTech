def calc_gcd(a, b):
    while(b != 0):
        remainder = a%b
        a = b
        b = remainder
    return a

a = int(input('Enter your first Number: '))
b = int(input('Enter your first Number: '))

gcd = calc_gcd(a, b)
print(f'GCD of {a} and {b} is {gcd}')