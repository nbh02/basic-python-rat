# 🕶️ ShadowRAT – Basic Python Remote Access Tool for beginners (Educational)

ShadowRAT is a simple Python-based Remote Access Tool (RAT) designed for **educational purposes only**. It allows a user to remotely interact with another machine through a socket connection and execute various commands such as taking screenshots, typing text, moving the mouse, locking the screen, and more.

---

## 📁 Files in This Repository

- `client.py` – Run this script on the **target/victim machine**
- `server.py` – Run this script on the **admin/attacker machine**

---

## ⚙️ How It Works

ShadowRAT uses basic **TCP socket programming** in Python. The client connects to the server, waits for commands, and executes them on the victim machine. The server sends commands and receives output.

---

## 🚀 Setup & Usage

### 1. Install Requirements

On the **client machine**, install required packages:

```bash
pip install pyautogui
