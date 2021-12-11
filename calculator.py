from tkinter import *
from tkinter import ttk
import math
import sys

screen = Tk()
screen.title("Calculator")
list_button = [
"7", "8", "9", "+", "*",
"4", "5", "6", "-", "/",
"1", "2", "3",  "=", "xⁿ",
".", "0", "±", "C",
"π", "sin", "cos",
"n!","√2", "Exit"]

# Создаем кнопки.
r = 1
c = 0
for i in list_button:
    rel = ""
    cmd = lambda x=i: calc(x)
    ttk.Button(screen, text=i, command=cmd, width=10).grid(row=r, column=c)
    c += 1
    if c > 4:
        c = 0
        r += 1

# Создаем поле ввода.
calculator_entry = Entry(screen, width=60)
calculator_entry.grid(row=0, column=0, columnspan=5, ipadx=0, ipady=20)
calculator_entry.config(state="normal")

def calc(key):
    if key == "=":
        # Исключаем написание слов.
        valid_char = "+-0123456789.*/)("
        if calculator_entry.get()[0] not in valid_char:
            calculator_entry.insert(END, "***Символ не является числом!***")
        # Считаем результат.
        else:
            result = eval(calculator_entry.get())
            calculator_entry.delete(0, END)
            calculator_entry.insert(END, str(result))
    # Очищаем поле ввода.
    elif key == "C":
        calculator_entry.delete(0, END)
    elif key == "±":
        if calculator_entry.get()[0] == "-":
            calculator_entry.delete(0)
        else:
            calculator_entry.insert(0, "-")
    # Вывод числа Пи.
    elif key == "π":
        calculator_entry.insert(END, math.pi)
    elif key == "n!":
        result = str(math.factorial(int(calculator_entry.get())))
        calculator_entry.delete(0, END)
        calculator_entry.insert(END, result)
    elif key == "√2":
        result = str(math.sqrt(int(calculator_entry.get())))
        calculator_entry.delete(0, END)
        calculator_entry.insert(END, result)
    elif key == "sin":
        result = str(math.sin(float(calculator_entry.get())))
        calculator_entry.delete(0, END)
        calculator_entry.insert(END, result)
    elif key == "cos":
        result = str(math.cos(float(calculator_entry.get())))
        calculator_entry.delete(0, END)
        calculator_entry.insert(END, result)
    elif key == "xⁿ":
        calculator_entry.insert(END, "**")
    elif key == "Exit":
        screen.after(1, screen.destroy)
        sys.exit
    else:
        if "=" in calculator_entry.get():
            calculator_entry.delete(0, END)
        calculator_entry.insert(END, key)

screen.mainloop()
