class task:
    def __init__(self,description):
        self.description=description
        self.completed=False
class TodolistMananger:
        def __init__(self):
            self.tasks=[]
        def add_task(self,description):
            self.tasks.append(task(description))
        def del_task(self,task_index):
            if 0<=task_index<len(self.tasks):
                self.tasks[task_index].completed=True
            else:
                print('invalid task')
        def mark_complete(self,task_index):
            if 0<=task_index<len(self.tasks):
                self.tasks[task_index].completed=True
            else:
                print('Invalid task index')
        def list_tasks(self):
            for i,task in enumerate(self.tasks):
                completion_status="completed" if task.completed else "pending"
                print(f"{i+1}.{task.description}({completion_status})")
if __name__=="__main__":
    todo_list=TodolistMananger()
    while True:
        print("\n To-Do list Manager")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Mark Task completed")
        print("4. List Tasks")
        print("5. Exit")
        choice=input("Enter 1-5\n")
        if choice=="1":
            description=input("Enter task description:")
            todo_list.add_task(description)
            print("Task added successfully")
        elif choice=="2":
            todo_list.list_tasks()
            task_index=int(input("Enter task index to delete:"))-1
            todo_list.del_task(task_index)
        elif choice=="3":
            todo_list.list_tasks()
            task_index=int(input("Enter task index to Mark complete:"))-1
            todo_list.mark_complete(task_index)
        elif choice=="4":
            todo_list.list_tasks()
        elif choice=='5':
            break
        else:
            print("Invalid choice")    
                