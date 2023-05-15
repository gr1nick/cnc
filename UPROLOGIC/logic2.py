import re
import window
import mmap

def logic(file_name, offset_c, offset_x, offset_y):
    with open(file_name, 'r') as f_upro:
        #with mmap.mmap(upro.fileno(), length=0, access=mmap.ACCESS_READ) as upro_m:
        upro = f_upro.readlines()
        for line in upro:

            x_fin = []
            y_fin = []
            x_fin_str = ''
            y_fin_str = ''
            line_replace = line
            x_re_find = ''.join(re.findall('([X]\d+\.\d+)', line))
            x_str = x_re_find[1:]

            y_re_find = ''.join(re.findall('([Y]\d+\.\d+)', line))
            y_str = (y_re_find[1:])

            len_x_find = len(x_re_find)
            len_y_find = len(y_re_find)

            if len_x_find > 0:

                for i in range(1, offset_c + 1):

                    x_fin.append('X' + str(round((float(x_str) + offset_x * i), 3)))

            if len_y_find > 0:

                for i in range(1, offset_c + 1):

                    y_fin.append('Y' + str(round((float(y_str) + offset_y * i), 3)))

#///////////////////////////////////////////////////////////////////////
            for i in range(1, offset_c + 1):
                if len_x_find > 0:
                    line_replace = line.replace(x_re_find, str(x_fin[i-1]))
                if len_y_find > 0:
                    line_replace = line_replace.replace(y_re_find, str(y_fin[i-1]))
                write_to_file(line_replace, i)

def write_to_file(line, count = 1):
    import mmap
    from test import file_name#test
    fl_name = ''.join(re.findall('([\/]\w+\.[t][a][p])', file_name))
    # print(fl_name)
    new_file_name = fl_name[1:(-4)] + '_' + 'offset' + str(count) + '.tap'
    len_fl_name = len(fl_name[1:])
    path_new_file = file_name[:-len_fl_name]
    # print(fl_name)
    '''with open(path_new_file + new_file_name, 'a') as new_file:
        new_file.write(line[:-1])'''

    with open(path_new_file + new_file_name, 'a') as new_file:
        new_file.write(line)
