inventory_list = []
from abc import ABC, abstractmethod

class AbstractInventory(ABC):
    @abstractmethod
    def add_item(self):
        pass
    
    @abstractmethod
    def remove_item(self):
        pass

    @abstractmethod
    def update_item(self):
        pass
    
    @abstractmethod
    def view_invettory(self):
        pass

    @abstractmethod
    def low_stock_report(self):
        pass

class InventoryItem(AbstractInventory):
    
    def __init__(self, name, price, quantity, category):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category
    
    def add_item(self):
        if self.price > 0 and self.quantity >1:
            inventory_dict = {'name':self.name, 'price':self.price, 'quantity':self.quantity, 'category':self.category}
            inventory_list.append(inventory_dict)
            print('add_item called')
        

    def remove_item(self):
        try:
            name = str(input('Enter the name of the product: '))
        except Exception:
            print(Exception)
            
        is_product_there = [item for item in inventory_list if item['name'] == name]
        if is_product_there:
            inventory_list.remove(is_product_there[0])
        else:
            print(f'Item {name} is not present in Inventory list')
            
    def update_item(self):
        try:
            name = str(input('Enter the name of the product: '))
        except Exception:
            print(Exception)
        is_product_there = [item for item in inventory_list if item['name'] == name]
        if is_product_there:
            try:
                new_price = int(input(f'Enter the new Price of the Item {name} : ')) 
            except:
                new_price = None
            try:
                new_quantity = int(input(f'Enter the new quantity of the item {name}: '))
            except:
                new_quantity = None
            try:
                new_category = str(input(f'Enter the new category of the item {name}: '))
            except:
                new_category = None    
            
                
            for item in inventory_list:
                if is_product_there[0] == item:
                    if new_price is not None:
                        item['price'] = new_price
                        

                    if new_quantity is not None:
                        item['quantity'] = new_quantity

                    if new_category is not None:
                        item['category'] = new_category
        else:
            print(f'Item {name} is not present in the inventory!!')         
            
    def view_invettory(self):
        if inventory_list:
            for x in range(len(inventory_list)):
                print()
                for key, value in inventory_list[x].items():
                    print(f'{key}   {value}') 
                print()
                    
        else:
            print('Inventory list is empty!!')      

    def low_stock_report(self):
        warning_quantity = 10
        
        print(type(inventory_list[0]['quantity']))
        low_stocks = [item for item in inventory_list if item['quantity'] < warning_quantity]
        print(low_stocks)
        if low_stocks:
            for x in range(len(low_stocks)):
                print()
                print('Low stock Items are: ')
                for key, value in low_stocks[x].items():
                    print(f'{key}   {value}')           
                print()
        else:
            print('Items are in excessive quantity!!')



class Electronics(InventoryItem):
    def __init__(self, name, price, quantity, category):
        super().__init__(name, price, quantity, category)


help_message = f'Enter command for inventory: [add, update, remove, view, report]'
print(help_message)

while True:
    command = input('Enter a command: ')
    if command in ['add', 'update', 'remove', 'view', 'report']:
        match command:
            case 'add':
                try:
                    name = str(input('Enter the name of the product: '))
                    price = float(input(f'Enter the price of the product {name}: '))
                    quantity = int(input('Enter quantity: '))
                    category = str(input('Enter the category: '))
                    inventory_instance = InventoryItem(name, price, quantity, category)
                    inventory_instance.add_item()
                except Exception:
                    print(Exception)
                    
            
            case 'update':
                inventory_instance.update_item()
            
            case 'remove':
                inventory_instance.remove_item()
            
            case 'view':
                inventory_instance.view_invettory()
            
            case 'report':
                inventory_instance.low_stock_report()
                
            case 'exit':
                break
    
    else:
        print(help_message)
        print('Enter a valid command!!')