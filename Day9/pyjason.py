# import json

# class Serializer_Deserializer:
#     def __init__(self):
#         pass
    
#     @classmethod
#     def serialize(self, data):
#         print('#####Serialized data####')
#         serialize_data = json.dumps(data)
#         print(serialize_data)
#         print(type(serialize_data))
#         return serialize_data
#     @classmethod    
#     def deserialize(self, data):
#         print('#####Deserialized data####')
#         deserialize_data = json.loads(data)
#         print(deserialize_data)
#         print(type(deserialize_data))
        
# play = True
# while play:
#     data_type = input('Enter data type [list, tuple, set, dictionary] or "exit": ')
#     if data_type in ['list', 'tuple', 'set', 'dictionary', 'exit']:
#         match data_type:
#             case 'list':
#                 mylist = []
#                 n = int(input('Enter number of data in list: '))
#                 for x in range(n):
#                     data = input(f'Enter data {x+1}: ')
#                     mylist.append(data)
                
#                 serialized_data = Serializer_Deserializer.serialize(mylist)
                
#                 Serializer_Deserializer.deserialize(serialized_data)
            
#             case 'tuple':
#                 mylist = []
#                 n = int(input('Enter number of data in tuple: '))
#                 for x in range(n):
#                     data = input(f'Enter data {x+1}: ')
#                     mylist.append(data)
#                 mytuple = tuple(mylist)
                
#                 serialized_data = Serializer_Deserializer.serialize(mytuple)
                
#                 Serializer_Deserializer.deserialize(serialized_data)
            
#             case 'set':
#                 myset = set()
#                 n = int(input('Enter number of data in list: '))
#                 for x in range(n):
#                     data = input(f'Enter data {x+1}: ')
#                     myset.add(data)
#                 mylist = list(myset)
                    
#                 serialized_data = Serializer_Deserializer.serialize(mylist)
                
#                 Serializer_Deserializer.deserialize(serialized_data)
            
#             case 'dictionary':
#                 user_input_str = input("Enter a dictionary in JSON format: ")

#                 try:
#                     user_dict = json.loads(user_input_str)
#                     print("User input dictionary:", user_dict)
#                 except json.JSONDecodeError:
#                     print("Invalid JSON format. Please enter a valid dictionary.")
                    
#                 print('Serialized form: ', Serializer_Deserializer.serialize(user_dict))
                
#                 print('Deserialized form: ', Serializer_Deserializer.deserialize(user_dict))
                            
#             case 'exit':
#                 play = False



import json

class Serializer_Deserializer:
    def __init__(self):
        pass
    
    @classmethod
    def serialize(cls, data):
        print('#####Serialized data####')
        serialize_data = json.dumps(data)
        print(serialize_data)
        print(type(serialize_data))
        return serialize_data
    
    @classmethod    
    def deserialize(cls, data):
        print('#####Deserialized data####')
        deserialize_data = json.loads(data)
        print(deserialize_data)
        print(type(deserialize_data))

play = True
while play:
    data_type = input('Enter data type [list, tuple, set, dictionary] or "exit": ')
    if data_type in ['list', 'tuple', 'set', 'dictionary', 'exit']:
        match data_type:
            case 'list':
                mylist = []
                n = int(input('Enter number of data in list: '))
                for x in range(n):
                    data = input(f'Enter data {x+1}: ')
                    mylist.append(data)
                
                serialized_data = Serializer_Deserializer.serialize(mylist)
                
                Serializer_Deserializer.deserialize(serialized_data)
            
            case 'tuple':
                mylist = []
                n = int(input('Enter number of data in tuple: '))
                for x in range(n):
                    data = input(f'Enter data {x+1}: ')
                    mylist.append(data)
                mytuple = tuple(mylist)
                
                serialized_data = Serializer_Deserializer.serialize(mytuple)
                
                Serializer_Deserializer.deserialize(serialized_data)
            
            case 'set':
                myset = set()
                n = int(input('Enter number of data in list: '))
                for x in range(n):
                    data = input(f'Enter data {x+1}: ')
                    myset.add(data)
                mylist = list(myset)
                    
                serialized_data = Serializer_Deserializer.serialize(mylist)
                
                Serializer_Deserializer.deserialize(serialized_data)
            
            case 'dictionary':
                name = input("Enter your name: ")
                age = int(input('Enter your age: '))

                user_dict = {'name':name, 'age':age}
                print("User input dictionary:", user_dict)

                serialized_data = Serializer_Deserializer.serialize(user_dict)                    
                Serializer_Deserializer.deserialize(serialized_data)
                            
            case 'exit':
                play = False
