from tkinter import *
from numpy import e
#from numpy import left_shift

#from sqlalchemy import column

import pandas as pd

import matplotlib.pyplot as plt
from regex import A, B

#plt.plot([1, 2, 3, 4])



data = {'name' : ['Mark', 'Jane', 'Chris', 'Ryan'],
         'age' : [33, 32, 44, 41],
         'score' : [91.3, 83.4, 77.5, 87.7]}



#plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
#plt.axis([0, 6, 0, 20])


top = Tk()
top.title("GUI 코딩 테스트")
#top.resizable(False, False)
top.resizable(True, True)
#top.configure(background='gray')
top.geometry("640x550")

chkvar = IntVar()
chkbox = Checkbutton(top, text="오늘하루 보지 않기", variable=chkvar)
chkbox.select()  # 자동 선택
#chkbox.place(x = 5, y = 10)
#chkbox.pack(pady = 1,padx = 1)

#chkbox.pack(side="left")
chkbox.grid(row = 0, column = 0, sticky=W)

chkvar2 = IntVar()
chkbox2 = Checkbutton(top, text="일주일동안 보지 않기", variable=chkvar2)
chkbox2.deselect() # 선택 해제
#chkbox2.place(x = 5, y = 40)
#chkbox2.pack()
#chkbox2.grid(row = 2, column = 1, sticky=W+E+N+S)
chkbox2.grid(row = 1, column = 0, sticky=W)

#textcont = StringVar()
#display = Entry(top, width=28, textvariable=textcont)
edit1 = Text(top, width=40, height=10)
#edit1.place(x = 5, y = 70)
edit1.grid(row = 2, column = 0, rowspan=10, sticky=W)
#display.pack()
#display.grid(row = 6, column = 1)

label1 = Label(top, width=60, height=20, text = "출력")
label1.configure(background="white")
#label1.place(x = 5, y = 320)
label1.grid(row = 14, column=0)


def btncmd():
    print(chkvar.get()) # 체크해제 : 0,  체크 : 1
    print(chkvar2.get())
    result=edit1.get("1.0","end")
    print(result)
    label1.configure(text=str(result), anchor=W)
    

btn = Button(top, text="클릭", command=btncmd)
#btn.pack()
#btn.place(x = 5, y = 220)
btn.grid(row=12, column=0, sticky=W)

def btncmd2():
    df = pd.DataFrame(data)
    label1.configure(text=str(df), anchor=W)
    #df.plot(kind = 'kde')
    #plt.show()

btn1 = Button(top, text="데이터 출력", command=btncmd2)
#btn.pack()
#btn1.place(x = 55, y = 220)
btn1.grid(row=12, column=0, sticky=E)


def sel_sort(a):
    n = len(a)
    #v=0
    k = []
    #k.append([])
    for i in range(0, n - 1):
        min_idx = i
        b =[]
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
        print(a)     # 정렬 과정 출력하기
        #b = a.copy()
        #k.append(b)
        k.append(a.copy())
        #print(k)
        #v = v+1
    df = pd.DataFrame(k)
    label1.configure(text=str(df), anchor=W)

def btncmd3():
    d = [2,6, 4,9, 5,8,12, 1, 3]
    print(d)
    sel_sort(d)


btn2 = Button(top, text="선택정렬", command=btncmd3)
btn2.grid(row=12, column=1, sticky=E)
 

#display.grid(row = 0, column = 0)
#chkbox.grid(row=3, column=0)
#chkbox2.grid(row=4,  column=0)
#btn.grid(row=5, column=0)


top.mainloop()