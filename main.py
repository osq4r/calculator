# Import Tkinter
from tkinter import *


def add_digit(digit):
    value = calc.get() + str(digit)  # Добавляем цифру в виде строки к другой и записываем в переменную value
    calc.delete(0, END)              # Очищаем поле
    calc.insert(0, value)            # Добавляем не цифру а значение

def add_operator(operator):
    value = calc.get() + operator
    calc.delete(0, END)
    calc.insert(0, value)

def calculate():
    expression = calc.get()
    result = eval(expression)
    calc.delete(0, END)
    calc.insert(0, result)

def clear():
    calc.delete(0, END)

win = Tk()                          # Создаём окошко
win.geometry("400x300")             # Задаём размер
win['bg'] = 'blue'                  # Цвет заднего фона
win.title = "Calculator"            # Тайтл окна

# Добавляем поле ввода
calc = Entry(win, justify=RIGHT, font=('Arial', 15))

# Задаём местоположение
# Columnspan добавляем чтобы длина поля была по ширине кнопок
calc.grid(row=0, column=0, columnspan=3, stick='we') 

# Кнопки
Button(text='1', command=lambda : add_digit(1)).grid(row=1, column=0, stick='wens', padx=5, pady=5)
Button(text='2', command=lambda : add_digit(2)).grid(row=1, column=1, stick='wens', padx=5, pady=5)
Button(text='3', command=lambda : add_digit(3)).grid(row=1, column=2, stick='wens', padx=5, pady=5)
Button(text='4', command=lambda : add_digit(4)).grid(row=2, column=0, stick='wens', padx=5, pady=5)
Button(text='5', command=lambda : add_digit(5)).grid(row=2, column=1, stick='wens', padx=5, pady=5)
Button(text='6', command=lambda : add_digit(6)).grid(row=2, column=2, stick='wens', padx=5, pady=5)
Button(text='7', command=lambda : add_digit(7)).grid(row=3, column=0, stick='wens', padx=5, pady=5)
Button(text='8', command=lambda : add_digit(8)).grid(row=3, column=1, stick='wens', padx=5, pady=5)
Button(text='9', command=lambda : add_digit(9)).grid(row=3, column=2, stick='wens', padx=5, pady=5)
Button(text='0', command=lambda : add_digit(0)).grid(row=4, column=1, stick='wens', padx=5, pady=5)

Button(text='+', command=lambda: add_operator('+')).grid(row=1, column=3, stick='wens', padx=5, pady=5)
Button(text='-', command=lambda: add_operator('-')).grid(row=2, column=3, stick='wens', padx=5, pady=5)
Button(text='*', command=lambda: add_operator('*')).grid(row=3, column=3, stick='wens', padx=5, pady=5)
Button(text='/', command=lambda: add_operator('/')).grid(row=4, column=3, stick='wens', padx=5, pady=5)
Button(text='=', command=calculate).grid(row=4, column=2, stick='wens', padx=5, pady=5)
Button(text='C', command=clear).grid(row=4, column=0, stick='wens', padx=5, pady=5)

# Распределяет столбцы по мин. ширине
win.grid_columnconfigure(0, minsize=60)     
win.grid_columnconfigure(1, minsize=60)
win.grid_columnconfigure(2, minsize=60)
win.grid_columnconfigure(3, minsize=60)

# Распределяет строки по мин. ширине
win.grid_rowconfigure(1, minsize=60)     
win.grid_rowconfigure(2, minsize=60)
win.grid_rowconfigure(3, minsize=60)
win.grid_rowconfigure(4, minsize=60)

win.mainloop()
