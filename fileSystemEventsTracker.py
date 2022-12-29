import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "/Users/mehvishbondre/Desktop/holypickles"

class FileEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(f"-> {event.src_path} has been created <-")

    def on_deleted(self, event):
        print(f"-> {event.src_path} has been deleted <-")

    def on_modified(self, event):
        print(f"-> {event.src_path} has been modified <-")

    def on_moved(self, event):
        print(f"-> {event.src_path} has been moved <-")

eventhandler = FileEventHandler()
observer = Observer()
observer.schedule(eventhandler, from_dir, recursive=True)
observer.start()

try:

    while True:
        time.sleep(2)
        print("running..")

except KeyboardInterrupt:

    print("stopped")
    observer.stop()