import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Initialize the to-do list as a list of dictionaries
tasks = []

# Function to update the task list in the listbox
def update_task_list():
    task_listbox.delete(0, tk.END)
    for task_info in tasks:
        task_listbox.insert(tk.END, f"{task_info['task']} (Added on: {task_info['time']})")

# Function to add a new task with a timestamp
def add_task():
    task = task_entry.get()
    if task:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Get the current time
        tasks.append({"task": task, "time": current_time})  # Store task with timestamp
        update_task_list()
        task_entry.delete(0, tk.END)
        print(f"Task added at {current_time}!")
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

# Function to delete a task
def delete_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        tasks.pop(selected_task_index[0])
        update_task_list()
    else:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

# GUI setup
window = tk.Tk()
window.title("To-Do List Application")

# Increase the window size
window.geometry("500x400")  # Set window width to 500 and height to 400

# Title label
title_label = tk.Label(window, text="To-Do List", font=("Times new roman", 24, "bold"))  # Title text with larger font
title_label.pack(pady=20)  # Padding above and below the title

# Description label
description_label = tk.Label(window, text="Easily organize and manage your daily tasks with this simple To-Do List. Add new tasks, update, and delete them as needed, all in one place.", font=("Times new roman", 15))  # Small description text
description_label.pack(pady=5)  # Padding between the description and the title

# Task entry (Increase the width)
task_entry = tk.Entry(window, width=60)  # Increase entry width
task_entry.pack(pady=40)  # Add padding around the entry widget

# Buttons
add_button = tk.Button(window, text="Add Task", command=add_task)
add_button.pack(pady=20)  # Add padding below the button

delete_button = tk.Button(window, text="Delete Task", command=delete_task)
delete_button.pack(pady=20)  # Add padding below the button

# Task list display (Increase the size of the listbox)
task_listbox = tk.Listbox(window, width=60, height=20)  # Increase width and height
task_listbox.pack(pady=20)  # Add padding around the listbox

# Start the GUI
window.mainloop()
