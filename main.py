import os
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import time


def instant_shutdown():
    confirm = messagebox.askyesno("Confirmation", "Do you really want to shut down the PC immediately?")
    if confirm:
        os.system("shutdown /s /t 0")

def shutdown_timer():
    try:
        minutes = int(entry.get())
        seconds = minutes * 60
        messagebox.showinfo("Shutdown Timer", f"The PC will shut down in {minutes} minutes.")
        os.system(f"shutdown /s /t {seconds}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

def cancel_shutdown():
    os.system("shutdown /a")
    messagebox.showinfo("Cancellation", "The scheduled shutdown has been canceled.")

root = tk.Tk()
root.title("Shutdown Timer by Spaghett21")
root.geometry("300x200")

tk.Label(root, text="Shtudown Timer (Minutes:)").pack(pady=5)
entry = tk.Entry(root)
entry.pack(pady=5)

tk.Button(root, text="Shut Down Now", command=instant_shutdown, bg="red", fg="white").pack(pady=5)
tk.Button(root, text="Set Timer", command=shutdown_timer, bg="blue", fg="white").pack(pady=5)
tk.Button(root, text="Cancel Shutdown", command=cancel_shutdown, bg="green", fg="white").pack(pady=5)


root.mainloop()


