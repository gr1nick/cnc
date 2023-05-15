my_list = [[1,2,5,4,[1,2,3,[4,3],3],8,3,6]]
def func(my_list):
    for item in my_list:
        if isinstance(item, list):
            for subitem in func(item):
                yield subitem
        else:
            yield item
