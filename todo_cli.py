import os
from datetime import datetime

# Initialize the to-do list as a list of dictionaries
todo_list = []

# Load tasks from a file (if any)
def load_tasks():
    if os.path.exists('tasks.txt'):
        with open('tasks.txt', 'r') as file:
            for line in file:
                task_data = line.strip().split(" | ")
                todo_list.append({"task": task_data[0], "time": task_data[1]})

# Save tasks to a file
def save_tasks():
    with open('tasks.txt', 'w') as file:
        for task_info in todo_list:
            file.write(f"{task_info['task']} | {task_info['time']}\n")

# Function to display tasks
def show_tasks():
    if not todo_list:
        print("No tasks in the to-do list.")
    else:
        for i, task_info in enumerate(todo_list, 1):
            print(f"{i}. {task_info['task']} (Added on: {task_info['time']})")

# Add a task with the current time
def add_task():
    task = input("Enter a new task: ")
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Store the current time
    todo_list.append({"task": task, "time": current_time})
    print(f"Task added successfully at {current_time}!")

# Remove a task
def remove_task():
    show_tasks()
    task_num = int(input("Enter the task number to remove: "))
    if 0 < task_num <= len(todo_list):
        removed = todo_list.pop(task_num - 1)
        print(f"Task '{removed['task']}' removed successfully!")
    else:
        print("Invalid task number.")

# Update a task
def update_task():
    show_tasks()
    task_num = int(input("Enter the task number to update: "))
    if 0 < task_num <= len(todo_list):
        new_task = input("Enter the updated task: ")
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Update with the current time
        todo_list[task_num - 1] = {"task": new_task, "time": current_time}
        print("Task updated successfully!")
    else:
        print("Invalid task number.")

# Main program loop
def main():
    load_tasks()
    while True:
        print("\nTo-Do List Application")
        print("1. View tasks")
        print("2. Add a task")
        print("3. Update a task")
        print("4. Remove a task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            show_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            update_task()
        elif choice == '4':
            remove_task()
        elif choice == '5':
            save_tasks()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
