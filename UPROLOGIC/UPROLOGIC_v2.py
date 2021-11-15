import re
from tkinter import *
import tkinter as tk
from tkinter import filedialog as fd
import time

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

def write_to_file(line, count = 1):
    fl_name = ''.join(re.findall('([\/]\w+\.[t][a][p])', file_name))
    # print(fl_name)
    new_file_name = fl_name[1:(-4)] + '_' + 'offset' + str(count) + '.tap'
    len_fl_name = len(fl_name[1:])
    path_new_file = file_name[:-len_fl_name]
    # print(fl_name)
    with open(path_new_file + new_file_name, 'a') as new_file:
        new_file.write(line)
    
def clicked():
    lbl_status.configure(text = 'Старт')
    X = int(enter_x.get() or 0)
    Y = int(enter_y.get() or 0)
    C = int(enter_c.get() or 1)
    t0 = time.time()
    # print(file_name)
# -----------------------------------------------------------
    with open(file_name, 'r') as upro:
        for line in upro:

            # y_float = 0
            x_fin = []
            y_fin = []
            x_fin_str = ''
            y_fin_str = ''
            line_replace = line
            # x_float = 0
            # line_decode = line.decode()
            # print('++++++++++')
            # print(line)
            x_re_find = ''.join(re.findall('([X]\d+\.\d+)', line))
            x_str = x_re_find[1:]

            y_re_find = ''.join(re.findall('([Y]\d+\.\d+)', line))
            y_str = (y_re_find[1:])

            len_x_find = len(x_re_find)
            len_y_find = len(y_re_find)

            if len_x_find > 0:
                                
                # x_float = float(x_str)
                
                # x_fin = [ round((float(x_str) + X * c), 3) for c in range(1, C+1)]
                for i in range(1, C + 1):
                    
                    x_fin.append('X' + str(round((float(x_str) + X * i), 3)))
                    # x_fin[i-1] = 'X' + str(x_fin[i-1])
                    
                
                # x_fin_str ='X' + str(x_fin)

            if len_y_find > 0:
                
                # y_float = float(y_str)
                
                # y_fin = [round((float(y_str) + Y * c), 3) for c in range(1, C+1)]
                for i in range(1, C + 1):
                    
                    y_fin.append('Y' + str(round((float(y_str) + Y * i), 3)))
                    # y_fin[i-1] = 'Y' + str(y_fin[i-1])
                    
                
                
                # y_fin_str ='Y'+ str(y_fin)
#///////////////////////////////////////////////////////////////////////
            
            
            # print(line_replace)
            for i in range(1, C + 1):
                if len_x_find > 0:
                    line_replace = line.replace(x_re_find, str(x_fin[i-1]))
                if len_y_find > 0:
                    line_replace = line_replace.replace(y_re_find, str(y_fin[i-1]))
                write_to_file(line_replace, i)
                
                
    t1 = time.time() -t0
    lbl_status.configure(text = t1)
# -----------------------------------------------------------

btn = Button(window, text="Старт", command = clicked)
btn.grid(column=2, row=5)
window.mainloop()
