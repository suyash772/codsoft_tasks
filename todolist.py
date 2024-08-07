print("*"*200)
print()
print("                     ~~~~~~~~~~~~~~~~~~~~~~~ TO DO LIST ~~~~~~~~~~~~~~~~~~~~~~~~                                       ")
print()
print("*"*200)

def display_tasks(tasks):

    """Display the current list of tasks."""

    if not tasks:
        print("No tasks found.")
        return

    print("\nTo-Do List:")
    for idx, task in enumerate(tasks, start=1):
        status = "Done" if task['done'] else "Pending"
        print(f"{idx}. {task['task']} - {status}")


def add_task(tasks):

    """Add a new task to the list."""

    task_description = input("Enter the task description: ")
    task = {
        'task': task_description,
        'done': False
    }
    tasks.append(task)
    print(f"Task '{task_description}' added successfully!")



def update_task(tasks):

    """Update the status of an existing task."""

    display_tasks(tasks)
    try:
        task_index = int(input("Enter the number of the task to update: ")) - 1
        if 0 <= task_index < len(tasks):
            tasks[task_index]['done'] = not tasks[task_index]['done']
            status = "Done" if tasks[task_index]['done'] else "Pending"
            print(f"Task '{tasks[task_index]['task']}' marked as {status}.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def delete_task(tasks):

    """Delete a task from the list."""

    display_tasks(tasks)
    try:
        task_index = int(input("Enter the number of the task to delete: ")) - 1
        if 0 <= task_index < len(tasks):
            removed_task = tasks.pop(task_index)
            print(f"Task '{removed_task['task']}' deleted successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def main():
    tasks = []

    while True:
        print("\n<<<<<<<<<<<<<<<< To-Do List Application >>>>>>>>>>>>>>>> ")
        print()
        print("*" * 70)

        print("1. Display Tasks")
        print("*" *70)

        print("2. Add Task")
        print("*" * 70)

        print("3. Update Task")
        print("*" * 70)

        print("4. Delete Task")
        print("*" * 70)

        print("5. Exit")
        print("*" * 70)
        print()


        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            update_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
