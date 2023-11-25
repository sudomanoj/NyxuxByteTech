help_message = """• add -> add a task to the to-do list.
• complete -> mark a task as complete.
• view all -> view the current tasks in the to-do list.
• view complete -> view all the completed tasks in the to-do list.
• delete -> Delete the to-do list and take it to the bin if it is not permanent.
• view incomplete -> view all the incomplete tasks in the to-do list.
• view bin -> view all the tasks that are deleted and are not currently in bin.
• restore -> restore the deleted task from the bin.
• clear bin -> delete all the to-dos that are presented in the bin.
• help -> display all the help message.
• exit -> exit the program. """


todo_list = []
# completed_tasks = []
bin_tasks = []

class TodoManager:
    id_counter = 1
    
    @classmethod
    def get_next_id(cls):
        next_id = cls.id_counter
        cls.id_counter += 1
        return next_id

def add_task():
    try:
        task_id = TodoManager.get_next_id()
        task_name = str(input('Enter the name of task: '))
        task_desc = str(input('Enter the description about task: '))
        task_status = 'Incomplete'
        task_dict = {'task_id':task_id, 'task_name':task_name, 'task_desc':task_desc, 'task_status':task_status}
        already_in_todo = [task for task in todo_list if task['task_name'] == task_dict['task_name']]
        if not already_in_todo:
            todo_list.append(task_dict)
        else:
            print(f'Task {task_name} is already in Todo!')
    except Exception as e:
        print(e)

    
def complete_task():
    id = int(input('Enter the ID of task which is completed: '))
    try:
        is_task_in_todo = [x for x in todo_list if x['task_id'] == id]
        if is_task_in_todo:
            for index, task in enumerate(todo_list):
                if task == is_task_in_todo[0]:
                    todo_list[index]['task_status'] = 'Complete'
        else:
            print(f'Sorry Task Id {id} is not in Todo!')
    except Exception as e:
        print(e)

def view_all_tasks():
    for x in range(len(todo_list)):
        print('---------------------------------------------')
        for key, value in todo_list[x].items():
            print(f'{key}  :  {value}')
        print('---------------------------------------------')

def delete_task():
    try:
        id = int(input('Enter the ID of task to delete: '))
    except Exception as e:
        print(e)
    try:
        is_task_in_todo = [x for x in todo_list if x['task_id'] == id]
        if is_task_in_todo:
            are_you_sure = str(input(f'Do you wanna delete task {id} permanently? (yes/y): ' )).lower().strip()
            if are_you_sure in ['y', 'yes']:
                todo_list.remove(is_task_in_todo[0])
            else:
                bin_tasks.append(is_task_in_todo[0])
                todo_list.remove(is_task_in_todo[0])
    except:
        print(f'Task ID {id} is not in todo!!')
        
def view_completed_tasks():
    completed_tasks = [task for task in todo_list if task['task_status'] == 'Complete']
    if completed_tasks:
        for x in range(len(completed_tasks)):
            print('---------------------------------------------')
            for key, value in completed_tasks[x].items():
                print(f'{key}  :  {value}')
            print('---------------------------------------------')
    else:
        print('There is no completed task!!')
        
def view_incompleted_tasks():
    incompleted_tasks = [task for task in todo_list if task['task_status'] == 'Incomplete']
    if incompleted_tasks:
        for x in range(len(incompleted_tasks)):
            print('---------------------------------------------')
            for key, value in incompleted_tasks[x].items():
                print(f'{key}  :  {value}')
            print('---------------------------------------------')
    else:
        print('There is no incomplete task!!')

def view_bin_tasks():   
    for x in range(len(bin_tasks)):
        print('---------------------------------------------')
        for key, value in bin_tasks[x].items():
            print(f'{key}  :  {value}')
        print('---------------------------------------------')
        
def restore_from_bin():
    if bin_tasks:
        for deleted_task in bin_tasks:
            task_id = deleted_task['task_id']
            todo_list.insert(task_id-1, deleted_task)
        bin_tasks.clear()
    else:
        print('Bin is already in empty state!!')
    
def clear_bin():
    if bin_tasks:
        bin_tasks.clear()
    else:
        print('Bin is already in empty state!!')
    

print(help_message)
while True:
    command_by_user = input('Enter Command for Todo: ').lower().replace(' ', '')
    try:
        match command_by_user:
            case 'add':
                add_task()
            
            case 'complete':
                try:
                    complete_task()
                except Exception as e:
                    print(e)
                
            case 'viewall':
                view_all_tasks()
            
            case 'viewcomplete':
                view_completed_tasks()
            
            case 'delete':
                delete_task()
            
            case 'viewincomplete':
                view_incompleted_tasks()
            
            case 'viewbin':
                view_bin_tasks()
            
            case 'restore':
                restore_from_bin()
            
            case 'clearbin':
                clear_bin()
            
            case 'help':
                print(help_message)
            
            case 'exit':
                break
            
        
    except:
        print(help_message)
        print('Enter a valid Command!')
    