import sys
import os

import tkinter
from tkinter import filedialog

from pystray import Icon, Menu, MenuItem
from plyer import notification
from PIL import Image

import filemove

global root, systray, track_display, target_display

app_name = 'File Mover'

track_folder = "C:/Users/notri/Downloads"
target_folder = "C:/Users/notri/Desktop/School"	

root = None

#Button functions--------------------------------------------------------------------------------------------

def browse_directory(mode):
	path = filedialog.askdirectory()
	if mode == 'track':
		global track_folder
		track_folder = path
		print("track changed")
		track_display.config(text=path)
	elif mode == 'target':
		global target_folder
		target_folder = path
		print("target chanegd")
		target_display.config(text=path)

def on_apply(lb):
	my_observer.pause()
	my_observer.set_suffixes(lb.get(0, 'end'))
	my_observer.set_path(track_folder, target_folder)	

def add_suffix(listbox, entry):
	s = entry.get()
	listbox.insert('end', s)
	entry.delete(0, 'end')

def del_suffix(listbox):
	items = listbox.curselection()
	if len(items) == 0: return
	items = reversed(items)
	for c in items:
		listbox.delete(int(c))

#Callbacks--------------------------------------------------------------------------------------------

def quit_program():		
	systray.stop()
	root.destroy()				

def open_window():
	systray.stop()
	root.after(0, root.deiconify)

def on_close():			
	root.withdraw()	

	global systray

	my_menu = Menu(MenuItem("Open", open_window), MenuItem("Quit", quit_program))
	systray = Icon('File Mover', Image.open(sys.path[0] + "\\icon.ico"), menu=my_menu)																
	systray.run()		

def notify(count):	
	notification.notify(
		title = "File Mover",
		message = str(count) + " files has been successfully moved!",
		timeout = 3,
		app_icon = sys.path[0] + "\\icon.ico",
		app_name = app_name
	)

#GUI--------------------------------------------------------------------------------------------

def create_directory_settings(main_frame):
	global track_display, target_display

	#track
	track_label = tkinter.Label(main_frame, text="Folder to observe change and extract from:")
	track_frame = tkinter.Frame(main_frame)
	track_display = tkinter.Label(track_frame, text=track_folder, width=32, bd=2, relief=tkinter.SUNKEN, 
		anchor=tkinter.W)
	track_browse = tkinter.Button(track_frame, command=lambda: browse_directory('track'), text='Browse')

	track_display.pack(padx=5, side=tkinter.LEFT)
	track_browse.pack(padx=5, side=tkinter.LEFT)	
	track_label.pack()
	track_frame.pack(pady=5)	

	#target
	target_frame = tkinter.Frame(main_frame)
	target_label = tkinter.Label(main_frame, text="Folder to put the files in: ")
	target_display = tkinter.Label(target_frame, text=target_folder, width=32, bd=2, relief=tkinter.SUNKEN,
		anchor=tkinter.W)
	target_browse = tkinter.Button(target_frame, command=lambda: browse_directory('target'), text='Browse')	
	
	target_display.pack(padx=5, side=tkinter.LEFT)
	target_browse.pack(padx=5, side=tkinter.LEFT)

	target_label.pack()	
	target_frame.pack(pady=5)	

def create_list_of_suffixes(main_frame):
	suffix_label = tkinter.Label(main_frame, text="Suffixes of files to check for:")
	suffix_label.pack()

	suffix_frame = tkinter.Frame(main_frame)
	suffix = tkinter.Listbox(suffix_frame, height=10, width=15, selectmode='extended')
	suffix.insert(1, 'pdf')
	suffix.insert(2, 'doc')
	suffix.insert(3, 'docx')

	suffix_edit_frame = tkinter.Frame(suffix_frame)

	suffix_insert = tkinter.Entry(suffix_edit_frame, width=8)	
	add_button = tkinter.Button(suffix_edit_frame, text='Add', 
		command=lambda: add_suffix(suffix, suffix_insert))
	delete_button = tkinter.Button(suffix_edit_frame, text='Delete', command=lambda: del_suffix(suffix))

	suffix_insert.pack(pady=5)
	add_button.pack(pady=5)
	delete_button.pack(pady=5)

	suffix.pack(padx=5, side=tkinter.LEFT)
	suffix_edit_frame.pack(padx=5, side=tkinter.LEFT)

	suffix_frame.pack(pady=5)
	return suffix

def GUI():
	global root, track_str_var, target_str_var
	root = tkinter.Tk()	
	root.geometry('400x450')
	root.title(app_name)
	root.iconbitmap(sys.path[0] + "\\icon.ico")			

	main_frame = tkinter.Frame(root, bd=2, relief=tkinter.GROOVE)
	create_directory_settings(main_frame)
	suffix_lb = create_list_of_suffixes(main_frame)

	main_frame.pack(anchor=tkinter.NW, fill=tkinter.X)
	
	confirm_setting = tkinter.Button(root, text="Apply", 
		command=lambda: on_apply(suffix_lb))
	confirm_setting.pack(pady=5)

	working_text = tkinter.Label(root, text="checking for files to be moved...", 
		font="Helvetica 13 italic")
	working_text.pack(pady=5)

	root.protocol("WM_DELETE_WINDOW", on_close)				
	root.mainloop()		

if __name__ == "__main__":
	my_observer = filemove.MyObserver()
	my_observer.set_notification(notify)
	my_observer.set_path(track_folder, target_folder)	
	my_observer.check()

	GUI()		
	
#cd Desktop\Programming\Python\FileMover

