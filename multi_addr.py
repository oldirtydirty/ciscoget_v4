'''Multiple Switch Function'''
def multi_addr() -> None:
    '''Multi Address Function'''
    print('''What is the IP address of the Switch?
Multiple switches separate by comma or by range.
Example - 192.168.1.1, 192.168.1.2
Example - 192.168.1.1-5\n''')
    options = input("Input IP addresses: ")
    if ',' in  options:
        options_list = options.split(',')
        lst = [i for i in options_list]
        return lst
    if '-' in options:
        options_list = options.split(".")
        lst = [i.split('-') for i in options_list]
        start,finish = int(lst[3][0]),\
                       int(lst[3][1])
        range_list =  [".".join([options_list[0],
                                 options_list[1],
                                 options_list[2],
                                 str(i)]) for i in range(start,
                                                         finish +1)
                                                         ]
        return range_list
    if "," or "-" not in options:
        single = [options]
        return single
