import tkinter
import tkinter.messagebox
import pickle

root = tkinter.Tk()
root.title("To-Do List")

def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tkinter.END, task)
        entry_task.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="You must Enter a task.")

def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="Select the task to be Deleted")
# Create GUI
frame_tasks = tkinter.Frame(root)
frame_tasks.pack()

listbox_tasks = tkinter.Listbox(frame_tasks,bg="black",fg="white",font=("Arial",0,"bold"),height=15, width=55)
listbox_tasks.pack(side=tkinter.LEFT)

scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tkinter.RIGHT, fill=tkinter.Y)


entry_task = tkinter.Entry(root,width=53,borderwidth=70,fg="white",bd=13,bg="black",font=("Arial",0,"bold"))
entry_task.pack()

button_add_task = tkinter.Button(root, text="Add task", width=26, command=add_task,bg="black",fg="white",font=("Arial",0,"bold"))
button_add_task.pack(side="left")

button_delete_task = tkinter.Button(root, text="Delete task", width=25, command=delete_task,bg="black",fg="white",font=("Arial",0,"bold"))
button_delete_task.pack(side="right")
root.mainloop()