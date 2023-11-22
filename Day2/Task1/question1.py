# 1. Write a program that prompts the user to enter a number. Create a list of squares of all
# numbers from 1 to the user-entered number.

squared_list = list()
number = int(input('Enter a number Upto which you wanna calculate squares: '))

for num in range(1, number+1, 1):
    squared_list.append(num*num)
    
print(squared_list)