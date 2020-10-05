import time
import os
import sys

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from infi.systray import SysTrayIcon
from plyer import notification

import gui

global my_observer

running = True
app_name = "File Mover"
check_suffix = ['.pdf', '.doc', '.docx']


class Handler(FileSystemEventHandler):
	def on_modified(self, event):
		count = 0
		for filename in os.listdir(gui.track_folder):		
			suffix = os.path.splitext(filename)[1]
			if suffix not in check_suffix:				
				continue

			curr_dir = gui.track_folder + "\\" + filename	
			new_dir = gui.target_folder + "\\" + filename

			name_exists = True
			while name_exists:
				try:
					os.rename(curr_dir, new_dir)						
				except FileExistsError:					
					filename = filename[:len(filename)-len(suffix)] + '1' + suffix
					new_dir = gui.target_folder + "\\" + filename
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
	sys.exit(0)

def open_window(systray):	
	gui.open_window()

if __name__ == "__main__":	
	global my_observer
	my_observer = Observer()
	event_handler = Handler()
	
	menu_options = (("Open", None, open_window),)
	systray = SysTrayIcon("icon.ico", app_name, menu_options, on_quit=force_quit)

	my_observer.schedule(event_handler, gui.track_folder, recursive=True)
	my_observer.start()
	systray.start()
	
	event_handler.on_modified(None)
	gui.GUI()

#cd Desktop\Programming\Python\FileMover
		