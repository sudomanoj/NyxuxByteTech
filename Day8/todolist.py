import os
import csv
help_message = """• add -> add a task to the to-do list.
• complete -> mark a task as complete.
• viewall -> view the current tasks in the to-do list.
• viewcomplete -> view all the completed tasks in the to-do list.
• viewincomplete -> view all the incomplete tasks in the to-do list.
• help -> display all the help message.
• exit -> exit the program. """

file_name = 'alltasks.csv'
file_path = os.path.join(os.getcwd(), file_name)


class TodoManager:
    id_counter = 1
    
    @classmethod
    def get_next_id(cls):
        next_id = cls.id_counter
        cls.id_counter += 1
        return next_id

all_commands = ['add', 'complete', 'viewall', 'viewcomplete', 'viewincomplete', 'help', 'exit']
print(help_message)


todo = True
while todo:
    print()
    command = input('Enter the command for todo_list: ').lower().strip()
    if command in all_commands:
        if command == 'add':
            already_in_todo = False
            try:
                task_id = TodoManager.get_next_id()
                task_name = str(input('Enter the name of task: '))
                task_desc = str(input('Enter the Description for task: '))
                completed = 'False'
                try:
                    with open(file_name, 'r', newline='') as f:
                        reader = csv.reader(f)
                        tasks = list(reader)
                    if tasks:
                        already_in_todo = [task for task in tasks if task[1] == task_name]
                        if already_in_todo:
                            print('Task is already in todo list!')
                except:
                    print('File has not been created yet!add')
                
                if not already_in_todo:
                    with open('alltasks.csv', 'a', newline = "") as f:
                        writer = csv.writer(f)
                        writer.writerow([task_id, task_name, task_desc, completed])

            except ValueError:
                print('Please enter a valid Input')
            
                
        elif command == 'complete':
            task_id = int(input('Enter the id of the task: '))
            try:
                with open(file_name, 'r', newline='') as f:
                    reader = csv.reader(f)
                    tasks = list(reader)
                found = False
                for task in tasks:
                    if int(task[0]) == task_id:
                        task[3] = 'True'
                        found = True
                        break
                if found:
                    with open(file_name, 'w', newline='') as f:
                        writer = csv.writer(f)
                        writer.writerows(tasks)
                    print(f'Task id {task_id} completed')
                else:
                    print(f'Task id {task_id} not found')
            except FileNotFoundError:
                print('File not found!')
            except Exception as e:
                print(e)
 
                
        elif command == 'viewall':
            try:
                with open(file_name, 'r', newline='') as f:
                    reader = csv.reader(f)
                    tasks = list(reader)
                if tasks:
                    for task in tasks:
                        print(f'id : {task[0]}      Name : {task[1]}        Description : {task[2]}     Complete:{task[3]}')
                else:
                    print(f'No task is there!!')
            except FileNotFoundError:
                print(f'File not found!!')
            except Exception as e:
                print(e)
                
        elif command == 'viewcomplete':
            try:
                with open(file_name, 'r', newline='') as f:
                        reader = csv.reader(f)
                        tasks = list(reader)
                        if tasks:
                            for task in tasks:
                                if task[3] == 'True':
                                    print(f'id: {task[0]} Name: {task[1]} Description:{task[2]} Complete:{task[3]}')
                                else:
                                    print('No task has been completed yet!')
            except FileNotFoundError:
                print('File not found!')

        elif command == 'viewincomplete':
            try:
                with open(file_name, 'r', newline='') as f:
                        reader = csv.reader(f)
                        tasks = list(reader)
                        if tasks:
                            for task in tasks:
                                if task[3] == 'False':
                                    print(f'id: {task[0]} Name: {task[1]} Description:{task[2]} Complete:{task[3]}')
                                else:
                                    print('All tasks are completed!')
            except FileNotFoundError:
                print('File not found!')
                    
        elif command == 'help':
            print(help_message)

        elif command == 'exit':
            sure_for_exit = input('Are you sure for exit? (yes/y)').lower().strip()
            if sure_for_exit == 'yes' or sure_for_exit == 'y':
                todo = False
                
    else:
        print('Enter a valid Command')
        print(help_message)