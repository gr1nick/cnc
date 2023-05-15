my_file = '1ch8.tap'
def func1(file):
    with open(my_file, 'r') as f_upro:

        upro = f_upro.readlines()
        print(len(upro))
        for i in upro:
            print(i[:-1])
