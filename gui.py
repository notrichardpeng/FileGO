import sys
import os
import threading

import tkinter

from pystray import Icon, Menu, MenuItem
from PIL import Image

import filemove

global root, systray

app_name = 'File Mover'

track_folder = "C:\\Users\\notri\\Downloads"
target_folder = "C:\\Users\\notri\\Desktop\\School"	
track_str_var = None
target_str_var = None

root = None

def quit_program():		
	systray.stop()
	root.destroy()				

def open_window():
	systray.stop()
	root.after(0, root.deiconify)

def on_close():		
	print("withdrawn")
	root.withdraw()	

	global systray

	my_menu = Menu(MenuItem("Open", open_window), MenuItem("Quit", quit_program))
	systray = Icon('File Mover', Image.open(sys.path[0] + "\\icon.ico"), menu=my_menu)		
	systray.run()	

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
	root.geometry('400x420')
	root.title(app_name)
	root.iconbitmap(sys.path[0] + "\\icon.ico")	

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


if __name__ == "__main__":
	my_observer = filemove.MyObserver()
	my_observer.set_path(track_folder, target_folder)
	
	GUI()		
	

#cd Desktop\Programming\Python\FileMover
#Desktop\Programming\Python\FileMover\gui.py
