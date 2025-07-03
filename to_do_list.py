from tkinter import *
from tkinter import messagebox
import sqlite3

def add_task():
    task = task_entry.get()
    if task == "":
        messagebox.showinfo('Error', 'Please enter a task.')
    else:
        tasks.append(task)
        cursor.execute('INSERT INTO tasks (title) VALUES (?)', (task,))
        update_task_list()
        task_entry.delete(0, 'end')
def update_task_list():
    clear_task_list()
    for task in tasks:
        task_listbox.insert(END, task)
def delete_task():
    try:
        selected_task = task_listbox.get(task_listbox.curselection())
        tasks.remove(selected_task)
        cursor.execute('DELETE FROM tasks WHERE title = ?', (selected_task,))
        update_task_list()
    except:
        messagebox.showinfo('Error', 'No task selected.')
def delete_all_tasks():
    if messagebox.askyesno('Delete All', 'Are you sure you want to delete all tasks?'):
        tasks.clear()
        cursor.execute('DELETE FROM tasks')
        update_task_list()
def clear_task_list():
    task_listbox.delete(0, END)
def close_app():
    connection.commit()
    cursor.close()
    gui.destroy()
def load_tasks():
    for row in cursor.execute('SELECT title FROM tasks'):
        tasks.append(row[0])
if __name__ == "__main__":
    gui = Tk()
    gui.title("To-Do List")
    gui.geometry("665x400")
    gui.configure(bg="#B5E5CF")
    connection = sqlite3.connect('tasks.db')
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS tasks (title TEXT)')
    tasks = []
    frame = Frame(gui, bg="#8EE5EE")
    frame.pack(expand=True, fill=BOTH)
    Label(frame, text="TO-DO LIST\nEnter Task Title:", font=("Arial", 14, "bold"), bg="#8EE5EE").pack(pady=10)
    task_entry = Entry(frame, font=("Arial", 14), width=42)
    task_entry.pack(pady=10)
    button_frame = Frame(frame, bg="#8EE5EE")
    button_frame.pack(pady=10)
    Button(button_frame, text="Add", width=15, bg='#D4AC0D', command=add_task).pack(side=LEFT, padx=5)
    Button(button_frame, text="Remove", width=15, bg='#D4AC0D', command=delete_task).pack(side=LEFT, padx=5)
    Button(button_frame, text="Delete All", width=15, bg='#D4AC0D', command=delete_all_tasks).pack(side=LEFT, padx=5)
    Button(button_frame, text="Exit", width=15, bg='#D4AC0D', command=close_app).pack(side=LEFT, padx=5)
    task_listbox = Listbox(frame, width=70, height=9, selectmode=SINGLE)
    task_listbox.pack(pady=10)
    load_tasks()
    update_task_list()
    gui.mainloop()