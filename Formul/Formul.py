from tkinter import *
from math import sqrt
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter import messagebox

root = Tk() # родительский элемент
root.title("Калькулятор") # устанавливаем название окна
root.minsize(350,350) # устанавливаем минимальный размер окна 
root.resizable(width = True, height = True) # выключаем возможность изменять окно

def solver(a,b,c): #Решает квадратное уравнение и выводит отформатированный ответ, находим дискриминант
    D = b * b - 4 * a * c
    if D > 0:
        x1 = (-b + sqrt(D)) / (2 * a)
        x2 = (-b - sqrt(D)) / (2 * a)
        text = "Дискриминант: %s \n X1: %s \n X2: %s \n" % (D, x1, x2)
    if D == 0:
        a=int(ent2.get())
        x1 = (-b / 2 * a)
        text = "Дискриминант: %s \n X1: %s \n X2: %s \n" % (D, x1, x2)
    else:
        text = "Дискриминант: %s \n Это уравнение не имеет решений" % D 
    return text

def inserter(value): #Вставляет указанное значение в текстовый виджет
    output.delete(0.0, END) 
    output.insert(0.0, value)

def handler(): #Получает содержимое записей и передает результат в область вывода
    try: #проверка, что мы ввели правильные значения
        a_val = float(a.get())
        b_val = float(b.get())
        c_val = float(c.get())
        inserter(solver(a_val, b_val, c_val))
    except ValueError:
        inserter("Проверьте, ввели ли вы 3 значения")

def clear(event): #функция для очищения ячеек после нажатия "решение"
    ud = event.widget
    ud.delete(0, END)

 
frame = Frame(root) # создаем рабочую область
frame.grid()

def knopka(event): #Показывает Формулу по которой идет расчет
    canvas = Canvas(root, height=350, width=350)
    image = Image.open("kartinka.png")
    photo = ImageTk.PhotoImage(image)
    image = canvas.create_image(0, 0, anchor = 'nw',image = photo)
    messagebox.showinfo (" ", "При нажатии на ОК или на крестик формула пропадет!")
    messagebox.showinfo ("Внимание!", canvas.grid(row = 5, columnspan = 8))

a = Entry(frame, width = 3) # поле для ввода первого аргумента уравнения (a)
a.bind("<FocusIn>", clear)
a.grid(row = 1, column = 1, padx = (10,0))
 
a_lab = Label(frame, text = "x ** 2 +").grid(row=1,column=2) # текст после первого аргумента
 
b = Entry(frame, width = 3) # поле для ввода второго аргумента уравнения (b)
b.bind("<FocusIn>", clear)
b.grid(row = 1,column = 3)

b_lab = Label(frame, text= "x +").grid(row = 1, column = 4) # текст после второго аргумента
 
c = Entry(frame, width = 3) # поле для ввода третьего аргумента уравнения (с)
c.bind("<FocusIn>", clear)
c.grid(row = 1, column = 5)

c_lab = Label(frame, text = "= 0").grid(row = 1, column = 6) # текст после третьего аргумента
 
but = Button(frame, text = "Решить", command = handler).grid(row = 1, column = 7, padx = (10,0)) # кнопка решить

but1 = Button(frame, text = "Формула")
but1.bind("<Button-1>", knopka)
but1.grid(row = 2, column = 7, padx = (10,0))
 
output = Text(frame, bg = "lightblue", font = "Arial 12") # место для вывода решения уравнения
output.grid(row = 5, columnspan = 8)


root.mainloop() # запускаем главное окно