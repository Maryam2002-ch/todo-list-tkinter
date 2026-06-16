import tkinter as tk
import json
import os

file_name = "tasks.json"

def load_task():
    """load task from json file"""
    if os.path.exists(file_name):
        with open(file_name) as f_obj:
            return json.load(f_obj)
    else:
        return []

def add_to_file():
    """add task to json file"""
    old_task = load_task()
    new_task = entry.get().strip()

    if new_task:
        old_task.append(new_task)
        with open(file_name, 'w') as f_obj:
            json.dump(old_task, f_obj, indent=5)
        
        #insert new task to listbox
        listbox.insert(tk.END, new_task)
    
    entry.delete(0, tk.END)

def delete_task():
    """delete task from listbox and json file"""
    tasks = load_task()
    selected = listbox.curselection()

    if selected:
        index = selected[0]
        tasks.pop(index)
        listbox.delete(selected)

    #update file
    with open(file_name, 'w') as f_obj:
        json.dump(tasks, f_obj)

window = tk.Tk()
window.title("To-Do List 📃")
window.geometry("400x400")

#create entry
entry = tk.Entry(window, width=35)
entry.pack(pady=10)

#create add button
button = tk.Button(window, text="➕ Add task", command=add_to_file)
button.pack(pady=5)

#create frame for listbox
frame = tk.Frame(window)
frame.pack(pady=10, fill=tk.BOTH, expand=True)

#create scrollbar for listbox
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

#create listbox of task in json file
listbox = tk.Listbox(frame, yscrollcommand=scrollbar.set)
listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar.config(command=listbox.yview)

#insert task of json file in listbox
old_task = load_task()
for task in old_task:
    listbox.insert(tk.END, task)

delete_button = tk.Button(window, text="🗑️ Delete", command=delete_task)
delete_button.pack(pady=10)

window.mainloop()