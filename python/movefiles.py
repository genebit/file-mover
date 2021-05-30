import os
import shutil
import time
from watchdog import observers 

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyHandler(FileSystemEventHandler):
    
    def on_any_event(self, event):
        print('Changes to the directory detected')
        for file in os.listdir(downloads_folder):
            name, extension = os.path.splitext(file)
            absolute_path = (downloads_folder + name + extension)
            
            # Folder for each extension
            txt_folder = '.txt/'
    
            if extension == '.txt':
                print('Moving {0} in the txt folder'.format(file))
                shutil.move(absolute_path, destination_folder + txt_folder)

            elif extension != '.ini':
                print('There are no files to move yet')


downloads_folder = 'C:/Users/Gene/Downloads/'
destination_folder = './dest/'

event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, downloads_folder, recursive=True)
observer.start()

try:
    while True:
        time.sleep(5) 
except KeyboardInterrupt:
    observer.stop()
observer.join()