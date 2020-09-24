import tkinter

app_name = 'File Mover'
root = None

def open_window():
	root.deiconify()

def on_close():
	root.withdraw()

def close_program():
	print("close")
	root.destroy()

def GUI():
	global root
	root = tkinter.Tk()
	root.withdraw()
	root.geometry('400x420')
	root.title(app_name)
	root.iconbitmap('icon.ico')

	task_a = tkinter.Frame(root, bd=1, relief=tkinter.GROOVE)
	task_a_title = tkinter.Label(task_a, text="Task A")
	task_a_edit_button = tkinter.Button(task_a, text="Edit")
	task_a_title.pack(side=tkinter.LEFT, padx=5)
	task_a_edit_button.pack(side=tkinter.LEFT, padx=5)

	task_a.pack(anchor=tkinter.NW, fill=tkinter.X)
	
	root.protocol("WM_DELETE_WINDOW", on_close)
	root.mainloop()