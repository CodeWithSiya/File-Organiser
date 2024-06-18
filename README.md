# Linux File Organiser Script README

## Overview

This script automates the organization of files in a specified directory by categorizing them into folders based on their file extensions. Files without extensions are moved to a folder named 'None'. The script uses the Watchdog library to monitor the directory for changes and reorganize files accordingl.

## Features

- Monitors a specified directory for changes.
- Automatically organizes files into folders based on their file extensions.
- Creates a 'None' folder for files without extensions.
- Uses the Watchdog library for efficient file system event handling.

## Requirements

- Python 3
- Watchdog Library (`pip install watchdog`)
- Make Utility(`sudo apt-get install make`)

## Usage

### Method 1 - Running directly from the Python script.
Run the script by providing the path to the directory you wish to organize as an argument:
```bash
python3 file_organiser.py /path/to/directory &
```
Example:
```bash
python3 file_organiser.py /home/user/Downloads &
```

### Method 2 - Running using the provided Makefile.
Run the script by using `make run` and providing the path to the directory you wish to organize as an argument:
```bash
make run DIR=/path/to/directory
```
Example:
```bash
make run file_organiser.py DIR=/home/user/Downloads
```
End the script using `make stop`.

## How It Works

1. The script initializes a `MovingEventHandler` class that extends `FileSystemEventHandler`.
2. Upon modification of any file in the specified directory, the `on_modified` method triggers, calling `move_files`.
3. `move_files` iterates over all files in the directory, organizing them into folders named after their file extensions. Files without extensions are placed in a 'None' folder.
4. The script continuously monitors the directory for modifications, reorganizing files as needed.

## Author

- Siyabonga Madondo

## Version

- 17/06/2024

## Credits

This project utilizes the Watchdog library for file system event monitoring. More about Watchdog can be found at [Watchdog Quickstart Guide](https://pythonhosted.org/watchdog/quickstart.html#a-simple-example).

## License

This project is licensed under the MIT License.
