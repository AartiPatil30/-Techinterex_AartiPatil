import json

tasks = []

# Load tasks from file
def load_tasks():
    global tasks
    try:
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []

# Save tasks to file
def save_tasks():
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=4)

# Add a new task
def add_task(title):
    task = {
        'id': len(tasks) + 1,
        'title': title,
        'completed': False
    }
    tasks.append(task)

# View all tasks
def view_tasks():
    if not tasks:
        print("No tasks found.")
    for task in tasks:
        status = "✔️" if task['completed'] else "❌"
        print(f"{task['id']}: {task['title']} [{status}]")

# Update task completion
def update_task(task_id):
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = not task['completed']
            print("Task updated successfully.")
            return
    print("Task not found.")

# Delete a task
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    print("Task deleted successfully.")

# Main menu loop
def main():
    load_tasks()
    while True:
        print("\n📋 To-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            title = input("Enter task title: ")
            add_task(title)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            try:
                task_id = int(input("Enter task ID to update: "))
                update_task(task_id)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == '4':
            try:
                task_id = int(input("Enter task ID to delete: "))
                delete_task(task_id)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == '5':
            save_tasks()
            print("Exiting... Tasks saved.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
