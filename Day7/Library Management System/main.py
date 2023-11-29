from book_management import *
from borrow_return import *
from members_management import *
from report_generation import *


help_message = """
• add book -> Add a Book in the Library.
• update book -> Update a Book.
• view book -> View book in the Library.
• delete book -> Delete a book from Library.
• add member -> Add a member in the Library.
• update member -> Update a member.
• view member -> View member in the Library.
• delete member -> Delete a member from Library.
• update book quantity -> update a quantity of books.
• book status -> check for book status.
• update transaction -> update book transaction.
• view transaction -> view book transaction.
• calculate fine -> calculate overdue fine.
• delete -> delete the student.
• exit -> exit the program.
• sort -> Sort.
"""
print(help_message)

while True:
    try:
        command = str(input('Enter the command: ')).lower().replace(' ', '')
    except ValueError:
        print(ValueError)

    if command in ['addbook', 'updatebook', 'viewbook', 'deletebook', 'addmember', 'updatemember', 'viewmember', 'deletemember', 'updatebookquantity', 'bookstatus', 'updatetransaction', 'viewtransaction', 'calculatefine', 'exit', 'sort']:
        book_instance = Book()
        library_instance = LibraryMember()
        report_instance = Report_Generation()
        borrow_return_instance = Borrow_Return()
        
        match command:
            case 'addbook':
                book_instance.add_books(19)
            
            case 'updatebook':
                book_instance.update_book()
            
            case 'viewbook':
                book_instance.view_book()
            
            case 'deletebook':
                book_instance.remove_book()
            
            case 'addmember':
                library_instance.add_member()
            
            case 'updatemember':
                library_instance.update_member()
            
            case 'viewmember':
                library_instance.view_member()
            
            case 'deletemember':
                library_instance.remove_member()
            
            case 'sort':
                report_instance.sort_by_input()
                
            case 'updatebookquantity':
                borrow_return_instance.update_for_availability_quantity()
                
            case 'bookstatus':
                borrow_return_instance.is_book_available()
                
            case 'updatetransaction':
                borrow_return_instance.handle_member_transactions()
                
            case 'viewtransaction':
                borrow_return_instance.view_transaction()
                
            case 'calculatefine':
                borrow_return_instance.calculate_fine()
            
            case 'exit':
                break
            
            case 'help':
                print(help_message)
    else:
        print(f'Please provide a valid input!!')
            
            
            
