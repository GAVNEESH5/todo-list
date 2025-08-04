import os

TASKS_FILE = "tasks.txt"

# Load tasks from file
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return [line.strip() for line in f.readlines()]
    else:
        return []

# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")

# Display tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    print()

# Add a task
def add_task(tasks):
    task = input("Enter new task: ").strip()
    if task:
        tasks.append(task)
        print("Task added.\n")
    else:
        print("⚠ Empty task not added.\n")

# Remove a task
def remove_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter task number to remove: "))
        if 1 <= index <= len(tasks):
            removed = tasks.pop(index - 1)
            print(f"Removed: {removed}\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("⚠ Please enter a valid number.\n")

# Main loop
def main():
    tasks = load_tasks()
    while True:
        print("=== TO-DO LIST MENU ===")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            save_tasks(tasks)
            print("Goodbye! Tasks saved.")
            break
        else:
            print("Invalid choice. Try again.\n")

if _name_ == "_main_":
    main()