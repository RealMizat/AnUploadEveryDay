import tkinter as tk
import time
 
presentDate =  time.asctime()[0:11]
 
root=tk.Tk()
root.configure(bg="black")
root.geometry("300x200")
tasks = []
tasks=["1", "2", "3"]
 
 
def update_listbox():
    for task in tasks:
        lb_update.insert("end", task)
 
def addTask():
    update_listbox()
 
def completeTask():
    pass
 
date=tk.Label(text=presentDate)
date.pack()
title = tk.Label(root, text="Welcome Name",)
title.pack()
entry = tk.Entry(root)
entry.pack()


add_task = tk.Button(root, text="Add Task", command=update_listbox)
add_task.pack()

completeTask = tk.Button(root, text="Finish Task", command=completeTask())
completeTask.pack()

lb_update = tk.Listbox(root)
lb_update.pack()

root.mainloop()
