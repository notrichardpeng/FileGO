import tkinter

app_name = 'File Mover'

track_folder = "C:\\Users\\notri\\Downloads"
target_folder = "C:\\Users\\notri\\Desktop\\School"	

root = None

def open_window():
	root.deiconify()

def on_close():	
	root.withdraw()	

def GUI():
	global root
	root = tkinter.Tk()
	root.withdraw()
	root.geometry('400x420')
	root.title(app_name)
	root.iconbitmap('icon.ico')

	track_str_var = tkinter.StringVar()
	target_str_var = tkinter.StringVar()

	my_frame = tkinter.Frame(root, bd=2, relief=tkinter.GROOVE)
	track_entry = tkinter.Entry(my_frame, textvariable=track_str_var)
	target_entry = tkinter.Entry(my_frame, textvariable=target_str_var)
	track_label = tkinter.Label(my_frame, text="Folder to observe change and extract from:")
	target_label = tkinter.Label(my_frame, text="Folder to put the files in: ")

	"""
	task_a_title = tkinter.Label(task_a, text="Task A")
	task_a_edit_button = tkinter.Button(task_a, text="Edit")
	task_a_title.pack(side=tkinter.LEFT)
	task_a_edit_button.pack(side=tkinter.RIGHT)
	"""

	track_label.pack()
	track_entry.pack(pady=5)
	target_label.pack()	
	target_entry.pack(pady=5)	
	my_frame.pack(anchor=tkinter.NW, fill=tkinter.X)
	
	root.protocol("WM_DELETE_WINDOW", on_close)
	root.mainloop()

#cd Desktop\Programming\Python\FileMover
