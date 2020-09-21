import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from infi.systray import SysTrayIcon

from plyer import notification


running = True
track_folder = "C:\\Users\\notri\\Downloads"
target_folder = "C:\\Users\\notri\\Desktop\\School"
check_suffix = ['.pdf', '.doc', '.docx']


class Handler(FileSystemEventHandler):
	def on_modified(self, event):
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
			app_name='File Mover',
			app_icon='icon.ico')


def quit_program(systray):
	global running
	running = False	

if __name__ == "__main__":	
	observer = Observer()
	event_handler = Handler()
	
	systray = SysTrayIcon("icon.ico", "File Mover", None, on_quit=quit_program)
	systray.start()

	observer.schedule(event_handler, track_folder, recursive=True)
	observer.start()
	event_handler.on_modified(None)

	while running:
		time.sleep(5)