#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    length = len(argv)
    if length == 1:
        print("{} {}.".format(length - 1, "arguments"))
    if length == 2:
        print("{} {}:".format(length - 1, "argument"))
        print("{}: {}".format(length - 1, argv[1]))
    else:
        for i in range(length):
            if i == 0:
                print("{} {}:".format(length - 1, "arguments"))
            else:
                print("{}: {}".format(i, argv[i]))
