import logic
import time

file_name = 'C://Users//nick//Documents//project//UPROLOGIC//Test_upro//1ch8.tap'
offset_c = 3
offset_x = 500
offset_y = 300
t1 = time.time()
logic.logic(file_name, offset_c, offset_x, offset_y)
print(time.time() - t1)#time 103.890
