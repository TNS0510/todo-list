import json
import os

DATA_FILE = "tasks.json"

def load_tasks():
    """Reads and returns tasks from tasks.json. Returns empty list if file is missing."""
    if not os.path.exists(DATA_FILE):
        return []
    
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []

def save_tasks(tasks):
    """Saves the current list of tasks into tasks.json with formatting."""
    with open(DATA_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks, title):
    """Creates a new task dictionary and appends it to the tasks list."""
    new_id = len(tasks) + 1
    new_task = {
        "id": new_id,
        "title": title,
        "completed": False
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f'\nTask "{title}" added successfully!')

def display_tasks(tasks):
    """Prints all tasks in a formatted view."""
    if not tasks:
        print("\nYour to-do list is empty!")
        return

    print("\n--- YOUR TO-DO LIST ---")
    for task in tasks:
        status = "✅ Done" if task["completed"] else "⏳ Pending"
        print(f'[{task["id"]}] {task["title"]} - {status}')
    print("------------------------")

def complete_task(tasks, task_id):
    """Finds a task by ID and sets its completed status to True."""
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            save_tasks(tasks)
            print(f'\nTask [{task_id}] marked as completed!')
            return
    print(f"\nTask with ID {task_id} not found.")

def delete_task(tasks, task_id):
    """Removes a task with matching ID from the list."""
    initial_length = len(tasks)
    updated_tasks = [t for t in tasks if t["id"] != task_id]
    
    if len(updated_tasks) < initial_length:
        save_tasks(updated_tasks)
        print(f"\nTask [{task_id}] deleted successfully!")
        return updated_tasks
    else:
        print(f"\nTask with ID {task_id} not found.")
        return tasks

# Main Application Menu Loop
if __name__ == "__main__":
    tasks = load_tasks()
    
    while True:
        print("\n=== TO-DO LIST MENU ===")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task Complete")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("\nSelect an option (1-5): ").strip()
        
        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            title = input("Enter task title: ").strip()
            if title:
                add_task(tasks, title)
            else:
                print("Task title cannot be empty.")
        elif choice == "3":
            try:
                task_id = int(input("Enter task ID to mark complete: "))
                complete_task(tasks, task_id)
            except ValueError:
                print("Invalid input. Please enter a numerical task ID.")
        elif choice == "4":
            try:
                task_id = int(input("Enter task ID to delete: "))
                tasks = delete_task(tasks, task_id)
            except ValueError:
                print("Invalid input. Please enter a numerical task ID.")
        elif choice == "5":
            print("\nGoodbye! All your tasks are safely stored.")
            break
        else:
            print("\nInvalid choice! Please select a number between 1 and 5.")