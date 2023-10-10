import tkinter as tk
from tkinter import messagebox

def calc_lcm():
    try:
        num1 = int(entry_num1.get())
        num2 = int(entry_num2.get())

        lcm = num1 * num2 // gcd(num1, num2)
        text_res.config(state="normal")
        text_res.delete('1.0', tk.END)
        text_res.insert(tk.END, str(lcm))
        text_res.config(state="disable")

    except ValueError:
        messagebox.showerror("error", "Please enter a vaild integer.")

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# main window
window = tk.Tk()
window.title("Least common multiple calculator")

#
label_num1 = tk.Label(window, text="num1:")
label_num1.pack()
entry_num1 = tk.Entry(window)
entry_num1.pack()

label_num2 = tk.Label(window, text="num2:")
label_num2.pack()
entry_num2 = tk.Entry(window)
entry_num2.pack()

#
button_calc = tk.Button(window, text="calc", command=calc_lcm)
button_calc.pack()

#
text_res = tk.Text(window, width=20, height=1, state="disable")
text_res.pack()

window.mainloop()

