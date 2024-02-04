import tkinter as tk
from tkinter import messagebox
import subprocess

def execute_action():
    input_text1 = entry1.get()
    toggle_state = toggle_var.get()
    
    # Your execution logic here
    result = f"Executing with input1: {input_text1}, Toggle state: {'ON' if toggle_state else 'OFF'}"
    
    messagebox.showinfo("Execution Result", result)

    if toggle_state = True:
        subprocess.run("SYN.exe", input_text1)
    else:
        subprocess.run("TCP.exe", input_text1)

def toggle_action():
    if toggle_var.get():
        toggle_button.config(text="SYN scan is: ON")
    else:
        toggle_button.config(text="SYN scan is: OFF")

def exit_application():
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Smasher V1.0")

# Styling
root.geometry("400x200")
root.resizable(False, False)
root.configure(bg='#f0f0f0')

# Create and place widgets
title_label = tk.Label(root, text="Smasher V1.0", font=("Helvetica", 16), bg='#f0f0f0')
title_label.grid(row=0, column=0, columnspan=3, pady=(10, 20), sticky="n")

label1 = tk.Label(root, text="IPV4 Address:", bg='#f0f0f0')
label1.grid(row=1, column=0, padx=(10, 5), sticky="e")
entry1 = tk.Entry(root)
entry1.grid(row=1, column=1, padx=(0, 10), pady=5, sticky="w")

toggle_var = tk.BooleanVar()
toggle_button = tk.Checkbutton(root, text="SYN scan is: OFF", variable=toggle_var, command=toggle_action, bg='#f0f0f0')
toggle_button.grid(row=2, column=0, columnspan=2, pady=(0, 10))

execute_button = tk.Button(root, text="Execute", command=execute_action, bg='#4caf50', fg='white', padx=10)
execute_button.grid(row=3, column=0, columnspan=2, pady=(20, 10))

exit_button = tk.Button(root, text="Exit", command=exit_application, bg='#f44336', fg='white', padx=10)
exit_button.grid(row=0, column=2, sticky="ne", padx=10, pady=(10, 20))

# Start the GUI event loop
root.mainloop()

