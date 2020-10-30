import os
import sys
import threading

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

check_suffix = ['.pdf', '.doc', '.docx']

class Handler(FileSystemEventHandler):
	
	def __init__(self):
		self.track_folder = ""
		self.target_folder = ""

	def set_notification(self, func):
		self.notify_callback = func

	def on_modified(self, event):		
		count = 0
		for filename in os.listdir(self.track_folder):		
			suffix = os.path.splitext(filename)[1]
			if suffix not in check_suffix:				
				continue

			curr_dir = self.track_folder + "\\" + filename	
			new_dir = self.target_folder + "\\" + filename

			name_exists = True
			while name_exists:
				try:
					os.rename(curr_dir, new_dir)						
				except FileExistsError:					
					filename = filename[:len(filename)-len(suffix)] + '1' + suffix
					new_dir = self.target_folder + "\\" + filename
				else:
					name_exists = False

			count += 1

		if count > 0:
			self.notify_callback(count)
	

class MyObserver:

	def __init__(self):
		self.event_handler = Handler()
		self.observer = Observer()
		self.started = False

	def set_path(self, track, target):
		self.observer.unschedule_all()
		self.event_handler.track_folder = track
		self.event_handler.target_folder = target		
		self.observer.schedule(self.event_handler, track)

		if self.started: return
		self.observer.start()
		self.started = True

	def set_notification(self, func):
		self.event_handler.set_notification(func)

	#auto check folder at start of program
	def check(self):
		self.event_handler.on_modified(None)


#cd Desktop\Programming\Python\FileMover
		