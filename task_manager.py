from datetime import datetime
from pprint import pprint
tasks = list()
#task_col = dict()
#tasks.append(task_col)
def add_task():
    task_name = input("Enter the task name: ")
    task_start = input("Enter the task starting date(DD/MM/YY):")
    date_st = datetime.strptime(task_start, "%d/%M/%Y").date()
    task_end = input("Enter the task end date(DD/MM/YY):")
    date_end = datetime.strptime(task_end, "%d/%M/%Y").date()
    task_status = input("Enter tasks status: ") 
    global task_col
    task_col = dict(task_name = task_name,task_start = task_start, task_end =task_end, task_status= task_status  )
    tasks.append(task_col)
    pprint("Task registerd successfully")

def view_tasks():
    if tasks :
        pprint("Tasks:")
        pprint(list(tasks))
    else:
        pprint("Error,no tasks found.")

def delete_a_task():
    for task_col in tasks:
        task_name = input("Enter the task name ")
        for task_name in task_col.keys():
            task_col.clear()
            pprint("Task deleted successfully")
            return
        pprint("Task not found.")
def delete_tasks():
    if tasks:
        tasks.clear()
        pprint("All task are cleared successfully")
    else:
        pprint("Empty tasks.")    

while True:
    print("\nTask Manager Menu:\n 1. Add Task\n 2. View Tasks \n 3. Delete A Task \n 4. Delete All Tasks \n 5. Exit ")

    option = input("Enter your option: ")
    if option == "1":
        add_task()
    elif option == "2":
        view_tasks()
    elif option == "3":
        delete_a_task()    
    elif option == "4":
        delete_tasks()
    elif option == "5":
        pprint("Exiting Task Manager")
        break
    else:
        pprint("Please enter again your option correctly.")
