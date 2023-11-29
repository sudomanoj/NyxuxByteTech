from abc import ABC, abstractmethod

class Abstract_class(ABC):
    @abstractmethod
    def add_books(self):
        pass
    
    @abstractmethod
    def update_book(self):
        pass
    
    @abstractmethod
    def remove_book(self):
        pass

class Idgenerator:
    id = 1
    
    @classmethod
    def get_next_id(cls):
        next_id = cls.id
        cls.id += 1
        return next_id
        

class Book(Abstract_class):
    book_list = [] 
    def add_books(self, age):
        book_id = Idgenerator.get_next_id()
        book_name = str(input('Enter the name of the book: '))
        author_name = str(input('Enter the name of the autor: '))
        book_dict = {'book_id':book_id, 'book_name':book_name, 'author_name':author_name}
        self.book_list.append(book_dict)


    def update_book(self):
        book_id = int('Enter the id of the book: ')
        is_book_there = [book for book in self.book_list if book['book_id'] == book_id]
        if is_book_there:
            book_name = str(input('Enter the name of the book: '))
            author_name = str(input('Enter the name of the autor: '))
            
            if len(book_name) > 0:
                for book in self.book_list:
                    if book == is_book_there[0]:
                        book['book_name'] = book_name
                        
            if len(author_name) > 0:
                for book in self.book_list:
                    if book == is_book_there[0]:
                        book['author_name'] = author_name
                
            
        else:
            print(f'Sorry! book with id {book_id} is not present there!!')
            
    def view_book(self):
        if self.book_list:
            for x in range(len(self.book_list)):
                print('#########################################')
                for key, value in self.book_list[x].items():
                    print(f'{key}  :  {value}')        
                print('#########################################')
    
    def remove_book(self):
        book_id = int(input('Enter the id of the book: '))
        is_book_there = [book for book in self.book_list if book['book_id'] == book_id]
        if is_book_there:
            self.book_list.remove(is_book_there[0])
        else:
           print(f'Sorry! book with id {book_id} is not present there!!') 
    
