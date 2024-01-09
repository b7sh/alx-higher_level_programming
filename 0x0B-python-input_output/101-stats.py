#!/usr/bin/python3
""" a script that reads stdin line by line and computes metrics"""


def print_status(size, stat_code):
    """print the ststus
    args:
    size (int): the size
    stat_code (dict): the stat code
    """
    print("File size: {}".format(size))
    for k in sorted(stat_code):
        print("{}: {}".format(k, stat_code[k]))

if __name__ == "__main__":
    import sys
    size = 0
    stat_code = {}
    v_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    count = 0
    
    try:
        for i in sys.stdin:
            if count == 10:
                print_status(size, stat_code)
                count = 1
            else:
                count += 1
            i = i.split()
            try:
                size += int(i[-1])
            except (IndexError, ValueError):
                pass
            try:
                if i[-2] in v_codes:
                    if stat_code.get(i[-2], -1) == -1:
                        stat_code[i[-2]] = 1
                    else:
                        stat_code[i[-2]] += 1
            except IndexError:
                pass
        print_status(size, stat_code)
    except KeyboardInterrupt:
        print_status(size, stat_code)
        raise
