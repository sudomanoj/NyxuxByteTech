# 3. Write a program that takes N numbers as input from a user and puts them in a list.
# Then the program should find out the sum of all the odd numbers and the sum of all the even numbers from the list and print them out. 

def sum(numbers):
    sum_of_odd = 0
    sum_of_even = 0
    
    for number in numbers:
        if number%2 == 0:
            sum_of_even += number
        else:
            sum_of_odd += number 
    
    return sum_of_odd, sum_of_even

mylist = []
num = int(input('How Many Number?'))

for i in range(num):
    number = int(input('Enter Number: '))
    mylist.append(number)

sum_of_odd, sum_of_even = sum(mylist)

print('Sum of odd numbers ', sum_of_odd)
print('Sum of Even numbers ', sum_of_even)
