from tkinter import *
import tkinter as tk
from tkinter import filedialog as fd
import time
import re
import logic

def interface():
    window = Tk()
    window.title("UPROLOGIC")
    window.geometry('700x250')

    lbl_x = Label(window, text="введите смещение по Х: ")
    lbl_x.grid(column=1, row=0)
    enter_x = Entry(window, width = 10)
    enter_x.grid(column=2, row=0)

    lbl_y = Label(window, text="введите смещение по У: ")
    lbl_y.grid(column=1, row=1)
    enter_y = Entry(window, width = 10)
    enter_y.grid(column=2, row=1)

    lbl_c = Label(window, text="колличество повторений: ")
    lbl_c.grid(column=1, row=2)
    enter_c = Entry(window, width = 10)
    enter_c.grid(column=2, row=2)

    lbl_status = Label(window, text = 'Ожидание данных...')
    lbl_status.grid(column = 1, row = 5)

    lbl_status_open = Label(window, text = 'name.tap')
    lbl_status_open.grid(column = 3, row = 4)

    def callback():
        global file_name
        file_name = fd.askopenfilename()
        lbl_status_open.configure(text = file_name)
        return file_name

    btn_open = Button(window, text='открыть файл',command=callback)
    btn_open.grid(column=1, row=4)

######write_to_file

#####
    def clicked():
        lbl_status.configure(text = 'Старт')
        offset_x = int(enter_x.get() or 0)
        offset_y = int(enter_y.get() or 0)
        offset_c = int(enter_c.get() or 1)
        t0 = time.time()
        # print(file_name)
    # -----------------------------------------------------------
        print(file_name)
        logic.logic(file_name, offset_c, offset_x, offset_y)

        t1 = time.time() -t0
        lbl_status.configure(text = t1)
    # -----------------------------------------------------------

    btn = Button(window, text="Старт", command = clicked)
    btn.grid(column=2, row=5)
    window.mainloop()



#btn_open = Button(window, text='открыть файл',command=callback)
#btn_open.grid(column=1, row=4)
