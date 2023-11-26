help_message = """• add -> add a student to the system.
• view -> view students.
• search -> search for a student.
• update -> update a student.
• delete -> delete the student.
• exit -> exit the program.
• sort -> Sort student by marks.
"""
class Idcounter:
    id = 1
    
    @classmethod
    def get_next_id(cls):
        next_id = cls.id
        cls.id += 1
        return next_id

class Student:
    student_list = []
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks
    
    def __str__(self):
        return f'{self.name} {self.roll_number} {self.marks}'
    
    def add_student(self):
        try:
            stu_roll = Idcounter.get_next_id()
            stu_name = str(input('Enter the name of student: '))
            marks = int(input('Enter the marks obtained by student: '))
            stu_dict = {'roll':stu_roll, 'stu_name':stu_name, 'marks':marks}
            self.student_list.append(stu_dict)
            Print(f'Student with roll {stu_roll} added successfully!')
        except Exception as e:
            print(e)
            
    def view_all_students(self):
        try:
            for x in range(len(self.student_list)):
                print('---------------------------------------------')
                for key, value in self.student_list[x].items():
                    print(f'{key}  :  {value}')
                print('---------------------------------------------')
                     

        except Exception as e:
            print(e)

    def search_for_student(self):
        roll_number = int(input('Ener the roll no of the student: '))
        try:
            student_exists = [student for student in self.student_list if student['roll'] == roll_number]
            if student_exists:
                print('---------------------------------------------')
                for key, value in student_exists[0].items():
                    print(f'{key}  :  {value}')
                print('---------------------------------------------')
                print(f'Student having roll {roll_number} updated successfully!!')
            else:
                print(f'Student with roll number {roll_number} does not exist!!')
        except Exception as e:
            print(e)

    def update_student_information(self):
        roll_number = int(input('Ener the roll no of the student you wanna update: '))
        try:
            student_exists = [student for student in self.student_list if student['roll'] == roll_number]
            if student_exists:
                try:
                    new_stu_name = str(input('Enter the name of student: ')).strip()
                except:
                    new_stu_name = None
                try:
                    new_marks = int(input('Enter the marks obtained by student: '))
                except:
                    new_marks = None
                for student in self.student_list:
                    if student_exists[0] == student:
                        if new_stu_name is not None:
                            student['stu_name'] = new_stu_name
                        else:
                            student['stu_name']
                        
                        if new_marks is not None:
                            student['marks'] = new_marks
                        else:
                            student['marks']
            else:
                print(f'Student with roll number {roll_number} does not exist!!')
            
        except Exception as e:
            print(e)

    def delete_student(self):
        try:
            roll_number = int(input('Ener the roll no of the student you wanna delete: '))
        except Exception as e:
            print(e)
        try:
            student_exists = [student for student in self.student_list if student['roll'] == roll_number]
            if student_exists:
                self.student_list.remove(student_exists[0])
                print(f'Student having roll {roll_number} deleted Successfully!!')
            else:
                print(f'Student with roll number {roll_number} does not exists!!')
        except Exception as e:
            print(e)
    
    
    def sort_students_by_marks(self):
        if self.student_list:
            try:
                sorted_by_marks = sorted(self.student_list, key = lambda x : x['marks'], reverse=True)
                    
                for student in sorted_by_marks:
                    print(student)

            except Exception as e:
                print('Exception occured!!')
                print(e)
        else:
            print(f'There is no student till now!!')
            
    
    
student_obj = Student('Manoj', 101, 98)

print(help_message)
while True:
    try:
        command = str(input('Enter a command: ')).lower().replace(' ', '')
    except Exception as e:
        print(e)
    try:
        match command:
            case 'add':
                student_obj.add_student()
            
            case 'view':
                student_obj.view_all_students()
            
            case 'search':
                student_obj.search_for_student()
            
            case 'update':
                student_obj.update_student_information()
                
            case 'sort':
                student_obj.sort_students_by_marks()
            
            case 'delete':
                student_obj.delete_student()
                
            case 'help':
                print(help_message)
            
            case 'exit':
                break
            
            case default:
                print('Please enter a valid command!!')
                
    except Exception:
        print(Exception)
        
