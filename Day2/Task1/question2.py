# 2. Write a program that prompts the user to enter two sets of numbers. Print the
# intersection and union of the two sets.

input1 = input('Enter values for set1 (values should be seperated by space): ')
input2 = input('Enter values for set2 (values should be seperated by space): ')

set1 = set(input1.split())
print(set1)
set2 = set(input2.split())
print(set2)
setunion=  set1.union(set2)
print(setunion)
setintersection = set1.intersection(set2)
print(setintersection)

