from book_management import *
from error_handling import *

class Idgenerator1:
    id = 1
    
    @classmethod
    def get_next_id(cls):
        next_id = cls.id
        cls.id += 1
        return next_id

class LibraryMember():
    member_list = [] 
    def add_member(self):
        member_id = Idgenerator1.get_next_id()
        member_name = str(input('Enter the name of the book: '))
        member_dict = {'member_id':member_id, 'member_name':member_name}
        self.member_list.append(member_dict)

    def view_member(self):
        if self.member_list:
            for x in range(len(self.member_list)):
                print('#########################################')
                for key, value in self.member_list[x].items():
                    print(f'{key}  :  {value}')        
                print('#########################################')
    
    def update_member(self):
        try:
            member_id = int(input('Enter the id of the member: '))
            CustomError.id_exception(member_id)
        except ValueError:
            print('Invalid input please enter a number!')
        except NegativeIdException as e:
             print(e)
        is_member_there = [member for member in self.member_list if member['member_id'] == member_id]
        if is_member_there:
            member_name = str(input('Enter the name of the member: '))
            
            if len(member_name) > 0:
                for member in self.member_list:
                    if member == is_member_there[0]:
                        member['member_name'] = member_name                
            
        else:
            print(f'Sorry! member with id {member_id} is not present there!!')
            
            
    
    def remove_member(self):
        member_id = int(input('Enter the id of the member: '))
        is_member_there = [member for member in self.member_list if member['member_id'] == member_id]
        if is_member_there:
            self.member_list.remove(is_member_there[0])
        else:
           print(f'Sorry! member with id {member_id} is not present there!!') 