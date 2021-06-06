import time

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class ObserverFolder(FileSystemEventHandler):
    def on_modified(self, event):
        print('File Modified')

    def on_created(self, event):
        print('File Created')

    def on_moved(self, event):
        print('File Moved')
    
    def on_closed(self, event):
        print('File Closed')
    
    def on_deleted(self, event):
        print('File Deleted')

    def on_any_event(self, event):
        print('Event Occured')

downloads_folder = 'C:/Users/Gene/Downloads/'
destination_folder = './dest/'

event_handler = ObserverFolder()
observer = Observer()
observer.schedule(event_handler, downloads_folder, recursive=True)
observer.start()

try:
    while True:
        time.sleep(5) 
except KeyboardInterrupt:
    observer.stop()
observer.join()