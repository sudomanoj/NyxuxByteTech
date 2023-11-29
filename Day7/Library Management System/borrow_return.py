from book_management import *
from members_management import *
import datetime

class Borrow_Return:
    
    borrow_return_list = []
    book_availabilisy_list = []
    def update_for_availability_quantity(self):
        book_name = [book for book in Book.book_list]
        for book in book_name:
            book_quantity = int(f'Enter the quantity of book {book["book_name"]}: ')
            ans = str(input(f'Is book {book["book_name"]} available? (y/yes): ')).lower().replace('', ' ')
            if ans in ['y', 'yes']:
                is_available = bool(True)
            else:
                is_available = bool(False)
            book_availability_dict = {'book_name':book['book'], 'is_available':is_available}
            self.book_availabilisy_list.append(book_availability_dict)

    def is_book_available(self):
        for x in range(len(self.book_availabilisy_list)):
            print('#########################################')
            for key, value in self.book_availabilisy_list[x].items():
                print(f'{key}  :  {value}')        
            print('#########################################')
        
    def handle_member_transactions(self):
        member_id = int(input('Enter the id of the member: '))
        is_member_there = [member for member in LibraryMember.member_list if member['member_id'] == member_id]
        if is_member_there:
            book_id = int(input('Enter the id of the book: '))
            is_book_there = [book for book in Book.book_list if book['book_id'] == book_id]
            if is_book_there:
                transaction_status = str(input('Enter the transaction status of the member (b/borrow/r/return): ')).lower().replace('', ' ')
                if transaction_status in ['b', 'borrow', 'r', 'return']:
                    if transaction_status in ['b', 'borrow']:
                        date_input = input("Enter date of borrow (YYYY-MM-DD): ")
                        try:
                            date_of_borrow = datetime.strptime(date_input, '%Y-%m-%d')
                            date_of_return = ''
                            print("Date of borrow:", date_of_borrow)
                        except ValueError:
                            print("Invalid date format. Please use YYYY-MM-DD.")
                        
                    else:
                        date_input = input("Enter date of return (YYYY-MM-DD): ")
                        try:
                            date_of_return = datetime.strptime(date_input, '%Y-%m-%d')
                            if self.borrow_return_list:
                                for book in self.borrow_return_list:
                                    if book['book_id'] == book_id:
                                        date_of_borrow = book['borrow_date']
                                    else:
                                        date_of_borrowed = '1990-01-01'
                                        date_of_borrow = datetime.strptime(date_of_borrowed, '%Y-%m-%d')
                            print("Date of return:", date_of_return)
                            
                        except ValueError:
                            print("Invalid date format. Please use YYYY-MM-DD.")
                                                
                    borrow_return_dict = {'member_id': member_id, 'member_name':is_member_there[0]['member_name'], 'book_id':book_id, 'book_name':is_book_there[0]['book_name'], 'borrow_date':date_of_borrow, 'return_date':date_of_return}
                    self.borrow_return_list.append(borrow_return_dict)
                else:
                    print(f'Enter a valid input (b/borrow/r/return)')
            else:
                print(f'Sorry book with ID{book_id} is not Present!!')
        else:
            print(f'Sorry memeber with ID{member_id} is not Present!!')

    
    def view_transaction(self):
        for x in range(len(self.borrow_return_list)):
            print('#########################################')
            for key, value in self.borrow_return_list[x].items():
                print(f'{key}  :  {value}')        
            print('#########################################')
        
       
    def calculate_fine(self):
        member_id = int(input('Enter the id of the member: '))
        is_member_there = [member for member in LibraryMember.member_list if member['member_id'] == member_id]
        if is_member_there:
            try:
                total_fine = 0
                for member in is_member_there:
                    borrow_date = member['borrow_date']
                    return_date = member['return_date']
                    day_difference = (return_date.borrow_date).days
                    if day_difference > 15:
                        fine = (day_difference-15)*2
                        total_fine += fine
                    else: 
                        fine = 0
                        total_fine += fine
            except Exception:
                print(Exception)
            
            for member in LibraryMember.member_list:
                for m in is_member_there:
                    if member['member_id'] == member_id:
                        member['fine'] = total_fine

        # book_name = 