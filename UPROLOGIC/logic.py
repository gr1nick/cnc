import re
import window

def logic(file_name, repeat, offset_x, offset_y):
    with open(file_name, 'r') as f_upro:
        upro = f_upro.read().split('\n')
        pattern = '([A-Z][^A-Z]+)'
        pattern_xy = '([X,Y][^A-Z]+)'
        fin_upro = upro.copy()[:-3] 
        safe_pos ='G0'+''.join(re.findall(pattern_xy, upro[2]))
        for c in range(1, repeat + 1): 

            for line in upro[:-2]:
                re_find = (re.findall(pattern, line))
                g_dict = {k[0]:k[1:] for k in re_find}
                g_dict_up = g_dict.copy()
                
                if 'X' in g_dict:
                    g_dict_up.update(X=round(offset_x * c + float(g_dict['X']),3))
                if 'Y' in g_dict:
                    g_dict_up.update(Y=round(offset_y * c + float(g_dict['Y']),3))
                line_replace = [k + str(i) for k,i in g_dict_up.items()] 
                fin_upro.append(''.join(line_replace))

        fin_upro.append(safe_pos)
        fin_upro.append('G0X0Y0')
        fin_upro.append('M30')
        write_upro = '\n'.join(fin_upro)
        write_to_file(write_upro, 2)

def write_to_file(line, count = 1):

    fl_name = ''.join(re.findall('([\/]\w+\.[t][a][p])', file_name))
    # print(fl_name)
    new_file_name = fl_name[1:(-4)] + '_' + 'offset' + str(count) + '.tap'
    len_fl_name = len(fl_name[1:])
    path_new_file = file_name[:-len_fl_name]

    with open(path_new_file + new_file_name, 'a') as new_file:
        new_file.write(line)
logic(file_name, repeat, offset_x, offset_y)
