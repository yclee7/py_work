from tkinter import *
from numpy import left_shift

from sqlalchemy import column


top = Tk()
top.title("GUI 코딩 테스트")
#top.resizable(False, False)
top.resizable(True, True)
#top.configure(background='gray')
top.geometry("640x480")

chkvar = IntVar()
chkbox = Checkbutton(top, text="오늘하루 보지 않기", variable=chkvar)
chkbox.select()  # 자동 선택
chkbox.place(x = 5, y = 10)
#chkbox.pack(pady = 1,padx = 1)

#chkbox.pack(side="left")
#chkbox.grid(row = 1, column = 1)

chkvar2 = IntVar()
chkbox2 = Checkbutton(top, text="일주일동안 보지 않기", variable=chkvar2)
chkbox2.deselect() # 선택 해제
chkbox2.place(x = 5, y = 30)
#chkbox2.pack()

textcont = StringVar()
#display = Entry(top, width=28, textvariable=textcont)
display = Text(top, width=30, height=10)
display.place(x = 5, y = 50)
#display.pack()
#display.grid(row = 6, column = 1)

def btncmd():
    print(chkvar.get()) # 체크해제 : 0,  체크 : 1
    print(chkvar2.get())
    result=display.get("1.0","end")
    print(result)

btn = Button(top, text="클릭", command=btncmd)
#btn.pack()
btn.place(x = 5, y = 190)


#display.grid(row = 0, column = 0)
#chkbox.grid(row=3, column=0)
#chkbox2.grid(row=4,  column=0)
#btn.grid(row=5, column=0)


top.mainloop()