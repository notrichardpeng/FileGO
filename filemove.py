import time
import os
import sys
import threading

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from infi.systray import SysTrayIcon
from plyer import notification

import gui

global my_observer, event_handler, track_folder, target_folder, gui_thread

running = True
app_name = "File Mover"
check_suffix = ['.pdf', '.doc', '.docx']
track_folder = ""
target_folder = ""

class Handler(FileSystemEventHandler):
	def on_modified(self, event):
		global track_folder, target_folder

		if target_folder != gui.target_folder:
			target_folder = gui.target_folder
			print("changed target_folder")

		count = 0
		for filename in os.listdir(track_folder):		
			suffix = os.path.splitext(filename)[1]
			if suffix not in check_suffix:				
				continue

			curr_dir = track_folder + "\\" + filename	
			new_dir = target_folder + "\\" + filename

			name_exists = True
			while name_exists:
				try:
					os.rename(curr_dir, new_dir)						
				except FileExistsError:					
					filename = filename[:len(filename)-len(suffix)] + '1' + suffix
					new_dir = target_folder + "\\" + filename
				else:
					name_exists = False

			count += 1

		if count > 0:
			notification.notify(
			title='File Moved!',
			message=str(count) + " files had been moved to its supposed destination!",
			app_name=app_name,
			app_icon='icon.ico',
			timeout=3)			

def force_quit(systray):
	gui.force_quit()
	sys.exit(0)

def open_window(systray):	
	gui.open_window()	

def observer_init():
	global my_observer, event_handler
	my_observer = Observer()
	my_observer.schedule(event_handler, track_folder, recursive=True)
	my_observer.start()
	

if __name__ == "__main__":		
	event_handler = Handler()
	
	menu_options = (("Open", None, open_window),)
	systray = SysTrayIcon("icon.ico", app_name, menu_options, on_quit=force_quit)
	systray.start()

	track_folder = gui.track_folder
	target_folder = gui.target_folder
	
	observer_init()
	event_handler.on_modified(None)

	#TODO: USE GUI AS MAIN CODE, TKINTER CANNOT BE THREADED
"""
	t = threading.Thread(target=gui.GUI)
	t.setDaemon(True)
	t.start()
"""

	#while True:
	#	if track_folder != gui.track_folder:
	#		track_folder = gui.track_folder
	#		observer_init()

#cd Desktop\Programming\Python\FileMover
		