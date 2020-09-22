import tkinter

app_name = 'File Mover'

root = tkinter.Tk()
root.geometry('400x420')
root.title(app_name)
root.iconbitmap('icon.ico')

task_a = tkinter.Frame(root, bd=1, relief=tkinter.GROOVE)
task_a_title = tkinter.Label(task_a, text="Task A")
task_a_edit_button = tkinter.Button(task_a, text="Edit")
task_a_title.pack(side=tkinter.LEFT, padx=5)
task_a_edit_button.pack(side=tkinter.LEFT, padx=5)

task_a.pack(anchor=tkinter.NW, fill=tkinter.X)





root.mainloop()