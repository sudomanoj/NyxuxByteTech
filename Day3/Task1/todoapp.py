
help_message = """• add -> add a task to the to-do list.
• complete -> mark a task as complete.
• viewall -> view the current tasks in the to-do list.
• viewcomplete -> view all the completed tasks in the to-do list.
• viewincomplete -> view all the incomplete tasks in the to-do list.
• help -> display all the help message.
• exit -> exit the program. """

todo_list = []
completed_tasks = []

all_commands = ['add', 'complete', 'viewall', 'viewcomplete', 'viewincomplete', 'help', 'exit']
print(help_message)
todo = True

while todo:
    command = input('Enter the command for todo_list: ').lower().strip()
    if command in all_commands:
        if command == 'add':
            try:
                todo_dict = {}
                todo_dict['task_id'] = int(input('Enter the id of task: '))
                todo_dict['task_name'] = str(input('Enter the name of task: '))
                already_in_todo = [x for x in todo_list if todo_dict['task_id'] == x['task_id']]
                if already_in_todo:
                    print('Task is already in todo list!')
                else:
                    todo_list.append(todo_dict)
            except ValueError:
                print('Please enter a valid Input')
            
        elif command == 'complete':
            task_id = int(input('Enter the id of the task: '))
            matching_task = next((x for x in todo_list if x['task_id'] == task_id), None)
            if matching_task:
                completed_tasks.append(matching_task)
            else:
                print('Task not found in the todo list.')
                
        elif command == 'viewall':
            if todo_list:
                for x in todo_list:
                    print(x)
            else:
                print('Your todo list is empty!')
                
        elif command == 'viewcomplete':
            if completed_tasks:
                for x in completed_tasks:
                    print(x)
            else:
                print('No task has been completed yet!!')

        elif command == 'viewincomplete':
            for x in todo_list:
                if x not in completed_tasks:
                    print(x)
                    
        elif command == 'help':
            print(help_message)

        elif command == 'exit':
            sure_for_exit = input('Are you sure for exit? (yes/y)').lower().strip()
            if sure_for_exit == 'yes' or sure_for_exit == 'y':
                todo = False
                
    else:
        print('Enter a valid Command')
        print(help_message)
