from tkinter import *
import os
from tkinter.filedialog import *


top = Tk()
top.title("계산기")
top.resizable(False, False)
top.configure(background='blue')
top.geometry("210x230")


def cal(e):
    val = Entry.get(display)
    result = eval(val)
    display.delete(0,END)
    display.insert(0,result)

def clear(pos):
    display.delete(0,END)


def b_press(val):
    display.insert("end",val)

def ce():
    ms = Entry.get(display)
    x = ''
    for i in range(len(ms)-1):
        x+=ms[i]

    display.delete(0,END)
    display.insert(0,x)

def m_cal():
    my = Entry.get(display)
    mc = 12900 *int(my) *0.95
    display.delete(0,END)
    display.insert(0,mc)

def ver():
    my = Entry.get(display)
    v = int(my) * -1
    display.delete(0,END)
    display.insert(0,v)
  
   

display = Entry(top, width=28, justify="right")
display.focus_set()

b_my = Button(top, text='M', width=5, command = m_cal)
b_c = Button(top, text='C', width=5, command = lambda:clear(END))
b_ce = Button(top, text = 'CE', width=5, command = ce)
b_e = Button(top, text='=', width=5, command = cal)



b_1 = Button(top, text = '1', width=5, command = lambda:b_press('1'))
b_2 = Button(top, text = '2', width=5, command = lambda:b_press('2'))
b_3 = Button(top, text = '3', width=5, command = lambda:b_press('3'))
b_a = Button(top, text = '+', width=5, command = lambda:b_press('+'))

b_4 = Button(top, text = '4', width=5, command = lambda:b_press('4'))
b_5 = Button(top, text = '5', width=5, command = lambda:b_press('5'))
b_6 = Button(top, text = '6', width=5, command = lambda:b_press('6'))
b_s = Button(top, text = '-', width=5, command = lambda:b_press('-'))

b_7 = Button(top, text = '7', width=5, command = lambda:b_press('7'))
b_8 = Button(top, text = '8', width=5, command = lambda:b_press('8'))
b_9 = Button(top, text = '9', width=5, command = lambda:b_press('9'))
b_m = Button(top, text = '*', width=5, command = lambda:b_press('*'))

b_0 = Button(top, text = '0', width=5, command = lambda:b_press('0'))
b_v = Button(top, text = '+/-', width=5, command = ver)
b_p = Button(top, text = '.', width=5, command = lambda:b_press('.'))
b_d = Button(top, text = '/', width=5, command = lambda:b_press('/'))



display.grid(row = 0, column = 0, columnspan=4, pady=10, padx=4)

b_my.grid(row=1, column=0, pady=3)
b_c.grid(row=1,  column=1)
b_ce.grid(row=1, column=2)
b_e.grid(row=1,  column=3)

b_1.grid(row=2, column=0, pady=3)
b_2.grid(row=2, column=1)
b_3.grid(row=2, column=2)
b_a.grid(row=2, column=3)

b_4.grid(row=3, column=0, pady=3)
b_5.grid(row=3, column=1)
b_6.grid(row=3, column=2)
b_s.grid(row=3, column=3)


b_7.grid(row=4, column=0, pady=3)
b_8.grid(row=4, column=1)
b_9.grid(row=4, column=2)
b_m.grid(row=4, column=3)

b_0.grid(row=5, column=0, pady=3)
b_v.grid(row=5, column=1)
b_p.grid(row=5, column=2)
b_d.grid(row=5, column=3)


top.bind('<Return>', cal)

top.mainloop()
