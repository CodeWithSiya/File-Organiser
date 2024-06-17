# Makefile to run the file organizer script with a specified directory path in the background
# Directory to be monitored must be provided
DIR?=

# Command to run the application in the background.
run:
# Check if the DIR variable is set, if not, print an error and exit
ifndef DIR
	$(error Error: DIR variable not set. Usage: make run DIR=your_directory_path)
else
	# For Unix systems, use '&' to run the script in the background.
	python3 src/file_organiser.py $(DIR) &
endif

# Command to stop the application.
stop:
# For Unix systems, use 'pkill' to stop the script.
	pkill -f file_organiser.py