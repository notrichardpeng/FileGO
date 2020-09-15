import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

track_folder = "C:\\Users\\notri\\Downloads"

class Handler(FileSystemEventHandler):
	def on_modified(self, event):
		print("wtf")

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


