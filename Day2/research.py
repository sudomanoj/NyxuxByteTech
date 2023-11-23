# Error Handling
# List,Set,Tuples

# try:
#     ans = 10/0
#     print(ans)
    
# except:
#     print('An exception occured!')
    
# else:
#     print('No exception occured')

# finally:
#     print('Exception handeling')

# exception raising 

# name = 'Manoj'

# if name != 'NyxuxByte':
#     raise Exception('Sorry name should be NyxuxByte!')

# Dictionary can be created using dict() constructor as well

# mydict = dict(name = 'Manoj', age=22)
# print(mydict)

# car_dict = {
#     'brand':'BMW',
#     'model':'latest',
# }
# print(car_dict['brand'])
# 
# car = list()
# car_dict = {
#     'brand':'Ford',
#     'model':'latest',
# }

# print(car_dict.keys())
# print(car_dict.values())
# car.append(car_dict)
# print(car)
# isavailable = [c for c in car if c.get('brand') == 'BMW']
# if isavailable:
#     print('Car is available')
# else:
#     print('Car is not available')

# Items method will return each item in a dictionary as a tulple in a list 

# man = {
#     'name':'Manoj',
#     'age':22,
#     'sex':'M'
# }

# x = man.items()
# print(man.items())
# man['is_married'] = False
# print(x)
# if 'Manoj' in man.values():
#     print('Exists')

# We can update dictionary 
# book = {'Name':'Author'}

# title = input('Enter the name of the book: ')
# author = input('Enter the author of the book: ')
# book.update({title:author})
# print(book)

# we can remove the key value pair from the dictionary using pop method 

# for key, value in book.items():
#     print(f'{key}  {book[key]}')

