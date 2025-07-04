import tkinter as tk
from tkinter import messagebox

def greet_user():
    name = entry.get()
    messagebox.showinfo("Приветствие", f"Привет, {name}!")


# Создание  окна
window = tk.Tk()
window.title("приветствия")
window.geometry("300x150")

label = tk.Label(window, text="Введите ваше имя:")
label.pack(pady=10)

# Поле ввода
entry = tk.Entry(window)
entry.pack(pady=5)

# Кнопка
button = tk.Button(window, text="Поприветствовать", command=greet_user)
button.pack(pady=10)

window.mainloop()