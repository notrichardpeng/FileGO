import sys
import tkinter

global root

app_name = 'File Mover'

track_folder = "C:\\Users\\notri\\Downloads"
target_folder = "C:\\Users\\notri\\Desktop\\School"	
track_str_var = None
target_str_var = None

root = None

def force_quit():
	root.quit()
	root.destroy()

def open_window():
	root.deiconify()

def on_close():	
	root.withdraw()	

def on_apply(*args):
	global track_folder, target_folder
	track_folder = track_str_var.get()
	target_folder = target_str_var.get()
	print(track_folder)
	print(target_folder)
	print("---")

def GUI():
	global root, track_str_var, target_str_var
	root = tkinter.Tk()
	root.withdraw()
	root.geometry('400x420')
	root.title(app_name)
	root.iconbitmap('icon.ico')	

	track_str_var = tkinter.StringVar()
	target_str_var = tkinter.StringVar()
	track_str_var.set(track_folder)
	target_str_var.set(target_folder)

	my_frame = tkinter.Frame(root, bd=2, relief=tkinter.GROOVE)
	track_entry = tkinter.Entry(my_frame, textvariable=track_str_var)
	target_entry = tkinter.Entry(my_frame, textvariable=target_str_var)
	track_label = tkinter.Label(my_frame, text="Folder to observe change and extract from:")
	target_label = tkinter.Label(my_frame, text="Folder to put the files in: ")
	
	track_label.pack()
	track_entry.pack(pady=5)
	target_label.pack()	
	target_entry.pack(pady=5)	
	my_frame.pack(anchor=tkinter.NW, fill=tkinter.X)
	
	confirm_setting = tkinter.Button(root, text="Apply", command=on_apply)
	confirm_setting.pack()

	root.protocol("WM_DELETE_WINDOW", on_close)
	root.mainloop()

#cd Desktop\Programming\Python\FileMover
