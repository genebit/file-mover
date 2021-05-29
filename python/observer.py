import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

download_path = 'C:\\Users\\BitaraPC\\Downloads\\'
destination_file = './dest/'

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
                        
    event_handler = LoggingEventHandler()
    observer = Observer()
    observer.schedule(event_handler, download_path, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1) 
    except KeyboardInterrupt:
        observer.stop()
    observer.join()