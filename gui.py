import sys
import os
import threading

import tkinter

from pystray import Icon, Menu, MenuItem
from plyer import notification
from PIL import Image

import filemove

global root, systray

app_name = 'File Mover'

track_folder = "C:\\Users\\notri\\Downloads"
target_folder = "C:\\Users\\notri\\Desktop\\School"	

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


def on_apply_dest():
	pass

def notify(count):	
	notification.notify(
		title = "File Mover",
		message = str(count) + " files has been successfully moved!",
		timeout = 3,
		app_icon = sys.path[0] + "\\icon.ico",
		app_name = app_name
	)

def browse_directory(mode):
	pass

def create_directory_settings(main_frame):
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

def GUI():
	global root, track_str_var, target_str_var
	root = tkinter.Tk()	
	root.geometry('400x420')
	root.title(app_name)
	root.iconbitmap(sys.path[0] + "\\icon.ico")			

	main_frame = tkinter.Frame(root, bd=2, relief=tkinter.GROOVE)
	create_directory_settings(main_frame)
	main_frame.pack(anchor=tkinter.NW, fill=tkinter.X)
	
	confirm_setting = tkinter.Button(root, text="Apply", command=on_apply_dest)
	confirm_setting.pack()

	root.protocol("WM_DELETE_WINDOW", on_close)				
	root.mainloop()		

if __name__ == "__main__":
	my_observer = filemove.MyObserver()
	my_observer.set_path(track_folder, target_folder)
	my_observer.set_notification(notify)
	my_observer.check()

	GUI()		
	
#cd Desktop\Programming\Python\FileMover
#Desktop\Programming\Python\FileMover\gui.py

