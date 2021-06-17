import os
import shutil
import time

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyHandler(FileSystemEventHandler):
    
    def on_any_event(self, event):
        print(event)
        # for file in os.listdir(directory_to_track):
        #     name, extension = os.path.splitext(file)
        #     absolute_path = (directory_to_track + name + extension)
            
            # print('Moving {0} in the txt folder'.format(file))
            # shutil.move(absolute_path, destination_folder + txt_folder)

directory_to_track = 'C:/Users/Gene/Downloads/'

event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, directory_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(2) 
except KeyboardInterrupt:
    observer.stop()
observer.join()