commands = ['add', 'display', 'remove', 'exit']   
books = list()
help_message = """add -> add a book to the inventory
remove -> remove a book from the inventory
display -> display the current books in the inventory
exit -> exit the program """

print(help_message)
stay = True
while stay:
    ans = input('Enter a command: ')
    if ans in commands:
        if ans == 'add':
            title = input('Enter the title of Book: ')
            if title not in books:
                books.append(title)

        if ans == 'remove':
            title = input('Enter the title of the book to remove: ')
            if title in books:
                books.remove(title)
                
            else:
                print('Book does not exist in library!!')

        if ans == 'display':
            if books:
                for book in books:
                    print(book)
            else:
                print('There is no book in library!!')
                
        if ans == 'exit':
            sure_want_to_exit = input('Are you sure want to exit? (y/yes)').lower()
            if sure_want_to_exit == 'yes' or sure_want_to_exit == 'y':
                stay = False
    
    else:
        print('Enter a valid Command')        

        
            
            
            
