from tkinter import *
from tkinter import messagebox

frame = Tk()
frame.geometry('400x400')
txt1 = Entry(frame, width=20, justify=RIGHT)
txt1.place(relx=0.3, rely=0.3, anchor=W)
txt2 = Entry(frame, width=20, justify=RIGHT)
txt2.place(relx=0.3, rely=0.4, anchor=W)
txt3 = Label(frame, width=20)
txt3.place(relx=0.3, rely=0.5, anchor=W)


def clk1():
    a = txt1.get()
    b = txt2.get()
    if a == '' or b == '':
        messagebox.showwarning('warning', 'value missing')
    a = int(a)
    b = int(b)
    c = a + b
    txt3.configure(text=c)


def clk2():
    a = txt1.get()
    b = txt2.get()
    if a == '' or b == '':
        messagebox.showwarning('warning', 'value missing')
    a = int(a)
    b = int(b)
    c = a - b
    txt3.configure(text=c)


def clk3():
    a = txt1.get()
    b = txt2.get()
    if a == '' or b == '':
        messagebox.showwarning('warning', 'value missing')
    a = int(a)
    b = int(b)
    c = a * b
    txt3.configure(text=c)


def clk4():
    a = txt1.get()
    b = txt2.get()
    a = int(a)
    b = int(b)
    if a == '' or b == '':
        messagebox.showwarning('warning', 'values missing')
    c = a / b
    txt3.configure(text=c)


btn1 = Button(frame, text='+', command=clk1)
btn1.place(relx=0.3, rely=0.6, anchor=W)
btn2 = Button(frame, text='-', command=clk2)
btn2.place(relx=0.4, rely=0.6, anchor=W)
btn1 = Button(frame, text='*', command=clk3)
btn1.place(relx=0.5, rely=0.6, anchor=W)
btn1 = Button(frame, text='/', command=clk4)
btn1.place(relx=0.6, rely=0.6, anchor=W)
frame.mainloop()
