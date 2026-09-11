# ⌨️ Simple Educational Keylogger

A simple **Python-based educational keylogger** built with **Tkinter** to demonstrate keyboard event handling, GUI development, file logging, and timestamp-based activity tracking.

> ⚠️ **Educational Use Only:** This project is intentionally limited to recording keyboard input **inside its own application window/text area**. It does not implement system-wide or background keylogging.

---

## 🚀 Features

* 🖥️ Simple graphical user interface using Tkinter
* ▶️ Start and stop logging controls
* ⌨️ Records key presses inside the application's text area
* 📝 Saves recorded keys to `keylog.txt`
* 🕒 Records the timestamp when logging starts
* 🔤 Identifies common special keys such as:

  * Space
  * Enter
  * Backspace
  * Tab
  * Escape
* 📊 Displays the current logging status
* 🐍 Built entirely with Python standard libraries

The application provides a text area, Start Logging button, Stop Logging button, and status indicator.

---

## 🛠️ Technologies Used

* **Python 3**
* **Tkinter** — GUI development
* **datetime** — Timestamp generation
* **File I/O** — Saving keyboard events to a text file

---

## 📂 Project Structure

```text
Simple-Keylogger/
│
├── keylog.py
├── keylog.txt          # Created automatically when logging starts
└── README.md
```

---

## ⚙️ Installation

### 1. Install Python

Make sure Python 3 is installed on your system.

Check your Python version:

```bash
python --version
```

### 2. Clone the repository

```bash
git clone https://github.com/prince-jha8533/Simple-Keylogger.git
```

### 3. Navigate to the project

```bash
cd Simple-Keylogger
```

---

## ▶️ Usage

Run the application:

```bash
python keylog.py
```

The application will open a GUI window titled:

```text
Simple Keylogger
```

### Start Logging

Click:

```text
Start Logging
```

The status changes to:

```text
Status: Logging Started
```

A logging-start entry containing the current date and time is written to `keylog.txt`.

### Enter Text

Type inside the application's text box.

The program captures the keyboard events generated within that text area.

### Stop Logging

Click:

```text
Stop Logging
```

The status changes to:

```text
Status: Logging Stopped
```

A corresponding entry is added to the log file.

---

## ⌨️ Supported Special Keys

The program converts several special keyboard events into readable labels:

| Key       | Recorded As   |
| --------- | ------------- |
| Space     | `[SPACE]`     |
| Enter     | `[ENTER]`     |
| Backspace | `[BACKSPACE]` |
| Tab       | `[TAB]`       |
| Escape    | `[ESC]`       |

Other characters are recorded using their keyboard event character, while unidentified keys are represented using their key symbol.

---

## 📄 Log File

The application stores keyboard input in:

```text
keylog.txt
```

The file is opened in **append mode**, allowing new logging sessions to be added without immediately overwriting previous entries.

Example:

```text
----- Logging Started -----
Time: 2026-09-11 21:30:15
Hello[SPACE]World[ENTER]

----- Logging Stopped -----
```

---

## 🧠 How It Works

The application creates a Tkinter window and initializes the `SimpleKeylogger` class.

The text area is bound to the Tkinter:

```python
<KeyPress>
```

event.

When a key is pressed:

```text
Key Press
    ↓
Check Logging Status
    ↓
Identify Key
    ↓
Convert Special Key if Required
    ↓
Write Key to keylog.txt
    ↓
Display Key in Terminal
```

The application only processes the event when logging is enabled.

---

## 🔐 Security & Ethical Considerations

Keylogging technology can be abused to capture sensitive information such as:

* Passwords
* Personal messages
* Authentication codes
* Financial information
* Private data

Therefore, this project should only be used in **authorized environments**, such as:

* Cybersecurity education
* Personal laboratory environments
* Security research
* Controlled demonstrations

This implementation is intentionally restricted to keyboard input within its own text area and does not provide covert system-wide monitoring.

---

## ⚠️ Disclaimer

This project is created strictly for **educational and authorized cybersecurity learning purposes**.

Do not use keylogging software to monitor another person's device or capture their information without explicit authorization.

The author is not responsible for misuse of this project.

---
