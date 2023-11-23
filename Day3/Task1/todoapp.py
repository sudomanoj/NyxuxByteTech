
help_message = """• add -> add a task to the to-do list.
• complete -> mark a task as complete.
• viewall -> view the current tasks in the to-do list.
• viewcomplete -> view all the completed tasks in the to-do list.
• viewincomplete -> view all the incomplete tasks in the to-do list.
• help -> display all the help message.
• exit -> exit the program. """

todo_list = []
completed_tasks = []
incomplete_tasks = []

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
            try:
                todo_dict = {}
                todo_dict['task_id'] = TodoManager.get_next_id()
                todo_dict['task_name'] = str(input('Enter the name of task: '))
                todo_dict['task_desc'] = str(input('Enter the Description for task: '))
                todo_dict['completed'] = 'False'
                already_in_todo = [x for x in todo_list if todo_dict['task_id'] == x['task_id']]
                if already_in_todo:
                    print('Task is already in todo list!')
                else:
                    todo_list.append(todo_dict)
            except ValueError:
                print('Please enter a valid Input')
            
                
        elif command == 'complete':
            task_id = int(input('Enter the id of the task: '))
            is_in_todo = [x for x in todo_list if x['task_id'] == task_id]
            is_completed = [x for x in completed_tasks if x['task_id'] == task_id]
            if is_in_todo:
                if not is_completed:
                    is_in_todo[0]['completed'] = 'True'
                    completed_tasks.append(is_in_todo[0])
                    for a in range(len(completed_tasks)):
                        print('---------------------------------------------')
                        for x, y in completed_tasks[a].items():
                            print(f'{x} : {y}')
                        print('---------------------------------------------')
                            
                else:
                    print('Task was already completed!!')
                
        elif command == 'viewall':
            if todo_list:
                for a in range(len(todo_list)):
                        print('---------------------------------------------')
                        for x, y in todo_list[a].items():
                            print(f'{x} : {y}')
                        print('---------------------------------------------')
            else:
                print('Your todo list is empty!')
                
        elif command == 'viewcomplete':
            if completed_tasks:
                # for x in completed_tasks:
                #     print(x)
                for a in range(len(completed_tasks)):
                        print('---------------------------------------------')
                        for x, y in completed_tasks[a].items():
                            print(f'{x} : {y}')
                        print('---------------------------------------------')
            else:
                print('No task has been completed yet!!')

        elif command == 'viewincomplete':
            for x in todo_list:
                if x not in completed_tasks:
                    if x not in incomplete_tasks:
                        incomplete_tasks.append(x)

            if incomplete_tasks:
                for a in range(len(incomplete_tasks)):
                    print('---------------------------------------------')
                    for x, y in incomplete_tasks[a].items():
                        print(f'{x} : {y}')
                    print('---------------------------------------------')
                    
        elif command == 'help':
            print(help_message)

        elif command == 'exit':
            sure_for_exit = input('Are you sure for exit? (yes/y)').lower().strip()
            if sure_for_exit == 'yes' or sure_for_exit == 'y':
                todo = False
                
    else:
        print('Enter a valid Command')
        print(help_message)
