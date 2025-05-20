import sys

todo_list = []

def add_task(task):
    todo_list.append(task)
    print(f'"{task}" has been added to the list.')

def remove_task():
    if not todo_list:
        print("No task to remove.")
    else:
        print("Current Tasks:")
        view_tasks()
        task_to_remove = input("Enter the exact task you want to remove: ")
        if task_to_remove in todo_list:
            todo_list.remove(task_to_remove)
            print(f'"{task_to_remove}" has been removed.')
        else:
            print(f'"{task_to_remove}" not found in the list.')

def view_tasks():
    if not todo_list:
        print("The task list is currently empty.")
    else: 
        print("\nTasks:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")

def main():
    while True:
        print("\n-- Menu --")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            task = input("Enter a task: ")
            add_task(task)
        elif choice == 2:
            remove_task()
        elif choice == 3:
            view_tasks()
        elif choice == 4:
            print("Exiting... Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please select between 1 and 4.")

if __name__ == "__main__":
    main()
