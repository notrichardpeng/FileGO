import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from infi.systray import SysTrayIcon

running = True
track_folder = "C:\\Users\\notri\\Downloads"
target_folder = "C:\\Users\\notri\\Desktop\\School"

class Handler(FileSystemEventHandler):
	def on_modified(self, event):
		for filename in os.listdir(track_folder):		
			suffix = os.path.splitext(filename)[1]
			if suffix != '.pdf' and suffix != '.doc':				
				continue

			curr_dir = track_folder + "\\" + filename	
			new_dir = target_folder + "\\" + filename
			os.rename(curr_dir, new_dir)


def say_hello(systray):
    print("Hello, World!")

def quit_program(systray):
	global running
	running = False	

if __name__ == "__main__":	
	observer = Observer()
	event_handler = Handler()

	menu_options = (("Say Hello", None, say_hello),)
	systray = SysTrayIcon("icon.ico", "Example tray icon", menu_options, on_quit=quit_program)
	systray.start()

	observer.schedule(event_handler, track_folder, recursive=True)
	observer.start()

	while running:
		time.sleep(5)