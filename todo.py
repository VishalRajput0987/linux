import os
TODO_FILE='todo.txt'
def load_tasks():
  if os.path.exists(TODO_FILE):
     with open(TODO_FILE, 'r')as file:
       return file.read().splitlines()
  return []

def save_tasks(tasks):
   with open(TODO_FILE,'w')as file:
     file.write('\n'.join(tasks))

def add_task(task):
   tasks=load_tasks()
   tasks.append(task)
   save_tasks(tasks)
   print(f'Added Task: {task}')

def view_tasks():
   tasks=load_tasks()
   if tasks:
       print("To-Do list: ")
       for index, task in enumerate(tasks, start=1):
          print(f"{index}.{task}")
   else:
      print("no task in the to-do list")

def remove_task(index):
   tasks=load_tasks()
   if 0 < index <= len(tasks):
      removed= tasks.pop(index-1)
      save_tasks(tasks)
      print(f'Removed task: {removed}')
   else:
      print("invalid task number")

def main():
  while True:
    print("\nTo-Do list Applicaton")
    print("1. Add task")
    print("2. View task")
    print("3.Remove task")
    print("4. Exit")

    choice=input("choose an option")

    if choice =='1':
       task=input("enter the task: ")
       add_task(task)
    elif choice =='2':
       view_tasks()
    elif choice=='3':
       try:
          index=int(input("enter task number to remove: "))
          remove_task(index)
       except ValueError:
          print("please enter a valid number")
    elif choice=='4':
       break
    else:
       print("invalid choice")

if __name__== '__main__':
    main() 

