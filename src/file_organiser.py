import os
import sys
import time
import logging
import shutil as sh
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

"""
Linux File Organiser Script.

This script monitors a specified directory and automatically organizes its files into folders based on their file extensions.
If a file has no extension, it will be moved to a folder named 'None'.

Usage:
    python3 file_organiser.py <path_to_directory>

Example:
    python3 file_organiser.py /home/user/Downloads

:author: Siyabonga Madondo
:version: 17/06/2024
"""

class MovingEventHandler(FileSystemEventHandler):
    """
    Handles file system events and moves files into respective folders based on their extensions.
    This class overrides the on_modified method to move files when the directory is modified.
    """

    def move_files(self) -> None:
        """
        Organizes files in the target directory by moving them into subfolders named after their extensions.
        If a file has no extension, it will be moved to a folder named 'None'.
        :return: None
        """
        # Obtaining a list of files in the given target directory.
        target_folder = sys.argv[1]
        files = os.listdir(target_folder)

        # Iterating through the files in the target directory.
        for file in files:
            # Skip if the current entry is a directory.
            if os.path.isdir(os.path.join(target_folder, file)):
                continue  

            # Split the file name from its extension.
            filename, file_extension = os.path.splitext(file)  
            # Remove the dot from the file extension and capitalize the extention name.
            file_extension = file_extension[1:].title()

            # If the file extension is empty, add the extension 'None' to the file.
            if not file_extension:
                file_extension = "None"

            # Define the destination folder for the file.
            destination_folder = os.path.join(target_folder, file_extension)

            # If the folder exists, move the file to the folder, else create a new folder with the extension name.
            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)

            # Move the file to the destination folder. 
            sh.move(os.path.join(target_folder, file), os.path.join(destination_folder, file))

    def on_modified(self, event):
        """
        Method that overrides the on_modified method to move files when the directory is modified.
        :param event: The event that triggered the method.
        :return: None
        """
        self.move_files()

if __name__ == "__main__":
    """
    Monitor the target directory for changes and move files to their respective folders based on their extensions using the Watchdog API.
    Source: https://pythonhosted.org/watchdog/quickstart.html#a-simple-example
    """
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    path = sys.argv[1]
    event_handler = MovingEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
