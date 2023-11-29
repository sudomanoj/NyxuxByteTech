from borrow_return import *

class Report_Generation:
    
    def display_book_inventory(self):
        for x in range(Book.book_list):
            print('#########################################')
            for key, value in Book.book_list[x].items():
                print(f'{key}  :  {value}')
            print('#########################################')
                
    
    def sort_by_input(self):
        sorting_options = ['member_id', 'member_name', 'book_id', 'book_name', 'borrow_date']
        if Borrow_Return.borrow_return_list:
            sorting_parameter = print(f'Enter sorting parameter among {sorting_options}')
            match sorting_parameter:
                case 'member_id':
                    sorted_list = sorted(Borrow_Return.borrow_return_list, key=lambda x : x['member_id'])
                    for x in range(len(sorted_list)):
                        print('#########################################')
                        for key, value in sorted_list[x].items():
                            print(f'{key}  :  {value}')
                        print('#########################################')
                case 'member_name':
                    sorted_list = sorted(Borrow_Return.borrow_return_list, key=lambda x : x['member_name'])
                    for x in range(len(sorted_list)):
                        print('#########################################')
                        for key, value in sorted_list[x].items():
                            print(f'{key}  :  {value}')
                        print('#########################################')
                
                case 'book_id':
                    sorted_list = sorted(Borrow_Return.borrow_return_list, key=lambda x : x['book_id'])
                    for x in range(len(sorted_list)):
                        print('#########################################')
                        for key, value in sorted_list[x].items():
                            print(f'{key}  :  {value}')
                        print('#########################################')
                
                case 'book_name':
                    sorted_list = sorted(Borrow_Return.borrow_return_list, key=lambda x : x['book_name'])
                    for x in range(len(sorted_list)):
                        print('#########################################')
                        for key, value in sorted_list[x].items():
                            print(f'{key}  :  {value}')
                        print('#########################################')
                
                case 'borrow_date':
                    sorted_list = sorted(Borrow_Return.borrow_return_list, key=lambda x : x['borrow_date'])
                    for x in range(len(sorted_list)):
                        print('#########################################')
                        for key, value in sorted_list[x].items():
                            print(f'{key}  :  {value}')
                        print('#########################################')
    
    def member_borrowing_report(self):
        for x in range(Borrow_Return.borrow_return_list):
            print('#########################################')
            for key, value in Borrow_Return.borrow_return_list[x].items():
                print(f'{key}  :  {value}')
            print('#########################################')