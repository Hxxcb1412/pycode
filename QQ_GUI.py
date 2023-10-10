from tkinter import messagebox
import tkinter as tk


def login():
    username = entry_username.get()
    password = entry_password.get()

    # Username and password authentication
    if username=="admin" and password=="123456":
        messagebox.showinfo("success", "welcome back!")
    else:
        messagebox.showinfo("fail", "please check your password!")


# main window
window = tk.Tk()
window.title("QQ login")
window.geometry("300x150")

# Create username and password label and input fields
label_username = tk.Label(window, text="username")
label_username.pack()

entry_username = tk.Entry(window)
entry_username.pack()

#
label_password = tk.Label(window, text="password")
label_password.pack()

entry_password = tk.Entry(window, show="*")
entry_password.pack()

# Create a login button
button_login = tk.Button(window, text="login", command=login)
button_login.pack()

window.mainloop()