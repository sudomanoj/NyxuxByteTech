1. Write a program that takes a number as input from the user and prints all the even numbers up to that number using a loop and conditional statement.

num = int(input('Enter a number: '))
for i in range(num + 1):
    if i % 2 == 0:
        print(i)
import random
secret_num = random.randint(0, 100)
number = int(input('Enter a number between 1 and 100: '))
