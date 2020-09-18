import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

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

if __name__ == "__main__":
	observer = Observer()
	event_handler = Handler()

	observer.schedule(event_handler, track_folder, recursive=True)
	observer.start()
	try:
		while True:
			time.sleep(5)
	except KeyboardInterrupt:
		observer.stop()

	observer.join()


