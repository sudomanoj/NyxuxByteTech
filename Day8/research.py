# File Handling
# Read Files
# Write Files
# Append
# Delete

# f = open('anotherfile.txt', 'r')
# print(f.read())
# f.close()

# f= open('demofile2.txt', 'w')
# f.write('There is some content while creating!')
# f.close()

# f = open('demofile2.txt', 'a')
# f.write(' Now there is more extra content on it.')

# f = open('demofile2.txt', 'r')
# print(f.read())
# print(f.writable())

# Deleting file using os module 

# import os
# os.remove('anotherfile.txt')
# os.remove('demofile2.txt')

# f = open('demofile.txt', 'w')
# f.write('I am gonna write on this!')


import os
# print(os.path.abspath('demofile.txt'))
quiz_list = []
def quiz_game():
    question = str(input('Question: '))
    answer = str(input('Answer: '))
    quiz_dict = {'question':question, 'answer':answer}
    if not os.path.exists('demofile.txt'):
        with open('demofile.txt', 'w') as m:
            m.write(question, answer)
    else:
        with open('demofile.txt', 'a') as m:
            m.write(question, answer)
            
while True:
    quiz_game()
# import os
# file_name = 'todoapp.txt'
# file_path = os.path.join(os.getcwd(), file_name)
# print(file_path)
# print(os.getcwd())