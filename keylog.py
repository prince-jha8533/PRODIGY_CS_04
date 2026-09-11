import tkinter as tk
from datetime import datetime


class SimpleKeylogger:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Keylogger")
        self.root.geometry("600x450")

        self.logging = False
        self.log_file = "keylog.txt"

        # Title
        title = tk.Label(
            root,
            text="Simple Keylogger",
            font=("Arial", 20, "bold")
        )
        title.pack(pady=15)

        # Information
        info = tk.Label(
            root,
            text="Educational keylogger - records keys in this window only",
            font=("Arial", 10)
        )
        info.pack(pady=5)

        # Text area
        self.text_area = tk.Text(
            root,
            height=12,
            width=60,
            font=("Arial", 12)
        )
        self.text_area.pack(pady=15)

        # Start button
        start_button = tk.Button(
            root,
            text="Start Logging",
            width=15,
            command=self.start_logging
        )
        start_button.pack(pady=5)

        # Stop button
        stop_button = tk.Button(
            root,
            text="Stop Logging",
            width=15,
            command=self.stop_logging
        )
        stop_button.pack(pady=5)

        # Status
        self.status = tk.Label(
            root,
            text="Status: Not Logging",
            font=("Arial", 10, "bold")
        )
        self.status.pack(pady=10)

        # Detect key presses inside the text box
        self.text_area.bind("<KeyPress>", self.key_pressed)

    def start_logging(self):
        self.logging = True

        self.status.config(
            text="Status: Logging Started"
        )

        with open(self.log_file, "a", encoding="utf-8") as file:
            file.write("\n")
            file.write("----- Logging Started -----\n")
            file.write(
                "Time: "
                + datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                + "\n"
            )

    def stop_logging(self):
        self.logging = False

        self.status.config(
            text="Status: Logging Stopped"
        )

        with open(self.log_file, "a", encoding="utf-8") as file:
            file.write("\n")
            file.write("----- Logging Stopped -----\n")

    def key_pressed(self, event):
        # Don't record anything when logging is stopped
        if not self.logging:
            return

        # Identify special keys
        if event.keysym == "space":
            key = "[SPACE]"

        elif event.keysym == "Return":
            key = "[ENTER]"

        elif event.keysym == "BackSpace":
            key = "[BACKSPACE]"

        elif event.keysym == "Tab":
            key = "[TAB]"

        elif event.keysym == "Escape":
            key = "[ESC]"

        else:
            key = event.char

            if key == "":
                key = "[" + event.keysym + "]"

        # Save the key to the log file
        with open(self.log_file, "a", encoding="utf-8") as file:
            file.write(key)

        print("Key pressed:", key)


# Start the application
root = tk.Tk()

app = SimpleKeylogger(root)

root.mainloop()