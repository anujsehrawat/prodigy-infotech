import tkinter as tk
from tkinter import messagebox
import re

def check_pw():
    pw = entry.get()
    
    # Password strength conditions
    if len(pw) < 8:
        result.config(text="Password must be at least 8 characters long.", fg="red")
    elif not re.search("[A-Z]", pw):
        result.config(text="Must contain one uppercase letter.", fg="red")
    elif not re.search("[a-z]", pw):
        result.config(text="Must contain one lowercase letter.", fg="red")
    elif not re.search("[0-9]", pw):
        result.config(text="Must contain one number.", fg="red")
    elif not re.search("[@#$%^&*!]", pw):
        result.config(text="Must contain one special char (@#$%^&*!).", fg="red")
    else:
        result.config(text="Password is strong!", fg="green")

# Main window
root = tk.Tk()
root.title("Password Checker")
root.geometry("400x250")
root.config(bg="lightblue")

# Title
title = tk.Label(root, text="Password Checker", font=("Helvetica", 16, "bold"), bg="lightblue")
title.pack(pady=20)

# Password Entry
entry_label = tk.Label(root, text="Enter your password:", font=("Helvetica", 12), bg="lightblue")
entry_label.pack(pady=5)

entry = tk.Entry(root, width=30, show="*")
entry.pack(pady=10)

# Check Button
check_btn = tk.Button(root, text="Check", command=check_pw, font=("Helvetica", 12))
check_btn.pack(pady=10)

result = tk.Label(root, text="", font=("Helvetica", 12), bg="lightblue")
result.pack(pady=10)

root.mainloop()
