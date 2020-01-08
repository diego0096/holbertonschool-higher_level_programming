|:|:sr/bin/python3
def safe_print_list(my_list=[], x=0):
    t = 0
    try:
        for nums in range(x):
            print("{}".format(my_list[nums]), end="")
            t += 1
    except IndexError:
        pass
    print()
    return t
