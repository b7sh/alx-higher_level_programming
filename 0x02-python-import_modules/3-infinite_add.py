#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argc = len(argv)
    if argc < 2:
        print("{}".format(argc - 1))
    else:
        result = 0
        for n in range(1, argc):
            result += int(argv[n])
        print("{}".format(result))
